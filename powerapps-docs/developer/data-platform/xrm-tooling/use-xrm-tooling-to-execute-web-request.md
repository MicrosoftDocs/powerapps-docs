---
title: "Use XRM tooling to execute actions in Microsoft Dataverse| MicrosoftDocs"
description: "Object of CrmServiceClient class can be used to perform create, retrieve, update and delete operations on Dynamics 365 data"
ms.custom: ""
ms.date: 03/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 72e9238d-e0fb-453b-b1ab-3a15ffb19838
caps.latest.revision: 13
ms.author: "nabuthuk"
manager: "kvivek"
author: Nkrb
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# Use XRM tooling to execute a web request against web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class object is used to perform actions on your Dynamics 365 data such as create, update, retrieve or delete data.

You can now use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest%2A?displayProperty=nameWithType> method to execute a web request against XRM web API.

The following code sample demonstrates how you can execute a web request using `ExecuteCrmWebRequest` method.

>[!NOTE]
> This method is only applicable when the authentication type is specified as `OAuth` or `Certificate`.

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

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]