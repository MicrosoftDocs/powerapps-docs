---
title: Relationship management
description: Learn how to create relationships between tables.
ms.date: 05/20/2026
author: phecke
ms.author: pehecke
ms.reviewer: pehecke
ms.topic: concept-article
---

# Manage table relationships

Table relationships in Microsoft Dataverse define the ways that table rows can be associated with rows from other tables or the same table. There are two types of table relationships: one-to-many, and many-to-many. You can create create relationships between tables by using the relationship APIs as demonstrated below.

More information: [Microsoft Dataverse table relationships](../../../maker/data-platform/create-edit-entity-relationships.md)

```python
from PowerPlatform.Dataverse.models.relationship import (
    LookupAttributeMetadata,
    OneToManyRelationshipMetadata,
    ManyToManyRelationshipMetadata,
)
from PowerPlatform.Dataverse.models.labels import Label, LocalizedLabel

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
print(f"Created lookup field: {result['lookup_schema_name']}")

# Create a many-to-many relationship: Employee (N) <-> Project (N)
# Employees work on multiple projects; projects have multiple team members
m2m_relationship = ManyToManyRelationshipMetadata(
    schema_name="new_employee_project",
    entity1_logical_name="new_employee",
    entity2_logical_name="new_project",
)

result = client.tables.create_many_to_many_relationship(m2m_relationship)
print(f"Created M:N relationship: {result['relationship_schema_name']}")

# Query relationship metadata
rel = client.tables.get_relationship("new_Department_Employee")
if rel:
    print(f"Found: {rel['SchemaName']}")

# List all relationships
rels = client.tables.list_relationships()
for rel in rels:
    print(f"{rel['SchemaName']} ({rel.get('@odata.type')})")

# List relationships for a specific table (one-to-many + many-to-one + many-to-many)
account_rels = client.tables.list_table_relationships("account")
for rel in account_rels:
    print(f"{rel['SchemaName']} -> {rel.get('@odata.type')}")

# Delete a relationship
client.tables.delete_relationship(result['relationship_id'])
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

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
