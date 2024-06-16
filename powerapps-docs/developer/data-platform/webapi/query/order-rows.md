---
title: Order rows using OData
description: Learn how to use OData to order rows when you retrieve data from Microsoft Dataverse Web API.
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
# Order rows using OData

Use the `$orderby` [query option](overview.md#odata-query-options) to specify the order in which items are returned. Use the `asc` or `desc` suffix to specify ascending or descending order, respectively. The default is ascending. The following example retrieves the `name` and `revenue` properties of accounts, ordered by ascending `revenue` and descending `name`:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]

## Descending order

## Process `link-entity` orders first

## Ordering lookup and choice columns

### Lookup Columns

### Choice columns

#### Override default choice columns sort order

## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]