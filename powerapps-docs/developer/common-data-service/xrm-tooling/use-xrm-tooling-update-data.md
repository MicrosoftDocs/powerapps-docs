---
title: "Use XRM tooling to update data (PowerApps Common Data Service for Apps)| MicrosoftDocs"
description: "Use CrmServiceClient class to update data on CDS for Apps"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 8ec3d4ca-d836-4e7e-b2bf-9d9f806bd145
caps.latest.revision: 14
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Use XRM tooling to update data

There are two methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for updating data in CDS for Apps: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.UpdateEntity(System.String,System.String,System.Guid,System.Collections.Generic.Dictionary{System.String,Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper},System.String,System.Boolean,System.Guid)> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.UpdateStateAndStatusForEntity(System.String,System.Guid,System.String,System.String,System.Guid)>.  
  
An update action using XRM Tooling API requires a data payload. The data payload takes the form of a Dictionary\<string, CrmDataTypeWrapper> object. <xref:Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper> is used to inform the interface what sort of handling needs to be applied to the data point you are referencing.  
  
## UpdateEntity  

This is the anchor method for updating any record in CDS for Apps, with the exception of setting status or state of a record. To use it, you need to know the following information: schema name of the entity you want to update, the primary key field of the entity you want to update, the GUID of the record you want to update, and finally the data payload array to update it with.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", “<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you are connected to  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    // Update the account record  
    Dictionary<string, CrmDataTypeWrapper> updateData = new Dictionary<string, CrmDataTypeWrapper>();  
    updateData.Add("name", new CrmDataTypeWrapper("Updated Sample Account Name", CrmFieldType.String));  
    updateData.Add("address1_city", new CrmDataTypeWrapper("Boston", CrmFieldType.String));  
    updateData.Add("telephone1", new CrmDataTypeWrapper("555-0161", CrmFieldType.String));   
    bool updateAccountStatus = crmSvc.UpdateEntity("account","accountid",_accountId,updateData);  
  
    // Validate if the account record was updated successfully, and then display the updated information  
    if (updateAccountStatus == true)  
    {  
        Console.WriteLine("Updated the account details as follows:");  
        Dictionary<string, object> data = crmSvc.GetEntityDataById("account", accountId, null);  
        foreach (var pair in data)  
        {  
            if ((pair.Key == "name") || (pair.Key == "address1_city") || (pair.Key == "telephone1"))  
            {  
                Console.WriteLine(pair.Key.ToUpper() + ": " + pair.Value);  
            }  
        }  
    }  
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
  
## UpdateStateAndStatusForEntity 
 
This method is used to set the state of a record in CDS for Apps. For example, all records generally start in an “open” state. The name of the state changes based on the kind of record, or even the developers choices. A quote, for example, has several possible status and states, **Draft**, **Active**, **Close**, **Lost**, **Won**.  
  
<!-- TODO:
> [!TIP]
>  You can use the OptionSets.cs file in the SDK\SampleCode\CS\HelperCode folder of the SDK download package to view and use the global option sets available for various entities in CDS for Apps. For more information about global option sets, see [Customize Global Option Sets](../org-service/customize-global-option-sets.md).   -->
  
Updating the state of an entity requires that you know what the target state and status are, either by the names or IDs. Both the names and the IDs can be found by querying the metadata for the entity and looking at the status and state fields. In this example, we will demonstrate how to set the status of an account record to **Inactive**.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", “<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected  
if (crmSvc != null && crmSvc.IsReady)  
{   
    //Display the CRM version number and org name that you are connected to  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",  
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    // Here are the state and status code values  
    // statecode = 1 ( Inactive )   
    // statuscode = 2 ( Inactive )   
  
    crmSvc.UpdateStateAndStatusForEntity("account" , accountId , 1 , 2 );  
  
    // the same command using the second form of the method  
    crmSvc.UpdateStateAndStatusForEntity("account" , accountId , "Inactive" , "Inactive");  
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
[Use XRM Tooling API to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)<br />
[Work with attribute metadata](../org-service/work-attribute-metadata.md)
