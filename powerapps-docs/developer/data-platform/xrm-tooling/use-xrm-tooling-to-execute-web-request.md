---
title: "Use ExecuteWebRequest to send requests to the Dataverse Web API | MicrosoftDocs"
description: "You can use the SDK for .NET to send requests to the Dataverse Web API"
ms.date: 10/15/2022
ms.reviewer: jdaly
applies_to: 
  - "Dynamics 365 (online)"
ms.author: jdaly
author: JimDaly
search.audienceType: 
  - developer
---
# Use ExecuteWebRequest to send requests to the Dataverse Web API

> [!NOTE]
> - The SDK for .NET enables a strongly typed programming model to work with data in Dataverse. When you use the SDK you don't need use the Dataverse Web API directly. However, you might choose to leverage the authentication capabilities of <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> or <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> rather than instantiate your own `HttpClient` when testing operations using the Web API.
> - This method is only applicable when the authentication type is specified as `OAuth` or `Certificate`.

You can use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.ExecuteWebRequest%2A?displayProperty=nameWithType> or <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest%2A?displayProperty=nameWithType> methods to execute a web request using Dataverse Web API.

The following code sample demonstrates how you can execute a web request using `ExecuteCrmWebRequest` method.

## Create a record

The following code sample demonstrates how to create a record using the `ExecuteCrmWebRequest` method. In this example, you will create an account, and then display the ID in the response object.  

```csharp
static void ExecuteCrmWebRequestExample(ServiceClient service)
{
    // Common headers for all requests
    Dictionary<string, List<string>> ODataHeaders = new() {
        {"Accept", new List<string>() { "application/json" } },
        {"OData-MaxVersion", new List<string>(){"4.0"}},
        {"OData-Version", new List<string>(){"4.0"}},
        {"If-None-Match", new List<string>(){"null"}}
    };

    //Create an account record
    HttpResponseMessage createResponse = service.ExecuteWebRequest(
        method: HttpMethod.Post,
        queryString: "accounts",
        body: new JObject { { "name","Test Account" } }.ToString(),
        customHeaders: ODataHeaders,
        contentType: "application/json");

    if (createResponse.IsSuccessStatusCode)
    {
        string accountUri = createResponse.Headers.GetValues("OData-EntityId").FirstOrDefault();
        Console.WriteLine($"Account URI: :{accountUri}");
    }
    else
    {
        Console.WriteLine($"Create operation failed:{createResponse.ReasonPhrase}");
    }
}
```

To learn more about using Dataverse Web API requests and responses, and handling errors, see [Use the Microsoft Dataverse Web API](../webapi/overview.md).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
