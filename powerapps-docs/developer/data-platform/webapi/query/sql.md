---
title: Use SQL to Query Data With the Dataverse Web API (Preview)
description: Learn how to use SQL to query data with the Microsoft Dataverse Web API. Retrieve table data using SQL SELECT commands passed via the sql query option.
ms.date: 03/17/2026
ms.topic: how-to
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - saurabhrb
  - JimDaly
---
# Use SQL to query data by using the Dataverse Web API (preview)

You can use Structured Query Language (SQL) to query data from Microsoft Dataverse by using the Web API. Pass SQL `SELECT` commands through the `sql` query option, using the entity set name of the table you want to query.

To use a SQL query like this:

```sql
SELECT name 
FROM account AS a 
WHERE a.name LIKE 'Fourth Coffee'
```

Set the URL encoded value of the query to the `sql` query option to an [entityset resource ](overview.md#entityset-resources) that matches the base table of your query.

**Request**

This example uses *percent-encoding* for the SQL query since spaces aren't allowed in a URL:

```http
GET [Organization URI]/api/data/v9.2/accounts?sql=SELECT%20name%20%0D%0AFROM%20account%20AS%20a%20%0D%0AWHERE%20a.name%20LIKE%20'Fourth%20Coffee' HTTP/1.1
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="*"
Accept: application/json
```


**Response**

The response is exactly what you get with the equivalent OData query: `accounts?$select=name&$filter=contains(name,'Fourth Coffee')`

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

List specific column names in the `SELECT` clause, separated by commas. You can use table aliases to qualify column references and column aliases to rename output fields.

> [!IMPORTANT]
> `SELECT *` is not supported. You must explicitly name each column you want to retrieve.

The following example selects three columns from the `account` table using a table alias:

```sql
SELECT a.name, a.telephone1, a.websiteurl
FROM account AS a
```

Use `DISTINCT` to return unique values:

```sql
SELECT DISTINCT a.address1_city
FROM account AS a
```

Use column aliases to rename output fields:

```sql
SELECT a.name AS account_name, a.telephone1 AS phone
FROM account AS a
```

## Join tables

Use `INNER JOIN` or `LEFT JOIN` to combine rows from two or more tables. Join on a related column, typically a primary key to a foreign key.

> [!NOTE]
> `RIGHT JOIN`, `FULL OUTER JOIN`, and `CROSS JOIN` are not supported.

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
SELECT TOP 10 a.name, c.fullname, o.name AS opportunity_name
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

## Order rows

Use `ORDER BY` to sort results by one or more columns. Specify `ASC` (ascending, the default) or `DESC` (descending).

> [!NOTE]
> `ORDER BY` can only reference column names. Expressions like `ORDER BY LEN(name)` are not supported.

The following example returns accounts sorted by name:

```sql
SELECT TOP 10 name, telephone1
FROM account
ORDER BY name ASC
```

Sort by multiple columns:

```sql
SELECT TOP 10 name, createdon
FROM account
ORDER BY name ASC, createdon DESC
```

## Page results

Use `TOP` with an integer literal to limit the number of rows returned. The maximum value for `TOP` is 5,000.

```sql
SELECT TOP 10 name, telephone1, websiteurl
FROM account
ORDER BY name
```

Use `OFFSET ... FETCH` with `ORDER BY` to implement keyset pagination:

```sql
SELECT name, accountid
FROM account
ORDER BY name
OFFSET 0 ROWS FETCH NEXT 25 ROWS ONLY
```

To retrieve the next page, advance the `OFFSET` value:

```sql
SELECT name, accountid
FROM account
ORDER BY name
OFFSET 25 ROWS FETCH NEXT 25 ROWS ONLY
```

Alternatively, use a cursor-based approach by filtering on the last seen ID from the previous page:

```sql
SELECT TOP 25 name, accountid
FROM account
WHERE accountid > '00000000-0000-0000-0000-000000000000'
ORDER BY accountid
```

## Aggregate data

Use aggregate functions with `GROUP BY` to summarize data. The supported aggregate functions are `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

> [!NOTE]
> `HAVING` is not supported. Filter data using a `WHERE` clause before aggregating.

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

### Always use `TOP` or `OFFSET FETCH`

Queries without a row limit can return large result sets that degrade performance. Always include `TOP` or `OFFSET ... FETCH NEXT`:

```sql
SELECT TOP 100 name, telephone1
FROM account
ORDER BY name
```

### Select only the columns you need

Selecting fewer columns reduces the amount of data transferred. Avoid requesting columns you don't use:

```sql
-- Avoid selecting all columns
-- SELECT * FROM account (not supported)

-- Select only needed columns
SELECT name, telephone1
FROM account
```

### Avoid leading wildcards in LIKE patterns

A leading wildcard (`%value`) forces a full table scan. Use a trailing wildcard or an exact match when possible:

```sql
-- Slower: leading wildcard causes a full scan
SELECT name FROM account WHERE name LIKE '%Coffee'

-- Faster: trailing wildcard can use an index
SELECT name FROM account WHERE name LIKE 'Fourth%'
```

### Filter on indexed columns

Filtering on primary keys and other indexed columns is faster than filtering on unindexed fields:

```sql
SELECT name, telephone1
FROM account
WHERE accountid = '00000000-0000-0000-0000-000000000000'
```

### Limit JOIN depth

While multi-table joins are supported, each additional join increases query cost. Limit joins to what is necessary for your query.
