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
|[LINQ](/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq)|Use [OrganizationServiceContext.QueryProvider](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.QueryProvider) to compose queries using the popular LINQ syntax. All LINQ queries are converted to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so the capabilities are limited to those available to `QueryExpression`.<br />This article focuses on SDK classes to retrieve data. [Learn how to query data with LINQ (.NET language-integrated query)](build-queries-with-linq-net-language-integrated-query.md)|

## How to send requests

<xref:Microsoft.Xrm.Sdk.Query.FetchExpression>, <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>, and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> derive from the <xref:Microsoft.Xrm.Sdk.Query.QueryBase> abstract class. There are two ways to get the results of a query defined using these classes:

- You can pass an instance of any of these classes as the `query` parameter to [IOrganizationService.RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) method.
- You can set the [RetrieveMultipleRequest.Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query) property of the class and use the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method.

   Generally, people use the [IOrganizationService.RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) method, but you might use the [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) to use [optional parameters](../optional-parameters.md) or to send the request as part of a batch using the [ExecuteMultipleRequest](execute-multiple-requests.md) or [ExecuteTransactionRequest](use-executetransaction.md) classes.

Both of these methods return an <xref:Microsoft.Xrm.Sdk.EntityCollection> that contains the results of the query in the <xref:Microsoft.Xrm.Sdk.EntityCollection.Entities> collection property. `EntityCollection` has other properties to manage paging results returned.

When you retrieve data using these classes there are some concepts you must understand. The rest of this article explains common concepts when retrieving data using the SDK for .NET classes.

## Null column values are not returned

When a table column contains a null value, or if the column wasn't requested, the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection won't include the value. There isn't a key to access it or a value to return. The absence of the attribute indicates that it's null.

Columns that are not valid for read always return null values. The definition of these columns have the [AttributeMetadata.IsValidForRead](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.isvalidforread) property set to `false`.

### Early bound classes manage null values

When you use the [early bound style](early-bound-programming.md#early-bound), the properties of the generated classes that inherit from [Entity class](xref:Microsoft.Xrm.Sdk.Entity) manage this and return a null value. [Learn about generating early bound classes](generate-early-bound-classes.md)

### How to mitigate null values using late bound classes

When you use the [late bound style](early-bound-programming.md#late-bound), if you try to access the value using an indexer on the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) or [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) collections, you'll get an <xref:System.Collections.Generic.KeyNotFoundException> with this message: `The given key was not present in the dictionary`.

To avoid this problem when using the late-bound style, you can use two strategies:

1. For an column that could be null, use the [Entity.Contains(System.String)](xref:Microsoft.Xrm.Sdk.Entity.Contains(System.String)) method to check whether the column value is null before attempting to access it with an indexer. For example:

    `Money revenue = (entity.Contains("revenue")? entity["revenue"] : null);`

1. Use [Entity.GetAttributeValue&lt;T&gt;(System.String)](xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue%60%601(System.String)) method to access the value. For example:

   `Money revenue = entity.GetAttributeValue<Money>("revenue");`

   > [!NOTE]
   > If the type specified with [Entity.GetAttributeValue&lt;T&gt;(System.String)](xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue%60%601(System.String)) is a value type that cannot be null, such as <xref:System.Boolean> or <xref:System.DateTime>, the value returned will be the default value, such as `false` or `1/1/0001 12:00:00 AM` rather than null.

## Each request can return up to 5000 records

Interactive applications will typically limit the number of records displayed to a number that a human can interact with, and then provide the option to navigate pages of data. For example, model-driven apps depend on a [personal option](../../../user/set-personal-options.md) that allows people to choose a value from 25 to 250. This information is stored in the [UserSettings.PagingLimit](../reference/entities/usersettings.md#BKMK_PagingLimit) column.

Applications that retrieve data from Dataverse without displaying data in an app don't need to specify a page size. The default and maximum page size is 5,000 rows. If you don't set a page size, Dataverse will return up to 5,000 rows of data at a time. To get more rows, you must send additional requests.

Paging works best when you use the paging cookie data that Dataverse returns with the [EntityCollection.PagingCookie](/dotnet/api/microsoft.xrm.sdk.entitycollection.pagingcookie) property, but it isn't required and some requests will not return a paging cookie value. Learn more:

- [Page results using FetchXml](../fetchxml/page-results.md)
- [Page results using QueryExpression](queryexpression/page-results.md)

## Formatted values are returned for some columns

For each [Entity](xref:Microsoft.Xrm.Sdk.Entity) in the [EntityCollection.Entities](xref:Microsoft.Xrm.Sdk.EntityCollection.Entities), access the table column (attribute) data values using the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection. 

You can display and edit simple data types like numbers and strings in applications directly. For certain complex data types, Dataverse provides read-only, formatted string values you can display in applications. The format of these string values may depend on environment settings, such as the currency configured for a field that stores a value of money.

Use the [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) collection to access formatted values for these types of columns:


|Type |AttributeMetadata type|Description|
|---------|---------|---------|
|**Yes/No**|[BooleanAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|Returns a boolean value. The formatted valued contains the localized label for the corresponding [BooleanOptionSetMetadata.FalseOption](/dotnet/api/microsoft.xrm.sdk.metadata.booleanoptionsetmetadata.falseoption) or [BooleanOptionSetMetadata.TrueOption ](/dotnet/api/microsoft.xrm.sdk.metadata.booleanoptionsetmetadata.trueoption) properties. |
|**Customer**<br />**Lookup**<br />**Owner**|[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|These columns return <xref:Microsoft.Xrm.Sdk.EntityReference> values. The formatted value contains the [EntityReference.Name](xref:Microsoft.Xrm.Sdk.EntityReference.Name) value.|
|**Date and Time**|[DateTimeAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|Returns a UTC [System.DateTime](/dotnet/api/system.datetime) value. The formatted value depends on the behavior and format configurations for the column. [Learn more about behavior and format of the date and time column](../../../maker/data-platform/behavior-format-date-time-field.md)|
|**Entity Name**|[EntityNameAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|Returns the logical name of a table or `none`. When the value isn't `none`, the formatted value is the localized [DisplayName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.displayname) value for the table.|
|**Currency**|[MoneyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)||
|**Choices**|[MultiSelectPicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)||
|**Choice**|[PicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)||
|**Status**|[StateAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)||
|**Status Reason**|[StatusAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)||


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
