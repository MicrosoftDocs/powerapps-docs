---
title: "Service protection API limits (Microsoft Dataverse) | Microsoft Docs" 
description: "Understand what a developer needs to do to manage service protection limits for API requests." 
ms.date: 11/26/2024
ms.reviewer: jdaly
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: sriknair 
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# Service protection API limits

To ensure consistent availability and performance for everyone, we apply some limits to how APIs are used. These limits are designed to detect when client applications are making extraordinary demands on server resources.

These limits shouldn't affect normal users of interactive clients. Only client applications that perform extraordinary volume of API requests should be affected. These limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Microsoft Dataverse platform.

When a client application makes extraordinarily demanding requests, the Dataverse follows the common pattern for online services. We return an error indicating that too many requests were received.

- With the Web API, we return a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error.
- With the Dataverse SDK for .NET, you get an [OrganizationServiceFault](/dotnet/api/microsoft.xrm.sdk.organizationservicefault) error with one of three specific error codes.

[Learn about the service protection API limit errors returned](#service-protection-api-limit-errors-returned)


## Impact on client applications

It's the responsibility of client applications to manage service protection API limit errors. Exactly how to manage this error depends on the nature of the application. 

### Interactive client applications

The service protection limits are high enough that it should be rare for an individual using an interactive client application to encounter them during normal usage. However, it's possible when the client application allows for bulk operations. Client application developers should be aware of how service protection API limits are enforced and design the UI to reduce the potential for users to send extremely demanding requests to the server. Even when they do this, they should still expect that service protection API limit errors can occur and be prepared to handle them.

Client application developers shouldn't just throw the error to display the message to the user. The error message isn't intended for end users. [Learn about specific strategies to retry operations](#retry-operations)

### Data integration applications

Applications designed to load data into Dataverse or perform bulk updates must manage service protection API limit errors. These applications prioritize throughput so they can complete their work in the minimum amount of time. These applications must have a strategy to retry operations. There are several strategies that they can apply to get the maximum throughput. [Learn how to maximize throughput](#how-to-maximize-throughput)

### Portal applications

Portal applications typically send requests from anonymous users through a service principal account. Because the service protection API limits are based on a per user basis, portal applications can hit service protection API limits based on the amount of traffic the portal experiences. Like interactive client applications, don't display service protection API limits errors to the portal end user. The UI for the portal should disable further requests and display a message that the server is busy. The message might include the time when the application can begin accepting new requests calculated using [the Retry-After duration](#the-retry-after-duration) returned with the error.

## Impact on plug-ins and custom workflow activities

Plug-ins and custom workflow activities apply business logic triggered by incoming requests. Service protection limits aren't applied to data operations that originate from plug-ins and custom workflow activities. Plug-ins and custom workflow activities are uploaded and run within the isolated sandbox service. Dataverse operations invoked on the sandbox service don't use the public API endpoints.

If your application performs operations that trigger custom logic, the number of requests sent by plug-ins or custom workflow activities won't be counted towards service protection API limits. However, the extra computation time that these operations contribute is added to the initial request that triggered them. This computation time is part of the service protection API limits. [Learn how service protection API limits are enforced](#how-service-protection-api-limits-are-enforced)

## Retry operations

When a service protection API limit error occurs, it provides a value indicating the duration before any new requests from the user can be processed.

- When a 429 error is returned from the Web API, the response includes a [Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After) header with number of seconds.
- With the SDK for .NET, a [TimeSpan](/dotnet/api/system.timespan) value is returned in the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> collection with the key `Retry-After`.

### The Retry-After duration

The `Retry-After` duration depends on the nature of the operations that were sent in the preceding 5-minute period. The more demanding the requests are, the longer it takes for the server to recover.

Today, because of the way the limits are evaluated, you can expect to exceed the number of requests and execution time limits for a 5-minute period before the service protection API limits take effect. However, exceeding the number of concurrent requests returns an error immediately. If the application continues to send such demanding requests, the duration is extended to minimize the impact on shared resources. This causes the individual retry-after duration period to be longer, which means your application sees longer periods of inactivity while it's waiting. This behavior might change in the future.

When possible, we recommend trying to achieve a consistent rate by starting with a lower number of requests and gradually increasing until you start hitting the service protection API limits. After that, let the server tell you how many requests it can handle within a 5-minute period. Keeping your maximum number of requests limited within this 5-minute period and gradually increasing keeps the retry-after duration low, optimizing your total throughput and minimizing server resource spikes.

### Interactive application retry

If the client is an interactive application, you should display a message that the server is busy while you retry the request the user made. You might want to provide an option for the user to cancel the operation. Don't allow users to submit more requests until the previous request you sent is complete.

### Non-interactive application retry

If the client isn't interactive, the common practice is to just wait for the duration to pass before sending the request again. This is commonly done by pausing the execution of the current task using [Task.Delay](/dotnet/api/system.threading.tasks.task.delay) or equivalent methods.

### How to retry

The following describes how to retry .NET applications using the Dataverse SDK for .NET or Web API:

#### [SDK for .NET](#tab/sdk)


If you're using the SDK for .NET, we recommend that you use the [PowerPlatform.Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) or [Xrm.Tooling.Connector.CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) classes. Those classes implement the [IOrganizationService](xref:Microsoft.Xrm.Sdk.IOrganizationService) methods and can manage any service protection API limit errors that are returned.

[Xrm.Tooling.Connector](xref:Microsoft.Xrm.Tooling.Connector) versions after [9.0.2.16 (May 2019)](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/9.0.2.16), it will automatically pause and resend the request after the `Retry-After` duration period.

If your application is currently using the low-level [Xrm.Sdk.Client.OrganizationServiceProxy](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy) or [Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient](xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient) classes, replace those with the `ServiceClient` or `CrmServiceClient` class. The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> is deprecated.

More information:

- [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md).
- [Deprecation of Office365 authentication type and OrganizationServiceProxy class for connecting to Dataverse](/power-platform/important-changes-coming#deprecation-of-office365-authentication-type-and-organizationserviceproxy-class-for-connecting-to-common-data-service)


#### [Web API](#tab/webapi)

If you're using the Web API with a client library, you might find that it supports the retry behavior expected for 429 errors. Check with the client library publisher.

If you're using PowerShell, the PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) [MaximumRetryCount parameter](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-maximumretrycount) specifies how many times PowerShell retries a request when a failure code is between 400 and 599, inclusive or 304 is received. This means PowerShell retries Dataverse service protection 429 errors when you include a value for this parameter. [Learn more about managing Dataverse service protection limits using PowerShell](webapi/use-ps-and-vscode-web-api.md#manage-dataverse-service-protection-limits)

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

#### HTTP Response headers

If you're using HTTP requests with the Web API, you can track the remaining limit values with the following HTTP response headers:

|Header  |Value Description  |
|---------|---------|
|`x-ms-ratelimit-burst-remaining-xrm-requests`|The remaining number of requests for this connection|
|`x-ms-ratelimit-time-remaining-xrm-requests`|The remaining combined duration for all connections using the same user account|

You shouldn't depend on these values to control how many requests you send. They're intended for debugging purposes. If you're removing the affinity cookie, these values are reset when you connect to a different server.

---

## How Service Protection API Limits are enforced

Two of the service protection API limits are evaluated within a 5 minutes (300 second) sliding window. If either limits are exceeded within the preceding 300 seconds, a service protection API Limit error is returned on subsequent requests to protect the service until the Retry-After duration ends.

The service protection API limits are evaluated per user. Each authenticated user is limited independently. Only those users accounts which are making extraordinary demands are limited. Other users won't be impacted.

Service protection API limits are enforced based on three facets:

- The number of requests sent by a user.
- The combined execution time required to process requests sent by a user.
- The number of concurrent requests sent by a user.

If the only limit was on the number of requests sent by a user, it would be possible to bypass it. The other facets were added to counter these attempts. For example:

- You could send fewer requests by bundling them in batch operations.
  - The combined execution time limit counters this.
- Rather than sending requests individually in succession, you could send a large number of concurrent requests before service protection API limits are enforced.
  - The concurrent request limit counters this.

Each web server available to your environment enforces these limits independently. Most environments have more than one web server. Trial environments are allocated only a single web server. The actual number of web servers that are available to your environment depends on multiple factors that are part of the managed service Dataverse provides. One of the factors is how many user licenses you purchased.

The following table describes the default service protection API limits enforced *per web server*:

|Measure|Description|Limit per web server|
|--|--|--|
|Number of requests|The cumulative number of requests made by the user.|6000 within the 5-minute sliding window|
|Execution time|The combined execution time of all requests made by the user.| 20 minutes (1,200 seconds) within the 5-minute sliding window|
|Number of concurrent requests|The number of concurrent requests made by the user|52 or higher|

> [!IMPORTANT]
> These limits are subject to change and may vary between different environments. These numbers represent default values and are provided to give you some idea of what values you can expect.



## Service Protection API Limit Errors returned

This section describes the three types of service protection API limit errors that can be returned as well as factors that cause these errors and possible mitigation strategies.

- The **Error code** is the numerical error value returned by the SDK for .NET <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails>.
- The **Hex code** is the hexadecimal error value returned by the Web API.

### Number of requests

This limit counts the total number of requests during the preceding 300-second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015902`|`0x80072322`|`Number of requests exceeded the limit of 6000 over time window of 300 seconds.`|

It isn't expected that a typical user of an interactive application is able to send 1,200 requests per minute to exceed this limit unless the application enables users to perform bulk operations.

For example, if a list view enables selection of 250 records at a time and allows a user to perform some operation on all these records, the user would need to perform this operation 24 times in a span of 300 seconds. The user would need to complete the operation on each list within 12.5 seconds.

If your application provides this capability, you should consider some of the following strategies:

- Decreasing the total number of records that can be selected in a list. If the number of items displayed in a list is reduced to 50, the user would need to perform this operation 120 times within 300 seconds. The user would have to complete the operation on each list within 2.5 seconds.
- Combine the selected operations into a batch. A batch can contain up to 1,000 operations and avoids the number of requests limit. However, you need to be prepared for the execution time limit.

### Execution time

This limit tracks the combined execution time of incoming requests during the preceding 300-second period.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015903`|`0x80072321`|`Combined execution time of incoming requests exceeded limit of 1,200,000  milliseconds over time window of 300 seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.`|

Some operations require more resources than others. Batch operations, importing solutions, and highly complex queries can be very demanding. These operations might also be performed simultaneously in concurrent requests. Therefore, within the 5-minute window it's possible to request operations that require more than 20 minutes of combined computation time.

This limit can be encountered when strategies using batch operations and concurrent requests are used to avoid the number of requests limit.

### Concurrent requests

This limit tracks the number of concurrent requests.

| Error code | Hex code | Message |
|------------|------------|-------------------------------------|
|`-2147015898`|`0x80072326`|`Number of concurrent requests exceeded the limit of 52.`|

Client applications aren't limited to sending individual requests sequentially. The client might apply parallel programming patterns or various methods to send multiple requests simultaneously. The server can detect when it's responding to multiple requests from the same user simultaneously. If this number of concurrent requests is exceeded, this error is thrown. The limit might be higher than 52 in some cases.

Sending concurrent requests can be a key part of a strategy to maximize throughput, but it's important to keep it under control. When using [Parallel Programming in .NET](/dotnet/standard/parallel-programming/) the default degree of parallelism depends on the number of CPU cores on the server running the code. It shouldn't exceed the limit. The [ParallelOptions.MaxDegreeOfParallelism Property](/dotnet/api/system.threading.tasks.paralleloptions.maxdegreeofparallelism) can be set to define a maximum number of concurrent tasks.

[Learn about sending parallel requests](send-parallel-requests.md)

## How to maximize throughput

When you have an application that must prioritize throughput to move the most data in the shortest period, there are some strategies you can apply.

### Let the server tell you how much it can handle

Don't try to calculate how many requests to send at a time. Each environment can be different. Gradually increase the rate you send requests until you begin to hit limits and then depend on the service protection API Limit `Retry-After` value to tell you when to send more. This value keeps your total throughput at the highest possible level.

### Use multiple threads

The higher limit on number of concurrent threads is something your application can use to have a significant improvement in performance. This is true if your individual operations are relatively quick. Depending on the nature of the data you're processing, you might need to adjust the number of threads to get optimum throughput. [Learn about sending requests in parallel](send-parallel-requests.md)

### Avoid large batches

*Batching* refers to sending multiple operations in a single request.

Most scenarios are fastest sending single requests with a high degree of parallelism. If you feel batch size might improve performance, it's best to start with a small batch size of 10 and increase concurrency until you start getting service protection API limit errors that you retry.

With the SDK for .NET this means using <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>, which typically allows sending up to 1,000 operations in a request. The main benefit this provides is that it reduces the total amount of XML payload that must be sent over the wire. This provides some performance benefit when network latency is an issue. For service protection limits it increases the total execution time per request. Larger sized batches increase the chance you encounter execution time limits rather than limits on the number of requests.

In the past, `ExecuteMultiple` operations were limited to just 2 at a time because of the impact on performance that this could have. This is no longer the case, because service protection execution time API limits have made that limit redundant.

When using the Web API, the smaller JSON payload sent over the wire for individual requests means that network latency isn't an issue. [Learn about executing batch operations using the Web API](webapi/execute-batch-operations-using-web-api.md)

> [!NOTE]
> Batch operations are not a valid strategy to bypass entitlement limits. Service protection API limits and Entitlement limits are evaluated separately. Entitlement limits are based on CRUD operations and accrue whether or not they are included in a batch operation. [Learn about entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits)

## Strategies to manage Service Protection API limits

This section describes ways that you can design your clients and systems to avoid service protection API limit errors. You might also want to consider how you manage your licenses to reduce the impact.

### Update your client application

Service Protection API limits have been applied to Dataverse since 2018, but there are many client applications written before these limits existed. These clients didn't expect these errors and can't handle the errors correctly. You should update these applications and apply the patterns to [Retry operations](#retry-operations) described previously.

### Move towards real-time integration

Remember that the main point of service protection API limits is to smooth out the impact of highly demanding requests occurring over a short period of time. If your current business processes depend on large periodic nightly, weekly, or monthly jobs which attempt to process large amounts of data in a short period of time, consider how you might enable a real-time data integration strategy. If you can move away from processes that require highly demanding operations, you can reduce the impact service protection limits have.


## Frequently asked questions

This section includes frequently asked questions. If you have questions that aren't answered, post them using the **Feedback** button at the bottom of this page to submit feedback about this page.

### I'm using an ETL application I licensed. How do I get optimum throughput?

Work with the ETL application vendor to learn which settings to apply. Make sure you're using a version of the product that supports the Retry-After behavior.

### Do these limits apply to Dataverse search?

No. Dataverse native search is a different API (`api/search` rather than `api/data`) and has different rules. When you use the Dataverse search API, there's a throttling limit of one request per second for each user.

[Learn about Dataverse Search Service Protection Limits](search/overview.md#service-protection-limits)

### How do these limits apply to how many requests a user is entitled to each day?

These limits aren't related to entitlement limits. [Learn about entitlement limits](../../maker/data-platform/api-limits-overview.md#entitlement-limits)

### Are limits applied differently for application users?

No. The limits are applied to all users in the same way.

### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Dataverse API limits overview](../../maker/data-platform/api-limits-overview.md)<br />
[Use Dataverse Web API](webapi/overview.md)<br />
[Use Dataverse SDK for .NET](org-service/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
