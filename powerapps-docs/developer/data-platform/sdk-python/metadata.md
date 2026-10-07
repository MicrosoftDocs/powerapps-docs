---
title: Use metadata to customize tables and columns
description: Learn how to customize Dataverse tables and columns definitions using metadata.
author: kewear
ms.author: kewear
ms.reviewer: pehecke
ms.date: 10/06/2026
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

## Set column constraints

To set constraints such as length, numeric range, precision, format, required level, or display name, pass a dictionary instead of a bare type string. The `type` key holds the column type, and the remaining keys set the constraints.

| Key | Applies to | Description |
| --- | --- | --- |
| `max_length` | `string`, `memo` | Maximum number of characters. |
| `min_value`, `max_value` | `int`, `decimal`, `money`, `float` | Allowed numeric range. |
| `precision` | `decimal`, `money`, `float` | Number of decimal places. |
| `format` | `string`, `int`, `datetime` | Format name for text columns (for example, `Email`, `Url`, or `Phone`), or the format for integer and date/time columns. |
| `required` | all | Required level: `None`, `Recommended`, or `ApplicationRequired`. |
| `display_name` | all | Display label shown in the maker portal and apps. |

```python
# Pass a dict spec to set constraints; a bare type string still works for simple columns.
client.tables.create("new_Feedback", {
    "new_Rating":  {"type": "int",  "min_value": 1, "max_value": 5},
    "new_Comment": {"type": "memo", "max_length": 2000, "display_name": "Comment"},
})
```

You can use dict specs anywhere a column type is accepted, including `add_columns()` and batch column creation.

## Update column definitions

Use `update_column` to change one column's constraints, or `update_columns` to change several in a single call. Both accept the same override keys as `create`. The SDK validates every specification before it sends any request, so an invalid entry fails the whole call without leaving earlier columns changed.

```python
# Widen one column
client.tables.update_column("new_Feedback", "new_Comment", {"max_length": 4000})

# Update several columns at once
client.tables.update_columns("new_Feedback", {
    "new_Rating":  {"max_value": 10},
    "new_Comment": {"display_name": "Customer Comment"},
})
```

An update retrieves the complete column definition, applies your changes, and sends the full definition back to Dataverse with the `MSCRM.MergeLabels` header. Labels in other languages are preserved, so changing one property (for example, `max_length`) leaves the rest of the column unchanged.

## Read typed column metadata

By default, `list_columns` and `get_column` return the base attribute metadata. Pass `typed=True` to retrieve the type-specific definition in a single request, which includes properties such as `MaxLength` for text columns or `MinValue` and `MaxValue` for numeric columns.

```python
# One column, with its type-specific fields
col = client.tables.get_column("new_Feedback", "new_Comment", typed=True)
print(col["MaxLength"])   # 4000

# All columns, each with type-specific fields
cols = client.tables.list_columns("new_Feedback", typed=True)
```

> [!NOTE]
> The `filter` parameter applies only to the default (`typed=False`) listing. Combining `filter` with `typed=True` raises a `ValueError`.

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

- `tables.create` returns a `TableInfo` object that describes the new table. It doesn't return record IDs.
- `tables.get` returns `None` when the table doesn't exist, which makes schema setup idempotent.
- `tables.add_columns` and `tables.remove_columns` return the list of column names that changed.
- `tables.list_columns` returns raw attribute metadata dictionaries that use the Web API PascalCase property names, such as `LogicalName` and `AttributeType`.

To create, read, update, and delete *records* in a table, see [Work with data](work-data.md).

## Related information

- [Tables](quick-guide-dataverse.md#tables)
- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
