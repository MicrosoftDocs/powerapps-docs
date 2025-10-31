---
title: "SDK package reference (preview)"
description: "Python API reference."
ms.author: paulliew
author: paulliew
ms.date: 10/31/2025
ms.reviewer: phecke
ms.topic: quickstart-sdk
contributors:
 - phecke
---

# Dataverse SDK for Python Package Reference

## Data operations

| Method | Signature (simplified) | Returns | Notes |
|--------|------------------------|---------|-------|
| `create` | `create(logical_name, record_dict)` | `list[str]` (len 1) | Single create; GUID from `OData-EntityId`. |
| `create` | `create(logical_name, list[record_dict])` | `list[str]` | Uses `CreateMultiple`; stamps `@odata.type` if missing. |
| `get` | `get(logical_name, id)` | `dict` | One record; supply GUID (with/without parentheses). |
| `get` | `get(logical_name, ..., page_size=None)` | `Iterable[list[dict]]` | Multiple records; Pages yielded (non-empty only). |
| `update` | `update(logical_name, id, patch)` | `None` | Single update; no representation returned. |
| `update` | `update(logical_name, list[id], patch)` | `None` | Broadcast; same patch applied to all IDs (UpdateMultiple). |
| `update` | `update(logical_name, list[id], list[patch])` | `None` | 1:1 patches; lengths must match (UpdateMultiple). |
| `delete` | `delete(logical_name, id)` | `None` | Delete one record. |
| `delete` | `delete(logical_name, list[id])` | `None` | Delete many (sequential). |

## SQL operations

| Method | Signature (simplified) | Returns | Notes |
|--------|------------------------|---------|-------|
| `query_sql` | `query_sql(sql)` | `list[dict]` | Constrained read-only SELECT via `?sql=`. |

## Metadata operations

| Method | Signature (simplified) | Returns | Notes |
|--------|------------------------|---------|-------|
| `create_table` | `create_table(tablename, schema)` | `dict` | Creates custom table + columns. Friendly name (e.g. `SampleItem`) becomes schema `new_SampleItem`; explicit schema name (contains `_`) used as-is. |
| `get_table_info` | `get_table_info(schema_name)` | `dict | None` | Basic table metadata by schema name (e.g. `new_SampleItem`). Friendly names not auto-converted. |
| `list_tables` | `list_tables()` | `list[dict]` | Lists non-private tables. |
| `delete_table` | `delete_table(tablename)` | `None` | Drops custom table. Accepts friendly or schema name; friendly converted to `new_<PascalCase>`. |

## Pandas client

| Method | Signature (simplified) | Returns | Notes |
|--------|------------------------|---------|-------|
| `PandasODataClient.create_df` | `create_df(logical_name, series)` | `str` | Create one record (returns GUID). |
| `PandasODataClient.update` | `update(logical_name, id, series)` | `None` | Returns None; ignored if Series empty. |
| `PandasODataClient.get_ids` | `get_ids(logical_name, ids, select=None)` | `DataFrame` | One row per ID (errors inline). |
| `PandasODataClient.query_sql_df` | `query_sql_df(sql)` | `DataFrame` | DataFrame for SQL results. |

## Additional information

- `create` always returns a list of GUIDs (1 for single, N for bulk).
- `update`/`delete` always return `None` (single and multi forms).
- Bulk update chooses broadcast vs per-record by the type of `changes` (dict vs list).
- Paging and SQL operations never mutate inputs.
- Metadata lookups for logical name stamping cached per entity set (in-memory).
