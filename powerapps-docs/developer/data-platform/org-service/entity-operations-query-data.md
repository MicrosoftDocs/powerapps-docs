---
title: "Query data using the SDK for .NET (Microsoft Dataverse) | Microsoft Docs"
description: "Introduces the different ways to query data using Microsoft Dataverse SDK assemblies."
ms.date: 03/22/2024
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

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The SDK for .NET provides several methods to query data. Each provides different advantages.

|Method|Advantages|
|--|--|
|[FetchExpression](#use-fetchxml-with-fetchexpression)|Use the proprietary FetchXML query language to create complex queries that can return paged data sets or grouped and aggregated data. You can create joins to include data from related records. FetchXml provides capabilities that other options do not.|
|[QueryExpression](#use-queryexpression)|Use a strongly-typed object model to create complex queries that can return paged data sets or grouped and aggregated data. You can create joins to include data from related records. Supports [most the features](queryexpression/overview.md#limitations) in FetchXML.|
|[QueryByAttribute](#use-querybyattribute)|A simpler object model for common queries to return rows that match all the criteria in your query. Supports paging, but not groups and aggregated data sets. Can only return data from a single table.|
|[LINQ](/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq)|Use <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.QueryProvider> to compose queries using the popular LINQ syntax. All LINQ queries are converted to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so the capabilities are limited to those available to  `QueryExpression` <br /> This topic will focus on the styles of queries available via the SDK assembly classes. More information: [Build queries with LINQ (.NET language-integrated query)](build-queries-with-linq-net-language-integrated-query.md)|

<xref:Microsoft.Xrm.Sdk.Query.FetchExpression>, <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>, and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> derive from the <xref:Microsoft.Xrm.Sdk.Query.QueryBase> abstract class. There are two ways to get the results of a query defined using these classes:

- You can pass an instance of any of these classes as the `query` parameter to <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method.
- You can set the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query> property of the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> class and use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

> [!NOTE]
> The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method is generally preferred. There are no special capabilities that require the use of the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> class.

Both of these methods will return an <xref:Microsoft.Xrm.Sdk.EntityCollection> that contains the results of the query in the <xref:Microsoft.Xrm.Sdk.EntityCollection.Entities> collection as well as properties to manage additional queries to receive paged results.

> [!NOTE]
> To ensure best performance, each query request can return a maximum of 5000 rows. To return larger result sets you must request additional pages.
>
> All filter conditions for string values are case insensitive.  

### Null table column values are not returned

When a table column (entity attribute) contains a null value, or if the attribute was not included in the FetchXml attributes or the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>, the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Attributes> collection will not include the attribute. There will be neither a key to access it or a value to return. The absence of the attribute indicates that it is null. When using the early bound style, the generated `Entity` class properties will manage this and return a null value.

When using the late bound style, if you try to access the value using an indexer on the <xref:Microsoft.Xrm.Sdk.Entity.Attributes> or <xref:Microsoft.Xrm.Sdk.Entity.FormattedValues> collections you will get an <xref:System.Collections.Generic.KeyNotFoundException> with the message `The given key was not present in the dictionary`.

To avoid this when using the late-bound style, you can use two strategies:

1. For an attribute that could be null, use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Contains(System.String)> method to check whether the attribute is null before attempting to access it with an indexer. For example:

    `Money revenue = (entity.Contains("revenue")? entity["revenue"] : null);`

1. Use <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)> to access the value. For example:

    `Money revenue = entity.GetAttributeValue<Money>();`

  > [!NOTE]
  > If the type specified with <xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)> is a value type that cannot be null, such as <xref:System.Boolean> or <xref:System.DateTime>, the value returned will be the default value, such as `false` or `1/1/0001 12:00:00 AM` rather than null.

## Use FetchXML with FetchExpression

FetchXml is a proprietary XML-based query language that can be used with SDK Assembly queries using <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> and by the Web API using the `fetchXml` query string. More information: [Query data using FetchXml](../fetchxml/overview.md)

The following example shows a simple query to return up to 50 matching account rows where the `address1_city` value equals `Redmond`, ordered by `name`.

```csharp
string fetchXml = @"
<fetch top='50' >
  <entity name='account' >
    <attribute name='name' />
    <filter>
      <condition 
        attribute='address1_city' 
        operator='eq' 
        value='Redmond' />
    </filter>
    <order attribute='name' />
  </entity>
</fetch>";

var query = new FetchExpression(fetchXml);

EntityCollection results = svc.RetrieveMultiple(query);

results.Entities.ToList().ForEach(x => {
  Console.WriteLine(x.Attributes["name"]);
});
```

> [!IMPORTANT]
> When retrieving table rows you should only request the column values you need by setting the specific attributes using `attribute` elements rather than using the `all-attributes` element to return all attributes.

More information:

- [Query data using FetchXml](../fetchxml/overview.md)
- [About quick find queries](../quick-find.md)
- [Page results using FetchXml](../fetchxml/page-results.md)
- [Aggregate data using FetchXml](../fetchxml/aggregate-data.md)
- [Sample: Use aggregation in FetchXML](samples/use-aggregation-fetchxml.md)
- [Sample: Use FetchXML with a paging cookie](samples/use-fetchxml-paging-cookie.md)

## Use QueryExpression

The <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class provides a strongly typed set of objects that is optimized for run-time manipulation of queries.

The following example shows a simple query to return up to 50 matching account rows where the `address1_city` value equals `Redmond`, ordered by `name`.

```csharp
var query = new QueryExpression("account")
{
  ColumnSet = new ColumnSet("name"),
  Criteria = new FilterExpression(LogicalOperator.And),
  TopCount = 50
};
query.Criteria.AddCondition("address1_city", ConditionOperator.Equal, "Redmond");
query.AddOrder("name", OrderType.Ascending);

EntityCollection results = svc.RetrieveMultiple(query);

results.Entities.ToList().ForEach(x =>
{
  Console.WriteLine(x.Attributes["name"]);
});
```

> [!IMPORTANT]
> When retrieving rows you should only request the column values you need by setting the specific attributes using the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor. Although <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor provides an overload that accepts a boolean `allColumns` parameter, you should not use this in production code.


More information:
- [Query data using QueryExpression](queryexpression/overview.md)
- [Page results using QueryExpression](queryexpression/page-results.md)
- [Filter rows using QueryExpression](queryexpression/filter-rows.md)
- [Select columns using QueryExpression](queryexpression/select-columns.md)
- [Sample: Retrieve multiple with the QueryExpression class](samples/retrieve-multiple-queryexpression-class.md)
- [Sample: Use QueryExpression with a paging cookie](samples/use-queryexpression-with-a-paging-cookie.md)

## Use QueryByAttribute

The <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class provides a strongly typed set of objects that is optimized for simple, common queries of table rows. Unlike FetchXML and `QueryExpression`,  `QueryByAttribute` can only return data from a single table. It doesn't enable retrieving data from related table rows or complex query criteria.

The following example shows a simple query to return up to 50 matching account rows where the `address1_city` value equals `Redmond`, ordered by `name`.

```csharp
var query = new QueryByAttribute("account")
{
  TopCount = 50,
  ColumnSet = new ColumnSet("name")
};
query.AddAttributeValue("address1_city", "Redmond");
query.AddOrder("name", OrderType.Ascending);

EntityCollection results = svc.RetrieveMultiple(query);

results.Entities.ToList().ForEach(x =>
{
  Console.WriteLine(x.Attributes["name"]);
});
```

More information:
- [Use the QueryByAttribute class](use-querybyattribute-class.md)
- [Sample: Retrieve multiple with the QueryByAttribute class](samples/retrieve-multiple-querybyattribute-class.md)

## Access formatted values

Regardless of the method you use to query tables, the data will be returned as <xref:Microsoft.Xrm.Sdk.EntityCollection>.<xref:Microsoft.Xrm.Sdk.EntityCollection.Entities>. You can access the table column (attribute) data values using the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Attributes> collection. But these values may be of type other than string which you would need to manipulate to get string values you can display in your application.

You can access string values that use the environments settings for formatting by using the values in the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.FormattedValues> collection.

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


## Convert queries between FetchXml and QueryExpression

You can convert <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> queries to FetchXml and FetchXml queries to QueryExpression using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> and <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> classes.

The [SavedQuery](../reference/entities/savedquery.md) table stores system views for a table (entity type) and the [UserQuery](../reference/entities/userquery.md) table stores saved user queries. Other tables may also store a query as a FetchXml string. These methods enable converting a FetchXml string to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so it can be manipulated using the object model and then converted back to FetchXml so it can be saved as a string.

More information: [Sample: Convert queries between Fetch and QueryExpression](samples/convert-queries-fetch-queryexpression.md)


## Query Condition Limits

Dataverse has a limit of 500 total conditions allowed in a query. Any joins included in the query are counted as part of this limit. If a query (and its joins) exceeds 500 conditions, the user will receive the following error when the query is executed:  "Number of conditions in query exceeded maximum limit." 

If this occurs a user must either: 

- Reduce the number of conditions in their query. 
- Use the In clause, which allows GUIDs and strings up to 850 characters with no limit on integers.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
