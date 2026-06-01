---
title: Use SQL to Query Data With the Dataverse Web API (Preview)
description: Learn how to use SQL to query data with the Microsoft Dataverse Web API. Retrieve table data using SQL SELECT commands passed via the sql query option.
ms.date: 06/01/2026
ms.topic: how-to
author: kewear
ms.author: kewear
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - saurabhrb
  - JimDaly
  - dmitmikh
---
# Use SQL to query data by using the Dataverse Web API (preview)

You can use Structured Query Language (SQL) to query data from Microsoft Dataverse by using the Web API. Pass SQL `SELECT` commands through the `sql` query option, using the entity set name of the table you want to query.

> [!NOTE]
> Each command must contain a single `SELECT` statement. Other T-SQL statements like `DECLARE`, `INSERT`, `DELETE`, or `ALTER TABLE` aren't supported. Commands with multiple result sets like `SELECT name FROM account; SELECT fullname FROM contact` aren't supported.

To use a SQL query like this:

```sql
SELECT name 
FROM account AS a 
WHERE a.name LIKE 'Fourth Coffee'
```

Set the URL encoded value of the query to the `sql` query option to an [entityset resource](overview.md#entityset-resources) that matches the base table of your query. In this case, the entity set name is `accounts`.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?sql=SELECT%20name%20%0D%0AFROM%20account%20AS%20a%20%0D%0AWHERE%20a.name%20LIKE%20'Fourth%20Coffee' HTTP/1.1
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="*"
Accept: application/json
```

**Response**

The response is similar to what you get with the equivalent OData query:

`/accounts?$select=name&$filter=contains(name,'Fourth Coffee')`

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid)",
   "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
   "@Microsoft.Dynamics.CRM.globalmetadataversion": "173309522",
   "value": [
      {
         "@odata.etag": "W/\"173325408\"",
         "accountid": "0bdd4472-981d-f111-8341-0022482aa957",
         "name": "Fourth Coffee"
      }
   ]
}
```

## Select columns

List specific column names in the `SELECT` clause, separated by commas. Use table aliases to qualify column references and use column aliases to rename output fields.

> [!IMPORTANT]
> `SELECT *` isn't supported. You must explicitly name each column you want to retrieve.

The following example selects three columns from the `account` table using a table alias:

```sql
SELECT a.name, a.telephone1, a.websiteurl
FROM account AS a
```



Use column aliases to rename output fields:

```sql
SELECT a.name AS account_name, a.telephone1 AS phone
FROM account AS a
```

The returned records look like this example:

```json
{
   "@odata.etag": "W/\"174033617\"",
   "accountid": "667ec6df-4a22-f111-8342-0022482aa3a2",
   "account_name@OData.Community.Display.V1.AttributeName": "name",
   "account_name": "Wide World Importers",
   "phone@OData.Community.Display.V1.AttributeName": "telephone1",
   "phone": "(555) 100-0006"
}
```

> [!NOTE]
> Selecting literal values, expressions, and functions other than aggregates isn't supported. Don't use `SELECT 'abc', 1+2 AS IntValue, DATEADD(day, -3, a.modifiedon), a.name FROM account a`.

## Join tables

Use `INNER JOIN` or `LEFT JOIN` to combine rows from two or more tables. Join on a related column, typically a primary key to a foreign key.

> [!NOTE]
> `RIGHT JOIN`, `FULL OUTER JOIN`, and `CROSS JOIN` aren't supported.

The following example returns accounts and their related contacts using an inner join:

```sql
SELECT a.name, c.fullname, c.emailaddress1
FROM account AS a
INNER JOIN contact AS c ON a.accountid = c.parentcustomerid
```

Use `LEFT JOIN` to include accounts that have no related contacts:

```sql
SELECT a.name, c.fullname
FROM account AS a
LEFT JOIN contact AS c ON a.accountid = c.parentcustomerid
```

You can join more than two tables. The following example joins accounts, contacts, and opportunities:

```sql
SELECT a.name, c.fullname, o.name AS opportunity_name
FROM account AS a
INNER JOIN contact AS c ON a.accountid = c.parentcustomerid
INNER JOIN opportunity AS o ON a.accountid = o.customerid
```

Use a self join to relate rows within the same table. The following example finds accounts and their parent accounts:

```sql
SELECT child.name AS account, parent.name AS parent_account
FROM account AS child
INNER JOIN account AS parent ON child.parentaccountid = parent.accountid
```

### Additional ON filters
`JOIN ... ON` clause must use an `=` operator between columns from the two tables. Any additional filters must be combined with this equality condition using the `AND` operator and must be applied to the joined table.

```sql
-- Not supported, must join on columns from the two tables
-- SELECT a.name, c.fullname, c.emailaddress1
-- FROM account AS a
-- INNER JOIN contact AS c ON c.emailaddress1 LIKE 'B%'

-- Not supported, must use "="
-- SELECT a.name, c.fullname, c.emailaddress1
-- FROM account AS a
-- INNER JOIN contact AS c ON a.accountid <> c.parentcustomerid

-- Not supported, must combine additional filters using AND
-- SELECT a.name, c.fullname, c.emailaddress1
-- FROM account AS a
-- INNER JOIN contact AS c ON a.accountid = c.parentcustomerid OR c.emailaddress1 LIKE 'B%'

-- Not supported, additional filters must be on the joined table
-- SELECT a.name, c.fullname, c.emailaddress1
-- FROM account AS a
-- INNER JOIN contact AS c ON a.accountid = c.parentcustomerid AND a.name LIKE 'A%'

-- This example works because it has a filter on the joined contact table fullname column:
SELECT a.name, c.fullname, c.emailaddress1
FROM account AS a
INNER JOIN contact AS c ON a.accountid = c.parentcustomerid AND c.fullname LIKE 'A%'
```

You can combine additional conditions with each other using a nested `OR` operator as long as the whole additional filter is combined with the column equality using `AND`:

```sql
SELECT a.name, c.fullname, c.emailaddress1
FROM account AS a
INNER JOIN contact AS c
   ON a.accountid = c.parentcustomerid
   AND (c.fullname LIKE 'A%' OR c.emailaddress1 LIKE 'B%')
```

## Order rows

Use `ORDER BY` to sort results by one or more columns. Specify `ASC` (ascending, the default) or `DESC` (descending).

> [!NOTE]
> `ORDER BY` can only reference column names. Expressions like `ORDER BY LEN(name)` aren't supported.

The following example returns accounts sorted by name:

```sql
SELECT name, telephone1
FROM account
ORDER BY name ASC
```

Sort by multiple columns:

```sql
SELECT name, createdon
FROM account
ORDER BY name ASC, createdon DESC
```

## Filter rows

Use a `WHERE` clause to filter rows by one or more conditions. The `WHERE` clause must compare a column to a constant value.

> [!IMPORTANT]
> Expressions and subqueries aren't supported in `WHERE` clauses. The comparison must be between a column and a literal value, or a [supported function](#using-dateadd-and-getutcdate-functions).

### Comparison operators

The supported comparison operators are: `=`, `!=`, `<>`, `<`, `>`, `<=`, and `>=`.

```sql
SELECT name, statecode
FROM account
WHERE statecode = 0
```

Use `!=` or `<>` to exclude rows.

```sql
SELECT name, statecode
FROM account
WHERE statecode <> 1
```

Use `<`, `>`, `<=`, or `>=` for range comparisons.

```sql
SELECT name
FROM account
WHERE name > 'M'
ORDER BY name
```

### Logical operators

Combine conditions by using `AND` and `OR`. Use parentheses to control evaluation order.

```sql
SELECT name, telephone1
FROM account
WHERE statecode = 0 AND telephone1 IS NOT NULL
```

```sql
SELECT name
FROM account
WHERE (name = 'Contoso' OR name = 'Fabrikam')
```

```sql
SELECT name, telephone1
FROM account
WHERE (statecode = 0 OR statecode = 1) AND telephone1 IS NOT NULL
```

### LIKE patterns

Use `LIKE` to match string patterns. The supported wildcards are:

| Wildcard | Description | Example |
| --- | --- | --- |
| `%` | Matches any sequence of characters | `'Fourth%'` matches `Fourth Coffee` |
| `_` | Matches any single character | `'_ontoso'` matches `Contoso` |
| `[%]` | Matches a literal percent sign | `'[%]off'` matches `50%off` |

```sql
SELECT name FROM account WHERE name LIKE 'Fourth%'
```

Use `NOT LIKE` to exclude matching rows:

```sql
SELECT name FROM account WHERE name NOT LIKE '%test%'
```

> [!TIP]
> Avoid leading wildcards (`LIKE '%value'`) when possible—they require a full table scan and hurt performance. A trailing wildcard (`LIKE 'value%'`) can use an index. To learn more, see [
Avoid leading wild cards in filter conditions](../../query-antipatterns.md#PerformanceLeadingWildCard).

### IN and NOT IN

Use `IN` to match any value in a list:

```sql
SELECT name
FROM account
WHERE name IN ('Contoso', 'Fabrikam', 'Fourth Coffee')
```

Use `NOT IN` to exclude values:

```sql
SELECT name
FROM account
WHERE name NOT IN ('Contoso', 'Fabrikam')
```

### BETWEEN

Use `BETWEEN` to filter rows within an inclusive range.

```sql
SELECT name
FROM account
WHERE name BETWEEN 'A' AND 'B'
```

### IS NULL and IS NOT NULL

Use `IS NULL` to find rows where a column has no value, and use `IS NOT NULL` to find rows where a column has a value.

```sql
SELECT name
FROM account
WHERE telephone1 IS NULL
```

```sql
SELECT name, telephone1
FROM account
WHERE telephone1 IS NOT NULL
```

> [!NOTE]
> Don't use `= NULL` to test for null values. Use `IS NULL` instead. The expression `WHERE name = NULL` doesn't return the expected results.

### DISTINCT

Use `DISTINCT` to return unique values.

```sql
SELECT DISTINCT a.address1_city
FROM account AS a
```

### Using DATEADD and GETUTCDATE functions
> [!NOTE]
> You must apply functions to a literal value or another supported function. You can't apply functions to column values.

Use the `DATEADD` function to return rows for a constant date range:

```sql
-- Do not pass column values to functions
-- SELECT a.name
-- FROM account a
-- WHERE DATEADD(day, 3, a.createdon) >= '2023-01-01 17:00:00' (not supported)

SELECT a.name
FROM account a
WHERE a.createdon >= DATEADD(day, -3, '2023-01-01 17:00:00')
```

Use the `GETUTCDATE` function to make the range relative to the current time:
```sql
-- Do not pass column values to functions
-- SELECT a.name
-- FROM account a
-- WHERE DATEADD(day, 3, a.createdon) >= GETUTCDATE() (not supported)

SELECT a.name
FROM account a
WHERE a.createdon >= DATEADD(day, -3, GETUTCDATE())
```

> [!NOTE]
> The `WHERE` and `ON` clause conditions support these functions. The `SELECT`, `ORDER BY`, and `GROUP BY` clauses don't support function calls.

### Unsupported WHERE clause features

The `WHERE` clause doesn't support the following features:

- Subqueries: `WHERE accountid IN (SELECT accountid FROM account)`.
- `EXISTS` and `NOT EXISTS`: These operators return an error.
- Literal-to-literal comparisons:  `WHERE 1=1` and `WHERE 1=0`.
- Column-to-column comparisons:  `WHERE a.modifiedon > a.createdon`.
- Expressions:  `WHERE a.revenue > 500.0 + 125.0`.
- Functions applied to column values: `WHERE DATEADD(day, 3, a.createdon) >= GETUTCDATE()`.
- Functions not listed in this document.

## Page results

Use OData paging with the `Prefer: odata.maxpagesize` request header and the `@odata.nextLink` annotation. [Learn more about paging](./page-results.md).

> [!NOTE]
> `TOP` and `OFFSET ... FETCH` aren't supported in queries. Use `Prefer: odata.maxpagesize` to limit the number of records.

Alternatively, use a cursor-based approach by filtering on the last seen ID from the previous page:

```sql
SELECT name, accountid
FROM account
WHERE accountid > '00000000-0000-0000-0000-000000000000'
ORDER BY accountid
```

## Aggregate data

Use aggregate functions with `GROUP BY` to summarize data. The supported aggregate functions are `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

> [!NOTE]
> `HAVING` isn't supported. Filter data by using a `WHERE` clause before aggregating.

The following example groups contacts by their parent account and counts them:

```sql
SELECT a.name, COUNT(*) AS contact_count
FROM account AS a
INNER JOIN contact AS c ON a.accountid = c.parentcustomerid
GROUP BY a.name
ORDER BY a.name
```

Use multiple aggregate functions in a single query:

```sql
SELECT COUNT(*) AS total_accounts,
       SUM(revenue) AS total_revenue,
       AVG(revenue) AS avg_revenue,
       MIN(revenue) AS min_revenue,
       MAX(revenue) AS max_revenue
FROM account
```

> [!NOTE]
> Grouping by functions, including by parts of date like `GROUP BY MONTH(a.createdon)`, isn't supported.

### Aggregate query record limits

[!INCLUDE [cc-query-aggregation-limitations](../../includes/cc-query-aggregation-limitations.md)]

## Count rows

Use `COUNT(*)` to count the number of rows that match your query:

```sql
SELECT COUNT(*) AS account_count
FROM account
```

Combine `COUNT` with a `WHERE` clause to count rows that meet a condition:

```sql
SELECT COUNT(*) AS active_contacts
FROM contact
WHERE statecode = 0
```

Use `COUNT` with `GROUP BY` to count rows per group:

```sql
SELECT a.name, COUNT(*) AS contact_count
FROM account AS a
INNER JOIN contact AS c ON a.accountid = c.parentcustomerid
GROUP BY a.name
```

## Optimize performance

Follow these guidelines to write efficient SQL queries against Dataverse.

### Avoid query anti-patterns

For guidance about general things to avoid when composing Dataverse queries, see [Query anti-patterns](../../query-antipatterns.md).

### Select only the columns you need

Selecting fewer columns reduces the amount of data transferred. Avoid requesting columns you don't use:

```sql
-- Avoid selecting all columns
-- SELECT * FROM account (not supported)

-- Select only needed columns
SELECT name, telephone1
FROM account
```

### Filter on indexed columns

Filtering on primary keys and other indexed columns is faster than filtering on unindexed fields.

```sql
SELECT name, telephone1
FROM account
WHERE accountid = '00000000-0000-0000-0000-000000000000'
```

### Limit JOIN depth

You can use multitable joins, but each extra join raises the query cost. Limit joins to what you need for your query.
