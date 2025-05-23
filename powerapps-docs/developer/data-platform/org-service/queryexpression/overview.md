---
title: Use QueryExpression to query data
description: Learn to compose a query using QueryExpression, an object model that is used in Microsoft Dataverse to compose queries to retrieve data.
ms.date: 05/12/2024
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

The [QueryExpression class](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), together with other classes in the [Microsoft.Xrm.Sdk.Query namespace](xref:Microsoft.Xrm.Sdk.Query), provides an object model to compose complex queries to retrieve records from Dataverse using the [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A). [Compare options when querying data using the SDK for .NET](../entity-operations-query-data.md)


## Compose a query

Use `QueryExpression` to compose dynamic queries that you can modify without the string/xml manipulation required [using FetchXml](../../fetchxml/overview.md).

All queries are based on a single table. Use the `QueryExpression` class to select the table the query retrieves data from.

### Object initialization style

The following example represents a simple `QueryExpression` query that returns the [Name column](../../reference/entities/account.md#BKMK_Name) of the first five rows from the [Account table](../../reference/entities/account.md) using the [object initializer](/dotnet/csharp/programming-guide/classes-and-structs/object-and-collection-initializers#object-initializers) so that the query is defined in a single assignment.

```csharp
public static EntityCollection SimpleExample(IOrganizationService service) {

   QueryExpression query = new("account")
   {
         ColumnSet = new ColumnSet("name"),
         TopCount = 5
   };

   return service.RetrieveMultiple(query);
}
```

When the query instance is initialized, you can:

- Specify the table as the [QueryExpression.EntityName property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName) using the [QueryExpression(String) constructor](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.-ctor#microsoft-xrm-sdk-query-queryexpression-ctor(system-string)).
- Specify the columns to return by setting the [QueryExpression.ColumnSet property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet) by instantiating a new [ColumnSet](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) and passing one or more column [LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) values to the [ColumnSet(String[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.columnset.-ctor#microsoft-xrm-sdk-query-columnset-ctor(system-string())). [Learn more about selecting columns](select-columns.md)
- Limit the number of records returned by setting the [QueryExpression.TopCount property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.TopCount)

### Property assignment style

You can compose the same query without the [QueryExpression(String) constructor](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.-ctor#microsoft-xrm-sdk-query-queryexpression-ctor(system-string)) or object initialization style and just set the properties to the instantiated instance as shown in the following example:

```csharp
public static EntityCollection SimpleExample(IOrganizationService service)
{

   QueryExpression query = new();
   query.EntityName = "account";
   query.ColumnSet.AddColumn("name");
   query.TopCount = 5;

   return service.RetrieveMultiple(query);
}
```

This example shows how you can:

- Specify the table as the [QueryExpression.EntityName property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName) directly after initializing the `QueryExpression` instance using the default constructor.
- Specify the columns to return by setting the [QueryExpression.ColumnSet](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet) using the [ColumnSet.AddColumn method](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AddColumn%2A) to add the column name. [Learn more about selecting columns](select-columns.md)
- Limit the number of records returned by setting the [QueryExpression.TopCount property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.TopCount) *after* object initialization.


Examples in this documentation will use a combination of object initialization and property assignment styles. As queries become more complex, the object initialization style can become unwieldy. You can always define the query properties separately and add them to the query by setting the properties or using the available methods.

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

> [!TIP]
> Try using the [QueryExpression sample code](sample.md) to use this method.

You can also use the  [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) set the query to the [RetrieveMultipleRequest.Query property](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query) to sent the request using the [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).

```csharp
RetrieveMultipleRequest request = new()
{
      Query = query
};
var response = (RetrieveMultipleResponse)service.Execute(request);

EntityCollection results = response.EntityCollection;
```

Use the [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) when you want to:

- [Send an optional parameter with the request](../../optional-parameters.md)
- Include the operation as part of a batch using the [ExecuteMultipleRequest](../execute-multiple-requests.md) or [ExecuteTransactionRequest](../use-executetransaction.md) classes.


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

- Retrieve data using the Dataverse Web API. There are some [Web API operations that enable `QueryExpression` parameters](#use-queryexpression-as-a-message-parameter), but you cannot compose a query using `QueryExpression` to retrieve data using the Web API.
- [Aggregation limitations](aggregate-data.md#queryexpression-aggregation-limitations) lists the following limitations for aggregations using `QueryExpression`:

   - [Get distinct number with CountColumn](aggregate-data.md#get-distinct-number-with-countcolumn)
   - [Time zone when grouping by date](aggregate-data.md#time-zone-when-grouping-by-date)
   - [Row aggregate](aggregate-data.md#row-aggregate)
   - [Per query limit](aggregate-data.md#per-query-limit)

- [Perform cross table column comparisons](../../fetchxml/filter-rows.md#cross-table-column-comparisons).
   `QueryExpression` supports [filtering on column values in the same row](filter-rows.md#filter-on-column-values-in-the-same-row), but they must be in the same table.
- [You can't override the default sort order for choice columns](../../fetchxml/order-rows.md#override-default-choice-columns-sort-order)
- You can't use the [Late Materialize query](../../fetchxml/optimize-performance.md#late-materialize-query) performance optimization.

> [!IMPORTANT]
> If you use the `FetchXmlToQueryExpression` message with either the SDK [FetchXmlToQueryExpressionRequest class](/dotnet/api/microsoft.crm.sdk.messages.fetchxmltoqueryexpressionrequest) or Web API [FetchXmlToQueryExpression function](/power-apps/developer/data-platform/webapi/reference/fetchxmltoqueryexpression), any capabilities not supported by `QueryExpression` are not applied and there will be no error.

## Community tools

The [XrmToolBox](../../community-tools.md#xrmtoolbox) [FetchXMLBuilder](https://fetchxmlbuilder.com/) is a free tool to compose and test FetchXml requests, but it also generates code for `QueryExpression` queries using the same designer experience.

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
> Web API Operations other than [BulkDelete](xref:Microsoft.Dynamics.CRM.BulkDelete), [SyncBulkOperation](xref:Microsoft.Dynamics.CRM.SyncBulkOperation), and [QueryExpressionToFetchXml action](xref:Microsoft.Dynamics.CRM.QueryExpressionToFetchXml) can use FetchXml via the [FetchExpression complex type](xref:Microsoft.Dynamics.CRM.FetchExpression). While the Web API contains the structures to compose queries using `QueryExpression`, such as the [QueryExpression](xref:Microsoft.Dynamics.CRM.QueryExpression), [ColumnSet](xref:Microsoft.Dynamics.CRM.ColumnSet), and [FilterExpression](xref:Microsoft.Dynamics.CRM.FilterExpression) complex types, there is currently no way to use these to retrieve data with `QueryExpression` using the Web API [as you can with FetchXml](../../fetchxml/retrieve-data.md). This means it isn't possible to test the results of the query you would send as a parameter using Web API.


## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Try some queries.

> [!div class="nextstepaction"]
> [QueryExpression sample code](sample.md)