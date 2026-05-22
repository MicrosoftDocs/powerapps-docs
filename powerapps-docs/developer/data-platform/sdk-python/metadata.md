---
title: Use metadata to customize tables and columns
description: Learn how to customize Dataverse tables and columns definitions using metadata.
author: phecke
ms.author: pehecke
ms.reviewer: pehecke
ms.date: 05/20/2026
ms.topic: concept-article
---

# Customize tables and columns

The SDK supports create, update, and delete (CUD) operations for [custom tables](quick-guide-dataverse.md#tables) and columns, optional solution association, plus retrieve and list table definitions.

Let's look at example code for working with a custom table.

```python
# Create a custom table, including the customization prefix value in the schema names for the table and columns.
table_info = client.tables.create("new_Product", {
    "new_Code": "string",
    "new_Description": "memo",
    "new_Price": "decimal",
    "new_Active": "bool"
})

# Create with custom primary column name and solution assignment
table_info = client.tables.create(
    "new_Product",
    columns={
        "new_Code": "string",
        "new_Price": "decimal"
    },
    solution="MyPublisher",  # Optional: add to specific solution
    primary_column="new_ProductName",  # Optional: custom primary column (default is "{customization prefix value}_Name")
)

# Get table information
info = client.tables.get("new_Product")
print(f"Logical name: {info['table_logical_name']}")
print(f"Entity set: {info['entity_set_name']}")

# List all tables
tables = client.tables.list()
for table in tables:
    print(table)

# Add columns to existing table (columns must include customization prefix value)
client.tables.add_columns("new_Product", {"new_Category": "string"})

# Remove columns
client.tables.remove_columns("new_Product", ["new_Category"])

# List all columns (attributes) for a table to discover schema
columns = client.tables.list_columns("account")
for col in columns:
    print(f"{col['LogicalName']} ({col.get('AttributeType')})")

# List only specific properties
columns = client.tables.list_columns(
    "account",
    select=["LogicalName", "SchemaName", "AttributeType"],
    filter="AttributeType eq 'String'",
)

# Clean up
client.tables.delete("new_Product")
```

> [!IMPORTANT]
> All custom column names must include the customization prefix value (for example, "new_"). This requirement ensures explicit, predictable naming and aligns with Dataverse metadata requirements.

For more information about working with custom table metadata:

- `create` always returns a list of GUIDs (length=1 for single input).
- `update` and `delete` return `None` for both single and multiple interfaces.
- Passing a list of payloads to `create` triggers a bulk create and returns `list[str]` of IDs.
- `get` supports single record retrieval with record ID or paging through result sets (prefer select to limit columns).
- For CRUD methods that take a record ID, pass the GUID string (36-character hyphenated). Parentheses around the GUID are accepted but not required.

## Related information

- [Tables](quick-guide-dataverse.md#tables)
- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
