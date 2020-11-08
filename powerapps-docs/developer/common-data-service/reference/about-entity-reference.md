---
title: "About table reference (Common Data Service)| Microsoft Docs"
description: "Use this reference to understand the available operations that can be performed for specific tables, the default columns of each table, and the relationships between tables."
author: KumarVivek
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.date: 11/08/2020
ms.author: kvivek
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# About table reference

> [!NOTE]
> Effective Nov 2020, some terminology in Common Data Service has been updated. For example, *entity* is now *table* and *attribute* is now *column*. [Learn more](https://go.microsoft.com/fwlink/?linkid=2147247)

Use this reference to understand the available operations that can be performed for specific tables, the default columns of each table, and the relationships between tables.

> [!IMPORTANT]
> This reference includes only tables where:
>
> -  **IsPrivate** equals `false`
>    - This excludes tables where no external use cases exist.
> - **IsIntersect** equals `false`
>    - This excludes tables used to define Many-to-many relationships.
> - The table supports some kind of direct data modification operation.
>    - This excludes tables that you can't work with directly. 
>
> To see all table metadata information for your environment, see [Browse the metadata for your organization](/powerapps/developer/common-data-service/browse-your-metadata).


## Table Properties

This section includes selected table properties rather than all of them. Only those properties expected to be most useful for developers are included. Some table property values can be changed.

## Columns
Columns are listed in two separate sections: **Writable Columns** and **Read-only Columns**. 

The purpose of this separation is to focus on the columns a developer can set when creating or updating a table instance. Understanding these columns helps a developer understand what they can do with the table beyond simply retrieving the values. 

- The columns in the **Writable Columns** section return true for *either*  the **IsValidForCreate** or **IsValidForUpdate** properties, (usually both). If either of these properties return false, this is indicated.

- **Read-only Columns** always return false for the **IsValidForCreate** *and* **IsValidForUpdate** properties.

## Relationships

The [EntityMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) class includes three properties to represent relationships:

|Property| Type  |Description  |
|---------|---------|---------|
|[OneToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.onetomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_OneToManyRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of one-to-many relationships for the table.|
|[EntityMetadata.ManyToOneRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytoonerelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToOneRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of many-to-one relationships for the table.|
|[EntityMetadata.ManyToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToManyRelationships)|[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)[]|Gets the array of many-to-many relationships for the table.|

> [!NOTE]
> It is important to keep in mind that while each table lists those relationships which apply to it, each relationship is shared by both tables. The relationships exist *between* the tables. While One-To-Many relationships exist, *Many-to-One* relationships are simply a view of a One-To-Many relationship from the referencing table.

### One-to-many relationships
In order to represent that there are no actual *Many-to-One* relationships with a minimum of confusion, the details of each relationship are only documented once. Each One-to-Many relationship is listed with the referenced table and includes selected relationship details and a link to the corresponding *Many-to-One* relationship. Each *Many-to-One* relationship listed includes only a link to the corresponding One-to-Many relationship.

For each one-to-many relationship the following properties are included:

|Property|Description|
|---------|---------|
|`ReferencingEntity`|The logical name of the related table.|
|`ReferencingAttribute`|The logical name of the column in the related table that contains a reference to primary key of the primary table.|
|`IsHierarchical`|Whether the relationship represents a self-referential hierarchical relationship|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|
|`ReferencedEntityNavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information:[Common Data Service Developer Guide Navigation properties](/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#navigation-properties)|
|`AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the related table data can be accessed in the UI from the primary table.|
|`CascadeConfiguration`|Data that describes which operations performed on the parent table will cascade down to related tables.<br />More information: [Cascade configuration](../entity-relationship-metadata.md#cascade-configuration)|


### Many-to-many relationships
Each many-to-many relationship includes [Entity1LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity1logicalname) and [Entity2LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity2logicalname). For this documentation relationship details are only included in the topic for *Entity1*. Each Many-to-Many relationship where the table is *Entity2* includes only a link to the details found in the topic for *Entity1*.

For each many-to-many relationship the following properties are included:

|Property|Description|
|---------|---------|
|`IntersectEntityName`|The logical name of the intersect table that supports this many-to-many relationship|
|`Entity1LogicalName`|The logical name for the first table in the relationship.|
|`Entity1IntersectAttribute`|The logical name of the intersect table column that includes a reference to the primary key of the first table.|
|`Entity1NavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information: [Navigation properties](/powerapps/developer/common-data-service/webapi/web-api-types-operations#navigation-properties)|
|`Entity1AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the first table data can be accessed in the UI from the second table.|
|`Entity2LogicalName`|The logical name for the second table in the relationship.|
|`Entity2IntersectAttribute`|The logical name of the intersect table column that includes a reference to the primary key of the second table.|
|`Entity2NavigationPropertyName`|This is typically the same as the `Entity1NavigationPropertyName`|
|`Entity2AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from the first table.|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|

## Helpful resources
