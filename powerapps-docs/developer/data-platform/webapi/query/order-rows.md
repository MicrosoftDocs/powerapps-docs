---
title: "Order rows using OData in Microsoft Dataverse"
description: Learn how to use OData $orderby query option to sort and order rows when retrieving data from Microsoft Dataverse Web API. Includes examples for lookup and choice columns.
ms.date: 03/27/2026
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
# Order rows by using OData

Use the `$orderby` [query option](overview.md#odata-query-options) to specify the order in which to return items. Use the `asc` or `desc` suffix to specify ascending or descending order, respectively. The default is ascending. The following example retrieves the `name` and `revenue` properties of accounts, ordered by ascending `revenue` and descending `name`:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

## Ordering lookup and choice columns

Most column types contain relatively simple data, so you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database isn't meaningful out of context.

### Lookup columns

When you order by using lookup columns, you sort the results by the primary name field for the related table. The database stores a GUID value. The [formatted value](select-columns.md#formatted-values) returned is the corresponding primary name field.

### Choice columns

When you order by using choice columns, you sort the results by the integer value of the choice.

> [!NOTE]
> This sorting method is different from how [FetchXml](../../fetchxml/order-rows.md#choice-columns) or [QueryExpression](../../org-service/queryexpression/order-rows.md#choice-columns) sort choice values. In these cases, the results are sorted by the localized label for the choice.
> 
> To order results by choice labels by using Dataverse Web API, you must use FetchXml to compose the query.

[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]


## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]