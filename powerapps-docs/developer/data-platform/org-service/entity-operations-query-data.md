---
title: "Query data using the SDK for .NET (Microsoft Dataverse) | Microsoft Docs"
description: "Introduces the different ways to query data using Microsoft Dataverse SDK for .NET assemblies."
ms.date: 04/25/2024
ms.reviewer: pehecke
ms.topic: article
author: divkamath
ms.author: jdaly
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Query data using the SDK for .NET

The SDK for .NET provides several methods to query data. Each provides different advantages.

|Method|Advantages|
|--|--|
|[FetchExpression class](/dotnet/api/microsoft.xrm.sdk.query.fetchexpression)|Use the proprietary FetchXML query language to create complex queries that can return paged data sets or grouped and aggregated data. You can create joins to include data from related records. FetchXml provides capabilities that other options don't.<br />[Learn how to query data using FetchXml](../fetchxml/overview.md) |
|[QueryExpression class](/dotnet/api/microsoft.xrm.sdk.query.queryexpression)|Use a strongly typed object model to create complex queries that can return paged data sets or grouped and aggregated data. You can create joins to include data from related records. Supports [most the features](queryexpression/overview.md#limitations) in FetchXML.<br />[Learn how to query data using QueryExpression](queryexpression/overview.md)|
|[QueryByAttribute class](/dotnet/api/microsoft.xrm.sdk.query.querybyattribute)|A simpler object model for common queries to return rows that match all the criteria in your query. Supports paging, but not groups and aggregated data sets. Can only return data from a single table.<br />[Learn how to query data using the QueryByAttribute class](use-querybyattribute-class.md)|
|[LINQ](/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq)|Use [OrganizationServiceContext.QueryProvider](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.QueryProvider) to compose queries using the popular LINQ syntax. All LINQ queries are converted to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so the capabilities are limited to those available to  `QueryExpression` <br />This article focuses on SDK classes to retrieve data.[Learn how to query data with LINQ (.NET language-integrated query)](build-queries-with-linq-net-language-integrated-query.md)|

## How to send requests

<xref:Microsoft.Xrm.Sdk.Query.FetchExpression>, <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>, and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> derive from the <xref:Microsoft.Xrm.Sdk.Query.QueryBase> abstract class. There are two ways to get the results of a query defined using these classes:

- You can pass an instance of any of these classes as the `query` parameter to [IOrganizationService.RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) method.
- You can set the [RetrieveMultipleRequest.Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query) property of the class and use the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method. Generally, people use the [IOrganizationService.RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) method, but you might use the [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) to use [optional parameters](../optional-parameters.md) or to send the request as part of a batch using the [ExecuteMultipleRequest](execute-multiple-requests.md) or [ExecuteTransactionRequest](use-executetransaction.md) classes.

Both of these methods return an <xref:Microsoft.Xrm.Sdk.EntityCollection> that contains the results of the query in the <xref:Microsoft.Xrm.Sdk.EntityCollection.Entities> collection and properties to manage more queries to receive paged results.

When you retrieve data using these classes there are some concepts you must understand. The rest of this article explains common concepts when retrieving data using the SDK for .NET classes.

## Null column values are not returned

When a table column contains a null value, or if the column wasn't requested, the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection won't include the value. There isn't a key to access it or a value to return. The absence of the attribute indicates that it's null. When you use the [early bound style](early-bound-programming.md#early-bound), the properties of the generated classes that inherit from [Entity class](xref:Microsoft.Xrm.Sdk.Entity) manage this and return a null value.

When you use the [late bound style](early-bound-programming.md#late-bound), if you try to access the value using an indexer on the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) or [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) collections, you'll get an <xref:System.Collections.Generic.KeyNotFoundException> with the message `The given key was not present in the dictionary`.

To avoid this problem when using the late-bound style, you can use two strategies:

1. For an column that could be null, use the [Entity.Contains(System.String)]xref:Microsoft.Xrm.Sdk.Entity.Contains(System.String)) method to check whether the column value is null before attempting to access it with an indexer. For example:

    `Money revenue = (entity.Contains("revenue")? entity["revenue"] : null);`

1. Use [Entity.GetAttributeValue&lt;T&gt;(System.String)](xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue%60%601(System.String)) method to access the value. For example:

    `Money revenue = entity.GetAttributeValue<Money>();`

  > [!NOTE]
  > If the type specified with [Entity.GetAttributeValue&lt;T&gt;(System.String)](xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue%60%601(System.String)) is a value type that cannot be null, such as <xref:System.Boolean> or <xref:System.DateTime>, the value returned will be the default value, such as `false` or `1/1/0001 12:00:00 AM` rather than null.

## Each request can return up to 5000 records

To ensure best performance, each query request can return a maximum of 5000 rows. To return larger result sets you must request additional pages.

## Formatted values are returned for some columns

Regardless of the method you use to query tables, the data will be returned as [EntityCollection.Entities](xref:Microsoft.Xrm.Sdk.EntityCollection.Entities). You can access the table column (attribute) data values using the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection. But these values may be of type other than string which you would need to manipulate to get string values you can display in your application.

You can access string values that use the environments settings for formatting by using the values in the [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) collection.

The following sample shows how to access the formatted string values for the following account attributes:

|Attribute logical name|Type|
|--|--|
|`primarycontactid`|<xref:Microsoft.Xrm.Sdk.EntityReference>|
|`createdon`|<xref:System.DateTime>|
|`revenue`|<xref:Microsoft.Xrm.Sdk.Money>|
|`statecode`|<xref:Microsoft.Xrm.Sdk.OptionSetValue>|

```csharp
var query = new QueryByAttribute("account")
{
TopCount = 50,
ColumnSet = new ColumnSet("name", "primarycontactid", "createdon", "revenue", "statecode")
};
query.AddAttributeValue("address1_city", "Redmond");
query.AddOrder("name", OrderType.Ascending);

EntityCollection results = svc.RetrieveMultiple(query);

results.Entities.ToList().ForEach(x =>
{
Console.WriteLine(@"
name:{0}
primary contact: {1}
created on: {2}
revenue: {3}
status: {4}",
  x.Attributes["name"],
  (x.Contains("primarycontactid")? x.FormattedValues["primarycontactid"]:string.Empty),
  x.FormattedValues["createdon"],
  (x.Contains("revenue") ? x.FormattedValues["revenue"] : string.Empty),
  x.FormattedValues["statecode"]
  );
});
```

> [!NOTE]
> Table columns (attributes) which contain null values are not returned in the query `Attributes` or `FormattedValues` collections. If a column may contain a null value you should check using the <xref:Microsoft.Xrm.Sdk.Entity.Contains*> method before attempting to access the value.

The formatted results would display like these:

```
name:A Datum (sample)
  primary contact: Rene Valdes (sample)
  created on: 2/28/2018 11:04 AM
  revenue: $10,000.000
  status: Active

name:City Power & Light (sample)
  primary contact: Scott Konersmann (sample)
  created on: 2/28/2018 11:04 AM
  revenue: $100,000.000
  status: Active

name:Contoso Pharmaceuticals (sample)
  primary contact: Robert Lyon (sample)
  created on: 2/28/2018 11:04 AM
  revenue: $60,000.000
  status: Active
```

## Columns that use an an alias return an AliasedValue

TODO

## Convert queries between FetchXml and QueryExpression

You can convert <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> queries to FetchXml and FetchXml queries to QueryExpression using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> and <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> classes.

The [SavedQuery](../reference/entities/savedquery.md) table stores system views for a table (entity type) and the [UserQuery](../reference/entities/userquery.md) table stores saved user queries. Other tables may also store a query as a FetchXml string. These methods enable converting a FetchXml string to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so it can be manipulated using the object model and then converted back to FetchXml so it can be saved as a string.

More information: [Sample: Convert queries between Fetch and QueryExpression](samples/convert-queries-fetch-queryexpression.md)


## Query Condition Limits

Dataverse has a limit of 500 total conditions allowed in a query. Any joins included in the query are counted as part of this limit. If a query (and its joins) exceeds 500 conditions, the user will receive the following error when the query is executed:  "Number of conditions in query exceeded maximum limit." 

If this occurs a user must either: 

- Reduce the number of conditions in their query. 
- Use the `In` clause, which allows GUIDs and strings up to 850 characters with no limit on integers.

## All filter conditions for string values are case insensitive

TODO

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
