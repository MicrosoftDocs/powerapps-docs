---
title: "Use XRM tooling to delete data (Common Data Service for Apps)| Microsoft Docs"
description: "Use CrmServiceClient class to delete data from CDS for Apps"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 7e503d2c-89df-4846-8528-632b5ee12bd5
caps.latest.revision: 14
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Use XRM tooling to delete data

There are two methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for deleting data in CDS for Apps: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntity(System.String,System.Guid,System.Guid)> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DeleteEntityAssociation(System.String,System.Guid,System.String,System.Guid,System.String,System.Guid)>.  
  
## DeleteEntity  

DeleteEntity is used to remove a single row of data from CDS for Apps. To use this method, you need to know the entity schema name you wish to affect, and the GUID of the row you want to remove.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", <Domain>),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you are connected to  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    // Delete the entity record  
    crmSvc.DeleteEntity("account", <accountId>);  
}  
else  
{  
    // Display the last error.  
    Console.WriteLine("An error occurred: {0}", crmSvc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(crmSvc.LastCrmException.Message);  
    Console.WriteLine(crmSvc.LastCrmException.Source);  
    Console.WriteLine(crmSvc.LastCrmException.StackTrace);  
  
    return;  
}  
  
```  
  
## DeleteEntityAssociation  

DeleteEntityAssociation removes the many-to-many association between records in entities. In this example, we will remove the association between a record in the lead and account entities.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", <Domain>),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected  
if (crmSvc != null && crmSvc.IsReady)  
{  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    Guid accountId = new Guid("<Account_GUID>");  
    Guid leadId = new Guid("<Lead_GUID>");  
    string accountLeadRelationshipName= "accountleads_association";   
    crmSvc.DeleteEntityAssociation("account" , accountId, "lead" ,  leadId, accountLeadRelationshipName)  
}  
else  
{  
    // Display the last error.  
    Console.WriteLine("An error occurred: {0}", crmSvc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(crmSvc.LastCrmException.Message);  
    Console.WriteLine(crmSvc.LastCrmException.Source);  
    Console.WriteLine(crmSvc.LastCrmException.StackTrace);  
  
    return;  
}  
  
```  
  
### See also  

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />
[Use XRM Tooling to connect to CDS for Apps](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling API to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)
