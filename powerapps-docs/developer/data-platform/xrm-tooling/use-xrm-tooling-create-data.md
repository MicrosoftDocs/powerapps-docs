---
title: "Use XRM tooling to create data (Microsoft Dataverse)| Microsoft Docs"
description: "Use CrmServiceClient class to create data on Microsoft Dataverse"
ms.custom: ""
ms.date: 04/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f6a03552-1f07-4d4b-b7ae-fa246a0d7c29
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
# Use XRM tooling to create data

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are seven methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for creating new data and associations. A create action using the XRM tooling API requires a data payload. The data payload takes the form of a `Dictionary<string, CrmDataTypeWrapper>` object. <xref:Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper> is used to inform the interface what sort of handling needs to be applied to the data point you are referencing. Some of the methods for creating data are listed in this topic.  
  
## CreateNewRecord  

This method is used to create any type of table data in Microsoft Dataverse. To use it, you need to know the schema name of the table you want to create a record in, and must construct a data payload to pass to it. This example creates an account record.

```csharp
CrmServiceClient svc = new CrmServiceClient("connectionstring");  
// Verify that you are connected  
if (svc != null && svc.IsReady)  
{  
    // Create an account record  
    Dictionary<string, CrmDataTypeWrapper> inData = new Dictionary<string, CrmDataTypeWrapper>();  
    inData.Add("name", new CrmDataTypeWrapper("Sample Account Name", CrmFieldType.String));  
    inData.Add("address1_city", new CrmDataTypeWrapper("Redmond", CrmFieldType.String));  
    inData.Add("telephone1", new CrmDataTypeWrapper("555-0160", CrmFieldType.String));  
    accountId = ctrl.CrmConnectionMgr.svc.CreateNewRecord("account", inData);  
  
    // Verify if the account is created.  
    if (accountId != Guid.Empty)  
    {  
        Console.WriteLine(“Account created.”);  
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

In this example, we created a data payload object called `indata`. Next, we populated it using the general syntax `crmFieldName , new CrmDataTypeWrapper(data,CrmFieldType)`. After setting up the `indata` object to get the values to create, we called `CreateNewRecord` method providing the table logical name for the account and the data payload (`indata`).  
  
> [!NOTE]
> You can also create a table record using XRM tooling by executing the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message with the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmOrganizationRequest*> method. More information: [Use messages with the ExecuteCrmOrganizationRequest method](use-messages-executecrmorganizationrequest-method.md)  
  
## CreateAnnotation
  
This method is used to create and attach a note object to any table record. While you can populate all the variables for the note in the first pass, you only need to provide subject and note text fields. In practice, this is generally used to attach system-generated notes to a table, or to attach files that are stored in Dataverse to a table. Additionally, if you provide your own UI for creating notes for your user, this is how you would attach that note to the owner table in Dataverse. This example continues from the prior example to create a note on the newly created account.  
  
```csharp
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
// Verify that you are connected.  
if (svc != null && svc.IsReady)  
{  
    // Create and attach a note.  
    inData.Clear();   
    inData.Add("subject", new CrmDataTypeWrapper("This is a NOTE from the API" , CrmFieldType.String));
    inData.Add("notetext", new CrmDataTypeWrapper("This is text that will go in the body of the note" , CrmFieldType.String));  
    Guid noteID = svc.CreateAnnotation("account", accountId, inData);  
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
[Use XRM Tooling API to execute actions in Dataverse](use-xrm-tooling-execute-actions.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]