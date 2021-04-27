---
title: "Paging behaviors and ordering (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the different paging behaviors for FetchXML queries and how you can write queries to get the desired paging results." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "NHelgren" # GitHub ID
ms.author: "nhelgren" # MSFT alias of Microsoft employees only
manager: "mayadu" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Paging behaviors and ordering

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

When querying data using FetchXML, paging query results can make viewing large
volumes of information easier. It is important when using paging to include
ordering parameters as well. Without proper ordering, paging requests for the
“next 50” records can result in retrieving the same records across multiple
pages making reviews and edits much more difficult. Proper page ordering
requires including unique values to help identify which records are included in
a page.

## Legacy paging

Legacy paging within the Microsoft Dataverse loads all the results of the query
up to the current page into memory on the server, selects the number of records
that are needed for the page, and then ignores the rest. This has benefits such
as quick back/forward paging through the data or skipping to a specific page,
but it also has restrictions such as a 50K row limit, performance issues with
large complex queries, and arbitrarily sorted distinct query results.

## Ordering with a paging cookie

When paging with ordering, a cache of the previous page’s results is stored in a
paging cookie. This is used to calculate what the next page of data should
display.

If a user does not specify any “order by” parameters, the system will
automatically insert “order by "\<\<entity name\>\>".\<\<entityId\>\> asc” to
provide some basic ordering. Depending on the data that is being queried, this
may result in inadequate and unexpected results as a single system user can be
associated with multiple records within any query.

If distinct FetchXML queries are being used, the system will not add any
additional ordering due to potential impacts to the data returned. In these
cases, users will have to add at least a single ordering value for a more
consistent paging experience.

> [!NOTE]
> Paging using FetchXML for Dataverse is dynamic. The page a
> record appears on is determined at the time that each page is rendered. If 1000
> records are being displayed 50 to a page, the first 50 records are displayed as
> page one. When page two is requested, the system determines what the next 50
> records should be at the time of request. Because of this, it would not be
> possible to use the new paging functionality for back paging. Legacy behavior is
> used for back paging which will have reduced performance and any returns after
> page 500 cannot be “paged back” due to legacy limitations. ￼

### Why ordering is important

If a query is run to retrieve all records with a state of “Open” this could
result in 1000 returns. When paging from page one to page two, there is no way
for the system to know which orders to display on page two because all of the
records have the same state. The paging of these records will not be efficient
or consistent.

Providing an “order by” value gives the paging cookie the ability to order the
data by an additional value and recognize the last record in a page based on the
values provided.

#### Example 1

A query is created to get all records with a state of ‘Open’, include the status
for every record, and show three records per page. The query is then ordered by
status. The query result would page as shown in the following table:

| State | Status | Page      |
|-----------|------------|---------------|
| Open      | Active     | 1             |
| Open      | Active     | 1             |
| Open      | Active     | End of page 1 |
| Open      | Active     |               |
| Open      | Active     |               |
| Open      | Inactive   |               |
| Open      | Inactive   |               |

The paging cookie will save information about the last record on the page, but
when it’s time to get page two in this example, there is no unique identifier to
ensure that the next page populated uses the unviewed records or include the
first two records that were on page one.

To solve this problem, queries should include “order by” columns that have
unique values. It is possible to use multiple “order by” values. Below is a
better way to order data for this query:

#### Example 2

A query is created to get all records of a state of ‘Open’, any status, include
the Case IDs, and show three records per page. It orders by status and by Case
ID (a unique identifier) which will order in ascending order. The query result
would page the results as shown below:

| State | Status | Case ID | Page      |
|-----------|------------|-------------|---------------|
| Open      | Active     | Case-0010   | 1             |
| Open      | Active     | Case-0021   | 1             |
| Open      | Active     | Case-0032   | End of Page 1 |
| Open      | Active     | Case-0034   |               |
| Open      | Active     | Case-0070   |               |
| Open      | Inactive   | Case-0015   |               |
| Open      | Inactive   | Case-0047   |               |

The query results are first ordered by the Status, and then ordered by the Case
ID in ascending order. When page two is generated, the result would be as shown
below:

| State | Status | Case ID | Page      |
|-----------|------------|-------------|---------------|
| Open      | Active     | Case-0010   |               |
| Open      | Active     | Case-0021   |               |
| Open      | Active     | Case-0032   | End of Page 1 |
| Open      | Active     | Case-0034   | 2             |
| Open      | Active     | Case-0070   | 2             |
| Open      | Inactive   | Case-0015   |               |
| Open      | Inactive   | Case-0047   |               |

When generating page two of this query set, the cookie will have Case-0032
stored as the last record in the first page, so page two will pick up at the
next record in the set after that record. This will allow for more consistent
results.

### Ordering suggestions

Listed below are some suggestions for improving ordering of paging results, along with some areas to avoid.

#### Best ordering

- Always include a column that has a unique identifier (i.e., table ID
  columns, auto-number columns, user/contact IDs)

#### Good ordering

- Include multiple fields that will most likely result in unique combinations:
  - First name + last name + email address
  - Full name + email address
  - Email address + company name

#### Poor ordering

- Orders that do not include unique identifiers

- Orders that have single or multiple fields that are not likely to provide
  uniqueness such as:
  - Status and state
  - Choices or Yes/No
  - Name values by themselves (i.e., last only, first only, company name
    only)
  - Text fields like titles, descriptions, multi-line text
  - Non unique number fields

### Ordering and multiple table queries

Sometimes data is needed that spans multiple tables and must be queried with a
table JOIN. In these cases, ordering can be included for both tables in the
query. Make sure to use at least one column with a unique ID per table to
ensure the paging provides the best results. However, the query will be
downgraded to legacy paging, where no paging cookie will be returned, in these
cases due to limitations of the N:1 relationship structure that could result in
missing data.

### See Also

[Page large result sets with FetchXML](page-large-result-sets-with-fetchxml.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]