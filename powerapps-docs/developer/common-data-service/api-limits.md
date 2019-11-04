---
title: "API Limits (Common Data Service) | Microsoft Docs" 
description: "Understand the limits for API requests." 
ms.custom: ""
ms.date: 03/21/2019
ms.reviewer: "kvivek"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.author: "bsimons" 
manager: "annbe" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# API Limits

We limit the number of API requests made by each user, per organization instance, within a five minute sliding window. Additionally, we limit the number of concurrent requests that may come in at one time.  When one of these limits is exceeded, an exception will be thrown by the platform.

The limit will help ensure that users running applications cannot interfere with each other based on resource constraints. The limits will not affect normal users of the platform. Only applications that perform a large number of API requests may be affected. The limit will help provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Common Data Service platform.

Since plug-ins and custom workflow activities execute on the server independent of a logged on user, API calls made from plug-in code will not count against this external API request limit.

If your application has the potential to exceed the limit, please consider the guidance given in the [What should I do if my application exceeds the limit?](#what-should-i-do-if-my-application-exceeds-the-limit) section below.

## What happens when the limit is exceeded?

When the limit is exceeded, all requests for the same user will return error responses.

If you use the .NET SDK assemblies, the platform will respond with a `FaultException<OrganizationServiceFault>` WCF Fault.  

| Error Code | Message |
|------------|-------------------------------------|
|`-2147015902`|`Number of requests exceeded the limit of 4000, measured over time window of 300 seconds.`|
|`-2147015903`|`Combined execution time of incoming requests exceeded limit of 1,200,000 milliseconds over time window of 300 seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.`|
|`-2147015898`|`Number of concurrent requests exceeded the limit of X`|

If you use HTTP requests, the response will include the same messages, but with:<br />
`StatusCode` : `429`

All requests will return these error responses until the volume of API requests falls below the limit. If you get these responses, your application should stop sending API requests until the volume of requests is below the limit.

## What should I do if my application exceeds the limit?

When your application exceeds the limit, the error response from the server may specify the amount of time you should wait before sending more requests. The response object is slightly different if you are using SDK assemblies or HTTP requests.

For a discussion of best practices, see [Azure Architecture Best Practices Transient fault handling](/azure/architecture/best-practices/transient-faults)

[The Polly Project](https://www.thepollyproject.org/) is a library which includes capabilities for dealing with transient faults using execution policies.

### HTTP requests

If you are using HTTP requests, you can look for the `Retry-After` HTTP header included in the error response. This will contain a value in seconds indicating how long you should wait before making a follow-up request. More information [MDN web docs Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After)

### SDK assemblies

If you are using the SDK assemblies, you can look for the `Retry-After` delay in the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>.<xref:Microsoft.Xrm.Sdk.BaseServiceFault.ErrorDetails> property, using the key `"Retry-After"`. The value returned is a [TimeSpan](/dotnet/api/system.timespan) object.

### .NET SDK Assembly Example

The following example uses the [Retry class](#retry-class) described below to retrieve one account using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method. If the request fails because an API limit has been exceeded, the `Retry` class will wait according to a delay specified by the server and try again.

```csharp
var qe = new QueryExpression("account") { TopCount = 1 };
EntityCollection result = Retry.Do(() => service.RetrieveMultiple(qe));
```

#### Retry class

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

[Use Common Data Service Web API](webapi/overview.md)<br />
[Use Common Data Service Organization Service](org-service/overview.md)<br />
[Execute batch operations using the Web API](webapi/execute-batch-operations-using-web-api.md)<br />
[Use ExecuteMultiple to improve performance for bulk data load](org-service/execute-multiple-requests.md)
