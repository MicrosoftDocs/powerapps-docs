---
title: Use QueryExpression to query data
description: Learn to compose a query using QueryExpression, an object model that is used in Microsoft Dataverse to compose queries to retrieve data.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Query data using QueryExpression
<!-- Does not replace entity-operations-query-data.md -->
<!-- Replaces build-queries-with-queryexpression.md -->

The [QueryExpression class](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), together with other classes in the [Microsoft.Xrm.Sdk.Query namespace](xref:Microsoft.Xrm.Sdk.Query), provides an object model to compose queries to retrieve records from Dataverse. [Compare options when querying data using the SDK for .NET](../entity-operations-query-data.md)


## Compose a query

Use the object model `QueryExpression` provides to compose queries that you can manipulate without depending on string manipulation using FetchXml.

All queries are based on a single table. Use the `QueryExpression` class to select the table the query retrieves data from. The following example represents a simple `QueryExpression` query:

```csharp
QueryExpression query = new("account")
{
      ColumnSet = new ColumnSet("name"),
      TopCount = 5
};
```

This query returns the [Name column](../../reference/entities/account.md#BKMK_Name) of the first five rows from the [Account table](../../reference/entities/account.md).

- Specify the table as the [QueryExpression.EntityName property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName) using the [QueryExpression(String) constructor](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.-ctor#microsoft-xrm-sdk-query-queryexpression-ctor(system-string)).
- Specify the columns to return by setting the [QueryExpression.ColumnSet](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet) by instantiating a new [ColumnSet](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) and passing one or more column [LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) values to the [ColumnSet(String[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.columnset.-ctor#microsoft-xrm-sdk-query-columnset-ctor(system-string())).
- Limit the number of records returned by setting the [QueryExpression.TopCount property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.TopCount)

You can compose the same query without the [QueryExpression(String) constructor](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.-ctor#microsoft-xrm-sdk-query-queryexpression-ctor(system-string)) or object initialization pattern and just set the properties to the instantiated instance as shown in the following example:

```csharp
QueryExpression query = new();
query.EntityName = "account";
query.ColumnSet = new ColumnSet();
query.ColumnSet.AddColumn("name");
query.TopCount = 5;
```

This example uses the [ColumnSet.AddColumn method](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AddColumn*). Some classes in the [Microsoft.Xrm.Sdk.Query namespace](xref:Microsoft.Xrm.Sdk.Query) have methods like this to enable adding items.

Examples in this documentation will use a combination of both patterns. As queries become more complex, the object initialization pattern can become unwieldy. You can always define the query properties separately and add them to the query by setting the properties or using the available methods.

## Limit the number of rows

To limit the number of rows returned, use the [QueryExpression.TopCount property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.TopCount). Without setting the `TopCount` property, Dataverse returns up to 5,000 rows.

Alternatively, specify a number of records to return using paging. Don't use the `TopCount` property when you request pages of data. [Learn how to request paged results](page-results.md)

You can't use `TopCount` property when you request a count of rows using the [PagingInfo.ReturnTotalRecordCount property](xref:Microsoft.Xrm.Sdk.Query.PagingInfo.ReturnTotalRecordCount). [Learn to count rows](count-rows.md)

## Return distinct results

Use the [QueryExpression.Distinct property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Distinct) to require the query to exclude any duplicate values in the results.

If you use the `Distinct` property, you must add at least one [OrderExpression](xref:Microsoft.Xrm.Sdk.Query.OrderExpression) to the [QueryExpression.Orders property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Orders) to have consistent paging.

When you use the `Distinct` property, the results returned don't include primary key values for each record because they represent an aggregation of all the distinct values.

## Retrieve Data

As explained in [Query data using the SDK for .NET](../entity-operations-query-data.md), `QueryExpression` is one of three types derived from the [QueryBase class](xref:Microsoft.Xrm.Sdk.Query.QueryBase), so you can pass it to the [IOrganizationService.RetrieveMultiple Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) to get an <xref:Microsoft.Xrm.Sdk.EntityCollection> containing the results.

```csharp
EntityCollection results = service.RetrieveMultiple(query);
```

You can also set the query to the [RetrieveMultipleRequest.Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query) property to sent the request using the [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).

```csharp
RetrieveMultipleRequest request = new()
{
      Query = query
};
var response = (RetrieveMultipleResponse)service.Execute(request);

EntityCollection results = response.EntityCollection;
```


## Refine your query

After you select the table to start your query with, refine the query to get the data you need. The following articles explain how to complete your query.


|Article|Task|
|---------|---------|
|[Select columns](select-columns.md)|Specify which columns of data to return.|
|[Join tables](join-tables.md)|Specify which related tables to return in the results.|
|[Order rows](order-rows.md)|Specify the sort order of the rows to return.|
|[Filter rows](filter-rows.md)|Specify which rows of data to return.|
|[Page results](page-results.md)|Specify how many rows of data to return with each request.|
|[Aggregate data](aggregate-data.md)|How to group and aggregate the data returned.|
|[Count number of rows](count-rows.md)|How to get a count of the number of rows returned.|
|[Performance optimizations](optimize-performance.md)|How to optimize performance|

## Limitations

There are some things that you can do using FetchXml that `QueryExpression` doesn't support.

- Retrieve data using the Dataverse Web API. Some [Web API operations that enable `QueryExpression` parameters](#use-queryexpression-as-a-message-parameter), but you cannot compose a query using `QueryExpression` to retrieve data using the Web API.
- [Cross table comparisons](../../fetchxml/filter-rows.md#cross-table-comparisons)
   `QueryExpression` supports [Filter on column values in the same row](filter-rows.md#filter-on-column-values-in-the-same-row), but they must be in the same table.
- Set arbitrary aliases for columns.

## Community tools

The [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/) is a free tool to compose and test FetchXml requests, but it also generates code for `QueryExpression` queries using the same designer experience.

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

## Use QueryExpression as a message parameter

You also use `QueryExpression` as a parameter for Dataverse operations such as the following messages:

|Message Name|SDK for .NET Request class|Web API Operation|
|---------|---------|---------|
|`BackgroundSendEmail`|[BackgroundSendEmailRequest](xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest)|[BackgroundSendEmail action](xref:Microsoft.Dynamics.CRM.BackgroundSendEmail)|
|`BulkDetectDuplicates`|[BulkDetectDuplicatesRequest](xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest)|[BulkDetectDuplicates action](xref:Microsoft.Dynamics.CRM.BulkDetectDuplicates)|
|`BulkDelete`|[BulkDeleteRequest](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest)|[BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete)|
|`FullTextSearchKnowledgeArticle`|[FullTextSearchKnowledgeArticleRequest](xref:Microsoft.Crm.Sdk.Messages.FullTextSearchKnowledgeArticleRequest)|[FullTextSearchKnowledgeArticle action](xref:Microsoft.Dynamics.CRM.FullTextSearchKnowledgeArticle)|
|`QueryExpressionToFetchXml`|[QueryExpressionToFetchXmlRequest](xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest)|[QueryExpressionToFetchXml action](xref:Microsoft.Dynamics.CRM.QueryExpressionToFetchXml)|
|`SendBulkMail`|[SendBulkMailRequest](xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest)|[SendBulkMail action](xref:Microsoft.Dynamics.CRM.SendBulkMail)|
|`SyncBulkOperation`|[SyncBulkOperationRequest](xref:Microsoft.Crm.Sdk.Messages.SyncBulkOperationRequest)|[SyncBulkOperation action](xref:Microsoft.Dynamics.CRM.SyncBulkOperation)|
|`Rollup`|[RollupRequest](xref:Microsoft.Crm.Sdk.Messages.RollupRequest)|[Rollup function](xref:Microsoft.Dynamics.CRM.Rollup)|

> [!NOTE]
> Web API Operations other than [BulkDelete](xref:Microsoft.Dynamics.CRM.BulkDelete), [SyncBulkOperation](xref:Microsoft.Dynamics.CRM.SyncBulkOperation), and [QueryExpressionToFetchXml action](xref:Microsoft.Dynamics.CRM.QueryExpressionToFetchXml) can use FetchXml via the [FetchExpression complex type](xref:Microsoft.Crm.Sdk.Messages.FetchExpression). While the Web API contains the structures to compose queries using `QueryExpression`, such as the [QueryExpression](xref:Microsoft.Crm.Sdk.Messages.QueryExpression),[ColumnSet](xref:Microsoft.Crm.Sdk.Messages.ColumnSet), and [FilterExpression](xref:Microsoft.Crm.Sdk.Messages.FilterExpression) complex types, there is currently no way to use these to retrieve data with `QueryExpression` using the Web API [as you can with FetchXml](../../fetchxml/retrieve-data.md). This means it isn't possible to test the results of the query you would send as a parameter.


## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)


