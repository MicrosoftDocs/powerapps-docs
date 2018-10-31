---
title: "Build queries with QueryExpression (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can use the QueryExpression class to programmatically build a query containing data filters and search conditions that define the scope of a database search" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Build queries with QueryExpression

In Common Data Service for Apps, you can use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class to programmatically build a query containing data filters and search conditions that define the scope of a database search. A query expression is used for single-object searches. For example, you can create a search to return all accounts that match certain search criteria. The <xref:Microsoft.Xrm.Sdk.Query.QueryBase> class is the base class for query expressions. There are two derived classes: <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute>. The `QueryExpression` class supports complex queries. The `QueryByAttribute` class is a simple means to search for entities where attributes match specified values.  
  
 Query expressions are used in methods that retrieve more than one record, such as the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method, in messages that perform an operation on a result set specified by a query expression, such as <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> and when the ID for a specific record is not known.  
  
 In addition, there is a new attribute on the organization entity, `Organization.QuickFindRecordLimitEnabled`. When this `Boolean` attribute is `true`, a limit is imposed on quick find queries. If a user provides search criteria in quick find that is not selective enough, the system detects this and stops the search. This supports a faster form of quick find and can make a big performance difference.  
  
> [!WARNING]
>  Don’t retrieve all attributes in a query because of the negative effect on performance. This is particularly true if the query is used as a parameter to an update request. In an update, if all attributes are included this sets all field values, even if they are unchanged, and often triggers cascaded updates to child records.  
  
 There are two additional ways to create queries to retrieve records from CDS for Apps. FetchXML, the proprietary CDS for Apps query language, can be used to perform some queries by using XML-based queries. For more information, see [Building Queries with FetchXML](/dynamics365/customer-engagement/developer/org-service/build-queries-fetchxml). You can also use .NET Language-Integrated Query (LINQ) to write queries. More information: [Build Queries with LINQ (.NET Language-Integrated Query)](build-queries-with-linq-net-language-integrated-query.md).  
  
 To save a query, you can convert it to FetchXML by using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> and save it as a saved view by using the `userquery` entity.  
  
## In This Section  
 [Using the QueryByAttribute Class](use-querybyattribute-class.md)  
  
 [Using the QueryExpression Class](use-queryexpression-class.md)  
  
 [Using the ColumnSet Class](use-the-columnset-class.md)  
  
 [Using the ConditionExpression Class](use-conditionexpression-class.md)  
  
 [Using the FilterExpression Class](use-filterexpression-class.md)  
  
 [Use a left outer join in QueryExpression to query for records "not in"](use-left-outer-join-queryexpression-query-records-not-in.md)  
  
 [Testing for a Null Value](/dynamics365/customer-engagement/developer/test-null-value)  
  
 [Page Large Result Sets with Query Expression and FetchXML](page-large-result-sets-with-queryexpression.md)  
  
 [Sample: Retrieve With One-To-Many Relationship](/dynamics365/customer-engagement/developer/org-service/sample-retrieve-with-one-to-many-relationship)  
  
 [Sample: Retrieve Multiple with Query By Attribute](/org-service/samples/retrieve-multiple-querybyattribute-class.md)  
  
 [Sample: Retrieve Multiple with Query Expression](/org-service/samples/retrieve-multiple-queryexpression-class.md)  
  
 [Sample: Use QueryExpression with a paging cookie](/dynamics365/customer-engagement/developer/org-service/sample-use-queryexpression-with-a-paging-cookie)  
  
## Reference  
 <xref:Microsoft.Xrm.Sdk.Query.QueryBase>  
  
 <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>  
  
 <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute>  
  
 <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>  
  
 <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>  
  
 <xref:Microsoft.Xrm.Sdk.Query.ConditionExpression>  
  
 <xref:Microsoft.Xrm.Sdk.Query.FilterExpression>  
  
 <xref:Microsoft.Xrm.Sdk.Query.PagingInfo.PagingCookie>  
  
### See also  
 [Sample: Convert queries between Fetch and QueryExpression](/dynamics365/customer-engagement/developer/org-service/sample-convert-queries-fetch-queryexpression)
