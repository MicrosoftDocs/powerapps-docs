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

## Order with multiple columns

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

## Specifying link attribute ordering (using entityName) on root entity for more control

Below is an example of how to normally order on both link-entity attributes and root-entity attributes. The results will be ordered by the following attributes (first -> last): 

1) parentaccountname.name
2) account.name

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <link-entity name='account' from='accountid' to='accountid' link-type='inner' alias='parentaccount'>
	<attribute name='name' alias='parentaccount' />
	    <order attribute='name' />
    </link-entity>
    <order attribute='name' />
  </entity>
</fetch>
```
Dataverse will always order by the link-entity first due to how the query is processed. You can change up this order by using 'entityname' and moving the link-entity orders to the root entity:


```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <link-entity name='account' from='accountid' to='accountid' link-type='inner' alias='parentaccount'>
	<attribute name='name' alias='parentaccount' />
    </link-entity>
    <order attribute='name' />
    <order entityname='parentaccount' attribute='name' />
  </entity>
</fetch>
```

The results will now be ordered by the following attributes (first -> last): 
1) account.name
2) parentaccountname.name

## Special Cases

### Lookup Columns
When ordering on lookups, the results will be ordered by the primary name field for the related table.

### Choice Columns
Choice column values are sorted using the display values rather than the values stored in the database.
As mentioned in [formatted values](select-columns.md#formatted-values), these columns are created as int. Sorting by the raw values can be non-intuitive, therefore when you use order on these columns, the display value is used for sorting. The string value that is sotred on is the localized label based on the users language.  

> [!NOTE]
> Since choice sorting is based on the localized label of the users's language, This will lead to different ordering for the results set if the user's language differs.

## Best practices for orders when paging data
> [!NOTE]
> When possible, queries should order on the table ID for the table as Dataverse is optimized for ordering on the tableid by default. Ordering by non-unique / complex fields can cause excess overhead and slower queries.
<!-- 

TODO: Does this capture all the guidance from https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/paging-behaviors-and-ordering? 
Does it need more examples?
Can it be simplified?

-->

When you retrieve a limited set of data to display in an application, or if you need to return more than 5000 rows of data, you will need to [page the results](page-results.md). The choices you make in determining the order of the results can effect whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page.

To prevent the same record from appearing in more than one page, apply the following best practices:

Always include a column that has a unique identifier. For example:

- table ID columns
- autonumber columns
- user/contact IDs

Include multiple fields that will most likely result in unique combinations. For example:

- First name + last name + email address
- Full name + email address
- Email address + company name


> [!NOTE]
> If no order element is included in the query, and the [fetch element](reference/fetch.md) `distinct` attribute is not used, Dataverse automatically adds an order element using the entity primary key to provide some basic ordering.

### Anti-patterns

The following are ordering choices to avoid:

- Orders that don't include unique identifiers
- Orders on calculated fields
- Orders that have single or multiple fields that aren't likely to provide uniqueness such as:

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