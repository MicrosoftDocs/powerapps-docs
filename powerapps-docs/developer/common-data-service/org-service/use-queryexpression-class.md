---
title: "Use the QueryExpression class (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "In Dynamics 365 (online) Customer Engagement, you can use the QueryExpression class to build complex queries for use with the IOrganizationService.QueryBase) method or the RetrieveMultipleRequest message" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use the QueryExpression class

In Common Data Service for Apps, you can use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class to build complex queries for use with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method or the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> message. You can set query parameters to the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> by using the <xref:Microsoft.Xrm.Sdk.Query.ConditionExpression>, <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>, and <xref:Microsoft.Xrm.Sdk.Query.FilterExpression> classes.  
  
 The <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class lets you create complex queries. The <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class is designed to be a simple way to search for entities where attributes match specified values.  
  
 The following table lists the properties that you set to create a query expression.  
  
|Property|Description|  
|--------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName>|Specifies which type of entity will be retrieved. A query expression can only retrieve a collection of one entity type.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet>|Specifies the set of attributes (columns) to retrieve.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Criteria>|Specifies complex conditional and logical filter expressions that filter the results of the query.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Distinct>|Specifies whether the results of the query contain duplicate records.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities>|Specifies the links between multiple entity types.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Orders>|Specifies the order in which the records are returned from the query.|  
|<xref:Microsoft.Xrm.Sdk.Query.QueryExpression.PageInfo>|Specifies the number of pages and the number of records per page returned from the query.|  
  
<a name="record_count"></a>   
## Record count  
 To find out how many records the query returned, set the <xref:Microsoft.Xrm.Sdk.Query.PagingInfo.ReturnTotalRecordCount> property to true before executing the query. When you do this, the <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> will be set. Otherwise, this value will be -1.  
  
## Example  
 The following sample shows how to use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class.  
  
```csharp  
//  Query using ConditionExpression and FilterExpression  
ConditionExpression condition1 = new ConditionExpression();  
condition1.AttributeName = "lastname";  
condition1.Operator = ConditionOperator.Equal;  
condition1.Values.Add("Brown");              
  
FilterExpression filter1 = new FilterExpression();  
filter1.Conditions.Add(condition1);  
  
QueryExpression query = new QueryExpression("contact");  
query.ColumnSet.AddColumns("firstname", "lastname");  
query.Criteria.AddFilter(filter1);  
  
EntityCollection result1 = _serviceProxy.RetrieveMultiple(query);  
Console.WriteLine();Console.WriteLine("Query using Query Expression with ConditionExpression and FilterExpression");  
Console.WriteLine("---------------------------------------");  
foreach (var a in result1.Entities)  
{  
    Console.WriteLine("Name: " + a.Attributes["firstname"] + " " + a.Attributes["lastname"]);  
}  
Console.WriteLine("---------------------------------------");  
```  
  
### See also  
 [Building Queries with QueryExpression](build-queries-with-queryexpression.md)   
 [Use the ColumnSet Class](use-the-columnset-class.md)   
 [Using the ConditionExpression Class](use-conditionexpression-class.md)   
 [Using the FilterExpression Class](use-filterexpression-class.md)   
 <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>