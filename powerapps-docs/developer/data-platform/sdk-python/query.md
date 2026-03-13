---
title: Querying data (preview)
description: Learn how to query Dataverse data using the SDK for Python.
ms.author: paulliew
author: paulliew
ms.date: 03/13/2026
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Querying data (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

This article describes available methods for querying Dataverse data using the SDK for Python. You can query data using Structured Query Language (SQL) and OData based APIs. <!--, and the Dataverse Web API.-->

Python developers should first learn about the SDK for Python by reading [Getting started (preview)](get-started.md) before continuing with this article.

## Query data using SQL

The SQL endpoint of the Dataverse web service provides a read-only interface to a limited set of SQL `SELECT` commands. This article describes what `SELECT` query options are available. You can also access the SQL endpoint by using the Dataverse Web API, so code written in languages other than Python can access it.

> [!IMPORTANT]
> The SQL support is limited to read-only queries. Complex joins, subqueries, and certain SQL functions may not be supported. The SQL query must follow the supported subset:
>
> - WHERE can only be a boolean expression tree where leaves are binary operators ( =, >, like, etc.) with one of the arguments being a direct column reference and another is a constant
> - TOP only allows an integer literal
> - ORDERBY can only reference columns and does not allow any complex expressions

The following example code demonstrates a SQL query in Python.

```python
# SQL query (read-only)
results = client.query.sql(
    "SELECT TOP 10 accountid, name FROM account WHERE statecode = 0"
)
for record in results:
    print(record["name"])
```

This call returns a list of result row dictionaries. An empty list is returned when no rows match.

## Query data using OData

You can use the SDK for Python `client.records` APIs to issue OData queries for data.

```python
# OData query with paging
# Note: filter and expand parameters are case sensitive
for page in client.records.get(
    "account",
    select=["accountid", "name"],  # select is case-insensitive (automatically lowercased)
    filter="statecode eq 0",       # filter must use lowercase logical names (not transformed)
    top=100,
):
    for record in page:
        print(record["name"])

# Query with navigation property expansion (case-sensitive!)
for page in client.records.get(
    "account",
    select=["name"],
    expand=["primarycontactid"],  # Navigation property names are case-sensitive
    filter="statecode eq 0",      # Column names must be lowercase logical names
):
    for account in page:
        contact = account.get("primarycontactid", {})
        print(f"{account['name']} - Contact: {contact.get('fullname', 'N/A')}")
```

When writing your OData calls, follow these guidelines.

- For the `filter` parameter, use exact lowercase logical names for column names (for example, "statecode eq 0", not "StateCode eq 0").
- For the `expand` parameter, use case-sensitive navigation property names that match the exact server names.
- The `select` statement and `orderby` parameter are case-insensitive and automatically converted to lowercase.

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started (preview)](get-started.md)
- [Use the Microsoft Dataverse Web API](../webapi/overview.md)
- [Use SQL to query data](../dataverse-sql-query.md)
