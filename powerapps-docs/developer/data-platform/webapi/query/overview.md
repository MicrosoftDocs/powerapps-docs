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

The Dataverse Web API is an OData version 4.0 service. These sections of the OData 4.0 specification describe how to retrieve data:

- [OData Version 4.0. Part 1: Protocol Plus Errata 03 11.2 Requesting Data](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752283)
- [OData Version 4.0. Part 2: URL Conventions Plus Errata 03 5 Query Options](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356)

This article and the other articles in this section describe the parts of the 4.0 OData specification implemented by the Dataverse Web API and how you can use it to retrieve business data from Dataverse.

> [!NOTE]
> The OData version 4.01 is the latest version. It include enhancements and additional features not available in version 4.0, and therefore not currently available in the Dataverse Web API.

## Entity collections

Every query begins with a collection of entities. Entity collections can be:

- [EntitySet resources](#entityset-resources): One of the Web API EntitySet collections.
- [Filtered collections](#filtered-collections): A set of entities returned by a [collection-valued navigation property](../web-api-navigation-properties.md#collection-valued-navigation-properties) for a specific record.
- An expanded collection-valued navigation property. More information: [Expand collection-valued navigation properties](join-tables.md#expand-collection-valued-navigation-properties)
- A collection returned by a function. Some functions are composable, which means you can apply `$select` or `$filter` system query options to limit the results returned. More information: [Composable functions](../use-web-api-functions.md#composable-functions)

### EntitySet resources

To find all the EntitySet resources available in your environment, send a `GET` request to the Web API [service document](../web-api-service-documents.md#service-document):

**Request:**

```http
GET [Organization URI]/api/data/v9.2/
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata",
    "value": [
        {
            "name": "aadusers",
            "kind": "EntitySet",
            "url": "aadusers"
        },
        {
            "name": "accountleadscollection",
            "kind": "EntitySet",
            "url": "accountleadscollection"
        },
        {
            "name": "accounts",
            "kind": "EntitySet",
            "url": "accounts"
        },
      ... <Truncated for brevity>
   [
}
```

> [!TIP]
> These values are usually the plural name of the table, but they can be different. Use this query to confirm you're using the correct EntitySet resource name.

To retrieve data from the [account entity type](xref:Microsoft.Dynamics.CRM.account), you start with the `accounts` EntitySet resource.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
```

### Filtered collections

You can query any collection of entities represented by a collection-valued navigation property of a specified record.

If you want to retrieve data from the [account entity type](xref:Microsoft.Dynamics.CRM.account), where a specific user is the [OwningUser](../../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property from the specified [systemuser](xref:Microsoft.Dynamics.CRM.systemuser) record.

```http
GET [Organization URI]/api/data/v9.2/systemusers(<systemuserid value>)/user_accounts?$select=name
```

To locate the name of the collection-valued navigation property:

- For any Dataverse tables and relationships, you can check the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?displayProperty=fullName>
- For any custom tables or relationships, look for the [collection-valued navigation properties](../web-api-navigation-properties.md#collection-valued-navigation-properties) within the [$metadata service document](../web-api-service-documents.md#csdl-metadata-document)


### OData query options

The following table describes the OData query options the Dataverse Web API supports.


|Option|Use to|More information|
|---------|---------|---------|
|`$select`|Request a specific set of properties for each entity or complex type.|[Select columns](select-columns.md)|
|`$expand`|Specify the related resources to be included in line with retrieved resources. |[Join tables](join-tables.md)|
|`$filter`|Filter a collection of resources. |[Filter rows](filter-rows.md)|
|`$orderby`|Request resources in a particular order. |[Order rows](order-rows.md)|
|`$apply`|Aggregate and group your data. |[Aggregate data](aggregate-data.md)|
|`$top`|Specify the number of items in the queried collection to be included in the result. Don't use `$top` when you retrieve pages of data. |[Don't use the $top query option while paging records.](page-results.md#dont-use-the-top-query-option-while-paging-records)|
|`$count`|Request a count of the matching resources included with the resources in the response. |[Count number of rows](count-rows.md)|

You can apply multiple options to a query. Separate query options from the resource path with a question mark (?). Separate each option after the first with an ampersand (&). Option names are case-sensitive.

The Dataverse Web API doesn't support these [OData query options](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356): `$skip`,`$search`,`$format`.

## Limit the number of rows

## Return distinct results

There is not any `$distinct` keyword in OData to restrict results to unique values. Instead, you can use the `$apply` system query option with the `groupby` transformation. This will effectively return distinct values for each property. 

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


## Community tools

## Use system query options as parameters for functions



## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Learn how to retrieve data with OData.

> [!div class="nextstepaction"]
> [Retrieve data with OData](retrieve-data.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]