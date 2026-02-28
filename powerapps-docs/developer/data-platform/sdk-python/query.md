---
title: Query data using SQL (preview)
description: Learn how to query Dataverse data from Python code using SQL.
ms.author: paulliew
author: paulliew
ms.date: 02/27/2026
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Query data using SQL (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

This article discusses using Structured Query Language (SQL) queries with the Dataverse SDK for Python. The SQL endpoint of the Dataverse web service provides a read-only interface to a limited set of SQL `SELECT` commands. This article describes what `SELECT` query options are available. Python developers should read [Getting started (preview)](get-started.md) first before continuing with this article.

You can also access the SQL endpoint by using the Dataverse Web API, so code written in languages other than Python can access it.

> [!IMPORTANT]
> The SQL support is limited to read-only queries. Complex joins, subqueries, and certain SQL functions may not be supported. The SQL query must follow the supported subset:
>
> - WHERE can only be a boolean expression tree where leaves are binary operators ( =, >, like, etc.) with one of the arguments being a direct column reference and another is a constant
> - TOP only allows an integer literal
> - ORDERBY can only reference columns and does not allow any complex expressions

## Query data with Python

When writing your SQL statements, follow these guidelines.

- For the `filter` parameter, use exact lowercase logical names for column names (for example, "statecode eq 0", not "StateCode eq 0").
- For the `expand` parameter, use case-sensitive navigation property names that match the exact server names.
- The `select` statement and `orderby` parameter are case-insensitive and automatically converted to lowercase.

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

## Query data with the Dataverse Web API

A `?sql` query option can be used in a Dataverse Web API call. The format of the message is shown in the next example where the query is on the "accounts" entity set.

```odata
[organization-root]/api/data/v9.2/accounts?sql=SELECT name FROM account AS a WHERE a.name LIKE "Fourth Coffee"
```

The web API call returns a standard OData JSON response, where the records are contained within the value array of the response body, for example:

```json
{
  "value": [
    {"accountid": "...", "name": "..."},
    {"accountid": "...", "name": "..."}
  ]
}
```

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started (preview)](get-started.md)
- [Use the Microsoft Dataverse Web API](../webapi/overview.md)
- [Use SQL to query data](../dataverse-sql-query.md)
