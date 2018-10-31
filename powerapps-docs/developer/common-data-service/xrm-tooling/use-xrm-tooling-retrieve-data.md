---
title: "Use XRM tooling to retrieve data (Common Data Service for Apps)| Microsoft Docs"
description: "Use CrmServiceClient class to retrieve data from CDS for Apps"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 2afc057e-8f70-4bea-bad4-d01e18ed92fd
caps.latest.revision: 14
author: "MattB-msft"
ms.author: "kvivek"
manager: "kvivek"
---
# Use XRM tooling to retrieve data

There are many methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for retrieving data in CDS for Apps. The following examples demonstrate how you can retrieve a record by ID or FetchXML query.  
  
## GetEntityDataById  

This method searches for an entity by the specified ID. In this sample, we specify null for the field list value to fetch all the attributes of the specified entity record (account), and then display the name of the retrieved account record.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", “<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected.  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you are connected to  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    Dictionary<string, object> data = crmSvc.GetEntityDataById("account", <Account_ID>, null);  
    foreach (var pair in data)  
    {  
        if (pair.Key == "name")  
        {  
            Console.WriteLine("Name of the account is {0}", pair.Value);  
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
  
## GetEntityDataByFetchSearchEC  

This method searches for the entity based on the specified FetchXML query. In this sample, we retrieve and display the count of all account records in the system.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserName>", "<Password>", “<Domain>”),"<Server>", "<Port>", "<OrgName>");  
  
// Verify that you are connected.  
if (crmSvc != null && crmSvc.IsReady)  
{  
    //Display the CRM version number and org name that you are connected to  
    Console.WriteLine("Connected to CRM! (Version: {0}; Org: {1}",   
    crmSvc.ConnectedOrgVersion, crmSvc.ConnectedOrgUniqueName);  
  
    string fetchXML =   
        @"<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false' returntotalrecordcount='true' >  
            <entity name='account'>  
              <attribute name='accountid' />  
            </entity>  
        </fetch>";  
    var queryResult = crmSvc.GetEntityDataByFetchSearchEC(fetchXML);  
    if (queryResult != null)  
    {  
        Console.WriteLine(String.Format("Account Records Count : {0}", queryResult.TotalRecordCount));  
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
  
### See also  

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />
[Use XRM Tooling to connect to CDS for Apps](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling API to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)
