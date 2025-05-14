---
title: "Use XRM tooling to update data (Microsoft Dataverse)| Microsoft Docs"
description: "Use CrmServiceClient class to update data on Microsoft Dataverse"
ms.date: 12/04/2024
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
---
# Use XRM tooling to update data

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are two methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for updating data in Microsoft Dataverse: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.UpdateEntity(System.String,System.String,System.Guid,System.Collections.Generic.Dictionary{System.String,Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper},System.String,System.Boolean,System.Guid)> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.UpdateStateAndStatusForEntity(System.String,System.Guid,System.String,System.String,System.Guid)>.

Similarly for the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class there are <xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions.UpdateEntity%2A> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.UpdateStateAndStatusForEntity%2A> methods.
  
An update action using XRM Tooling API requires a data payload. The data payload takes the form of a Dictionary\<string, CrmDataTypeWrapper> object. <xref:Microsoft.Xrm.Tooling.Connector.CrmDataTypeWrapper> is used to inform the interface what sort of handling needs to be applied to the data point you are referencing.  

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]
  
## UpdateEntity  

This is the anchor method for updating any record in Dataverse, with the exception of setting status or state of a record. To use it, you need to know the following information: schema name of the table you want to update, the primary key field of the table you want to update, the GUID of the record you want to update, and finally the data payload array to update it with.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
// Verify that you are connected  
if (svc != null && svc.IsReady)  
{ 
   // Update the account record  
    Dictionary<string, CrmDataTypeWrapper> updateData = new Dictionary<string, CrmDataTypeWrapper>();  
    updateData.Add("name", new CrmDataTypeWrapper("Updated Sample Account Name", CrmFieldType.String));  
    updateData.Add("address1_city", new CrmDataTypeWrapper("Boston", CrmFieldType.String));  
    updateData.Add("telephone1", new CrmDataTypeWrapper("555-0161", CrmFieldType.String));   
    bool updateAccountStatus = svc.UpdateEntity("account","accountid",_accountId,updateData);  
  
    // Validate if the account record was updated successfully, and then display the updated information  
    if (updateAccountStatus == true)  
    {  
        Console.WriteLine("Updated the account details as follows:");  
        Dictionary<string, object> data = svc.GetEntityDataById("account", accountId, null);  
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
    Console.WriteLine("An error occurred: {0}", svc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(svc.LastCrmException.Message);  
    Console.WriteLine(svc.LastCrmException.Source);  
    Console.WriteLine(svc.LastCrmException.StackTrace);  
  
    return;  
}  
```  
  
## UpdateStateAndStatusForEntity

This method is used to set the state of a record in Dataverse. For example, all records generally start in an “open” state. The name of the state changes based on the kind of record, or even the developers choices. A quote, for example, has several possible status and states, **Draft**, **Active**, **Close**, **Lost**, **Won**.  
  
Updating the state of a table requires that you know what the target state and status are, either by the names or IDs. Both the names and the IDs can be found by querying the definition for the table and looking at the status and state fields. In this example, we will demonstrate how to set the status of an account record to **Inactive**.  
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);  
  
// Verify that you are connected  
if (svc != null && svc.IsReady)  
{   
    // Here are the state and status code values  
    // statecode = 1 ( Inactive )   
    // statuscode = 2 ( Inactive )   
  
    svc.UpdateStateAndStatusForEntity("account" , accountId , 1 , 2 );  
  
    // the same command using the second form of the method  
    svc.UpdateStateAndStatusForEntity("account" , accountId , "Inactive" , "Inactive");  
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
[Use XRM Tooling API to execute actions in Dataverse](use-xrm-tooling-execute-actions.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
