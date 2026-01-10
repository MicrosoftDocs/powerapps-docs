---
title: "Service protection API limits (Microsoft Dataverse) | Microsoft Docs"
description: "Understand what a developer needs to do to manage service protection limits for API requests."
ms.date: 01/09/2026
ms.reviewer: jdaly
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# Service protection API limits

To ensure consistent availability and performance for everyone, the system applies limits to how APIs are used. These limits detect when client applications make extraordinary demands on server resources.

These limits don't affect normal users of interactive clients. They affect only client applications that perform an extraordinary volume of API requests. These limits protect the Microsoft Dataverse platform from random and unexpected surges in request volumes that threaten its availability and performance.

When a client application makes extraordinarily demanding requests, Dataverse follows the common pattern for online services. It returns an error that indicates too many requests were received.

- With the Web API, Dataverse returns a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error.
- With the Dataverse SDK for .NET, you get an [OrganizationServiceFault](/dotnet/api/microsoft.xrm.sdk.organizationservicefault) error with one of three specific error codes.

[Learn about the Service protection API limit errors](#service-protection-api-limit-errors)


## Impact on client applications

Client applications are responsible for managing service protection API limit errors. How you manage this error depends on the nature of the application. 

### Interactive client applications

The service protection limits are high enough that it should be rare for an individual using an interactive client application to encounter them during normal usage. However, it's possible when the client application allows for bulk operations. Client application developers should be aware of how service protection API limits are enforced and design the UI to reduce the potential for users to send extremely demanding requests to the server. Even when they do this, they should still expect that service protection API limit errors can occur and be prepared to handle them.

Client application developers shouldn't just throw the error to display the message to the user. The error message isn't intended for end users. [Learn about specific strategies to retry operations](#retry-operations).

### Data integration applications

Applications designed to load data into Dataverse or perform bulk updates must manage service protection API limit errors. These applications prioritize throughput so they can complete their work in the minimum amount of time. These applications must have a strategy to retry operations. There are several strategies that they can apply to get the maximum throughput. [Learn how to maximize throughput](#how-to-maximize-throughput).

### Portal applications

Portal applications typically send requests from anonymous users through a service principal account. Because the service protection API limits are based on a per user basis, portal applications can hit service protection API limits based on the amount of traffic the portal experiences. Like interactive client applications, don't display service protection API limits errors to the portal end user. The UI for the portal should disable further requests and display a message that the server is busy. The message might include the time when the application can begin accepting new requests calculated using [the Retry-After duration](#the-retry-after-duration) returned with the error.

## Impact on plug-ins and custom workflow activities

Plug-ins and custom workflow activities apply business logic triggered by incoming requests. Service protection limits don't apply to data operations that originate from plug-ins and custom workflow activities. Plug-ins and custom workflow activities run within the isolated sandbox service. Dataverse operations invoked on the sandbox service don't use the public API endpoints.

If your application performs operations that trigger custom logic, the number of requests sent by plug-ins or custom workflow activities doesn't count towards service protection API limits. However, the extra computation time that these operations contribute is added to the initial request that triggered them. This computation time is part of the service protection API limits. [Learn how the system enforces Service Protection API Limits](#how-the-system-enforces-service-protection-api-limits).

## Retry operations

When a service protection API limit error occurs, it provides a value indicating the duration before any new requests from the user can be processed.

- When a 429 error is returned from the Web API, the response includes a [Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After) header with number of seconds.
- With the SDK for .NET, a [TimeSpan](/dotnet/api/system.timespan) value is returned in the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> collection with the key `Retry-After`.

### The Retry-After duration

The `Retry-After` duration depends on the nature of the operations that were sent in the preceding 5-minute period. The more demanding the requests are, the longer it takes for the server to recover.

Today, because of the way the limits are evaluated, you can expect to exceed the number of requests and execution time limits for a 5-minute period before the service protection API limits take effect. However, exceeding the number of concurrent requests returns an error immediately. If the application continues to send such demanding requests, the duration is extended to minimize the impact on shared resources. This extension causes the individual retry-after duration period to be longer, which means your application sees longer periods of inactivity while it's waiting. This behavior might change in the future.

When possible, try to achieve a consistent rate by starting with a lower number of requests and gradually increasing until you start hitting the service protection API limits. After that, let the server tell you how many requests it can handle within a 5-minute period. Keeping your maximum number of requests limited within this 5-minute period and gradually increasing keeps the retry-after duration low, optimizing your total throughput and minimizing server resource spikes.

### Interactive application retry

If the client is an interactive application, display a message that the server is busy while you retry the request the user made. You might want to provide an option for the user to cancel the operation. Don't allow users to submit more requests until the previous request you sent is complete.

### Non-interactive application retry

If the client isn't interactive, wait for the duration to pass before sending the request again. To pause the execution of the current task, use [Task.Delay](/dotnet/api/system.threading.tasks.task.delay) or equivalent methods.

### How to retry

The following section describes how to retry .NET applications by using the Dataverse SDK for .NET or Web API:

#### [SDK for .NET](#tab/sdk)


If you're using the SDK for .NET, use the [PowerPlatform.Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) or [Xrm.Tooling.Connector.CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes. These classes implement the [IOrganizationService](xref:Microsoft.Xrm.Sdk.IOrganizationService) methods and can manage any service protection API limit errors that are returned.

Starting with versions after [9.0.2.16 (May 2019)](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/9.0.2.16) of [Xrm.Tooling.Connector](xref:Microsoft.Xrm.Tooling.Connector), the client automatically pauses and resends the request after the `Retry-After` duration period.

If your application currently uses the low-level [Xrm.Sdk.Client.OrganizationServiceProxy](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy) or [Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient](xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient) classes, replace those classes with the `ServiceClient` or `CrmServiceClient` class. The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> class is deprecated.

More information:

- [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md).
- [Deprecation of Office365 authentication type and OrganizationServiceProxy class for connecting to Dataverse](/power-platform/important-changes-coming#deprecation-of-office365-authentication-type-and-organizationserviceproxy-class-for-connecting-to-common-data-service)


#### [Web API](#tab/webapi)

If you're using the Web API with a client library, you might find that it supports the retry behavior expected for 429 errors. Check with the client library publisher.

If you're using PowerShell, the PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) [MaximumRetryCount parameter](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-maximumretrycount) specifies how many times PowerShell retries a request when a failure code is between 400 and 599, inclusive, or 304 is received. This means PowerShell retries Dataverse service protection 429 errors when you include a value for this parameter. [Learn more about managing Dataverse service protection limits using PowerShell](webapi/use-ps-and-vscode-web-api.md#manage-dataverse-service-protection-limits).

If you wrote your own library, you can include behaviors to be similar to the one included in this sample code for a helper [WebAPIService class library (C#)](webapi/samples/webapiservice.md).

```csharp
/// <summary>
/// Specifies the Retry policies
/// </summary>
/// <param name="config">Configuration data for the service</param>
/// <returns></returns>
static IAsyncPolicy<HttpResponseMessage> GetRetryPolicy(Config config)
{
    return HttpPolicyExtensions
      .HandleTransientHttpError()
      .OrResult(httpResponseMessage => httpResponseMessage.StatusCode == System.Net.HttpStatusCode.TooManyRequests)
      .WaitAndRetryAsync(
         retryCount: config.MaxRetries,
         sleepDurationProvider: (count, response, context) =>
         {
            int seconds;
            HttpResponseHeaders headers = response.Result.Headers;

            if (headers.Contains("Retry-After"))
            {
               seconds = int.Parse(headers.GetValues("Retry-After").FirstOrDefault());
            }
            else
            {
               seconds = (int)Math.Pow(2, count);
            }
            return TimeSpan.FromSeconds(seconds);
         },
         onRetryAsync: (_, _, _, _) => { return Task.CompletedTask; }
      );
}
```

This example uses [Polly](https://github.com/App-vNext/Polly), a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.

#### HTTP response headers

If you're using HTTP requests with the Web API, you can track the remaining limit values by using the following HTTP response headers:

|Header  |Value Description  |
|---------|---------|
|`x-ms-ratelimit-burst-remaining-xrm-requests`|The remaining number of requests for this connection|
|`x-ms-ratelimit-time-remaining-xrm-requests`|The remaining combined duration for all connections using the same user account|

Don't depend on these values to control how many requests you send. They're intended for debugging purposes. If you're removing the affinity cookie, these values are reset when you connect to a different server.

---

## How the system enforces Service Protection API Limits

Two of the service protection API limits use a five-minute (300 second) sliding window. If either limit exceeds the preceding 300 seconds, the system returns a service protection API limit error on subsequent requests. This error protects the service until the Retry-After duration ends.

The system evaluates service protection API limits for each user. Each authenticated user has an independent limit. The system limits only those user accounts that make extraordinary demands. Other users don't experience any impact.

The system enforces service protection API limits based on three facets:

- The number of requests that a user sends.
- The combined execution time that the system requires to process requests that a user sends.
- The number of concurrent requests that a user sends.

If the system enforced the limit only on the number of requests that a user sends, it would be possible to bypass it. The system adds the other facets to counter these attempts. For example:

- You could send fewer requests by bundling them in batch operations.
  - The combined execution time limit counters this limit.
- Rather than sending requests individually in succession, you could send a large number of concurrent requests before service protection API limits enforce.
  - The concurrent request limit counters this limit.

Each web server that your environment makes available enforces these limits independently. Most environments have more than one web server. Trial environments allocate only a single web server. Multiple factors determine the actual number of web servers that your environment makes available. Dataverse provides these factors as part of the managed service. One of the factors is how many user licenses you purchase.

The following table describes the default service protection API limits that the system enforces *per web server*:

|Measure|Description|Limit per web server|
|--|--|--|
|Number of requests|The cumulative number of requests that the user makes.|6,000 within the five-minute sliding window|
|Execution time|The combined execution time of all requests that the user makes.| 20 minutes (1,200 seconds) within the five-minute sliding window|
|Number of concurrent requests|The number of concurrent requests that the user makes.|52 or higher|

> [!IMPORTANT]
> These limits can change and might vary between different environments. These numbers represent default values and give you some idea of what values you can expect.



## Service protection API limit errors

This section describes the three types of service protection API limit errors that the system can return. It also describes factors that cause these errors and possible mitigation strategies.

- The **Error code** is the numerical error value that the SDK for .NET <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> returns.
- The **Hex code** is the hexadecimal error value that the Web API returns.

### Number of requests

This limit counts the total number of requests during the preceding 300-second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015902`|`0x80072322`|`Number of requests exceeded the limit of 6000 over time window of 300 seconds.`|

A typical user of an interactive application doesn't send 1,200 requests per minute to exceed this limit unless the application enables users to perform bulk operations.

For example, if a list view enables selection of 250 records at a time and allows a user to perform some operation on all these records, the user needs to perform this operation 24 times in a span of 300 seconds. The user needs to complete the operation on each list within 12.5 seconds.

If your application provides this capability, consider some of the following strategies:

- Decrease the total number of records that users can select in a list. If the number of items displayed in a list is reduced to 50, the user needs to perform this operation 120 times within 300 seconds. The user must complete the operation on each list within 2.5 seconds.
- Combine the selected operations into a batch. A batch can contain up to 1,000 operations and avoids the number of requests limit. However, you need to be prepared for the execution time limit.

### Execution time

This limit tracks the combined execution time of incoming requests during the preceding 300-second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015903`|`0x80072321`|`Combined execution time of incoming requests exceeded limit of 1,200,000  milliseconds over time window of 300 seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.`|

Some operations require more resources than others. Batch operations, importing solutions, and highly complex queries can be very demanding. These operations might also be performed simultaneously in concurrent requests. Therefore, within the 5-minute window, you can request operations that require more than 20 minutes of combined computation time.

You can encounter this limit when you use strategies that involve batch operations and concurrent requests to avoid the number of requests limit.

### Concurrent requests

This limit tracks the number of concurrent requests.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

Client applications aren't limited to sending individual requests sequentially. The client might apply parallel programming patterns or various methods to send multiple requests simultaneously. The server can detect when it's responding to multiple requests from the same user simultaneously. If this number of concurrent requests is exceeded, the server throws this error. The limit might be higher than 52 in some cases.

Sending concurrent requests can be a key part of a strategy to maximize throughput, but it's important to keep it under control. When you use [Parallel Programming in .NET](/dotnet/standard/parallel-programming/), the default degree of parallelism depends on the number of CPU cores on the server running the code. It shouldn't exceed the limit. You can set the [ParallelOptions.MaxDegreeOfParallelism Property](/dotnet/api/system.threading.tasks.paralleloptions.maxdegreeofparallelism) to define a maximum number of concurrent tasks.

[Learn about sending parallel requests](send-parallel-requests.md).

## How to maximize throughput

When you have an application that must prioritize throughput to move the most data in the shortest period, apply the following strategies.

### Let the server tell you how much it can handle

Don't try to calculate how many requests to send at a time. Each environment can be different. Gradually increase the rate you send requests until you begin to hit limits and then depend on the service protection API limit `Retry-After` value to tell you when to send more. This value keeps your total throughput at the highest possible level.

### Use multiple threads

The higher limit on number of concurrent threads is something your application can use to have a significant improvement in performance. This improvement is true if your individual operations are relatively quick. Depending on the nature of the data you're processing, you might need to adjust the number of threads to get optimum throughput. [Learn about sending requests in parallel](send-parallel-requests.md).

### Avoid large batches

*Batching* refers to sending multiple operations in a single request.

Most scenarios are fastest sending single requests with a high degree of parallelism. If you feel batch size might improve performance, start with a small batch size of 10 and increase concurrency until you start getting service protection API limit errors that you retry.

With the SDK for .NET, this approach means using <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>, which typically allows sending up to 1,000 operations in a request. The main benefit this approach provides is that it reduces the total amount of XML payload that must be sent over the wire. This approach provides some performance benefit when network latency is an issue. For service protection limits, it increases the total execution time per request. Larger sized batches increase the chance you encounter execution time limits rather than limits on the number of requests.

In the past, `ExecuteMultiple` operations were limited to just two at a time because of the impact on performance that this limit could have. This limit is no longer the case, because service protection execution time API limits have made that limit redundant.

When using the Web API, the smaller JSON payload sent over the wire for individual requests means that network latency isn't an issue. [Learn about executing batch operations using the Web API](webapi/execute-batch-operations-using-web-api.md).

> [!NOTE]
> Batch operations aren't a valid strategy to bypass entitlement limits. Service protection API limits and entitlement limits are evaluated separately. Entitlement limits are based on CRUD operations and accrue whether or not they're included in a batch operation. [Learn about entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits).

## Strategies to manage service protection API limits

This section describes ways that you can design your clients and systems to avoid service protection API limit errors. You might also want to consider how you manage your licenses to reduce the impact.

### Update your client application

Dataverse has enforced Service Protection API limits since 2018. However, many client applications were written before these limits existed. These clients don't expect these errors and can't handle the errors correctly. Update these applications and apply the patterns to [Retry operations](#retry-operations) described previously.

### Move towards real-time integration

The main point of service protection API limits is to smooth out the impact of highly demanding requests that occur over a short period of time. If your current business processes depend on large periodic nightly, weekly, or monthly jobs that attempt to process large amounts of data in a short period of time, consider how you might enable a real-time data integration strategy. If you can move away from processes that require highly demanding operations, you can reduce the impact service protection limits have.


## Frequently asked questions

This section includes frequently asked questions. If you have questions that aren't answered, post them by using the **Feedback** button at the bottom of this page to submit feedback about this page.

### I'm using an ETL application I licensed. How do I get optimum throughput?

Work with the ETL application vendor to learn which settings to apply. Make sure you're using a version of the product that supports the Retry-After behavior.

### Do these limits apply to Dataverse search?

No. Dataverse native search uses a different API (`api/search` rather than `api/data`) and has different rules. When you use the Dataverse search API, there's a throttling limit of one request per second for each user.

[Learn about Dataverse Search Service Protection Limits](search/overview.md#service-protection-limits).

### How do these limits apply to how many requests a user is entitled to each day?

These limits aren't related to entitlement limits. [Learn about entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits).

### Are limits applied differently for application users?

No. The system applies the same limits to all users.

### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Dataverse API limits overview](../../maker/data-platform/api-limits-overview.md)<br />
[Use Dataverse Web API](webapi/overview.md)<br />
[Use Dataverse SDK for .NET](org-service/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
