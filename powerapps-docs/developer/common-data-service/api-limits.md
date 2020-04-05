---
title: "Service Protection API Limits (Common Data Service) | Microsoft Docs" 
description: "Understand the service protection limits for API requests." 
ms.custom: ""
ms.date: 04/05/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Service Protection API Limits

To ensure consistent availability and performance for everyone we apply some limits to how APIs are used. These limits, sometimes called *throttles*, are designed to detect when client applications are making extraordinary demands on server resources.

The limits should not affect normal users of interactive clients. Only client applications that perform extraordinary API requests should be affected. The limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Common Data Service platform.

When a client application makes extraordinarily demanding requests, the Common Data Service follows the common pattern for online services. We return an error indicating that too many requests have been made.

- With the Web API we return a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error.
- With the Organization Service you will get an [OrganizationServiceFault](/dotnet/api/microsoft.xrm.sdk.organizationservicefault) error with one three specific error codes. More information: [API Limit Errors returned](#api-limit-errors-returned)


## Impact on client applications

It is the responsibility of the client application to manage API limit errors. Exactly how to manage this error depends on the nature of the application. 

### Interactive client applications

The service protection limits are high enough that it should be rare for an individual using an interactive client application to encounter them during normal usage. However, it is possible if the client application allows for bulk operations. Client application developers should be aware of how API limits are enforced and design the UI to reduce the potential for users to send extremely demanding requests to the server. But they should still expect that API Limit errors can occur and be prepared to handle them.

Client application developers should not simply throw the error to display the message to the user. The error message is not intended for end users. See [Retry operations](#retry-operations) for specific strategies.

### Data integration applications

Applications designed to extract, transfer, and load (ETL) data into CDS must also be able to manage API limit errors. These typically non-interactive applications prioritize throughput so they can complete their work in the minimum amount of time. These applications must have a strategy to retry operations. There are several strategies that they can apply to get the maximum throughput. More information: [How to maximize throughput](#how-to-maximize-throughput).

### Portal applications

Portal applications typically send requests from anonymous users through a single service principal account. Because the API limits are based on a per account basis, portal applications can hit API limits. Like interactive client applications, it isn't expected that the API limits errors are thrown and displayed to the user. It is expected that the UI should disable further requests and display a message that the server is busy. The message may include the time when the application can begin accepting new requests.

## Impact on plug-ins and custom workflow activities

Service protection limits are not applied to plug-ins and custom workflow activities. Plug-ins and custom workflow activities are uploaded and run within the isolated sandbox service. Common Data Service operations invoked on the sandbox service do not use the public API endpoints.

If your application performs operations that trigger custom logic that are performed by plug-ins or custom workflow activities, the number of requests sent by plug-ins or custom workflow activities will not be counted towards API limits. However, the additional computation time that these operations contribute will be added to the initial request that triggered them.

## Retry operations

When an API Limit error occurs, it will provide a value indicating the duration before any new requests can be processed.

- When a 429 error is returned from the Web API, the response will include a [Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After) with number of seconds.
- With the Organization service, a [TimeSpan](/dotnet/api/system.timespan) value is returned in the [OrganizationServiceFault.ErrorDetails](/dotnet/api/microsoft.xrm.sdk.baseservicefault.errordetails#Microsoft_Xrm_Sdk_BaseServiceFault_ErrorDetails) collection with the key `Retry-After`.

If the client is an interactive application, your application should display a message that the server is busy while you re-try the request the user made. Don't allow users to submit more requests until the previous request you sent has completed.

If the client is not interactive, the common practice is to simply wait for the duration to pass before sending the request again. This is commonly done by pausing the execution of the current thread using [Thread.Sleep](/dotnet/api/system.threading.thread.sleep) or equivalent methods.

The duration will depend on the nature of the operations that have been sent in the preceding 5 minute period. The more demanding the requests are, the longer it will take for the server to recover.

Today, because of the way the limits are evaluated, you can expect to exceed all limits for a 5 minute period before the service protection API limits will take effect. If the application continues to send such demanding requests, the duration will be extended to minimize the impact on shared resources. This will cause the individual retry-after duration period to be longer, which means your application will see longer periods of inactivity while it is waiting.

Instead, we recommend trying to achieve a consistent rate by starting with a lower number of requests and gradually increasing until you start hitting the API limits. After that, let the server tell you how many requests it can handle within a 5 minute period. Keeping your maximum number of requests limited within this 5 minute period will keep the retry-after duration low, optimizing your total throughput and minimizing server resource spikes.

## How API limits are enforced

The API limits are evaluated within a 5 minute (300 second) sliding window. If any of the limits are exceeded within the preceding 300 seconds, an API Limit error will be returned on subsequent requests to protect the service.

The API limits are evaluated per user. Each authenticated user is limited independently. Only those users accounts which are making extraordinary demands will be limited. Other users will not be impacted.

API Limits are enforced based on three facets:

- The number of requests were sent by a user.
- The combined execution time was required to process requests.
- The number of concurrent requests were sent.

Each of these facets are designed to address different ways that people could attempt to bypass API limits if the limits were based only on the number of requests that are sent individually in succession. For example:

- You can send fewer requests by bundling them in batch operations.
  - The combined execution time limit will counter this.
- Rather than sending requests individually in succession, you can send a large number of concurrent requests within the 5 minute sliding window before API limits are enforced.
  - The concurrent request limit will counter this.

Each web server available to your environment will enforce these limits independently. Most environments will have more than one web server. Trial environments are allocated only a single web server. The actual number of web servers that are available to your environment depends on multiple factors that are part of the managed service we provide. One of the factors is how many user licenses you have purchased.

The following table describes the default API limits enforced *per web server* within the 5 minute sliding window.

|Measure|Description|Limit per web server|
|--|--|--|
|Number of requests|The cumulative number of requests made by the user.|6000|
|Execution time|The combined execution time of all requests made by the user.| 20 minutes (1200 seconds)|
|Number of concurrent requests|The number of concurrent requests made by the user|52|

## API Limit Errors returned

This section describes the three types of API limit errors that can be returned as well as factors that cause these errors and possible mitigation strategies.

- The **Error code** is the numerical error value returned by the Organization Service <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails>.
- The **Hex code** is the hexadecimal error value returned by the Web API.

### Number of requests

This limit counts the total number of requests during the preceding 300 second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015902`|`0x80072322`|`Number of requests exceeded the limit of 6000 over time window of 300 seconds.`|

It is not expected that a typical user of an interactive application will be able to send 1,200 requests per minute to exceed this limit unless the application enables users to perform operations on selected items in a list.

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

This limit tracks the total number of concurrent requests during the preceding 300 second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

Client applications are not limited to sending requests individually in succession. The client may apply parallel programming patterns or various methods to send multiple requests simultaneously using JavaScript running in the browser. The server can detect when it is responding to multiple requests simultaneously. If this number of concurrent requests is exceeded during the 5 minute window, this error will be thrown.

Sending concurrent requests can be a key part of a strategy to maximize throughput, but it is important to keep it under control.

When using [Parallel Programming in .NET](/dotnet/standard/parallel-programming/) the default degree of parallelism depends on the number of CPU cores on the server running the code. This can be increased by TODO, but it should not exceed 52. The [ParallelOptions.MaxDegreeOfParallelism Property](/dotnet/api/system.threading.tasks.paralleloptions.maxdegreeofparallelism) can be set to define a maximum number of concurrent tasks.

For client-side JavaScript TODO

    <!-- I'm finding many different libraries that provide a way to limit concurrency:
    *    ES6 Promise Pool Runs Promises in a pool that limits their concurrency
    *    Vilic Vane's Promise Pool offers a similar API.
    *    Bluebird includes Promise.map(), which takes a concurrency option.
    *    Similarly, λ (a.k.a. contra) has λ.concurrent() with the optional cap parameter.
    *    With Q, you can use qlimit.
    *    Async does not use promises, but offers a queue() function. -->

## How to maximize throughput

When you have an ETL application that must prioritize throughput to move the most data in the shortest period, there are some strategies you can apply.

### Let the server tell you how much it can handle

You don't need to calculate how many requests to send at a time. Send as many individual requests as you want and then depend on the API Limit `Retry-After` value to tell you when to send more. This value will keep your total throughput at the highest possible level.

### Use multiple threads

The higher limit on number of concurrent threads is something your ETL application can use to have a significant improvement in performance. This is particularly true if your individual operations are relatively quick. Depending on the nature of the data you are processing, you may need to adjust the number of threads to get optimum throughput.

### Avoid batching

In the Organization Service the conventional wisdom has been to employ the ExecuteMultiple message to bundle multiple operations. The main benefit this provides is that it reduces the total amount of SOAP XML payload that must be sent over the wire. This provides some performance benefit when network latency is an issue.

In the past, ExecuteMultiple operations were limited to just 2 at a time because of the impact on performance that this could have. This is no longer the case, because API Limits have made that limit redundant.

Most scenarios will be fastest sending single requests with a high degree of parallelism. If you feel batch size might improve performance, it is best to start with a small batch size of 10 and increase concurrency until you start getting API limit errors that you will retry.

When using the Web API, the smaller JSON payload sent over the wire means that network latency is not an issue. The total amount of payload that is sent using $batch is greater than sending individual requests. $batch should only be used if you want to managed transactions using changesets.

> [!NOTE]
> Batch operations are not a valid strategy to bypass entitlement limits. Entitlement limits are based on CRUD operations and accrue whether or not they are included in a batch operation.

### Remove the affinity cookie

When you make a connection to a service on Azure a cookie is returned with the response and all your subsequent requests will attempt to be routed to the same server unless capacity management forces it to go to another server. If you remove this cookie, each request you send will be routed any of the eligible servers which can increase throughput.

> [!NOTE]
> This strategy should only be used by ETL applications that are seeking to optimize throughput. Interactive client applications benefit from the affinity cookie because it allows for reusing cached data that would otherwise need to be re-created leading to poorer performance.

The following code shows how to disable cookies when initializing an HttpClient with the Web API:

```csharp
HttpClient client = new HttpClient(new WebRequestHandler()
    { UseCookies = false },
    disposeHandler: true);
```

If you are using CrmServiceClient, add the following to the AppSettings node in the App.config file.

```xml
<add key="PreferConnectionAffinity" value="false" /> 
```

## Strategies to manage API limits

This section describes ways that you can design your clients and systems to avoid API limit errors. You may also want to consider how you manage your licenses to reduce the impact.

### Update your client application

API limits have been applied to CDS since 2018, but there are many client applications written before these limits existed. These clients didn't expect these errors and can't handle the errors correctly. You should update these applications and apply the patterns described in the [Using the Organization Service](#using-the-organization-service) or [Using the Web API](#using-the-web-api) sections below.

### Move towards real-time integration

Remember that the main point of API limits is to smooth out the impact of highly demanding requests occurring over a short period of time. If your current business processes depend on large periodic nightly, weekly, or monthly jobs which attempt to process large amounts of data in a short period of time, consider how you might enable a real-time data integration strategy. If you can move away from processes that require highly demanding operations, you can reduce the impact API limits will have.

## Using the Organization Service

If you are using the Organization Service, we recommend that you use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>. This class implements the IOrganizationService methods and can manage any API Limit errors that are returned. 

Since Xrm.Tooling.Connector version 9.0.2.16, it will automatically pause and re-send the request after the Retry-After duration period.

If your application is currently using the low-level <xref:Microsoft.Xrm.Sdk.Client>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> classes. You should be able to replace those with the CrmServiceClient class. More information: [Build Windows client applications using the XRM tools](/xrm-tooling/build-windows-client-applications-xrm-tools).

## Using the Web API

TODO need to provide an example

### HTTP Response headers

If you are using HTTP requests with the Web API, you can track the remaining limit values with the following HTTP response headers:

|Header  |Value Description  |
|---------|---------|
|`x-ms-ratelimit-burst-remaining-xrm-requests`|The remaining number of requests for this connection|
|`x-ms-ratelimit-time-remaining-xrm-requests`|The remaining combined duration for all connections using the same user account|

You should not depend on these values to control how many requests you send. They are intended for debugging purposes. If you are removing the affinity cookie, these values are re-set when you connect to a different server.

## Frequently asked questions

### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Common Data Service API limits overview](../../maker/common-data-service/api-limits-overview.md)<br />
[Use Common Data Service Web API](webapi/overview.md)<br />
[Use Common Data Service Organization Service](org-service/overview.md)
