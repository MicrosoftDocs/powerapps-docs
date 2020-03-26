---
title: "Service Protection API Limits (Common Data Service) | Microsoft Docs" 
description: "Understand the service protection limits for API requests." 
ms.custom: ""
ms.date: 11/23/2019
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

To ensure consistent availability and performance for everyone we apply some limits to how APIs are used. We limit the number of concurrent connections per user account, the number of API requests per connection, and the amount of execution time that can be used for each connection. These are evaluated within a five minute sliding window. When one of these limits is exceeded, an exception will be thrown by the platform.

Service protection API limits help ensure that users running applications cannot interfere with each other based on resource constraints. The limits will not affect normal users of the platform. Only applications that perform a large number of API requests may be affected. The limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Common Data Service platform.

Since plug-ins and custom workflow activities execute on the server independent of a logged on user, API calls made from plug-in code will not count against service protection API limits. 

## Limits

> [!IMPORTANT]
> These limits are applied per web server. Each scale group has multiple web servers that may process each request depending on load balancing. These numbers represent a single web server and therefore the lowest possible level of throughput due to these limits. Your actual throughput should be higher.
> 
> You will see significant differences between trial environments and production environments. Trial environments have fewer resources allocated to them so they will encounter these limits more easily than production environments.
> 
> Don't focus too much on the numbers here. The important thing to understand is that applications which depend on high volume data operations should be designed to respond to signals that the server will send to indicate when limits are reached. Don't try to hard-code solutions based on the numbers here. Instead use the techniques described below to get the highest possible throughput by responding to the signals the service will send.

Service protection limits expect that the application uses multiple threads to maximize performance. Each thread represents a separate connection and each connection is evaluated on a 5 minute (300 second) sliding window.

Within that 5 minute sliding window, there are three aspects that are measured as described in the following table:

|Measure|Description|Limit per web server|
|--|--|--|
|Number of requests|The actual number of requests made per connection.|6000|
|Execution time|The combined duration for all connections using the same user account| 20 minutes (1200 seconds)|
|Number of connections|The number of connections using the same user account|52|

The combination of **Number of requests** and **Execution time** accounts for the fact that some operations require more system resources than others. Performing a complex query requires more system resources that creating or updating a single record.

While API calls made from plug-in code will not be counted against the number of requests, the execution time of those calls will be applied to the originating call.

Some known long-running system operations, such as ImportSolution, will not have the full execution time included in the calculation of the limit. The contribution of these calls towards the limit calculation is capped at 5 minutes if the actual execution time is greater.

If your application has the potential to exceed these limits, please apply the guidance given in the [What should I do if my application exceeds the limit?](#what-should-i-do-if-my-application-exceeds-the-limit) section below.

Depending on the nature of the data you are processing, you can adjust the number of concurrent connections to get the maximum throughput. If each operation is relatively quick, use more connections.

## What happens when the limit is exceeded?

When the limit is exceeded, all requests for the same connection will return error responses.

If you use the .NET SDK assemblies, the platform will respond with a `FaultException<OrganizationServiceFault>` WCF Fault.  

| Error Code | Message |
|------------|-------------------------------------|
|`-2147015902`|`Number of requests exceeded the limit of 6000, measured over time window of 300 seconds.`|
|`-2147015903`|`Combined execution time of incoming requests exceeded limit of 1,200,000 milliseconds over time window of 300 seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.`|
|`-2147015898`|`Number of concurrent requests exceeded the limit of 52`|

If you use HTTP requests with the Web API, the response will include the same messages, but with:<br />
`StatusCode` : `429`

All requests will return these error responses until the volume of API requests falls below the limit. If you get these responses, your application should stop sending API requests until the volume of requests is below the limit.

> [!TIP]
> If you are using HTTP requests with the Web API, you can track the remaining limit values with the following HTTP response headers:
> 
> |Header  |Value Description  |
> |---------|---------|
> |`x-ms-ratelimit-burst-remaining-xrm-requests` |The remaining number of requests for this connection|
> |`x-ms-ratelimit-time-remaining-xrm-requests`  |The remaining combined duration for all connections using the same user account|

## What should I do if my application exceeds the limit?

When your application exceeds the limit, the error response from the server may specify the amount of time you should wait before sending more requests. The response object is slightly different if you are using SDK assemblies or HTTP requests with the Web API.

For a discussion of best practices, see [Azure Architecture Best Practices Transient fault handling](/azure/architecture/best-practices/transient-faults)

[The Polly Project](https://www.thepollyproject.org/) is a library which includes capabilities for dealing with transient faults using execution policies.

### HTTP requests with the Web API

If you encounter a 429 error code you can look for the `Retry-After` HTTP header included in the error response. This will contain a value in seconds indicating how long you should wait before making a follow-up request. More information [MDN web docs Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After)

### SDK assemblies

> [!NOTE]
> You do not need to apply these patterns when:
>
>  - Your code will run within a plug-in or custom workflow activity. You do not need to apply these patterns because service protection limits are not applied in these cases.
>  - You use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>. These patterns are built-in to that client. This is the recommended proxy class to use for client applications.
>
> You need to apply these patterns if you use the <xref:Microsoft.Xrm.Sdk.Client>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> proxy classes.

If you are using the SDK assemblies with the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> proxy classes, you can look for the `Retry-After` delay value in the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> property, using the key `"Retry-After"`. The value returned is a [TimeSpan](/dotnet/api/system.timespan) object.

## .NET SDK Assembly Example

The following example uses the [Retry class](#retry-class) described below to retrieve one account using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method. If the request fails because an API limit has been exceeded, the `Retry` class will wait according to a delay specified by the server and try again.

```csharp
var qe = new QueryExpression("account") { TopCount = 1 };
EntityCollection result = Retry.Do(() => service.RetrieveMultiple(qe));
```

### Retry class

The `Retry` class demonstrates how to retry requests that fail with transient errors based on known <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault> error codes. The `Retry` class waits before retrying. If the fault specifies a retry delay, wait according to the delay specified by the server. Else use exponential backoff to calculate the delay based on the number of retry attempts made.

```csharp
using System;
using System.ServiceModel;
using System.Threading;

public class Retry
{
    private const int RateLimitExceededErrorCode = -2147015902;
    private const int TimeLimitExceededErrorCode = -2147015903;
    private const int ConcurrencyLimitExceededErrorCode = -2147015898;

    public static TResult Do<TResult>(Func<TResult> func, int maxRetries = 3)
    {
        int retryCount = 0;

        while (true)
        {
            try
            {
                return func();
            }
            catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> ex) 
                when (IsTransientError(ex))
            {
                if (++retryCount >= maxRetries)
                {
                    throw;
                }

                if (ex.Detail.ErrorCode == RateLimitExceededErrorCode)
                {
                    // Use Retry-After delay when specified
                    delay = (TimeSpan)ex.Detail.ErrorDetails["Retry-After"];
                }
                else
                {
                    // else use exponential backoff delay
                    delay = TimeSpan.FromSeconds(Math.Pow(2, retryCount));
                }

                Thread.Sleep(delay);
            }
        }
    }

    private static bool IsTransientError(FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> ex)
    {
        // You can add more transient fault codes to retry here
        if (ex.Detail.ErrorCode == RateLimitExceededErrorCode ||
            ex.Detail.ErrorCode == TimeLimitExceededErrorCode ||
            ex.Detail.ErrorCode == ConcurrencyLimitExceededErrorCode)
        {
            return true;
        }

        return false;
    }
}
```

### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Common Data Service API limits overview](../../maker/common-data-service/api-limits-overview.md)<br />
[Use Common Data Service Web API](webapi/overview.md)<br />
[Use Common Data Service Organization Service](org-service/overview.md)
