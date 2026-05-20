---
title: Use metadata to customize tables and columns
description: Learn how to customize Dataverse tables and columns definitions using metadata.
author: phecke
ms.author: pehecke
ms.reviewer: pehecke
ms.date: 05/14/2026
ms.topic: concept-article
---

# Customize tables and columns

The SDK supports create, update, and delete (CUD) operations for [custom tables](quick-guide-dataverse.md#tables) and columns, optional solution association, plus retrieve and list table definitions.

Let's look at example code for working with a custom table.

```python
# Support enumerations with labels in different languages
class Status(IntEnum):
    Active = 1
    Inactive = 2
    Archived = 5
    __labels__ = {
        1033: {
            "Active": "Active",
            "Inactive": "Inactive",
            "Archived": "Archived",
        },
        1036: {
            "Active": "Actif",
            "Inactive": "Inactif",
            "Archived": "Archivé",
        }
    }

# Create a simple custom table and a few columns
info = client.create_table(
    "SampleItem",  # friendly name; defaults to SchemaName new_SampleItem
    {
        "code": "string",
        "count": "int",
        "amount": "decimal",
        "when": "datetime",
        "active": "bool",
        "status": Status,
    },
)

logical = info["entity_logical_name"]  # for example, "new_sampleitem"

# Create a record in the new table
# Set your publisher prefix (used when creating the table). If you used the default, it's "new".
prefix = "new"
name_attr = f"{prefix}_name"
id_attr = f"{logical}id"

rec_id = client.create(logical, {name_attr: "Sample A"})[0]

# Clean up
client.delete(logical, rec_id)          # delete record
client.delete_table("SampleItem")       # delete table (friendly name or explicit schema new_SampleItem)
```

For more information about working with custom table metadata:

- `create` always returns a list of GUIDs (length=1 for single input).
- `update` and `delete` return `None` for both single and multiple interfaces.
- Passing a list of payloads to `create` triggers a bulk create and returns `list[str]` of IDs.
- `get` supports single record retrieval with record ID or paging through result sets (prefer select to limit columns).
- For CRUD methods that take a record ID, pass the GUID string (36-character hyphenated). Parentheses around the GUID are accepted but not required.
<!-- TODO: Move this to the SQL article when written-->
- SQL queries are executed directly against the entity set endpoints by using the `?sql=` parameter. Supported subset only (single SELECT, optional WHERE/TOP/ORDER BY, alias). The service rejects unsupported constructs.

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
