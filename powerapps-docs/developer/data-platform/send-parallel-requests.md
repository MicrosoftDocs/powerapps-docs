---
title: "Send parallel requests (Dataverse)| Microsoft Docs"
description: "When your application needs to send a large number of requests to Dataverse you can achieve much higher total throughput by sending requests in parallel using multiple threads."
ms.date: 12/12/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: get-started-article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke
---

# Send parallel requests

When your application needs to send a large number of requests to Dataverse you can achieve much higher total throughput by sending requests in parallel using multiple threads. Dataverse is designed to support multiple concurrent users, so sending requests in parallel leverages this strength.

> [!NOTE]
> In plug-ins, sending parallel requests is not supported. More information: [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md)



## Optimize your connection

When using .NET and sending requests in parallel, apply the following configuration changes so your requests are not limited by default settings:

```csharp
// Change max connections from .NET to a remote service default: 2
System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
// Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4 
ThreadPool.SetMinThreads(100, 100);
// Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server 
System.Net.ServicePointManager.Expect100Continue = false;
// Can decrease overall transmission overhead but can cause delay in data packet arrival
System.Net.ServicePointManager.UseNagleAlgorithm = false;
```

More information:
- <xref:System.Net.ServicePointManager.DefaultConnectionLimit?displayProperty=fullName>
- <xref:System.Threading.ThreadPool.SetMinThreads%2A?displayProperty=fullName>
- <xref:System.Net.ServicePointManager.Expect100Continue?displayProperty=fullName>
- <xref:System.Net.ServicePointManager.UseNagleAlgorithm?displayProperty=fullName>

## Optimum degree of parallelism (DOP)

Part of the service that Dataverse provides is managing resource allocation for environments. Production environments that are heavily used by many licenced users will have more resources allocated to them. The number and capabilities of the servers allocatied may vary over time, so there is no fixed number that you should apply to get the optimum degree of parallelism. However, the `x-ms-dop-hint` response header returns an integer value that should provide good results for a given environment.

When using [Parallel Programming in .NET](/dotnet/standard/parallel-programming/) the default degree of parallelism depends on the number of CPU cores on the server running the code. You can set the [ParallelOptions.MaxDegreeOfParallelism Property](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism) to define a maximum number of concurrent tasks.

### Service protection limits

One of the three facets monitored for service protection limits is the number of concurrent requests. If more than 52 concurrent requests are sent to a single server, an error will be returned. If you are depending on the `x-ms-dop-hint` response header value to control the degree of parallelism, you should rarely hit this limit. If you encounter this error, you should reduce the number of concurrent threads.

There is a specific error returned when this limit is reached:

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

You can also mitigate the liklihood of this error occurring by sending your requests to all the servers that support the environment by disabling sever affinity.

## Server affinity

When you make a connection to a service on Azure a cookie is returned with the response and all your subsequent requests will attempt to be routed to the same server unless capacity management forces it to go to another server. Interactive client applications, especially browser clients, benefit from this because it allows for re-using data cached on the server. Web browsers always have server affinity enabled and it cannot be disabled.

When sending requests in parallel from your client applcation, you can gain performance benefits by disabling this cookie. Each request you send will be routed any of the eligible servers. Not only does this increase total throughput, it also helps reduce impact of service protection limits because each limit is applied per server.

Following are some examples showing how to disable server affinity with .NET.

### [SDK for .NET](#tab/sdk)

If you are using the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient)  or [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes, add the following to the `AppSettings` node in the `App.config` file.

```xml
<add key="PreferConnectionAffinity" value="false" />
```

### [Web API](#tab/webapi)

For .NET applications using [HttpClient](xref:System.Net.Http.HttpClient) with the Web API, the following code shows how to disable cookies using a custom [HttpMessageHandler](xref:System.Net.Http.HttpMessageHandler).

```csharp
HttpMessageHandler messageHandler = new OAuthMessageHandler(
    config,
    new HttpClientHandler() { UseCookies = false }
    );
HttpClient httpClient = new HttpClient(messageHandler)
```

If you are using dependency injection, you can use the [ConfigurePrimaryHttpMessageHandler](xref:Microsoft.Extensions.DependencyInjection.HttpClientBuilderExtensions.ConfigurePrimaryHttpMessageHandler%2A) method to set the [HttpClientHandler.UseCookies property](xref:System.Net.Http.HttpClientHandler.UseCookies) to false.

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

## Examples

The following .NET examples show use of [Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl) with Dataverse.

### [SDK for .NET](#tab/sdk)

With the Dataverse SDK for .NET, the [Clone](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.Clone%2A) method available in both [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) and [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) allows duplicating an existing connection to Dataverse so that you can leverage the [Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl) which simplifies the process of adding parallelism and concurrency to applications.

The `x-ms-dop-hint` response value is available via the [RecommendedDegreesOfParallelism](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.RecommendedDegreesOfParallelism) property in either `ServiceClient` or  `CrmServiceClient`. You should use this value when setting [ParallelOptions.MaxDegreeOfParallelism](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism) when you use [Parallel.ForEach](xref:System.Threading.Tasks.Parallel.ForEach%2A).

The id values of the responses are added to a [ConcurrentBag](xref:System.Collections.Concurrent.ConcurrentBag`1) of Guids. `ConcurrentBag` provides a thread-safe unordered collection of objects when ordering doesn't matter. When sending requests in parallel there is no way to know the order in which the responses will be returned.

```csharp
/// <summary>
/// Creates records in parallel
/// </summary>
/// <param name="serviceClient">The authenticated ServiceClient instance.</param>
/// <param name="entityList">The list of entities to create.</param>
/// <returns>The id values of the created records.</returns>
static Guid[] CreateRecordsInParallel(ServiceClient serviceClient, List<Entity> entityList)
{
    ConcurrentBag<Guid> ids = new ConcurrentBag<Guid>();
 
    Parallel.ForEach(entityList,
        new ParallelOptions()
        {
            MaxDegreeOfParallelism = serviceClient.RecommendedDegreesOfParallelism
        },
        () =>
        {
            //Clone the ServiceClient for each thread
            return serviceClient.Clone();
        },
        (entity, loopState, index, threadLocalSvc) =>
        {
            ids.Add(threadLocalSvc.Create(entity));

            return threadLocalSvc;
        },
        (threadLocalSvc) =>
        {
            //Dispose the cloned ServiceClient instance
            threadLocalSvc?.Dispose();
        }
    );
    return ids.ToArray();
}
```

### [Web API](#tab/webapi)

The following static method example shows the use of an authenticated [HttpClient](xref:System.Net.Http.HttpClient) that has been configured with a [BaseAddress Property](xref:System.Net.Http.HttpClient.BaseAddress) set to the Dataverse Web API Uri.

This method first sends a request using the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) and then accesses the `x-ms-dop-hint` value from the response, which is used to set the [ParallelOptions.MaxDegreeOfParallelism Property](xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism).

Then it uses [Parallel.ForEachAsync](xref:System.Threading.Tasks.Parallel.ForEachAsync%2A) to send the requests.

It then parses the id values of the records and sets them into a [ConcurrentBag](xref:System.Collections.Concurrent.ConcurrentBag`1) of Guids. `ConcurrentBag` provides a thread-safe unordered collection of objects when ordering doesn't matter. When sending requests in parallel there is no way to know the order in which the responses will be returned.

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

[!INCLUDE[footer-include](../../includes/footer-banner.md)]