---
title: "Dataverse table/entity reference | Microsoft Docs"
description: "Use this reference to understand the available operations that can be performed for specific tables, the default columns/attributes of each table/entity and the relationships between tables in Microsoft Dataverse"
author: phecke
ms.topic: reference
ms.date: 08/11/2025
ms.author: pehecke
ms.reviewer: jdaly
search.audienceType: 
  - developer
---
# Dataverse table/entity reference

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use this reference to understand the available operations that can be performed for specific tables, the default columns of each table and the relationships between tables.

This reference includes only those tables where:

- **IsPrivate** equals `false`
  - This excludes tables where no external use cases exist.

- **IsIntersect** equals `false` or **IsIntersect** equals `true` and the table contains more than 4 columns.
  - Most intersect tables contain just the 4 columns necessary to support the Many-to-Many relationship. They are not useful. Intersect tables with more than four columns are more interesting.

To view information about all tables in your environment, see [Browse tables definitions in your environment](../browse-your-metadata.md).

## Dynamics 365 products table reference

Dynamics 365 products use Dataverse. When you create an environment for Dynamics 365 products, the environment has a common set of tables for all Dynamics 365 products. These tables are included in the [Dynamics 365 Enabled apps table/entity reference](/dynamics365/developer/reference/about-entity-reference).

Each of the specific Dynamics 365 products may add additional tables. The following table shows the table reference for specific Dynamics 365 products:

|Product Documentation |Product Table reference|
|---------|---------|
|[Sales](/dynamics365/sales/)|[Sales table/entity reference](/dynamics365/sales/developer/about-entity-reference)|
|[Field Service](/dynamics365/field-service/)|[Field Service table/entity reference](/dynamics365/field-service/developer/reference/about-entity-reference)|
|[Customer Service](/dynamics365/customer-service/)|[Customer Service table/entity reference](/dynamics365/customer-service/develop/reference/about-entity-reference)| 


## Properties

This section includes selected entity properties rather than all of them. Only those properties expected to be most useful for developers are included. Some entity property values can be changed.

## Columns

Columns are listed in two separate sections: **Writable columns/attributes** and **Read-only columns/attributes**. The purpose of this separation is to focus on the columns a developer can set when creating or updating rows in a table. Understanding these columns helps a developer understand what they can do with the table beyond just retrieving the values.

The columns in the **Writable columns/attributes** section return true for *either*  the **IsValidForCreate** or **IsValidForUpdate** properties, (usually both). If either of these properties return false, this is indicated.

**Read-only columns/attributes** always return false for the **IsValidForCreate** *and* **IsValidForUpdate** properties.

Choice column options in this reference documentation come from a deployment where English is the base language. Some choice options can vary depending on the base language selected when the environment is created. These differences more closely align to options that best suite the language or culture. You are free to customize these options by changing the labels or adding and removing options as needed.

## Relationships

The [EntityMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) class includes three properties to represent relationships:

|Property| Type  |Description  |
|---------|---------|---------|
|[OneToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.onetomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_OneToManyRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of one-to-many relationships for the entity.|
|[ManyToOneRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytoonerelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToOneRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of many-to-one relationships for the entity.|
|[ManyToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToManyRelationships)|[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)[]|Gets the array of many-to-many relationships for the entity.|

> [!NOTE]
> It is important to keep in mind that while each table lists those relationships that apply to it, each relationship is shared by both tables. The relationships exist *between* the tables. While One-To-Many relationships exist, *Many-to-One* relationships are simply a view of a One-To-Many relationship from the referencing table.

### Many-to-One relationships

Includes these `OneToManyRelationship` properties:

|Property|Description|
|---------|---------|
|`ReferencedEntity`|The logical name of the related table.|
|`ReferencedAttribute`|The logical name of primary key of the related table.|
|`ReferencingEntity`|The logical name of the related table that has the lookup column.|
|`ReferencingAttribute`|The logical name of the lookup column in the related table that contains a reference to primary key of the primary table.|
|`IsHierarchical`|Whether the relationship represents a self-referential hierarchical relationship|
|`CascadeConfiguration`|Data that describes which operations performed on the parent entity will cascade down to related entities.<br />More information: [Cascade configuration](../entity-relationship-metadata.md#cascade-configuration)|



### One-to-many relationships

Includes these `OneToManyRelationship` properties:

|Property|Description|
|---------|---------|
|`ReferencingEntity`|The logical name of the related table.|
|`ReferencingAttribute`|The logical name of the column in the related table that contains a reference to primary key of the primary table.|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|
|`ReferencedEntityNavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information: [Web API Navigation Properties](../webapi/web-api-navigation-properties.md)|
|`AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the related entity data can be accessed in the UI from the primary entity.|


### Many-to-many relationships

Each many-to-many relationship includes [Entity1LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity1logicalname) and [Entity2LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity2logicalname). For this documentation, relationship details are provided in the context of the current table. Whether it is `Entity1` or `Entity2` isn't really important.

For each many-to-many relationship the following properties are included:

|Property|Description|
|---------|---------|
|`IntersectEntityName`|The logical name of the intersect table that supports this many-to-many relationship|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|
|`SchemaName`|The schema name of the relationship.|
|`IntersectAttribute`|The name of the column in the intersect table that is the primary key for records of this type.|
|`NavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information: [Web API Navigation Properties](../webapi/web-api-navigation-properties.md)|
|`AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table.|


In the rare case where a many-to-many relationship is self-referencing, such as for [Connection Role (ConnectionRole) connectionroleassociation_association](entities/connectionrole.md#BKMK_connectionroleassociation_association), `Entity1` or `Entity2` is prepended to the property.

|Property|Value|
|---|---|
|`Entity1IntersectAttribute`|The name of the column in the intersect table that is the primary key for records of this type as the first table.|
|`Entity2IntersectAttribute`|The name of the column in the intersect table that is the primary key for records of this type as the second table.|
|`Entity1NavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship as the first table.|
|`Entity2NavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship as the second table.|
|`Entity1AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table as the first table.|
|`Entity2AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table as the second table|

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
