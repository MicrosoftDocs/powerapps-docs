---
title: "Use XRM tooling to delete data (Common Data Service)| Microsoft Docs"
description: "Use CrmServiceClient class to delete data from Common Data Service"
ms.custom: ""
ms.date: 03/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 7e503d2c-89df-4846-8528-632b5ee12bd5
caps.latest.revision: 14
author: "MattB-msft"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use XRM tooling to delete data

There are two methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for deleting data in Common Data Service: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntity(System.String,System.Guid,System.Guid)> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntityAssociation(System.String,System.Guid,System.String,System.Guid,System.String,System.Guid)>.  
  
## DeleteEntity  

`DeleteEntity` is used to remove a single row of data from Common Data Service. To use this method, you need to know the entity schema name you wish to affect, and the GUID of the row you want to remove.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
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

`DeleteEntityAssociation` removes the many-to-many association between records in entities. In this example, we will remove the association between a record in the lead and account entities.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
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

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />
[Use XRM Tooling to connect to Common Data Service](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling API to execute actions in Common Data Service](use-xrm-tooling-execute-actions.md)
