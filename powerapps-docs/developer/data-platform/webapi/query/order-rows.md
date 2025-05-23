---
title: Order rows using OData
description: Learn how to use OData to order rows when you retrieve data from Microsoft Dataverse Web API.
ms.date: 07/11/2024
author: MicroSri
ms.author: sriknair
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Order rows using OData

Use the `$orderby` [query option](overview.md#odata-query-options) to specify the order in which items are returned. Use the `asc` or `desc` suffix to specify ascending or descending order, respectively. The default is ascending. The following example retrieves the `name` and `revenue` properties of accounts, ordered by ascending `revenue` and descending `name`:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

## Ordering lookup and choice columns

The data contained by most column types is relatively simple and you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database isn't meaningful out of context.

### Lookup Columns

When you order using lookup columns, the results are sorted using the primary name field for the related table. The database stores a GUID value. The [formatted value](select-columns.md#formatted-values) returned is the corresponding primary name field.

### Choice columns

When you order using choice columns, the results are ordered using the integer value of the choice.

> [!NOTE]
> This is different from how choice values are sorted using [FetchXml](../../fetchxml/order-rows.md#choice-columns) or [QueryExpression](../../org-service/queryexpression/order-rows.md#choice-columns). In these cases, the results are sorted by the localized label for the choice.
> 
> To order results by choice labels with Dataverse Web API, you must use FetchXml to compose the query.

[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]


## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]