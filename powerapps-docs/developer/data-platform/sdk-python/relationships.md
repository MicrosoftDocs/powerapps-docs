---
title: Relationship management
description: Learn how to create relationships between tables.
ms.date: 08/28/2026
author: kewear
ms.author: kewear
ms.reviewer: pehecke
ms.topic: concept-article
---

# Manage table relationships

Table relationships in Microsoft Dataverse define how table rows can be associated with rows from other tables or the same table. There are two types of table relationships: one-to-many, and many-to-many. You can create relationships between tables by using the relationship APIs as demonstrated in the following section.

More information: [Microsoft Dataverse table relationships](../../../maker/data-platform/create-edit-entity-relationships.md)

```python
from PowerPlatform.Dataverse.models import (
    CascadeConfiguration,
    Label,
    LocalizedLabel,
    LookupAttributeMetadata,
    ManyToManyRelationshipMetadata,
    OneToManyRelationshipMetadata,
)

# Create a one-to-many relationship: Department (1) -> Employee (N)
# This adds a "Department" lookup field to the Employee table
lookup = LookupAttributeMetadata(
    schema_name="new_DepartmentId",
    display_name=Label(localized_labels=[LocalizedLabel(label="Department", language_code=1033)]),
)

relationship = OneToManyRelationshipMetadata(
    schema_name="new_Department_Employee",
    referenced_entity="new_department",   # Parent table (the "one" side)
    referencing_entity="new_employee",    # Child table (the "many" side)
    referenced_attribute="new_departmentid",
)

result = client.tables.create_one_to_many_relationship(lookup, relationship)
print(f"Created lookup field: {result.lookup_schema_name}")

# Create a many-to-many relationship: Employee (N) <-> Project (N)
# Employees work on multiple projects; projects have multiple team members
m2m_relationship = ManyToManyRelationshipMetadata(
    schema_name="new_employee_project",
    entity1_logical_name="new_employee",
    entity2_logical_name="new_project",
)

result = client.tables.create_many_to_many_relationship(m2m_relationship)
print(f"Created M:N relationship: {result.relationship_schema_name}")

# Query relationship metadata
rel = client.tables.get_relationship("new_Department_Employee")
if rel:
    print(f"Found: {rel.relationship_schema_name}")

# List all relationships
rels = client.tables.list_relationships()
for rel in rels:
    print(f"{rel['SchemaName']} ({rel.get('RelationshipType')})")

# List relationships for a specific table (one-to-many + many-to-one + many-to-many)
account_rels = client.tables.list_table_relationships("account")
for rel in account_rels:
    print(f"{rel['SchemaName']} -> {rel.get('RelationshipType')}")

# Delete a relationship
client.tables.delete_relationship(result.relationship_id)
```

For simpler scenarios, use the convenience method.

```python
# Quick way to create a lookup field with sensible defaults
result = client.tables.create_lookup_field(
    referencing_table="contact",       # Child table gets the lookup field
    lookup_field_name="new_AccountId",
    referenced_table="account",        # Parent table being referenced
    display_name="Account",
)
```

For a complete working example, see [examples/advanced/relationships.py](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/examples/advanced/relationships.py).

## Configure cascade behavior

`CascadeConfiguration` controls what happens to child records when you perform an action on the parent record in a one-to-many relationship. The following values are valid for each cascade property (`assign`, `delete`, `merge`, `reparent`, `share`, `unshare`).

| Value | Behavior |
|---|---|
| `"Cascade"` | Perform the action on all associated child records. |
| `"NoCascade"` | Don't apply the action to any child records. |
| `"RemoveLink"` | Remove the lookup field value on all child records when the parent record is deleted. |
| `"Restrict"` | Prevent the parent record from being deleted when child records exist. |

By default, `delete` is `"RemoveLink"` and all other properties are `"NoCascade"`. You can import the constants to use the string values directly.

```python
from PowerPlatform.Dataverse.common.constants import (
    CASCADE_BEHAVIOR_CASCADE,
    CASCADE_BEHAVIOR_NO_CASCADE,
    CASCADE_BEHAVIOR_REMOVE_LINK,
    CASCADE_BEHAVIOR_RESTRICT,
)

relationship = OneToManyRelationshipMetadata(
    schema_name="new_Department_Employee",
    referenced_entity="new_department",
    referencing_entity="new_employee",
    referenced_attribute="new_departmentid",
    cascade_configuration=CascadeConfiguration(delete=CASCADE_BEHAVIOR_REMOVE_LINK),
)
```

## RelationshipInfo return object

The relationship-creation methods return a `RelationshipInfo` object with the following fields.

| Field | Description |
|---|---|
| `relationship_id` | GUID of the relationship metadata. Pass this value to `delete_relationship`. |
| `relationship_schema_name` | Schema name of the relationship. |
| `relationship_type` | `"one_to_many"` or `"many_to_many"`. |
| `lookup_schema_name` | Schema name of the lookup field created on the child table (one-to-many only). |
| `referenced_entity` / `referencing_entity` | Parent and child table logical names (one-to-many). |
| `entity1_logical_name` / `entity2_logical_name` | The two table logical names (many-to-many). |

> [!NOTE]
> If you don't supply an `intersect_entity_name` for a many-to-many relationship, the intersect table uses the relationship's `schema_name` as its name.

## create_lookup_field options

The `create_lookup_field` convenience method accepts the following optional parameters.

| Parameter | Default | Description |
|---|---|---|
| `display_name` | Referenced table name | Display name shown for the lookup field. |
| `description` | `None` | Optional description for the lookup field. |
| `required` | `False` | Whether the lookup field is required. |
| `cascade_delete` | `"RemoveLink"` | Delete cascade behavior: `"RemoveLink"`, `"Cascade"`, or `"Restrict"`. |
| `language_code` | `1033` | Language code (LCID) for generated labels. |
| `solution` | `None` | Solution unique name to associate the relationship with. |

```python
result = client.tables.create_lookup_field(
    referencing_table="new_order",
    lookup_field_name="new_AccountId",
    referenced_table="account",
    display_name="Account",
    required=True,
    cascade_delete="RemoveLink",
)
```

> [!IMPORTANT]
> Deleting a one-to-many relationship also removes the associated lookup field from the child table. This operation is irreversible. You must delete relationships before you can delete the tables they connect. `list_table_relationships` raises a `MetadataError` if the specified table doesn't exist.

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
