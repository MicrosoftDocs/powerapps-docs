---
title: "Use XRM tooling to retrieve data (Microsoft Dataverse)| Microsoft Docs"
description: "Use CrmServiceClient class to retrieve data from Microsoft Dataverse"
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
# Use XRM tooling to retrieve data

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are many methods available in the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> and <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> classes for retrieving data in Microsoft Dataverse. The following examples demonstrate how you can retrieve a record by ID or FetchXML query.

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]
  
## GetEntityDataById  

This method searches for a table by the specified ID. In this sample, we specify null for the field list value to fetch all the columns of the specified table record (account), and then display the name of the retrieved account record.

When using the `ServiceClient` class you can find the Get method here: <xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.QueryExtensions.GetEntityDataById%2A?displayProperty=nameWithType>
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring); 
// ServiceClient svc = new ServiceClient(connectionstring); 
  
// Verify that you are connected.  
if (svc != null && svc.IsReady)  
{  
    Dictionary<string, object> data = svc.GetEntityDataById("account", <Account_ID>, null);  
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
    Console.WriteLine("An error occurred: {0}", svc.LastCrmError);  
  
    // Display the last exception message if any.  
    Console.WriteLine(svc.LastCrmException.Message);  
    Console.WriteLine(svc.LastCrmException.Source);  
    Console.WriteLine(svc.LastCrmException.StackTrace);  
  
    return;  
}  
  
```  
  
## GetEntityDataByFetchSearchEC  

This method searches for the table based on the specified `FetchXML` query. In this sample, we retrieve and display the count of all account records in the system.

When using the `ServiceClient` class, the query method can be found here: <xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.QueryExtensions.GetEntityDataByFetchSearch%2A?displayProperty=nameWithType>
  
```csharp  
CrmServiceClient svc = new CrmServiceClient(connectionstring);
// ServiceClient svc = new ServiceClient(connectionstring);  
  
// Verify that you are connected.  
if (svc != null && svc.IsReady)  
{   
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
