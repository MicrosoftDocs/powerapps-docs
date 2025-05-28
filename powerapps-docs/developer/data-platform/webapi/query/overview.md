---
title: Use OData to query data
description: Learn to compose a query using OData with Microsoft Dataverse Web API
ms.date: 07/11/2024
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Use OData to query data

Every query begins with a collection of entities. Entity collections can be:

- [EntitySet resources](#entityset-resources): One of the Web API `EntitySet` collections.
- [Filtered collections](#filtered-collections): A set of entities returned by a [collection-valued navigation property](../web-api-navigation-properties.md#collection-valued-navigation-properties) for a specific record.
- [An expanded collection-valued navigation property](join-tables.md#expand-collection-valued-navigation-properties).
- [A collection returned by a function](../use-web-api-functions.md#composable-functions).

## `EntitySet` resources

To find all the `EntitySet` resources available in your environment, send a `GET` request to the Web API [service document](../web-api-service-documents.md#service-document):

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
> These values are usually the plural name of the table, but they can be different. Use the results of this request to confirm you're using the correct `EntitySet` resource name.

For example, start with the `accounts` EntitySet resource to retrieve data from the [account entity type](xref:Microsoft.Dynamics.CRM.account).

```http
GET [Organization URI]/api/data/v9.2/accounts
```

## Filtered collections

You can query any collection of entities represented by a collection-valued navigation property of a specified record. For example, if you want to retrieve data from the [account entity type](xref:Microsoft.Dynamics.CRM.account) where a specific user is the [OwningUser](../../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property from the specified [systemuser](xref:Microsoft.Dynamics.CRM.systemuser) record.


```http
GET [Organization URI]/api/data/v9.2/systemusers(<systemuserid value>)/user_accounts?$select=name
```

To locate the name of the collection-valued navigation property:

- For any Dataverse tables and relationships, you can check the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?displayProperty=fullName>
- For any custom tables or relationships, look for the [collection-valued navigation properties](../web-api-navigation-properties.md#collection-valued-navigation-properties) within the [$metadata service document](../web-api-service-documents.md#csdl-metadata-document)

## Retrieve Data

To retrieve data from a collection, send a `GET` request to the collection resource. The following example shows retrieving data from the [account entity type](/power-apps/developer/data-platform/webapi/reference/account).

This example also demonstrates:

- Limiting the columns returned using `$select`. [Learn more about selecting columns](select-columns.md)
- Ordering results using `$orderby`. [Learn more about ordering columns](order-rows.md)
- Limiting the rows returned using `$top`. [Learn about limiting the number of rows](#limit-the-number-of-rows)
- Showing formatted values using the request header: `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"`. [Learn about formatted values](select-columns.md#formatted-values)

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,statecode,statuscode&$orderby=name&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,statecode,statuscode)",
   "value": [
      {
         "@odata.etag": "W/\"112430907\"",
         "name": "A. Datum Corporation (sample)",
         "statecode@OData.Community.Display.V1.FormattedValue": "Active",
         "statecode": 0,
         "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
         "statuscode": 1,
         "accountid": "4b757ff7-9c85-ee11-8179-000d3a9933c9"
      }
   ]
}
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

## OData query options

Use these options to change the results returned from a collection. The following table describes the OData query options the Dataverse Web API supports.

|Option|Use to|More information|
|---------|---------|---------|
|`$select`|Request a specific set of properties for each entity or complex type.|[Select columns](select-columns.md)|
|`$expand`|Specify the related resources to be included in line with retrieved resources. |[Join tables](join-tables.md)|
|`$orderby`|Request resources in a particular order. |[Order rows](order-rows.md)|
|`$filter`|Filter a collection of resources. |[Filter rows](filter-rows.md)|
|`$apply`|Aggregate and group your data. |[Aggregate data](aggregate-data.md)|
|`$top`|Specify the number of items in the queried collection to be included in the result. |[Limit the number of rows](#limit-the-number-of-rows)|
|`$count`|Request a count of the matching resources included with the resources in the response. |[Count number of rows](count-rows.md)|

To apply multiple options, separate query options from the resource path with a question mark (`?`). Separate each option after the first with an ampersand (`&`). Option names are case-sensitive.

### Use parameter aliases with query options

You can use parameter aliases for `$filter` and `$orderby` query options, but not inside the `$expand` option. Parameter aliases allow you to use the same value multiple times in a request. If the alias isn't assigned a value, it's assumed to be null.

Without parameter aliases:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

With parameter aliases:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=@p1 asc,@p2 desc
&$filter=@p1 ne @p3&@p1=revenue&@p2=name
```

You can also use parameter aliases when using functions. [Learn to use Web API functions](../use-web-api-functions.md)

### Unsupported OData query options

The Dataverse Web API doesn't support the following [OData query options](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356): `$skip`,`$search`,`$format`.

### URL length limitations

The length of a URL in a `GET` request [is limited to 32 KB (32,768 characters)](../compose-http-requests-handle-errors.md#maximum-url-length). Including many complex OData query options as a parameter in the URL can reach the limit. You can execute a `$batch` operation using a `POST` request as a way to move the OData query options out of the URL and into the body of the request where the limit is twice as long. Sending a `GET` request within a `$batch` allows for URLs up to 64 KB (65,536 characters) in length. [Learn more about batch operations using the Web API](../execute-batch-operations-using-web-api.md).

## Limit the number of rows

To limit the number of rows returned, use the `$top` OData query option. Without this limit, Dataverse returns up to 5,000 rows.

Alternatively, specify a number of records to return using paging. Don't use `$top` when you request pages of data. [Learn how to request paged results](page-results.md)

## Limitations

There are some things that you can do using FetchXml that OData doesn't support.

- You can't [join tables without any relationship](../../fetchxml/join-tables.md#no-relationship). OData only allows using the `$expand` query option to join tables using navigation properties that are part of the relationships in the data model.
- [You can't use nested $expand with N:N relationships](join-tables.md#nested-expand-with-nn-relationships).
- [Aggregation limitations](aggregate-data.md#odata-aggregation-limitations) lists the following limitations for aggregations using OData:

  - [Get distinct number with CountColumn](aggregate-data.md#get-distinct-number-with-countcolumn)
  - [Time zone when grouping by date](aggregate-data.md#time-zone-when-grouping-by-date)
  - [Row aggregate](aggregate-data.md#row-aggregate)
  - [Per query limit](aggregate-data.md#per-query-limit)

- [Perform cross table column comparisons](../../fetchxml/filter-rows.md#cross-table-column-comparisons).
   OData supports [filtering on column values in the same row](filter-rows.md#column-comparison), but they must be in the same table.
- [You don't need to override the default sort order for choice columns](../../fetchxml/order-rows.md#override-default-choice-columns-sort-order). The default behavior when sorting choice columns is to use the integer values rather than the localized label value.
- You can't use the [Late Materialize query](../../fetchxml/optimize-performance.md#late-materialize-query) performance optimization.


## Community tools

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

The [Dataverse REST Builder](https://github.com/GuidoPreite/DRB) is an open source project that provides a user interface that helps you do many things using the Dataverse Web API, including composing queries.

The [XrmToolBox](../../community-tools.md#xrmtoolbox) [FetchXMLBuilder](https://fetchxmlbuilder.com/) is a free tool to compose and test FetchXml requests, but it also generates code for OData queries using the same designer experience.


## OData version 4.0 features

The Dataverse Web API is an OData version 4.0 service. These sections of the OData 4.0 specification describe how to retrieve data:

- [OData Version 4.0. Part 1: Protocol Plus Errata 03 11.2 Requesting Data](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752283)
- [OData Version 4.0. Part 2: URL Conventions Plus Errata 03 5 Query Options](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356)

This article and the other articles in this section describe the parts of the 4.0 OData specification implemented by the Dataverse Web API and how you can use it to retrieve business data from Dataverse.

> [!NOTE]
> The OData version 4.01 is the latest version. It include enhancements and additional features not available in version 4.0, and therefore not currently available in the Dataverse Web API.

## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
