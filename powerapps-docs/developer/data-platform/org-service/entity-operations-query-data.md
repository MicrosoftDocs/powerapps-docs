---
title: "Query data using the SDK for .NET (Microsoft Dataverse) | Microsoft Docs"
description: "Introduces the different ways to query data using Microsoft Dataverse SDK for .NET assemblies."
ms.date: 05/03/2024
ms.reviewer: pehecke
ms.topic: how-to
author: MicroSri
ms.author: sriknair
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

You can display and edit simple data types like numbers and strings in applications directly. For certain data types, Dataverse provides read-only, formatted string values you can display in applications. The format of some of these string values depend on settings that can be set by an administrator and overridden by each user.

- An administrator can [customize default regional options](/power-platform/admin/customize-regional-options-admins) that apply for all new users. These settings are stored in the [Organization table](../reference/entities/organization.md).
- Each user may [override these settings for their personal preferences](../../../user/set-personal-options.md). These settings are stored in the [UserSettings table](../reference/entities/usersettings.md).

Use the [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) collection to access formatted values for these types of columns:


|Type |Data type returned|Formatted value description|
|---------|---------|---------|
|**Yes/No**<br />[BooleanAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[Boolean ](/dotnet/api/system.boolean)|The localized label for the corresponding [BooleanOptionSetMetadata.FalseOption](/dotnet/api/microsoft.xrm.sdk.metadata.booleanoptionsetmetadata.falseoption) or [BooleanOptionSetMetadata.TrueOption ](/dotnet/api/microsoft.xrm.sdk.metadata.booleanoptionsetmetadata.trueoption) properties. |
|**Customer**, **Lookup**, and **Owner**<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference)|The [EntityReference.Name](xref:Microsoft.Xrm.Sdk.EntityReference.Name) value, which is the value of the primary name column for the record.|
|**Date and Time**<br />[DateTimeAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[DateTime ](/dotnet/api/system.datetime)|Depends on [the behavior and format configurations for the column](../../../maker/data-platform/behavior-format-date-time-field.md), organization settings, and personal options set by the user, such as the time zone they are in.|
|**Entity Name**<br />[EntityNameAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[String ](/dotnet/api/system.string)|When the value isn't `none`, the formatted value is the localized [DisplayName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.displayname) value for the table.|
|**Currency**<br />[MoneyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[Money ](/dotnet/api/microsoft.xrm.sdk.money)|Depends on the currency selected for the column as well as organization and user preferences.|
|**Choices**<br />[MultiSelectPicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[OptionSetValueCollection](/dotnet/api/microsoft.xrm.sdk.optionsetvaluecollection)|When a single option is selected, the localized label for the selected option. When multiple options are selected, a string with the localized labels for each selected option, separated by `; `. For example: `Appetizer; Entree; Dessert`|
|**Choice**<br />[PicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)<br />**Status**<br />[StateAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)<br />**Status&nbsp;Reason**<br />[StatusAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|[OptionSetValue ](/dotnet/api/microsoft.xrm.sdk.optionsetvalue)|The localized label for the selected option.|


The following sample shows how to access the formatted string values for the following account columns:

|Logical name|Type|
|--|--|
|`primarycontactid`|<xref:Microsoft.Xrm.Sdk.EntityReference>|
|`createdon`|<xref:System.DateTime>|
|`revenue`|<xref:Microsoft.Xrm.Sdk.Money>|
|`statecode`|<xref:Microsoft.Xrm.Sdk.OptionSetValue>|

```csharp
static void FormattedValuesExample(IOrganizationService service)
{
    List<string> columns = new() {
        "name",
        "primarycontactid",
        "createdon",
        "revenue",
        "statecode"
    };

    QueryExpression query = new("account")
    {
        ColumnSet = new ColumnSet(columns.ToArray()),
        TopCount = 3
    };

    EntityCollection accounts = service.RetrieveMultiple(query);

    accounts.Entities.ToList().ForEach(x =>
    {
        string name = (string)x.Attributes["name"];
        string primarycontactid = x.Contains("primarycontactid") ? 
           x.FormattedValues["primarycontactid"] : 
           string.Empty;
        string createdon = x.FormattedValues["createdon"];
        string revenue = x.Contains("revenue") ? 
           x.FormattedValues["revenue"] : 
           string.Empty;
        string statecode = x.FormattedValues["statecode"];

        Console.WriteLine(@$"
name:{name}
    primary contact: {primarycontactid}
    created on: {createdon}
    revenue: {revenue}
    status: {statecode}"
            );
    });
}
```

The formatted results would display like these:

```
name:A Datum (sample)
  primary contact: Rene Valdes (sample)
  created on: 2/28/2020 11:04 AM
  revenue: $10,000.000
  status: Active

name:City Power & Light (sample)
  primary contact: Scott Konersmann (sample)
  created on: 2/28/2024 11:04 AM
  revenue: $100,000.000
  status: Active

name:Contoso Pharmaceuticals (sample)
  primary contact: Robert Lyon (sample)
  created on: 2/28/2018 11:04 AM
  revenue: $60,000.000
  status: Active
```

## Columns that use an an alias return an AliasedValue

When you retrieve aggregated values, you need to specify an name for the column that contains the aggregated value. You can also specify a different column names for 'regular' queries, although this is less common.

When you specify an alias, the value returned is wrapped in an [AliasedValue](/dotnet/api/microsoft.xrm.sdk.aliasedvalue). The `AliasedValue` class has three properties:

|Property|Type|Description|
|---------|---------|---------|
|`EntityLogicalName`|`String`|The logical name of the table that has the column that the data came from.|
|`AttributeLogicalName`|`String`|The logical name of the column that the data came from.|
|`Value`|`Object`|The aggregated value or the value of the column row using an alias.|

When you use a column alias, you need to cast the `Value` property to access the value returned.

Learn more about column aliases:

- [FetchXMl Column aliases](../fetchxml/select-columns.md#column-aliases)
- [QueryExpression Column aliases](../fetchxml/select-columns.md#column-aliases)

## Convert queries between FetchXml and QueryExpression

You can convert <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> queries to FetchXml and FetchXml queries to QueryExpression using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> and <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> classes.

> [!NOTE]
> There are some FetchXml capabilities that QueryExpression doesn't have. When converting a FetchXml query to QueryExpression, these differences are lost. [Learn more about limitations for QueryExpression](queryexpression/overview.md#limitations)

The [SavedQuery](../reference/entities/savedquery.md) table stores system views for a table (entity type) and the [UserQuery](../reference/entities/userquery.md) table stores saved user queries. Other tables may also store a query as a FetchXml string. These methods enable converting a FetchXml string to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> so it can be manipulated using the object model and then converted back to FetchXml so it can be saved as a string.

More information: [Sample: Convert queries between Fetch and QueryExpression](samples/convert-queries-fetch-queryexpression.md)


## Query Condition Limits

Dataverse has a limit of 500 total conditions allowed in a query. Any joins included in the query are counted as part of this limit. If a query (and its joins) exceeds 500 conditions, the user will receive the following error when the query is executed: `Number of conditions in query exceeded maximum limit.`.

If this occurs a user must either:

- Reduce the number of conditions in their query.
- Use the `In` clause, which allows GUIDs and strings up to 850 characters with no limit on integers.

## All filter conditions for string values are case insensitive

When comparing string values, don't worry about the case. The following `QueryExpression` query will return account records with the name `Contoso, Ltd` and `CONTOSO, LTD`.

```csharp
QueryExpression query = new("account")
{
   ColumnSet = new ColumnSet("name"),
   Criteria = new FilterExpression(LogicalOperator.And) { 
      Conditions = {
         { 
               new ConditionExpression(
                  attributeName: "name", 
                  conditionOperator: ConditionOperator.Equal, 
                  value: "CONTOSO, LTD") 
         }
      }
   },
   TopCount = 3
};
```


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
