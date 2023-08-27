---
title: Order rows using FetchXml
description: Learn how to use FetchXml to order rows when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Order rows using FetchXml

Use the [order element](reference/order.md) within [entity](reference/entity.md) or [link-entity](reference/link-entity.md) elements to specify the sort order for the rows in tables.

The following query will return [account](../reference/entities/account.md) records in *ascending* order by `createdon`, `name`, and `accountnumber` values.

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <order attribute='createdon' />
    <order attribute='name' />
    <order attribute='accountnumber' />
  </entity>
</fetch>
```

## Order with multiple columns

The order of the elements determines the how the ordering is applied. To have ordering applied using `accountnumber`, change the elements so that the first element has attribute equal to `accountnumber`.

```xml
<order attribute='accountnumber' />   
<order attribute='createdon' />
<order attribute='name' />
```

## Descending order

If you want to use *descending* order, set the `descending` attribute to `true`. The following example will return account records with the most recently created records at the top.

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='createdon' />
    <order attribute='createdon' descending='true' />
  </entity>
</fetch>
```

## Lookup and choice columns

Lookup and choice column values are sorted using the display values rather than the values stored in the database.
As mentioned in [formatted values](select-columns.md#formatted-values), the values stored in the database for lookup and choice columns is a GUID value and an integer value respectively. The property values returned are the values stored in the database.  However, when you use order on these columns, the display value is used for sorting. For lookups, it is the primary name field for the related table. For choice columns, it is the value of the option label.

<!-- TODO: The option Label can be localized, so I expect this will impact the results returned -->

## Best practices for orders when paging data

<!-- 

TODO: Does this capture all the guidance from https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/paging-behaviors-and-ordering? 
Does it need more examples?
Can it be simplified?

-->

When you retrieve a limited set of data to display in an application, or if you need to return more than 5000 rows of data, you will need to page the results. The choices you make in determining the order of the results can effect whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page.

To prevent this from happening, apply the following best practices:

Always include a column that has a unique identifier. For example:

- table ID columns
- auto-number columns
- user/contact IDs

Include multiple fields that will most likely result in unique combinations:

- First name + last name + email address
- Full name + email address
- Email address + company name


> [!NOTE]
> If no order element is included in the query, and the [fetch element](reference/fetch.md) `distinct` attribute is not used, Dataverse automatically adds an order element using the entity primary key to provide some basic ordering.

### Anti-patterns

The following are ordering choices to avoid:

- Orders that do not include unique identifiers
- Orders that have single or multiple fields that are not likely to provide uniqueness such as:

  - Status and state
  - Choices or Yes/No
  - Name values by themselves. For example `name`, `firstname`, `lastname`
  - Text fields like titles, descriptions,  and multi-line text
  - Non unique number fields


## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]