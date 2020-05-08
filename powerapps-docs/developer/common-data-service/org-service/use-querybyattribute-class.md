---
title: "Use the QueryByAttribute class (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the QueryByAttribute class to build queries that test a set of attributes against a set of values"
ms.custom: ""
ms.date: 05/03/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use the QueryByAttribute class

You can use the <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class to build queries that test a set of attributes against a set of values. Use this class with the <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method or the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> method.
  
 The following table lists the properties that you can set to create a query expression using the <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class.  
  
|Property|Description|  
|--------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.EntityName>|Specifies which type of entity is retrieved. A query expression can only retrieve a collection of one entity type. You can also pass this value by using the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> constructor.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.ColumnSet>|Specifies the set of attributes (columns) to retrieve.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.Attributes>|Specifies the set of attributes selected in the query.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.Values>|Specifies the attribute values to look for when the query is executed.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.Orders>|Specifies the order in which the records are returned from the query.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute.PageInfo>|Specifies the number of pages and the number of records per page returned from the query.|  
  
 The following code example shows how to use the `QueryByAttribute` class.  
  
```csharp  
//  Create query using querybyattribute      
QueryByAttribute querybyexpression = new QueryByAttribute("account");      
querybyexpression.ColumnSet = new ColumnSet("name", "address1_city", "emailaddress1");  
  
//  Attribute to query      
querybyexpression.Attributes.AddRange("address1_city");  
  
//  Value of queried attribute to return      
querybyexpression.Values.AddRange("Detroit");      
  
//  Query passed to the service proxy      
EntityCollection retrieved = _serviceProxy.RetrieveMultiple(querybyexpression);     
  
//  Iterate through returned collection      
foreach (var c in retrieved.Entities)      
{  
      System.Console.WriteLine("Name: " + c.Attributes["name"]);  
      System.Console.WriteLine("Address: " + c.Attributes["address1_city"]);        
      System.Console.WriteLine("E-mail: " + c.Attributes["emailaddress1"]);      
}  
  
```  
  
### See also  
 [Build Queries with QueryExpression](build-queries-with-queryexpression.md)   
 <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute>