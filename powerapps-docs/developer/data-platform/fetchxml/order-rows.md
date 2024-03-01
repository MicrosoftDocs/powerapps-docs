---
title: Order rows using FetchXml
description: Learn how to use FetchXml to order rows when you retrieve data from Microsoft Dataverse.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
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


To ensure the `link-entity` order isn't applied first, move the `order` element from the `link-entity` element to the `entity` element and use the `entityname` attribute on the `order` element to refer to the `link-entity` `alias` value.


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

The data contained by most column types is relatively simple and you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database isn't meaningful out of context.

This behavior can be overridden by setting the [fetch element](reference/fetch.md) `useraworderby` (*Use Raw Order By*) boolean attribute. When this attribute is set, all sorting of lookup and choice columns will use the raw data, Guid or integer values respectively.

### Lookup Columns

When you order using lookup columns, the results are sorted using the primary name field for the related table. The database stores a GUID value. The [formatted value](select-columns.md#formatted-values) returned is the corresponding primary name field.

### Choice Columns

Choice column values are also sorted using the [formatted values](select-columns.md#formatted-values) rather than the values stored in the database. Data for these columns are stored as integers. The formatted value is a localized label based on the user's language.

> [!NOTE]
> Since choice sorting is based on the localized label of the users's language, This will lead to different ordering for the results set if the user's language differs.

## Ordering and paging

How a page is ordered makes a big difference when paging data. If the information about how the results are ordered is ambiguous, Dataverse can't consistently or efficiently return paged data.

Add an order element to your query. If you don't add any order elements to your query, Dataverse adds an order based on the primary key of the table. However, when your query uses the `distinct` attribute, no primary key values are returned, so Dataverse can't add this default order. You must specify a paging order. Without any order specified, `distinct` query results might be returned in random order. [Learn more about returning distinct results](overview.md#return-distinct-results)

Paging is dynamic. Each request is evaluated independently as they're received. A paging cookie tells Dataverse the previous page. With this paging cookie data, Dataverse can start with the next record after the last one on the preceding page.

Paging works best going forward. If you go back and retrieve a page you previously retrieved, the results can be different because records could be added, deleted, or modified during since you last retrieved the page. In other words, if your page size is 50 and you go back, you get 50 records, but they might not be the same 50 records. If you keep progressing forward through the pages of a data set, you can expect all the records are returned in a consistent sequence.

### Deterministic ordering is important

*Deterministic ordering* means that there's a way to calculate an order consistently. With a given set of records, the records are always returned in the same order. If you need consistent orders and paging, you must include some unique or semi-unique column values and specify an order for them to be evaluated.

#### Nondeterministic example

Let's look at an example that is *nondeterministic*. This data set contains only **State** and **Status** information and is filtered to only return records in an open **State**. The results are ordered by **Status**. The first three pages are requested. The results look like this:

| State | Status | Page      |
|-----------|------------|---------------|
| Open      | Active     | 1 Start       |
| Open      | Active     | 1             |
| Open      | Active     | 1 End         |
| Open      | Active     |               |
| Open      | Active     |               |
| Open      | Inactive   |               |
| Open      | Inactive   |               |

The paging cookie saves information about the last record on the page. When the next page is requested, the last record from the first page isn't included. However, given the nondeterministic data, there's no guarantee that the other two records on the first page aren't included in the second page.

To achieve deterministic ordering, add orders on columns that contain unique values, or values that are semi-unique.

#### Deterministic example

This query is like the [nondeterministic one](#nondeterministic-example), but it includes the **Case ID** column that includes unique values. It's also ordered by **Status**, but also ordered using **Case ID**. The results look like this:

| State | Status | Case ID | Page      |
|-----------|------------|-------------|---------------|
| Open      | Active     | Case-0010   | 1 Start       |
| Open      | Active     | Case-0021   | 1             |
| Open      | Active     | Case-0032   | 1 End         |
| Open      | Active     | Case-0034   |               |
| Open      | Active     | Case-0070   |               |
| Open      | Inactive   | Case-0015   |               |
| Open      | Inactive   | Case-0047   |               |

In the next page, the cookie will have `Case-0032` stored as the last record in the first page, so page two will start with the next record after that record. The results look like this:

| State | Status | Case ID | Page      |
|-----------|------------|-------------|---------------|
| Open      | Active     | Case-0010   | 1 Start       |
| Open      | Active     | Case-0021   | 1             |
| Open      | Active     | Case-0032   | 1 End         |
| Open      | Active     | Case-0034   | 2 Start       |
| Open      | Active     | Case-0070   | 2             |
| Open      | Inactive   | Case-0015   | 2 End         |
| Open      | Inactive   | Case-0047   |               |

Because this query orders unique column values, the order is consistent.

### Best practices for orders when paging data

> [!NOTE]
> When possible, queries should order on the primary key for the table because Dataverse is optimized for ordering on the primary key by default. Ordering by non-unique or complex fields cause excess overhead and slower queries.

When you retrieve a limited set of data to display in an application, or if you need to return more than 5,000 rows of data, you need to [page the results](page-results.md). The choices you make in determining the order of the results can determine whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page.

To prevent the same record from appearing in more than one page, apply the following best practices:

It's best to  include a column that has a unique identifier. For example:

- Table primary key columns
- Autonumber columns
- User/contact IDs

If you can't include a column with a unique identifier, include multiple fields that will most likely result in unique combinations. For example:

- First name + last name + email address
- Full name + email address
- Email address + company name


#### Anti-patterns for orders when paging data

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