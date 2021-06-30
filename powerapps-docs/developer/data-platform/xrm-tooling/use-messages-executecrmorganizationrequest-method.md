---
title: "Use messages with the ExecuteCrmOrganizationRequest method (Microsoft Dataverse)| Microsoft Docs"
description: "Learn how to use messages with the ExecuteCrmOrganizationRequest method. The samples demonstrate how to execute CreateRequest and RetrieveMultipleRequest message using the CrmServiceClient.String) method."
ms.custom: ""
ms.date: 04/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 1ba60f67-522d-4540-a6f9-0787d7074a79
caps.latest.revision: 17
author: "MattB-msft"
ms.author: "kvivek"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use messages with the ExecuteCrmOrganizationRequest method
  
[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The following code samples demonstrate how you can execute messages using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmOrganizationRequest*> method.  
  
## Example 1: CreateRequest message  

 The following code sample demonstrates how to execute the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmOrganizationRequest*> method. In this example, you create an account, and then display the ID in the response object.  
  
```csharp 
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
// Verify that you are connected.  
if (svc != null && svc.IsReady)  
{  
    var request = new CreateRequest();  
    var newAccount = new Entity("account");  
    newAccount.Attributes.Add("name", "Sample Test Account");  
    request.Target = newAccount;  
    var response = (CreateResponse)svc.ExecuteCrmOrganizationRequest(request);  
  
    // Display the ID of the newly created account record.  
    Console.WriteLine("Account record created with the following ID: {0}", response.id.ToString());  
}  
else  
{  
    // Display the last error.  
    Console.WriteLine("An error occurred: {0}", svc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(svc.LastCrmException.Message);  
    Console.WriteLine(svc.LastCrmException.Source);  
    Console.WriteLine(svc.LastCrmException.StackTrace);  
  
    return;  
}  
```  
  
## Example 2: RetrieveMultipleRequest  

 The following code sample demonstrates how to execute the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> message using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmOrganizationRequest*> method. In this example, you execute a retrieve multiple request to fetch all the contacts in the system, and display their full name.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
// Verify that you are connected.  
if (svc != null && svc.IsReady)  
{  
  
    var userSettingsQuery = new QueryExpression("contact");  
    userSettingsQuery.ColumnSet.AllColumns = true;  
    var retrieveRequest = new RetrieveMultipleRequest()  
    {  
        Query = userSettingsQuery  
    };  
    EntityCollection EntCol = (svc.ExecuteCrmOrganizationRequest(retrieveRequest) as RetrieveMultipleResponse).EntityCollection;  
    foreach (var a in EntCol.Entities)  
    {  
        Console.WriteLine("Account name: {0} {1}", a.Attributes["firstname"], a.Attributes["lastname"]);  
    }  
}  
else  
{  
    // Display the last error.  
    Console.WriteLine("An error occurred: {0}", svc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(svc.LastCrmException.Message);  
    Console.WriteLine(svc.LastCrmException.Source);  
    Console.WriteLine(svc.LastCrmException.StackTrace);  
  
    return;  
}  
```  
  
### See also  

[Use XRM Tooling to connect to Microsoft Dataverse](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling API to execute actions in Dataverse](use-xrm-tooling-execute-actions.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]