---
title: "Use XRM tooling to execute actions in Microsoft Dataverse| MicrosoftDocs"
description: "You can use ExecuteCrmWebRequest with the CrmServiceClient class to perform operations using the Dataverse Web API"
ms.date: 10/15/2022
ms.reviewer: jdaly
applies_to: 
  - "Dynamics 365 (online)"
ms.author: jdaly
author: JimDaly
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# Use XRM tooling to execute a web request against Dataverse Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest%2A?displayProperty=nameWithType> or <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.ExecuteWebRequest%2A?displayProperty=nameWithType> methods to execute a web request against XRM web API.

The following code sample demonstrates how you can execute a web request using `ExecuteCrmWebRequest` method.

>[!NOTE]
> - This method is only applicable when the authentication type is specified as `OAuth` or `Certificate`.
> - You should also be able to perform equivilent operations using the Organization Service. This method allows you to re-use the authentication capabilities of `CrmServiceClient` rather that instantiate your own `HttpClient` when you choose to use Web API rather than the Organization Service.

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