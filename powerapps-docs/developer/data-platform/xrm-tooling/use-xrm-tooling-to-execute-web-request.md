---
title: "Use XRM tooling to execute actions in Microsoft Dataverse| MicrosoftDocs"
description: "You can use ExecuteCrmWebRequest with the CrmServiceClient class to perform operations using the Dataverse Web API"
ms.date: 04/01/2022
ms.reviewer: jdaly
applies_to: 
  - "Dynamics 365 (online)"
ms.author: jdaly
manager: kvivek
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
 Dictionary<string, List<string>> ODataHeaders = new Dictionary<string, List<string>>() {
        { "Accept", new List<string>() { "application/json" } },
        {"OData-MaxVersion", new List<string>(){"4.0"}},
        {"OData-Version", new List<string>(){"4.0"}}
      };

using (CrmServiceClient svc = new CrmServiceClient(conn))
 {
    if (svc.IsReady)
    {
      HttpResponseMessage response = svc.ExecuteCrmWebRequest(HttpMethod.Get, "accounts?$select=name", "{ \"name\":\"Test Account\"}", ODataHeaders, "application/json");

    if (response.IsSuccessStatusCode)
     {
        var accountUri = response.Headers.GetValues("OData-EntityId").FirstOrDefault();
        Console.WriteLine("Account URI: {0}", accountUri);
       }
    else
     {
       Console.WriteLine(response.ReasonPhrase);
        }

  }
    else
      {
        Console.WriteLine(svc.LastCrmError);
           }
}
```

To learn more about using Dataverse Web API requests and responses, and handling errors, see [Use the Microsoft Dataverse Web API](../webapi/overview.md).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]