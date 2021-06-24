---
title: "Use FetchXML to query data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about FetchXML, a proprietary XML based language that is used in Microsoft Dataverse to query data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use FetchXML to construct a query

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

FetchXML is a proprietary XML based query language of Microsoft Dataverse used to query data using either the **Web API** or the **Organization service**. It's based on a schema that describes the capabilities of the language. The FetchXML language supports similar query capabilities as [query expressions](org-service/build-queries-with-queryexpression.md). In addition, it's used as a serialized form of query, used to save a query as a user-owned saved view in the [UserQuery Table](reference/entities/userquery.md) and as an organization-owned saved view in the [SavedQuery Table](reference/entities/savedquery.md).

## Create the FetchXML query string
  
To execute a FetchXML query, you must first build the XML query string. After you create the query string, use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method to execute the query string. The privileges of the logged on user affects the set of records returned. Only records for which the logged on user has read access will be returned.
  
 The FetchXML query string must conform to the schema definition for the FetchXML language. For more information, see [Fetch XML Schema](fetchxml-schema.md).  
  
 You can save a query by creating a `SavedQuery` record. Set `visible` on the `link-entity` node to `false` to hide the linked table in the **Advanced Find** user interface. It will still participate in the execution of the query and will return the appropriate results.  
  
> [!WARNING]
>  Don't retrieve all columns in a query because of the adverse effect on performance. This is particularly true if the query is used as a parameter to an update request. In an update, if all columns are included this sets all field values, even if they are unchanged, and often triggers cascaded updates to child records.    

### Example FetchXML query strings

In the following example, the **FetchXML** statement retrieves all accounts:  
  
```xml  
  
<fetch mapping='logical'>   
   <entity name='account'>  
      <attribute name='accountid'/>   
      <attribute name='name'/>   
   </entity>  
</fetch>  
  
```  
  
 In the following example, the **FetchXML** statement retrieves all accounts where the last name of the owning user is not equal to Cannon:  
  
```xml  
  
<fetch mapping='logical'>  
   <entity name='account'>   
      <attribute name='accountid'/>   
      <attribute name='name'/>   
      <link-entity name='systemuser' to='owninguser'>   
         <filter type='and'>   
            <condition attribute='lastname' operator='ne' value='Cannon' />   
          </filter>   
      </link-entity>   
   </entity>   
</fetch>  
  
```  
  
 In the following example, the **FetchXML** statement uses count to set the maximum number of records returned from the query. In this case first 3 accounts are returned from the query,  
  
```xml  
<fetch mapping='logical' count='3'>  
  <entity name='account'>  
   <attribute name='name' alias='name'/>  
  </entity>
</fetch>  
```  
  
This example shows an inner join between EntityMap and AttributeMap where the EntityMapID matches.  
  
```xml  
<fetch version='1.0' mapping='logical' distinct='false'>  
   <entity name='entitymap'>  
      <attribute name='sourceentityname'/>  
      <attribute name='targetentityname'/>  
      <link-entity name='attributemap' alias='attributemap' to='entitymapid' from='entitymapid' link-type='inner'>  
         <attribute name='sourceattributename'/>  
         <attribute name='targetattributename'/>  
      </link-entity>  
   </entity>  
 </fetch>  
```  

> [!IMPORTANT]
> A FetchXML query has a limit of a maximum of 10 allowed link tables.
>
> The `in` operator of a FetchXML query is limited to 2000 values.

## Execute the FetchXML query

You can execute a FetchXML query by using either the **Web API** or the **Organization service**.

### Using Web API

You can pass a URL encoded FetchXml string to the appropriate entityset using the `fetchXml` query string parameter. More information: [Use custom FetchXML](webapi/retrieve-and-execute-predefined-queries.md#use-custom-fetchxml).

### Using Organization service

Use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method passing an <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> where the <xref:Microsoft.Xrm.Sdk.Query.FetchExpression.Query> property contains the FetchXml query.

The following code shows how to execute a **FetchXML** query using the Organizations service:  
  
```csharp  
  
// Retrieve all accounts owned by the user with read access rights to the accounts and   
// where the last name of the user is not Cannon.   
string fetch2 = @"  
   <fetch mapping='logical'>  
     <entity name='account'>   
        <attribute name='accountid'/>   
        <attribute name='name'/>   
        <link-entity name='systemuser' to='owninguser'>   
           <filter type='and'>   
              <condition attribute='lastname' operator='ne' value='Cannon' />   
           </filter>   
        </link-entity>   
     </entity>   
   </fetch> ";   
  
EntityCollection result = _serviceProxy.RetrieveMultiple(new FetchExpression(fetch2));
foreach (var c in result.Entities)
{
   System.Console.WriteLine(c.Attributes["name"]);
}  
```

> [!NOTE]
> You can convert a FetchXML query to a query expression with the <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> message.
  
## FetchXML query results

 When you execute a FetchXML query by using the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.RetrieveMultiple(Microsoft.Xrm.Sdk.Query.QueryBase)> method, the return value is an <xref:Microsoft.Xrm.Sdk.EntityCollection> that contains the results of the query. You can then iterate through the table collection. The previous example uses the `foreach` loop to iterate through the result collection of the FetchXML query.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]