---
title: "Use XRM tooling to delete data (Microsoft Dataverse)| Microsoft Docs"
description: "Use CrmServiceClient class to delete data from Microsoft Dataverse"
ms.date: 12/04/2024
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke 
---
# Use XRM tooling to delete data

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are two methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for deleting data in Microsoft Dataverse: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntity(System.String,System.Guid,System.Guid)> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntityAssociation(System.String,System.Guid,System.String,System.Guid,System.String,System.Guid)>.

In the <xref:Microsoft.PowerPlatform.Dataverse.Client?displayProperty=fullName> namespace there are <xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions.DeleteEntity%2A?displayProperty=nameWithType> and <xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions.DeleteEntityAssociation%2A?displayProperty=nameWithType> methods.

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]
  
## DeleteEntity  

`DeleteEntity` is used to remove a single row of data from Dataverse. To use this method, you need to know the table schema name you wish to affect, and the GUID of the row you want to remove.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);
// ServiceClient svc = new ServiceClient("connectionstring");
  
// Verify that you are connected  
if (svc != null && svc.IsReady)  
{  
    // Delete the entity record  
    svc.DeleteEntity("account", <accountId>);  
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
  
## DeleteEntityAssociation  

`DeleteEntityAssociation` removes the many-to-many association between records in tables. In this example, we will remove the association between a record in the lead and account tables.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);
// ServiceClient svc = new ServiceClient("connectionstring");  
  
// Verify that you are connected  
if (svc != null && svc.IsReady)  
{  
    Guid accountId = new Guid("<Account_GUID>");  
    Guid leadId = new Guid("<Lead_GUID>");  
    string accountLeadRelationshipName= "accountleads_association";   
    svc.DeleteEntityAssociation("account" , accountId, "lead" ,  leadId, accountLeadRelationshipName)  
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

[Use XRM Tooling to connect to Dataverse](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling API to execute actions in Dataverse](use-xrm-tooling-execute-actions.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
