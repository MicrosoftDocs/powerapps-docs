<!-- 
This content must remain generic. It is used for FetchXml and QueryExpression.
It is also used in the Web API content 
-->

## Ordering and paging

How a page is ordered makes a big difference when paging data. If the information about how the results are ordered is ambiguous, Dataverse can't consistently or efficiently return paged data.

Specify an order for your query. With [FetchXml](../fetchxml/overview.md), if you don't add any order elements to your query, Dataverse adds an order based on the primary key of the table. However [QueryExpression](../org-service/queryexpression/overview.md) does not, and when your query specifies `distinct` results, no primary key values are returned, so Dataverse can't add this default order. You must specify a paging order. Without any order specified, `distinct` query results might be returned in random order. OData doesn't provide any option to return distinct results, but you should still apply an order when retrieving paged results.

Paging is dynamic. Each request is evaluated independently as they're received. A paging cookie tells Dataverse the previous page. With this paging cookie data, Dataverse can start with the next record after the last one on the preceding page.

Paging works best going forward. If you go back and retrieve a page you previously retrieved, the results can be different because records could be added, deleted, or modified during since you last retrieved the page. In other words, if your page size is 50 and you go back, you get 50 records, but they might not be the same 50 records. If you keep progressing forward through the pages of a data set, you can expect all the records are returned in a consistent sequence.

### Deterministic ordering is important

*Deterministic ordering* means that there's a way to calculate an order consistently. With a given set of records, the records are always returned in the same order. If you need consistent orders and paging, you must include some unique values or combination of column values that are and specify an order for them to be evaluated.

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

When you retrieve a limited set of data to display in an application, or if you need to return more than 5,000 rows of data ([500 for elastic tables](../use-elastic-tables.md#query-rows-of-an-elastic-table)), you need to page the results. The choices you make in determining the order of the results can determine whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page.

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
