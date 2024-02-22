---
title: Order rows using FetchXml
description: Learn how to use FetchXml to order rows when you retrieve data from Microsoft Dataverse.
ms.date: 01/30/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Order rows using FetchXml

To specify the sort order for the rows in tables, use the [order element](reference/order.md) within [entity](reference/entity.md) or [link-entity](reference/link-entity.md) elements. The default sort order is *ascending*.

The following query returns [account](../reference/entities/account.md) records in ascending order by `createdon`, `name`, and `accountnumber` values.

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

The order of the elements determines how the ordering is applied. To have ordering applied using `accountnumber`, move that element to the first position.

```xml
<order attribute='accountnumber' />   
<order attribute='createdon' />
<order attribute='name' />
```

## Descending order

If you want to use *descending* order, set the `descending` attribute to `true`. The following example returns account records with the most recently created records at the top.

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='createdon' />
    <order attribute='createdon' descending='true' />
  </entity>
</fetch>
```

## Process `link-entity` orders last

Dataverse always orders attributes specified by the `link-entity` before attributes for the `entity` element.

The following example shows a conventional ordering pattern for both `link-entity` attributes and `entity` attributes.

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <link-entity name='account'
      from='accountid'
      to='parentaccountid'
      link-type='inner'
      alias='parentaccount'>
      <attribute name='name'
        alias='parentaccount' />
      <order attribute='name' />
    </link-entity>
    <order attribute='name' />
  </entity>
</fetch>
```

In this case, the results are ordered using following attributes:

- First => `parentaccountname.name`
- Last => `account.name`


To change this so that the `link-entity` order isn't applied first, move the `order` element from the `link-entity` element to the `entity` element and use the `entityname` attribute on the `order` element to refer to the `link-entity` `alias` value.


```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <link-entity name='account'
      from='accountid'
      to='parentaccountid'
      link-type='inner'
      alias='parentaccount'>
      <attribute name='name'
        alias='parentaccount' />
    </link-entity>
    <order attribute='name' />
    <order entityname='parentaccount'
      attribute='name' />
  </entity>
</fetch>
```

Now, the results are ordered using the following attributes:

- First => `account.name`
- Last => `parentaccount.name`

## Ordering lookup and choice columns

The data contained by most column types is relatively simple and you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database is not meaningful out of context.

### Lookup Columns

When you order using lookup columns, the results are sorted using the primary name field for the related table. The database stores a GUID value. The [formatted value](select-columns.md#formatted-values) returned is the corresponding primary name field.

### Choice Columns

Choice column values are also sorted using the [formatted values](select-columns.md#formatted-values) rather than the values stored in the database. Data for these columns are stored as integers. The formatted value is a localized label based on the user's language.

> [!NOTE]
> Since choice sorting is based on the localized label of the users's language, This will lead to different ordering for the results set if the user's language differs.

## Best practices for orders when paging data

> [!NOTE]
> When possible, queries should order on the primary key for the table because Dataverse is optimized for ordering on the primary key by default. Ordering by non-unique or complex fields cause excess overhead and slower queries.

When you retrieve a limited set of data to display in an application, or if you need to return more than 5,000 rows of data, you need to [page the results](page-results.md). The choices you make in determining the order of the results can determine whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page.

To prevent the same record from appearing in more than one page, apply the following best practices:

Always include a column that has a unique identifier. For example:

- Table primary key columns
- Autonumber columns
- User/contact IDs

Include multiple fields that will most likely result in unique combinations. For example:

- First name + last name + email address
- Full name + email address
- Email address + company name


> [!NOTE]
> If no `order` element is included in the query, and the [fetch element](reference/fetch.md) `distinct` attribute is not used, Dataverse automatically adds an `order` element using the table primary key to provide some basic ordering.

### Anti-patterns

The following are ordering choices to avoid:

- Orders that don't include unique identifiers
- Orders on calculated fields
- Orders that have single or multiple fields that aren't likely to provide uniqueness such as:

  - Status and state
  - Choices or Yes/No
  - Name values by themselves. For example `name`, `firstname`, `lastname`
  - Text fields like titles, descriptions, and multi-line text
  - Non unique number fields


## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]