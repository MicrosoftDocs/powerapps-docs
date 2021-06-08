---
title: "Build queries with QueryExpression (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can use the QueryExpression class to programmatically build a query containing data filters and search conditions that define the scope of a database search" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/01/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Build queries with QueryExpression

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class to programmatically build a query containing data filters and search conditions that define the scope of a database search. A query expression is used for single-object (table) searches. For example, you can create a search to return all accounts that match certain search criteria. The <xref:Microsoft.Xrm.Sdk.Query.QueryBase> class is the base class for query expressions. There are three derived classes: <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>, <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> and <xref:Microsoft.Xrm.Sdk.Query.FetchExpression>. The `QueryExpression` class supports complex queries. The `QueryByAttribute` class is a simple means to search for table rows where columns match specified values.

> [!NOTE]
> The third derived class, `FetchExpression` is used with FetchXML, the proprietary Dataverse query language, can be used to perform some queries by using XML-based queries. More information: [Use FetchXML to construct a query](../use-fetchxml-construct-query.md)
  
Query expressions are used in methods that retrieve more than one row, such as the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method, in messages that perform an operation on a result set specified by a query expression, such as <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> and when the ID for a specific record is not known.  

> [!WARNING]
>  Don’t retrieve all columns in a query because of the negative effect on performance. This is particularly true if the query is used as a parameter to an update request. In an update, if all columns are included this sets all field values, even if they are unchanged, and often triggers cascaded updates to child records.

To save a query so you can re-use it, you can convert it to FetchXML by using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> and save it as a saved query. More information: [Saved queries](../saved-queries.md) 
 
## Alternatives to QueryExpression

There are two additional ways to create queries to retrieve records from Dataverse. 

- FetchXML, the proprietary Dataverse query language, can be used to perform some queries by using XML-based queries. More information: [Use FetchXML to construct a query](../use-fetchxml-construct-query.md). 
- .NET Language-Integrated Query (LINQ). More information: [Build Queries with LINQ (.NET Language-Integrated Query)](build-queries-with-linq-net-language-integrated-query.md).  

<!-- This doesn't belong here. It should be in model driven app configuration -->
## Configuration for Quick find

In Model-driven apps, there is a Quick Find feature. If a user provides search criteria in quick find that is not selective enough, the system detects this and stops the search. This supports a faster form of quick find and can make a big performance difference. This is controlled by the Organization table [QuickFindRecordLimitEnabled](../reference/entities/organization.md#BKMK_QuickFindRecordLimitEnabled) column. When this `Boolean` column value is `true`, a limit is imposed on quick find queries.

## In This Section

[Using the QueryByAttribute Class](use-querybyattribute-class.md)<br />
[Using the QueryExpression Class](use-queryexpression-class.md)<br />
[Using the ColumnSet Class](use-the-columnset-class.md)<br />
[Using the ConditionExpression Class](use-conditionexpression-class.md)<br />
[Using the FilterExpression Class](use-filterexpression-class.md)<br />
[Use a left outer join in QueryExpression to query for records "not in"](use-left-outer-join-queryexpression-query-records-not-in.md)<br />
[Testing for a Null Value](test-null-value.md)<br />
[Page Large Result Sets with Query Expression and FetchXML](page-large-result-sets-with-queryexpression.md)<br />
[Sample: Retrieve With One-To-Many Relationship](/dynamics365/customer-engagement/developer/org-service/sample-retrieve-with-one-to-many-relationship)<br />
[Sample: Retrieve Multiple with Query By Attribute](samples/retrieve-multiple-querybyattribute-class.md)<br />
[Sample: Retrieve Multiple with Query Expression](samples/retrieve-multiple-queryexpression-class.md)<br />
[Sample: Use QueryExpression with a paging cookie](/dynamics365/customer-engagement/developer/org-service/sample-use-queryexpression-with-a-paging-cookie)  
  
## Reference

<xref:Microsoft.Xrm.Sdk.Query.QueryBase><br />
<xref:Microsoft.Xrm.Sdk.Query.QueryExpression><br />
<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute><br />
<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*><br />
<xref:Microsoft.Xrm.Sdk.Query.ColumnSet><br />
<xref:Microsoft.Xrm.Sdk.Query.ConditionExpression><br />
<xref:Microsoft.Xrm.Sdk.Query.FilterExpression><br />
<xref:Microsoft.Xrm.Sdk.Query.PagingInfo.PagingCookie><br />
  
### See also

[Sample: Convert queries between Fetch and QueryExpression](/dynamics365/customer-engagement/developer/org-service/sample-convert-queries-fetch-queryexpression)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
