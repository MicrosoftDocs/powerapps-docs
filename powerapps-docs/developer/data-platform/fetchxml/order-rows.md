---
title: Order rows using FetchXml
description: Learn how to use FetchXml to order rows when you retrieve data from Microsoft Dataverse.
ms.date: 03/06/2024
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
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

## Process `link-entity` orders first

Dataverse always orders attributes specified by the `link-entity` after attributes for the `entity` element.

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
        <!-- The link-entity parentaccount name -->
      <order attribute='name' />
    </link-entity>
    <!-- The entity account name -->
    <order attribute='name' />
  </entity>
</fetch>
```

In this case, the results are ordered using following attributes:

- First => `account.name`
- Last => `parentaccountname.name`


To ensure the `link-entity` order is applied first, move the `order` element from the `link-entity` element to the `entity` element above the other `order` element, and use the `entityname` attribute on the `order` element to refer to the `link-entity` `alias` value.


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
    <!-- The link-entity parentaccount name -->
    <order entityname='parentaccount'
      attribute='name' />
      <!-- The entity account name -->
    <order attribute='name' />
  </entity>
</fetch>
```

Now, the results are ordered using the following attributes:

- First => `parentaccount.name`
- Last => `account.name`

## Ordering lookup and choice columns

The data contained by most column types is relatively simple and you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database isn't meaningful out of context.

### Lookup Columns

When you order using lookup columns, the results are sorted using the primary name field for the related table. The database stores a GUID value. The [formatted value](select-columns.md#formatted-values) returned is the corresponding primary name field.

### Choice columns

Choice column values are also sorted using the [formatted values](select-columns.md#formatted-values) rather than the values stored in the database. Data for these columns are stored as integers. The formatted value is a localized label based on the user's language.

> [!NOTE]
> Since choice sorting is based on the localized label of the users's language, expect different ordering for the results set if the user's language differs.

#### Override default choice columns sort order

You can override the default sort order for choice columns by setting the [fetch element](reference/fetch.md) `useraworderby` (*Use Raw Order By*) boolean attribute. When this attribute is set, all sorting of choice columns will use the integer values instead.

[!INCLUDE [cc-ordering-paging](../includes/cc-ordering-paging.md)]


## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]