---
title: "Use XRM tooling to create data (Common Data Service for Apps)| Microsoft Docs"
description: "Use CrmServiceClient class to create data on CDS for Apps"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f6a03552-1f07-4d4b-b7ae-fa246a0d7c29
caps.latest.revision: 14
author: "ashvarma"
ms.author: "kvivek"
manager: "kvivek"
---
# Use XRM tooling to create data

There are seven methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for creating new data and associations. A create action using the XRM tooling API requires a data payload. The data payload takes the form of a `Dictionary<string, CrmDataTypeWrapper>` object. <xref:Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper> is used to inform the interface what sort of handling needs to be applied to the data point you are referencing. Some of the methods for creating data are listed in this topic.  
  
## CreateNewRecord  

This method is used to create any type of entity data in CDS for Apps. To use it, you need to know the schema name of the entity you want to create a record in, and must construct a data payload to pass to it. This example creates an account record.  
  
```csharp 
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>",“<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you’re connected to.  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    // Create an account record  
    Dictionary<string, CrmDataTypeWrapper> inData = new Dictionary<string, CrmDataTypeWrapper>();  
    inData.Add("name", new CrmDataTypeWrapper("Sample Account Name", CrmFieldType.String));  
    inData.Add("address1_city", new CrmDataTypeWrapper("Redmond", CrmFieldType.String));  
    inData.Add("telephone1", new CrmDataTypeWrapper("555-0160", CrmFieldType.String));  
    accountId = ctrl.CrmConnectionMgr.CrmSvc.CreateNewRecord("account", inData);  
  
    // Verify if the account is created.  
    if (accountId != Guid.Empty)  
    {  
        Console.WriteLine(“Account created.”);  
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
  
In this example, we created a data payload object called `indata`. Next, we populated it using the general syntax: `crmFieldName , new CrmDataTypeWrapper(data,CrmFieldType)`. After setting up the `indata` object to get the values to create, we called `CreateNewRecord` method providing the entity logical name for the account and the data payload (`indata`).  
  
> [!NOTE]
>  You can also create an entity record using XRM tooling by executing the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message with the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmOrganizationRequest*> method. More information: [Use messages with the ExecuteCrmOrganizationRequest method](use-messages-executecrmorganizationrequest-method.md)  
  
## CreateAnnotation
  
This method is used to create and attach a note object to any entity record. While you can populate all the variables for the note in the first pass, you only need to provide subject and note text fields. In practice, this is generally used to attach system-generated notes to an entity, or to attach files that are stored in CDS for Apps to an entity. Additionally, if you provide your own UI for creating notes for your user, this is how you would attach that note to the owner entity in CDS for Apps. This example continues from the prior example to create a note on the newly created account.  
  
```csharp
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", “<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected.  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you are connected to.  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    // Create and attach a note.  
    inData.Clear();   
    inData.Add("subject", new CrmDataTypeWrapper("This is a NOTE from the API" , CrmFieldType.String));   
    inData.Add("notetext", new CrmDataTypeWrapper("This is text that will go in the body of the note" , CrmFieldType.String));  
    Guid noteID = crmSvc.CreateAnnotation("account", accountId, inData);  
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
[Use XRM Tooling API to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)
