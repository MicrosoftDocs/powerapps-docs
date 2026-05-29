---
title: Query data
description: Learn how to query Dataverse data using the SDK for Python.
ms.author: kewear
author: kewear
ms.date: 05/21/2026
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Query data

This article describes available methods for querying Dataverse data by using the SDK for Python. You can query data by using Structured Query Language (SQL) and OData-based APIs.

Python developers should first learn about the SDK for Python by reading [Getting started](get-started.md) before continuing with this article.

## QueryBuilder

QueryBuilder is the recommended way to query records. It provides a fluent, type-safe interface that generates correct OData queries automatically. You don't need to remember OData filter syntax.

```python
# Fluent query builder (recommended)
from PowerPlatform.Dataverse.models.filters import col

for record in (client.query.builder("account")
               .select("name", "revenue")
               .where(col("statecode") == 0)
               .where(col("revenue") > 1000000)
               .order_by("revenue", descending=True)
               .top(100)
               .page_size(50)
               .execute()):
    print(f"{record['name']}: {record['revenue']}")
```

QueryBuilder handles value formatting, column name casing, and OData syntax automatically. Build filter expressions with `col()` and standard Python operators.

```python
# Get results as a pandas DataFrame (consolidates all pages)
df = (client.query.builder("account")
      .select("name", "telephone1")
      .where(col("statecode") == 0)
      .top(100)
      .execute()
      .to_dataframe())
print(f"Got {len(df)} accounts")
```

```python
# Comparison filters using col() expressions
query = (client.query.builder("contact")
         .where(col("statecode") == 0)                        # statecode eq 0
         .where(col("revenue") > 1000000)                     # revenue gt 1000000
         .where(col("name").contains("Corp"))                 # contains(name, 'Corp')
         .where(col("statecode").in_([0, 1]))                 # Microsoft.Dynamics.CRM.In(...)
         .where(col("revenue").between(100000, 500000))       # revenue ge 100000 and revenue le 500000
         .where(col("telephone1").is_null())                  # telephone1 eq null
         )
```

For complex logic (OR, NOT, grouping), compose expressions with `&`, `|`, `~`:

```python
from PowerPlatform.Dataverse.models.filters import col

# OR conditions: (statecode = 0 OR statecode = 1) AND revenue > 100k
for record in (client.query.builder("account")
               .select("name", "revenue")
               .where(((col("statecode") == 0) | (col("statecode") == 1))
                      & (col("revenue") > 100000))
               .execute()):
    print(record["name"])

# NOT, between, and in operators
for record in (client.query.builder("account")
               .where(col("statecode") != 2)                       # NOT inactive
               .where(col("revenue").between(100000, 500000))      # revenue in range
               .execute()):
    print(record["name"])
```

### Formatted values and annotations

This example demonstrates how to request localized labels, currency symbols, and display names.

```python
# Get formatted values (choice labels, currency, lookup names) — via query builder
for record in (client.query.builder("account")
               .select("name", "statecode", "revenue")
               .include_formatted_values()
               .execute()):
    status = record["statecode@OData.Community.Display.V1.FormattedValue"]
    print(f"{record['name']}: {status}")

# Get formatted values — via records.list() / records.retrieve() include_annotations param
result = client.records.list(
    "account",
    select=["name", "statecode"],
    include_annotations="OData.Community.Display.V1.FormattedValue",
)
for record in result:
    label = record.get("statecode@OData.Community.Display.V1.FormattedValue")
    print(f"{record['name']}: {label}")

record = client.records.retrieve(
    "account", account_id,
    select=["name", "statuscode"],
    include_annotations="OData.Community.Display.V1.FormattedValue",
)
if record:
    print(record.get("statuscode@OData.Community.Display.V1.FormattedValue"))
```

### Expand navigation properties

Use nested expand with options to expand navigation properties by using `$select`, `$filter`, `$orderby`, and `$top`.

```python
from PowerPlatform.Dataverse.models.query_builder import ExpandOption

# Expand related tasks with filtering and sorting
for record in (client.query.builder("account")
               .select("name")
               .expand(ExpandOption("Account_Tasks")
                       .select("subject", "createdon")
                       .filter("contains(subject,'Task')")
                       .order_by("createdon", descending=True)
                       .top(5))
               .execute()):
    print(record["name"], record.get("Account_Tasks"))
```

### Paging

Use `execute_pages()` to stream large result sets with full builder options, such as filtering, sorting, and formatted values. For simpler string-based OData filter queries, use `records.list()` and `records.list_pages()` as shortcuts.

```python
# Preferred: query.builder().execute_pages() — stream one page at a time, memory stays flat
# Supports composable filters, sorting, formatted values, and expand with nested selects
for page_num, page in enumerate(
    client.query.builder("account")
    .select("accountid", "name", "revenue")
    .where(col("statecode") == 0)
    .order_by("name")
    .page_size(500)        # optional: override Dataverse default (~5000/page)
    .execute_pages()
):
    print(f"Page {page_num + 1}: {len(page)} records")
    for record in page:
        print(f"  {record['name']}")

# Simple shortcut: records.list() — automatic paging, all records in memory
# Use for basic filter+select queries; string OData filter only (no composable expressions)
result = client.records.list(
    "account",
    filter="statecode eq 0",
    select=["name", "revenue"],
    orderby=["name asc"],          # optional sort
    top=500,                       # bounds total records returned and number of HTTP round-trips
    page_size=200,                 # optional: hint Dataverse default page size
)
for record in result:
    print(record["name"])

# Simple streaming shortcut: records.list_pages() — same params as records.list(), yields one page at a time
for page_num, page in enumerate(
    client.records.list_pages("account", filter="statecode eq 0", select=["name"], orderby=["name asc"])
):
    print(f"Page {page_num + 1}: {len(page)} records")
    for record in page:
        print(record["name"])
```

> [!NOTE]
> Both `execute(by_page=True)` and `execute(by_page=False)` are deprecated and emit a `UserWarning`. Replace them with `execute_pages()` (streaming) or plain `execute()` (eager). `QueryBuilder.to_dataframe()` is also deprecated - use `.execute().to_dataframe()` instead.
>
> The migration tool rewrites all of these calls automatically. Install the migration tool by running `pip install PowerPlatform-Dataverse-Client[migration]` and run `dataverse-migrate path/to/your/scripts/`. Alternately, execute `python -m PowerPlatform.Dataverse.migration.migrate_v0_to_v1` for development checkouts.

### Record count

To get a record count, include `$count=true` in the request.

```python
# Via query builder
results = (client.query.builder("account")
           .where(col("statecode") == 0)
           .count()
           .execute())

# Via records.list() — count=True adds $count=true to the OData request
results = client.records.list("account", filter="statecode eq 0", count=True)
```

### FetchXML queries

Calling `client.query.fetchxml()` returns an inert `FetchXmlQuery` object. No HTTP request is made until you call `.execute()` or `.execute_pages()`.

```python
xml = """
<fetch>
  <entity name="account">
    <attribute name="name"/>
    <attribute name="revenue"/>
    <filter><condition attribute="statecode" operator="eq" value="0"/></filter>
  </entity>
</fetch>
"""

# .execute() — blocking, fetches all pages and returns a single QueryResult
result = client.query.fetchxml(xml).execute()
df = result.to_dataframe()

# .execute_pages() — streaming, yields one QueryResult per HTTP page
# Use count="N" in the FetchXML <fetch> element to set page size
for page_num, page in enumerate(client.query.fetchxml(xml).execute_pages()):
    print(f"Page {page_num + 1}: {len(page)} records")
    for record in page:
        print(record["name"])
```

### Simple list shortcut

 The `records.list()` call accepts a raw OData filter string for basic queries. For anything beyond simple filter+select, prefer using `client.query.builder()` that provides composable filters, formatted values, and nested expand.

```python
# records.list() shortcut — raw OData filter string, all records loaded into memory
# Column names in filter must be lowercase logical names
for record in client.records.list(
    "account",
    select=["name"],
    filter="statecode eq 0",
    top=100,
):
    print(record["name"])

# Discover navigation property names for $expand (metadata-discovery helper, kept at GA)
nav_props = client.query.odata_expands("account")  # → list of navigation property metadata

# Expand navigation properties using the query builder
from PowerPlatform.Dataverse.models.query_builder import ExpandOption
for record in (client.query.builder("contact")
               .select("fullname")
               .expand(ExpandOption("parentcustomerid_account").select("name"))
               .execute()):
    acct = record.get("parentcustomerid_account") or {}
    print(f"{record['fullname']} -> {acct.get('name')}")

# Build @odata.bind for lookup fields (deprecated helper, still functional with DeprecationWarning)
bind = client.query.odata_bind("contact", "account", account_id)
# Returns: {"parentcustomerid_account@odata.bind": "/accounts(guid)"}
client.records.create("contact", {"firstname": "Jane", **bind})
```

## Query data using SQL

The SQL endpoint of the Dataverse web service provides a read-only interface to a limited set of SQL `SELECT` commands. Support for SQL JOINs, aggregates, GROUP BY, DISTINCT, and OFFSET FETCH pagination is provided.

You can also access the SQL endpoint using the Dataverse Web API `?sql=` parameter so code written in languages other than Python can access Dataverse data.

> [!IMPORTANT]
> The SQL support is limited to read-only queries. Complex joins, subqueries, and certain SQL functions may not be supported. The SQL query must follow the supported subset:
>
> - WHERE can only be a boolean expression tree where leaves are binary operators ( =, >, like, etc.) with one of the arguments being a direct column reference and another is a constant
> - TOP only allows an integer literal
> - ORDERBY can only reference columns and does not allow any complex expressions

The following example code demonstrates a SQL query in Python.

```python
# Basic query
results = client.query.sql(
    "SELECT TOP 10 accountid, name FROM account WHERE statecode = 0"
)

# JOINs and aggregates work
results = client.query.sql(
    "SELECT a.name, COUNT(c.contactid) as cnt "
    "FROM account a "
    "JOIN contact c ON a.accountid = c.parentcustomerid "
    "GROUP BY a.name"
)

# SQL results directly as a DataFrame
df = client.dataframe.sql(
    "SELECT name, revenue FROM account ORDER BY revenue DESC"
)

# Discover columns from metadata (schema-discovery helper, kept at GA)
cols_meta = client.query.sql_columns("account")
col_names = [c["LogicalName"] for c in cols_meta]

# Build queries using the discovered column names
sql = f"SELECT TOP 10 {', '.join(col_names[:5])} FROM account"
df = client.dataframe.sql(sql)
```

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Use the Microsoft Dataverse Web API](../webapi/overview.md)
- [Use SQL to query data](../dataverse-sql-query.md)
