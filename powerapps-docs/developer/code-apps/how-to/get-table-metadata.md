---
title: "How to: Get metadata for Dataverse tables"
description: "Use the getMetadata function to retrieve metadata about Dataverse tables (entities) at runtime."
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 12/5/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# How to: Get metadata for Dataverse tables

The table metadata contains customizations applied to tables in Dataverse. Metadata also contains localized labels when your organization supports multiple languages. Using metadata in your code app means your app can adapt to customization or localization changes without having to change your code.

Use the `getMetadata` function to retrieve Dataverse table (entity) metadata at runtime. This function lightly wraps the capabilities described in [Query table definitions using the Web API](../../data-platform/webapi/query-metadata-web-api.md) and provides strongly typed access to entity definitions, attributes, and relationships.

## getMetadata signature

The `getMetadata` function requires an instance of [`GetEntityMetadataOptions`](#getentitymetadataoptions-parameter) to define the data to return.

```typescript
AccountsService.getMetadata(
  options?: GetEntityMetadataOptions<Account>
): Promise<IOperationResult<Partial<EntityMetadata>>>
```

> [!NOTE]
> You must follow the steps in [Set up your code app](connect-to-dataverse.md#set-up-your-code-app) in [Connect to Dataverse](connect-to-dataverse.md) to initialize the Power SDK and import the service file before calling `getMetadata`.


## GetEntityMetadataOptions parameter

Set the [getMetadata](#getmetadata-signature) `options` parameter to select the metadata you want to retrieve:

```typescript
interface GetEntityMetadataOptions {
  metadata?: Array<String>;
  schema?: {
    columns?: "all" | Array<String>;
    oneToMany?: boolean;
    manyToOne?: boolean;
    manyToMany?: boolean;
  };
}
```

- `metadata`: Array of entity-level properties to fetch such as `["Privileges","DisplayName","IsCustomizable"]`. See [EntityMetadata properties](xref:Microsoft.Dynamics.CRM.EntityMetadata) for a full list of queryable table properties.
- `schema`:

    - `columns`:  Retrieve column (attribute) metadata - `"all"` or an array of column logical names such as `["name","telephone1","createdon"]`. See [AttributeMetadata properties](xref:Microsoft.Dynamics.CRM.AttributeMetadata ) for a full list of queryable attribute properties.

      > [!NOTE]
      > You can't specify properties that aren't included in `AttributeMetadata`. Properties defined by [derived types](/power-apps/developer/data-platform/webapi/reference/attributemetadata#derived-types) aren't available. This means you can't access properties such as choice (picklist) column options because they're defined by a derived type.

    - `oneToMany`, `manyToOne`, `manyToMany`: Set boolean values to include relationship metadata

      
The response includes arrays named `Attributes` of type [AttributeMetadata](xref:Microsoft.Dynamics.CRM.AttributeMetadata), `OneToManyRelationships` of type [OneToManyRelationshipMetadata](xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata), `ManyToOneRelationships` of type [OneToManyRelationshipMetadata](xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata), and `ManyToManyRelationships` of type [ManyToManyRelationshipMetadata](xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata) when requested.

## Examples

The following examples show common ways to retrieve and use table metadata.


### Get user-localized labels for all columns

Retrieve display names in the user's language. Use these labels to drive form labels, table headers, and accessibility text.

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

### Identify required fields for form validation

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

### Map column types for client-side validation

Get attribute types to inform validation and UI controls. Choose the right UI control (for example: date picker, money, choice) and validate values consistently.

```typescript
async function getColumnTypes() {
  const { data } = await AccountsService.getMetadata({
    schema: { columns: 'all' }
  });

  if (!data.Attributes) return [];

  // Map attributes to their types for validation
  const columnTypes = data.Attributes.map(attr => ({
    logicalName: attr.LogicalName,
    attributeType: attr.AttributeTypeName?.Value,
  }));

  console.log('Column types:', columnTypes);
  // Output: [
  //   {
  //     logicalName: "accountid",
  //     attributeType: "UniqueidentifierType",
  //   },
  //   {
  //     logicalName: "name",
  //     attributeType: "StringType",
  //   },
  //   {
  //     logicalName: "revenue",
  //     attributeType: "MoneyType",
  //   },
  //   {
  //     logicalName: "createdon",
  //     attributeType: "DateTimeType",
  //   }
  // ]
  
  return columnTypes;
}
```

### Discover lookup relationships (many‑to‑one)

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

- **Cache metadata** : Metadata calls can be heavy. Cache at app start or per session.
- **Request only what you need**  :  Prefer a column list over `"all"` for performance.
- **Defensive access**  :  Check for property existence before accessing nested values (For example: `DisplayName?.UserLocalizedLabel?.Label`).
- **Use TypeScript types**  :  Rely on generated types from the Dataverse Web API for safer code.
