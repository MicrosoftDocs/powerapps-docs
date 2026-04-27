---
title: "Send Parallel Requests to Dataverse"
description: "Learn how to send parallel requests to Dataverse to achieve higher throughput using multiple threads when your application needs to handle large numbers of requests."
ms.date: 03/26/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: how-to
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke
---

# Send parallel requests

When your application needs to send a large number of requests to Dataverse, you can achieve much higher total throughput by sending requests in parallel by using multiple threads. Dataverse is designed to support multiple concurrent users, so sending requests in parallel leverages this strength.

> [!NOTE]
> Sending parallel requests within a plug-in isn't supported. For more information, see [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md).


## Optimum degree of parallelism (DOP)

Dataverse manages resource allocation for environments. Production environments that many licensed users heavily use have more allocated resources. The number and capabilities of the servers allocated might vary over time, so there's no fixed number for the optimum degree of parallelism. Instead, use the integer value returned from the `x-ms-dop-hint` response header. This value provides a recommended degree of parallelism for the environment.

When you use [Parallel Programming in .NET](/dotnet/standard/parallel-programming/), the default degree of parallelism depends on the number of CPU cores on the client running the code. If the number of CPU cores exceeds the best match for the environment, you might be sending too many requests. Set the [ParallelOptions.MaxDegreeOfParallelism Property](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism) to define a maximum number of concurrent tasks.

### Service protection limits

One of the three facets monitored for service protection limits is the number of concurrent requests. By default, this value is 52 but it might be higher. An error is returned if the limit is exceeded. If you depend on the `x-ms-dop-hint` response header value to limit the degree of parallelism, you should rarely hit this limit. If you encounter this error, reduce the number of concurrent threads.

A specific error is returned when this limit is reached:

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

You can also reduce the likelihood of this error by sending your requests to all the servers that support the environment by disabling server affinity.

## Server affinity

When you connect to a service on Azure, the service returns a cookie with the response. All your subsequent requests try to go to the same server unless capacity management forces the request to go to another server. Interactive client applications, especially browser clients, benefit from this cookie because it allows the application to reuse data cached on the server. Web browsers always have server affinity enabled and you can't disable it.

When you send requests in parallel from your client application, you can gain performance benefits by disabling this cookie. Each request you send routes to any of the eligible servers. This change not only increases total throughput, but it also helps reduce the impact of service protection limits because each limit applies per server.

The following examples show how to disable server affinity by using .NET.

### [SDK for .NET](#tab/sdk)

If you're using the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) or [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes, add the following code to the `AppSettings` node in the `App.config` file.

```xml
<add key="PreferConnectionAffinity" value="false" />
```

You can also set the value of the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.EnableAffinityCookie> property by using either the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) or [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes.

You can also set this property by using the [ServiceClient(ConnectionOptions, Boolean, ConfigurationOptions)](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.%23ctor%2A#microsoft-powerplatform-dataverse-client-serviceclient-ctor(microsoft-powerplatform-dataverse-client-model-connectionoptions-system-boolean-microsoft-powerplatform-dataverse-client-model-configurationoptions)) constructor and the [ConfigurationOptions.EnableAffinityCookie](xref:Microsoft.PowerPlatform.Dataverse.Client.Model.ConfigurationOptions.EnableAffinityCookie) property.

### [Web API](#tab/webapi)

For .NET applications that use [HttpClient](xref:System.Net.Http.HttpClient) with the Web API, the following code shows how to disable cookies by using a custom [HttpMessageHandler](xref:System.Net.Http.HttpMessageHandler).

```csharp
HttpMessageHandler messageHandler = new OAuthMessageHandler(
    config,
    new HttpClientHandler() { UseCookies = false }
    );
HttpClient httpClient = new HttpClient(messageHandler)
```

If you're using dependency injection, you can use the [ConfigurePrimaryHttpMessageHandler](xref:Microsoft.Extensions.DependencyInjection.HttpClientBuilderExtensions.ConfigurePrimaryHttpMessageHandler%2A) method to set the [HttpClientHandler.UseCookies property](xref:System.Net.Http.HttpClientHandler.UseCookies) to false.

```csharp
IHostBuilder builder = Host.CreateDefaultBuilder();

builder.ConfigureServices(services =>
{
   services.AddHttpClient(
      name: "ClientName",
      configureClient: ConfigureHttpClientDelegate
      )
   .ConfigurePrimaryHttpMessageHandler(() =>
      new HttpClientHandler
      {
            UseCookies = false
      }
   );
});
```

---

## Optimize your connection

When you use .NET and send requests in parallel, change the default settings so your requests aren't limited by them. Make the following changes:

```csharp
// Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4 
ThreadPool.SetMinThreads(100, 100);
// Change max connections from .NET to a remote service default: 2
System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
// Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server 
System.Net.ServicePointManager.Expect100Continue = false;
// Can decrease overall transmission overhead but can cause delay in data packet arrival
System.Net.ServicePointManager.UseNagleAlgorithm = false;
```
### ThreadPool.SetMinThreads

This setting controls the minimum number of threads the thread pool creates on demand as new requests come in. After reaching this number, the thread pool switches to an algorithm that manages thread creation and destruction.

By default, the minimum number of threads is set to the processor count. Use `SetMinThreads` to increase the minimum number of threads. For example, you might temporarily increase the number to work around problems where some queued work items or tasks block thread pool threads. Those blockages sometimes lead to a situation where all worker or I/O completion threads are blocked (starvation). However, increasing the minimum number of threads might degrade performance in other ways.

The numbers you use can vary according to the hardware. The numbers you use are lower for a consumption-based Azure function than for code running on a dedicated host with high-end hardware.

More information: <xref:System.Threading.ThreadPool.SetMinThreads%2A?displayProperty=fullName>

### System.Net.ServicePointManager settings

In .NET Framework, [ServicePointManager](xref:System.Net.ServicePointManager) is a static class that you use to create, maintain, and delete instances of the [ServicePoint](xref:System.Net.ServicePoint) class. Use these settings with the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) or [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes. These settings should also apply when using [HttpClient](xref:System.Net.Http.HttpClient) with Web API in .NET Framework. However, with .NET Core, Microsoft recommends settings in `HttpClient` instead.

### DefaultConnectionLimit

The hardware ultimately limits this value. If you set it too high, other mechanisms throttle it. Raise it above the default value, and set it at least equal to the number of concurrent requests you intend to send.

When you use .NET Core with `HttpClient`, the [HttpClientHandler.MaxConnectionsPerServer](xref:System.Net.Http.HttpClientHandler.MaxConnectionsPerServer) property controls this setting. Its default value is [int.MaxValue](xref:System.Int32.MaxValue).

For more information, see:

- <xref:System.Net.ServicePointManager.DefaultConnectionLimit?displayProperty=fullName>
- [.NET Framework Connection Pool Limits and the new Azure SDK for .NET](https://devblogs.microsoft.com/azure-sdk/net-framework-connection-pool-limits/)
- [Configuring ServicePointManager for WebJobs](https://github.com/Azure/azure-webjobs-sdk/wiki/ServicePointManager-settings-for-WebJobs)
- [HttpClientHandler.MaxConnectionsPerServer](xref:System.Net.Http.HttpClientHandler.MaxConnectionsPerServer)

### Expect100Continue

When you set this property to true, the client waits for a round-trip confirmation of a connection to the server. For `HttpClient`, the default value of [HttpRequestHeaders.ExpectContinue](xref:System.Net.Http.Headers.HttpRequestHeaders.ExpectContinue) is false.

For more information, see:

- <xref:System.Net.ServicePointManager.Expect100Continue?displayProperty=fullName>
- [100 Continue](https://developer.mozilla.org/docs/Web/HTTP/Status/100)

### UseNagleAlgorithm

The Nagle algorithm reduces network traffic by buffering small packets of data and transmitting them as a single packet. This process is also referred to as "nagling." It's widely used because it reduces the number of packets transmitted and lowers the overhead per packet. Setting this value to false can decrease overall transmission overhead but can cause delay in data packet arrival.

For more information, see <xref:System.Net.ServicePointManager.UseNagleAlgorithm?displayProperty=fullName>.

## Examples

The following .NET examples show how to use the [Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl) with Dataverse.

### [SDK for .NET](#tab/sdk)

You can access the `x-ms-dop-hint` response value through the [RecommendedDegreesOfParallelism](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.RecommendedDegreesOfParallelism) property in either `ServiceClient` or `CrmServiceClient`. Use this value when setting [ParallelOptions.MaxDegreeOfParallelism](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism) when you use [Parallel.ForEach](xref:System.Threading.Tasks.Parallel.ForEach%2A).

These examples also show setting the [EnableAffinityCookie](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.EnableAffinityCookie) property to false.

In the following examples, add the ID values of the responses to a [ConcurrentBag](xref:System.Collections.Concurrent.ConcurrentBag`1) of GUIDs. `ConcurrentBag` provides a thread-safe unordered collection of objects when ordering doesn't matter. You can't expect the order of the GUIDs returned by this method to match the order of the items sent in the `entityList` parameter.

### Using ServiceClient with .NET 6 or higher

By using .NET 6 or higher, you can use the [Parallel.ForEachAsync](xref:System.Threading.Tasks.Parallel.ForEachAsync%2A) method with the asynchronous methods included with [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), such as [CreateAsync](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.CreateAsync%2A).

```csharp
/// <summary>
/// Creates records in parallel
/// </summary>
/// <param name="serviceClient">The authenticated ServiceClient instance.</param>
/// <param name="entityList">The list of entities to create.</param>
/// <returns>The id values of the created records.</returns>
static async Task<Guid[]> CreateRecordsInParallel(
    ServiceClient serviceClient, 
    List<Entity> entityList)
{
    ConcurrentBag<Guid> ids = new();

    // Disable affinity cookie
    serviceClient.EnableAffinityCookie = false;

    var parallelOptions = new ParallelOptions()
    { MaxDegreeOfParallelism = 
        serviceClient.RecommendedDegreesOfParallelism };

    await Parallel.ForEachAsync(
        source: entityList,
        parallelOptions: parallelOptions,
        async (entity, token) =>
        {
            ids.Add(await serviceClient.CreateAsync(entity, token));
        });

    return ids.ToArray();
}
```

### Using CrmServiceClient with .NET Framework

When you use .NET Framework, the [Clone](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.Clone%2A) method available in [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) duplicates an existing connection to Dataverse so that you can use the [Parallel.ForEach](xref:System.Threading.Tasks.Parallel.ForEach%2A) method.

```csharp
/// <summary>
/// Creates records in parallel
/// </summary>
/// <param name="crmServiceClient">The authenticated CrmServiceClient instance.</param>
/// <param name="entityList">The list of entities to create.</param>
/// <returns>The id values of the created records.</returns>
static Guid[] CreateRecordsInParallel(
    CrmServiceClient crmServiceClient, 
    List<Entity> entityList)
{
   ConcurrentBag<Guid> ids = new ConcurrentBag<Guid>();

    // Disable affinity cookie
    crmServiceClient.EnableAffinityCookie = false;

   Parallel.ForEach(entityList,
      new ParallelOptions()
      {
            MaxDegreeOfParallelism = crmServiceClient.RecommendedDegreesOfParallelism
      },
      () =>
      {
            //Clone the CrmServiceClient for each thread
            return crmServiceClient.Clone();
      },
      (entity, loopState, index, threadLocalSvc) =>
      {
            ids.Add(threadLocalSvc.Create(entity));

            return threadLocalSvc;
      },
      (threadLocalSvc) =>
      {
            //Dispose the cloned crmServiceClient instance
            threadLocalSvc?.Dispose();
      }
   );
   return ids.ToArray();
}
```

### [Web API](#tab/webapi)

The following static method example shows how to use an authenticated [HttpClient](xref:System.Net.Http.HttpClient) that's configured with a [BaseAddress Property](xref:System.Net.Http.HttpClient.BaseAddress) set to the Dataverse Web API Uri.

This method first sends a request by using the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI), but it doesn't use the data in the body of the response. The `x-ms-dop-hint` response header value is what the method needs. It uses this value to set the [ParallelOptions.MaxDegreeOfParallelism Property](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism). Then it uses [Parallel.ForEachAsync](xref:System.Threading.Tasks.Parallel.ForEachAsync%2A) to send the requests by using those options.

The method then parses the ID values of the records and sets them into a [ConcurrentBag](xref:System.Collections.Concurrent.ConcurrentBag`1) of Guids. `ConcurrentBag` provides a thread-safe unordered collection of objects when ordering doesn't matter. The order of the Guids returned by this method can't be expected to match the order of the items sent in the `entityList` parameter.

```csharp
/// <summary>
/// Creates account records in parallel
/// </summary>
/// <param name="client">Authenticated HttpClient instance</param>
/// <param name="entityList">List of JObject representing account records</param>
/// <returns>The id values of the created records.</returns>
static async Task<Guid[]> CreateRecordsInParallel(HttpClient client, List<JObject> entityList)
{
   ConcurrentBag<Guid> ids = new ConcurrentBag<Guid>();

   HttpResponseMessage whoAmIResponse = await client.SendAsync(new HttpRequestMessage
   {
         Method = HttpMethod.Get,
         RequestUri = new Uri(
         uriString: "WhoAmI",
         uriKind: UriKind.Relative)
   });

   int recommendedDegreeOfParallelism = int.Parse(whoAmIResponse.Headers.GetValues("x-ms-dop-hint").FirstOrDefault());

   var parallelOptions = new ParallelOptions() { MaxDegreeOfParallelism = recommendedDegreeOfParallelism };

   // Send the requests in parallel
   await Parallel.ForEachAsync(entityList, parallelOptions, async (jObject, token) =>
   {
        // Send the request to create an account record.
         var createResponse = await client.SendAsync(new HttpRequestMessage()
         {
            Method = HttpMethod.Post,
            RequestUri = new Uri(
            uriString: "accounts",
            uriKind: UriKind.Relative),
            Content = new StringContent(
               content: jObject.ToString(),
               encoding: System.Text.Encoding.UTF8,
               mediaType: "application/json")
         });

         string? uri = createResponse.Headers.GetValues("OData-EntityId").FirstOrDefault();

         // Parse the Id from the URI returned
         int firstParen = uri.LastIndexOf('(') + 1;
         int lastParen = uri.LastIndexOf(')');

         if (Guid.TryParse(uri[firstParen..lastParen], out Guid id))
         {
            ids.Add(id);
         }

   });

   return ids.ToArray();
}
```

---


### See also

[Service protection API limits](api-limits.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapi/samples/webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapi/samples/webapiservice-tpl-dataflow-parallel-operations.md)<br />
[Sample: Task Parallel Library with CrmServiceClient](xrm-tooling/sample-tpl-crmserviceclient.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
