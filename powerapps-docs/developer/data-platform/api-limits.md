---
title: "Service protection API limits (Microsoft Dataverse) | Microsoft Docs" 
description: "Understand the service protection limits for API requests." 
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.subservice: dataverse-developer
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Service protection API limits

To ensure consistent availability and performance for everyone we apply some limits to how APIs are used. These limits are designed to detect when client applications are making extraordinary demands on server resources.

The limits should not affect normal users of interactive clients. Only client applications that perform extraordinary API requests should be affected. The limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Microsoft Dataverse platform.

When a client application makes extraordinarily demanding requests, the Dataverse follows the common pattern for online services. We return an error indicating that too many requests have been made.

- With the Web API, we return a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error.
- With the Organization Service, you will get an [OrganizationServiceFault](/dotnet/api/microsoft.xrm.sdk.organizationservicefault) error with one of three specific error codes. More information: [Service protection API limit errors returned](#service-protection-api-limit-errors-returned)


## Impact on client applications

It is the responsibility of client applications to manage service protection API limit errors. Exactly how to manage this error depends on the nature of the application. 

### Interactive client applications

The service protection limits are high enough that it should be rare for an individual using an interactive client application to encounter them during normal usage. However, it is possible if the client application allows for bulk operations. Client application developers should be aware of how service protection API limits are enforced and design the UI to reduce the potential for users to send extremely demanding requests to the server. But they should still expect that service protection API limit errors can occur and be prepared to handle them.

Client application developers should not simply throw the error to display the message to the user. The error message is not intended for end users. See [Retry operations](#retry-operations) for specific strategies.

### Data integration applications

Applications designed to load data into Dataverse or perform bulk updates must also be able to manage service protection API limit errors. These applications prioritize throughput so they can complete their work in the minimum amount of time. These applications must have a strategy to retry operations. There are several strategies that they can apply to get the maximum throughput. More information: [How to maximize throughput](#how-to-maximize-throughput).

### Portal applications

Portal applications typically send requests from anonymous users through a service principal account. Because the service protection API limits are based on a per user basis, portal applications can hit service protection API limits based on the amount of traffic the portal experiences. Like interactive client applications, it isn't expected that the service protection API limits errors should be displayed to the portal end user. It is expected that the UI should disable further requests and display a message that the server is busy. The message may include the time when the application can begin accepting new requests.

## Impact on plug-ins and custom workflow activities

Plug-ins and custom workflow activities apply business logic triggered by incoming requests. Service protection limits are not applied to plug-ins and custom workflow activities. Plug-ins and custom workflow activities are uploaded and run within the isolated sandbox service. Dataverse operations invoked on the sandbox service do not use the public API endpoints.

If your application performs operations that trigger custom logic, the number of requests sent by plug-ins or custom workflow activities will not be counted towards service protection API limits. However, the additional computation time that these operations contribute will be added to the initial request that triggered them. This computation time is part of the service protection API limits. More information: [How service protection API limits are enforced](#how-service-protection-api-limits-are-enforced)

## Retry operations

When a service protection API limit error occurs, it will provide a value indicating the duration before any new requests from the user can be processed.

- When a 429 error is returned from the Web API, the response will include a [Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After) with number of seconds.
- With the Organization Service, a [TimeSpan](/dotnet/api/system.timespan) value is returned in the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> collection with the key `Retry-After`.

### Interactive application re-try 

If the client is an interactive application, you should display a message that the server is busy while you re-try the request the user made. You may want to provide an option for the user to cancel the operation. Don't allow users to submit more requests until the previous request you sent has completed.

### Non-interactive application re-try

If the client is not interactive, the common practice is to simply wait for the duration to pass before sending the request again. This is commonly done by pausing the execution of the current thread using [Thread.Sleep](/dotnet/api/system.threading.thread.sleep) or equivalent methods.

## How Service Protection API Limits are enforced

Two of the service protection API limits are evaluated within a 5 minute (300 second) sliding window. If either limits are exceeded within the preceding 300 seconds, a service protection API Limit error will be returned on subsequent requests to protect the service until the Retry-After duration has ended.

The service protection API limits are evaluated per user. Each authenticated user is limited independently. Only those users accounts which are making extraordinary demands will be limited. Other users will not be impacted.

Service protection API limits are enforced based on three facets:

- The number of requests were sent by a user.
- The combined execution time was required to process requests sent by a user.
- The number of concurrent requests sent by a user.

If the only limit was on the number of requests sent by a user, it would be possible to bypass it. The other facets were added to counter these attempts. For example:

- You could send fewer requests by bundling them in batch operations.
  - The combined execution time limit will counter this.
- Rather than sending requests individually in succession, you could send a large number of concurrent requests before service protection API limits are enforced.
  - The concurrent request limit will counter this.

Each web server available to your environment will enforce these limits independently. Most environments will have more than one web server. Trial environments are allocated only a single web server. The actual number of web servers that are available to your environment depends on multiple factors that are part of the managed service we provide. One of the factors is how many user licenses you have purchased.

The following table describes the default service protection API limits enforced *per web server*:

|Measure|Description|Limit per web server|
|--|--|--|
|Number of requests|The cumulative number of requests made by the user.|6000 within the 5 minute sliding window|
|Execution time|The combined execution time of all requests made by the user.| 20 minutes (1200 seconds) within the 5 minute sliding window|
|Number of concurrent requests|The number of concurrent requests made by the user|52|

> [!IMPORTANT]
> These limits are subject to change and may vary between different environments. These numbers represent default values and are provided to give you some idea of what values you can expect.

### The Retry-After duration

The `Retry-After` duration will depend on the nature of the operations that have been sent in the preceding 5 minute period. The more demanding the requests are, the longer it will take for the server to recover.

Today, because of the way the limits are evaluated, you can expect to exceed the number of requests and execution time limits for a 5 minute period before the service protection API limits will take effect. However, exceeding the number of concurrent requests will immediately return an error. If the application continues to send such demanding requests, the duration will be extended to minimize the impact on shared resources. This will cause the individual retry-after duration period to be longer, which means your application will see longer periods of inactivity while it is waiting. This behavior may change in the future.

When possible, we recommend trying to achieve a consistent rate by starting with a lower number of requests and gradually increasing until you start hitting the service protection API limits. After that, let the server tell you how many requests it can handle within a 5 minute period. Keeping your maximum number of requests limited within this 5 minute period and gradually increasing will keep the retry-after duration low, optimizing your total throughput and minimizing server resource spikes.

## Service Protection API Limit Errors returned

This section describes the three types of service protection API limit errors that can be returned as well as factors that cause these errors and possible mitigation strategies.

- The **Error code** is the numerical error value returned by the Organization Service <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails>.
- The **Hex code** is the hexadecimal error value returned by the Web API.

### Number of requests

This limit counts the total number of requests during the preceding 300 second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015902`|`0x80072322`|`Number of requests exceeded the limit of 6000 over time window of 300 seconds.`|

It is not expected that a typical user of an interactive application will be able to send 1,200 requests per minute to exceed this limit unless the application enables users to perform bulk operations.

For example, if a list view enables selection of 250 records at a time and allows a user to perform some operation on all these records, the user would need to perform this operation 24 times in a span of 300 seconds. The user would need to complete the operation on each list within 12.5 seconds.

If your application provides this capability, you should consider some of the following strategies:

- Decreasing the total number of records that can be selected in a list. If the number of items displayed in a list is reduced to 50, the user would need to perform this operation 120 times within 300 seconds. The user would have to complete the operation on each list within 2.5 seconds.
- Combine the selected operations into a batch. A batch can contain up to 1000 operations and will avoid the number of requests limit. However, you will need to be prepared for the execution time limit.

### Execution time

This limit tracks the combined execution time of incoming requests during the preceding 300 second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015903`|`0x80072321`|`Combined execution time of incoming requests exceeded limit of 1,200,000  milliseconds over time window of 300 seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.`|

Some operations require more resources than others. Batch operations, importing solutions, and highly complex queries can be very demanding. These operations may also be performed simultaneously in concurrent requests. Therefore, within the 5 minute window it is possible to request operations that will require more than 20 minutes of combined computation time.

This limit can be encountered when strategies using batch operations and concurrent requests are used to avoid the number of requests limit.

### Concurrent requests

This limit tracks the number of concurrent requests.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

Client applications are not limited to sending requests individually in succession. The client may apply parallel programming patterns or various methods to send multiple requests simultaneously. The server can detect when it is responding to multiple requests from the same user simultaneously. If this number of concurrent requests is exceeded, this error will be thrown.

Sending concurrent requests can be a key part of a strategy to maximize throughput, but it is important to keep it under control.

When using [Parallel Programming in .NET](/dotnet/standard/parallel-programming/) the default degree of parallelism depends on the number of CPU cores on the server running the code. It should not exceed 52. The [ParallelOptions.MaxDegreeOfParallelism Property](/dotnet/api/system.threading.tasks.paralleloptions.maxdegreeofparallelism) can be set to define a maximum number of concurrent tasks.

## How to maximize throughput

When you have an application that must prioritize throughput to move the most data in the shortest period, there are some strategies you can apply.

### Let the server tell you how much it can handle

Don't try to calculate how many requests to send at a time. Each environment can be different. Gradually increase the rate you send requests until you begin to hit limits and then depend on the service protection API Limit `Retry-After` value to tell you when to send more. This value will keep your total throughput at the highest possible level.

### Use multiple threads

The higher limit on number of concurrent threads is something your application can use to have a significant improvement in performance. This is true if your individual operations are relatively quick. Depending on the nature of the data you are processing, you may need to adjust the number of threads to get optimum throughput.

More information:

- [Use Task Parallel Library with Web API](#use-task-parallel-library-with-web-api)
- [Use Task Parallel Library with CrmServiceClient](#use-task-parallel-library-with-crmserviceclient)

### Avoid batching

In the Organization Service the conventional wisdom has been to employ the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> to bundle multiple operations. The main benefit this provides is that it reduces the total amount of SOAP XML payload that must be sent over the wire. This provides some performance benefit when network latency is an issue.

In the past, ExecuteMultiple operations were limited to just 2 at a time because of the impact on performance that this could have. This is no longer the case, because service protection API limits have made that limit redundant.

Most scenarios will be fastest sending single requests with a high degree of parallelism. If you feel batch size might improve performance, it is best to start with a small batch size of 10 and increase concurrency until you start getting service protection API limit errors that you will retry.

When using the Web API, the smaller JSON payload sent over the wire for individual requests means that network latency is not an issue. The total amount of payload that is sent using $batch is greater than sending individual requests. Only use $batch if you want to manage transactions using changesets. More information: [Execute batch operations using the Web API](webapi/execute-batch-operations-using-web-api.md)

> [!NOTE]
> Batch operations are not a valid strategy to bypass entitlement limits. Service protection API limits and Entitlement limits are evaluated separately. Entitlement limits are based on CRUD operations and accrue whether or not they are included in a batch operation. More information: [Entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits)

### Remove the affinity cookie

When you make a connection to a service on Azure a cookie is returned with the response and all your subsequent requests will attempt to be routed to the same server unless capacity management forces it to go to another server. If you remove this cookie, each request you send will be routed any of the eligible servers. This increases throughput because limits are applied per server. This simply allows you to use more servers if they are available.

> [!NOTE]
> This strategy should only be used by applications that are seeking to optimize throughput. Interactive client applications benefit from the affinity cookie because it allows for reusing cached data that would otherwise need to be re-created leading to poorer performance.

The following code shows how to disable cookies when initializing an HttpClient with the Web API, assuming you are using a custom HttpMessageHandler to manage authentication. More information: [Example demonstrating a DelegatingHandler](authenticate-oauth.md#example-demonstrating-a-delegatinghandler)

```csharp
HttpMessageHandler messageHandler = new OAuthMessageHandler(
    config,
    new HttpClientHandler() { UseCookies = false }
    );
HttpClient httpClient = new HttpClient(messageHandler)
```

If you are using CrmServiceClient, add the following to the AppSettings node in the App.config file.

```xml
<add key="PreferConnectionAffinity" value="false" /> 
```

### Optimize your connection

You can expect greater throughput by optimizing the connection. Supporting .NET sample code uses these settings:

```csharp
//Change max connections from .NET to a remote service default: 2
System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
//Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4 
System.Threading.ThreadPool.SetMinThreads(100, 100);
//Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server 
System.Net.ServicePointManager.Expect100Continue = false;
//Can decreas overall transmission overhead but can cause delay in data packet arrival
System.Net.ServicePointManager.UseNagleAlgorithm = false;
```
More information: [Managing Connections](/dotnet/framework/network-programming/managing-connections)

## Strategies to manage Service Protection API limits

This section describes ways that you can design your clients and systems to avoid service protection API limit errors. You may also want to consider how you manage your licenses to reduce the impact.

### Update your client application

Service Protection API limits have been applied to Dataverse since 2018, but there are many client applications written before these limits existed. These clients didn't expect these errors and can't handle the errors correctly. You should update these applications and apply the patterns described in the [Using the Organization service](#using-the-organization-service) or [Using the Web API](#using-the-web-api) sections below.

### Move towards real-time integration

Remember that the main point of service protection API limits is to smooth out the impact of highly demanding requests occurring over a short period of time. If your current business processes depend on large periodic nightly, weekly, or monthly jobs which attempt to process large amounts of data in a short period of time, consider how you might enable a real-time data integration strategy. If you can move away from processes that require highly demanding operations, you can reduce the impact service protection limits will have.

## Using the Web API

If you are using the Web API with a client library, you may find that it supports the retry behavior expected for 429 errors. Check with the client library publisher.

If you have written your own library, you can include behaviors to be similar to the one included in this sample code for a helper [Web API CDSWebApiService class sample (C#)](webapi/samples/cdswebapiservice.md).

```csharp
private async Task<HttpResponseMessage> SendAsync(
    HttpRequestMessage request,
    HttpCompletionOption httpCompletionOption = HttpCompletionOption.ResponseHeadersRead,
    int retryCount = 0)
{
    HttpResponseMessage response;
    try
    {
        //The request is cloned so it can be sent again.
        response = await httpClient.SendAsync(request.Clone(), httpCompletionOption);
    }
    catch (Exception)
    {
        throw;
    }

    if (!response.IsSuccessStatusCode)
    {
        if ((int)response.StatusCode != 429)
        {
            //Not a service protection limit error
            throw ParseError(response);
        }
        else
        {
            // Give up re-trying if exceeding the maxRetries
            if (++retryCount >= config.MaxRetries)
            {
                throw ParseError(response);
            }

            int seconds;
            //Try to use the Retry-After header value if it is returned.
            if (response.Headers.Contains("Retry-After"))
            {
                seconds = int.Parse(response.Headers.GetValues("Retry-After").FirstOrDefault());
            }
            else
            {
                //Otherwise, use an exponential backoff strategy
                seconds = (int)Math.Pow(2, retryCount);
            }
            Thread.Sleep(TimeSpan.FromSeconds(seconds));

            return await SendAsync(request, httpCompletionOption, retryCount);
        }
    }
    else
    {
        return response;
    }
}
```

You may also want to use [Polly](https://github.com/App-vNext/Polly), a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.

### HTTP Response headers

If you are using HTTP requests with the Web API, you can track the remaining limit values with the following HTTP response headers:

|Header  |Value Description  |
|---------|---------|
|`x-ms-ratelimit-burst-remaining-xrm-requests`|The remaining number of requests for this connection|
|`x-ms-ratelimit-time-remaining-xrm-requests`|The remaining combined duration for all connections using the same user account|

You should not depend on these values to control how many requests you send. They are intended for debugging purposes. If you are removing the affinity cookie, these values are re-set when you connect to a different server.

### Use Task Parallel Library with Web API

To achieve optimum throughput, you should use multiple-threads. The Task Parallel Library (TPL) makes developers more productive by simplifying the process of adding parallelism and concurrency to applications.

See these examples using the [Web API CDSWebApiService class sample (C#)](webapi/samples/cdswebapiservice.md):

- [Web API CDSWebApiService Parallel Operations sample (C#)](webapi/samples/cdswebapiservice-parallel-operations.md)
- [Web API CDSWebApiService Async Parallel Operations sample (C#)](webapi/samples/cdswebapiservice-async-parallel-operations.md)


## Using the Organization Service

If you are using the Organization Service, we recommend that you use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>. This class implements the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and can manage any service protection API limit errors that are returned. 

Since Xrm.Tooling.Connector version 9.0.2.16, it will automatically pause and re-send the request after the Retry-After duration period.

If your application is currently using the low-level <xref:Microsoft.Xrm.Sdk.Client>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> classes. You should be able to replace those with the CrmServiceClient class. The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> is deprecated.

More information:

- [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md).
- [Deprecation of Office365 authentication type and OrganizationServiceProxy class for connecting to Dataverse](/power-platform/important-changes-coming#deprecation-of-office365-authentication-type-and-organizationserviceproxy-class-for-connecting-to-common-data-service)

### Use Task Parallel Library with CrmServiceClient

To achieve optimum throughput you should use multiple-threads. The Task Parallel Library (TPL) makes developers more productive by simplifying the process of adding parallelism and concurrency to applications.

TPL can be used with <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> because CrmServiceClient includes a <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.Clone> method that allows for managing multiple instances of the client with TPL. For an example, see [Sample: Task Parallel Library with CrmServiceClient](xrm-tooling/sample-tpl-crmserviceclient.md).

## Frequently asked questions

This section includes frequently asked questions. If you have questions that are not answered, please post them using the **Feedback** button at the bottom of this page to submit feedback about this page.

### I'm using an ETL application I licensed. How do I get optimum throughput?

Work with the ETL application vendor to learn which settings to apply. Make sure you are using a version of the product that supports the Retry-After behavior.

### Do these limits apply to Relevance Search?

No. Relevance search is a different API (`api/search` rather than `api/data`) and has different rules. When using the relevance search API, there is a throttling limit of one request per second for each user.

More information: [Search across table data using relevance search](webapi/relevance-search.md)

### How do these limits apply to how many requests a user is entitled to each day?

These limits are not related to entitlement limits. More information: [Entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits)

### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Dataverse API limits overview](../../maker/data-platform/api-limits-overview.md)<br />
[Use Dataverse Web API](webapi/overview.md)<br />
[Use Dataverse Organization service](org-service/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]