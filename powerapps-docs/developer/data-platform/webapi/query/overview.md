---
title: Use OData to query data
description: Learn to compose a query using OData with Microsoft Dataverse Web API
ms.date: 07/01/2024
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Use OData to query data

The Dataverse Web API is an OData v4.0 service. These sections of the OData specification describe how to retrieve data from an OData service:

- [OData Version 4.0. Part 1: Protocol Plus Errata 03 11.2 Requesting Data](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752283)
- [OData Version 4.0. Part 2: URL Conventions Plus Errata 03 5 Query Options](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356)

This article and the other articles in this section describe the parts of the OData specification that the Dataverse Web API applies and how you can use it to retrieve business data from Dataverse.

You can also use Web API to query data about *table definitions*, or *entity metadata*. The structure of the data is different, so many of the capabilities described here do not apply. More information: [Query table definitions using the Web API](../query-metadata-web-api.md) and [Query schema definitions](../../query-schema-definitions.md)

## Compose a query



## Limit the number of rows

## Return distinct results

## Retrieve Data

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

There are some things that you can do using FetchXml that OData doesn't support.

- [Aggregation limitations](aggregate-data.md#odata-aggregation-limitations) lists the following limitations for aggregations using OData:

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

## Use OData as a message parameter

## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Learn how to retrieve data with OData.

> [!div class="nextstepaction"]
> [Retrieve data with OData](retrieve-data.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]