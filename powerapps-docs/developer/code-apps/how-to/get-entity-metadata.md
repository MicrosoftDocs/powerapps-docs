---
title: "How to: Get metadata for Dataverse tables (preview)"
description: "Use the getMetadata function to retrieve metadata about Dataverse tables (entities) at runtime."
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 12/5/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# How to: Get metadata for Dataverse tables (preview)

Use the getMetadata() function to retrieve Dataverse table (entity) metadata at runtime. This function lightly wraps the [Dataverse Web API metadata query capabilities](/power-apps/developer/data-platform/webapi/query-metadata-web-api) and provides strongly-typed access to entity definitions, attributes, and relationships.

## Function signature

```typescript
AccountsService.getMetadata(
  options?: GetEntityMetadataOptions<Account>
): Promise<IOperationResult<Partial<EntityMetadata>>>
```
> [!NOTE]
> You must follow the steps in **Set up your code app** in [Connect to Dataverse](/power-apps/developer/code-apps/how-to/connect-to-dataverse) to initialize the Power SDK and import the service file before calling `getMetadata()`.


### Options parameter

The `options` parameter allows you to specify which metadata to retrieve. See example:

```typescript
interface GetEntityMetadataOptions<Account> {
  metadata?: Array<"Privileges" | "DisplayName" | "IsCustomizable" | ...>;
  schema?: {
    columns?: "all" | Array<"name" | "telephone1" | "createdon" | ...>;
    oneToMany?: boolean;
    manyToOne?: boolean;
    manyToMany?: boolean;
  };
}
```

- `metadata`: array of entity-level properties to fetch. See [EntityMetadata](/power-apps/developer/data-platform/webapi/reference/entitymetadata?view=dataverse-latest) for a full list of queryable table properties.
- `schema`:
    - `columns`:  Retrieve column (attribute) metadata - `"all"` or an array of column logical names.
    - `oneToMany`, `manyToOne`, `manyToMany`: booleans to include relationship metadata
      
The response includes arrays named `Attributes` of type [AttributeMetadata](/power-apps/developer/data-platform/webapi/reference/attributemetadata?view=dataverse-latest), `OneToManyRelationships` of type [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata?view=dataverse-latest), `ManyToOneRelationships` of type [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata?view=dataverse-latest), and `ManyToManyRelationships` of type [ManyToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/manytomanyrelationshipmetadata?view=dataverse-latest) when requested.

## Examples

1. **Get user-localized labels for all columns**

Retrive display names in the user's language. Use these labels to drive form labels, table headers, and accessibility text.

```typescript
async function getColumnDisplayNames() {
  // Request all column metadata
  const { data } = await AccountsService.getMetadata({
    schema: { columns: 'all' }
  });

  const columnDisplayNames: Record<string, string> = {};
  if (data.Attributes) {
    for (const attr of data.Attributes) {
      const label = attr.DisplayName?.UserLocalizedLabel?.Label;
      if (label) {
        columnDisplayNames[attr.LogicalName] = label;
      }
    }
  }

  console.log(columnDisplayNames);
  // Output: { "accountid": "Account", "name": "Account Name", ... }
  return columnDisplayNames;
}
```

2. **Identify required fields for form validation**

Find attributes that are required on forms to build client‑side validation rules based on metadata instead of hard‑coding.

```typescript
async function getRequiredFields() {
  const { data } = await AccountsService.getMetadata({
    schema: { columns: 'all' }
  });
  if (!data.Attributes) return [];

  // Filter attributes that are required for forms
  const requiredColumns = data.Attributes
    .filter(attr => attr.IsRequiredForForm)
    .map(attr => ({
      logicalName: attr.LogicalName,
      displayName: attr.DisplayName?.UserLocalizedLabel?.Label,
      attributeType: attr.AttributeTypeName?.Value
    }));

  console.log('Required fields:', requiredColumns);
  // Output: [
  //   { logicalName: "name", displayName: "Account Name", attributeType: "StringType" },
  //   { logicalName: "ownerid", displayName: "Owner", attributeType: "OwnerType" }
  // ]
  
  return requiredColumns;
}
```

3. **Map column types for client-side validation**
   
Get attribute types to inform validation and UI controls. Choose the right UI control (e.g., date picker, money, choice) and validate values consistently.

```typescript
async function getColumnTypes() {
  const { data } = await AccountsService.getMetadata({
    schema: { columns: 'all' }
  });

  if (!data.Attributes) return [];

  // Map attributes to their types for validation
  const columnTypes = data.Attributes.map(attr => ({
    logicalName: attr.LogicalName,
    attributeType: attr.AttributeType,
  }));

  console.log('Column types:', columnTypes);
  // Output: [
  //   {
  //     logicalName: "accountid",
  //     attributeType: "Uniqueidentifier",
  //   },
  //   {
  //     logicalName: "name",
  //     attributeType: "String",
  //   },
  //   {
  //     logicalName: "revenue",
  //     attributeType: "Money",
  //   },
  //   {
  //     logicalName: "createdon",
  //     attributeType: "DateTime",
  //   }
  // ]
  
  return columnTypes;
}
```

4. **Discover lookup relationships (many‑to‑one)**
Find which lookup fields point to other tables to dynamically build lookup UI and navigation based on relationships.

```typescript
async function getLookupRelationships() {
  const { data } = await AccountsService.getMetadata({
    metadata: ['LogicalName', 'DisplayName'],
    schema: { 
      manyToOne: true  // Get lookup relationships
    }
  });

  if (!data.ManyToOneRelationships) return [];

  // Get all lookup fields pointing to other tables
  const lookupRelationships = data.ManyToOneRelationships.map(rel => ({
    lookupField: rel.ReferencingAttribute,
    relatedTable: rel.ReferencedEntity,
    relatedTableAttribute: rel.ReferencedAttribute,
    relationshipName: rel.SchemaName,
  }));

  console.log('Lookup relationships:', lookupRelationships);
  // Output: [
  //   {
  //     lookupField: "primarycontactid",
  //     relatedTable: "contact",
  //     relatedTableAttribute: "contactid",
  //     relationshipName: "account_primary_contact",
  //   },
  //   {
  //     lookupField: "ownerid",
  //     relatedTable: "systemuser",
  //     relatedTableAttribute: "systemuserid",
  //     relationshipName: "owner_accounts",
  //   }
  // ]
  
  return lookupRelationships;
```

## Best practices

1. Cache metadata – Metadata calls can be heavy; cache at app start or per session.
2. Request only what you need – Prefer a column list over `"all"` for performance.
3. Defensive access – Check for property existence before accessing nested values (e.g., `DisplayName?.UserLocalizedLabel?.Label`).
4. Use TypeScript types – Rely on generated types from the Dataverse Web API for safer code.

## Options reference (quick view)

- `metadata` — Entity‑level properties (see EntityMetadata).
- `schema.columns` — `"all"` or `["name", "telephone1", ...]`. Response includes Attributes (type `AttributeMetadata`).
- `schema.oneToMany` — Includes `OneToManyRelationships` (type `OneToManyRelationshipMetadata`).
- `schema.manyToOne` — Includes `ManyToOneRelationships` (type `OneToManyRelationshipMetadata`).
- `schema.manyToMany` — Includes `ManyToManyRelationships` (type `ManyToManyRelationshipMetadata`). 

For full schema and property lists, see the [Dataverse Web API documentation](/power-apps/developer/data-platform/webapi/query-metadata-web-api).






