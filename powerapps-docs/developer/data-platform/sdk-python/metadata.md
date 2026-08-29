---
title: Use metadata to customize tables and columns
description: Learn how to customize Dataverse tables and columns definitions using metadata.
author: kewear
ms.author: kewear
ms.reviewer: pehecke
ms.date: 08/28/2026
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
    print(f"{col['name']} ({col.get('AttributeType')})")

# List only specific properties
columns = client.tables.list_columns(
    "account",
    select=["LogicalName", "SchemaName", "AttributeType"],
    filter="AttributeType eq 'String'",
)

# Clean up
client.tables.delete("new_Product")
```

## Supported column types

The following type strings are accepted by `create()` and `add_columns()`.

| Type | Accepted aliases |
|------|-----------------|
| `string` | `text` |
| `memo` | `multiline` |
| `int` | `integer` |
| `decimal` | `money` |
| `float` | `double` |
| `bool` | `boolean` |
| `datetime` | `date` |
| `file` | — |

For optionset (choice) columns, pass an `IntEnum` subclass (or an `Enum` whose members have integer values) directly as the column type value instead of a string. The SDK uses the class members to define the optionset values.

```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

table_info = client.tables.create("new_Task", {
    "new_Title": "string",
    "new_Priority": Priority,   # optionset column
})
```

## TableInfo return object

The `client.tables.create()` method returns a `TableInfo` object. Access its properties directly, or use legacy dict-key notation for backward compatibility.

```python
table_info = client.tables.create("new_Product", {"new_Code": "string"})

print(table_info.schema_name)       # new_Product
print(table_info.logical_name)      # new_product
print(table_info.entity_set_name)   # new_products
print(table_info.columns_created)   # ['new_Code', ...]

# Legacy dict-key access still works
print(table_info["table_schema_name"])
```

The `add_columns()` and `remove_columns()` methods return the list of column schema names that they create or remove. The `get()` method returns table metadata, or `None` if the table doesn't exist, which makes it useful for existence checks.

## Alternate keys

An alternate key identifies a record by one or more business columns instead of a Dataverse-generated GUID. Alternate keys are required for [upsert](work-data.md#upsert-create-and-update) operations. Define them in the Power Apps maker portal under **Table** > **Keys**, or programmatically by using `client.tables.create_alternate_key`.

```python
# Create an alternate key on the accountnumber column
key = client.tables.create_alternate_key(
    "account",
    "account_accountnumber_ak",
    ["accountnumber"],
    display_name="Account Number",
)
print(f"Created key {key.schema_name} ({key.metadata_id}), status={key.status}")

# The key status transitions from Pending to Active asynchronously - poll before upserting
for k in client.tables.get_alternate_keys("account"):
    if k.schema_name == "account_accountnumber_ak":
        print(f"{k.schema_name}: {k.status}")
```

> [!IMPORTANT]
> The transition from `Pending` to `Active` isn't immediate. Check the key status right after creation and wait until it's `Active` before issuing upsert requests. Without an active alternate key, Dataverse rejects upsert requests with a 400 error.

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
