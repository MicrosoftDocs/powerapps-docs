---
title: "Dataverse table/entity reference | Microsoft Docs"
description: "Use this reference to understand the available operations that can be performed for specific tables, the default columns/attributes of each table/entity and the relationships between tables in Microsoft Dataverse"
author: JimDaly
ms.topic: reference
ms.date: 10/26/2026
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---
# Dataverse table/entity reference

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use this reference to understand the available operations for specific tables, the default columns of each table, and the relationships between tables. Table definitions use the [EntityMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata).

This reference includes only those tables where:

- **[`EntityMetadata.IsPrivate`](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsPrivate)** equals `false`

   This condition excludes tables with no external use cases.

- **[`EntityMetadata.IsIntersect`](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsIntersect)** equals `false` or **IsIntersect** equals `true` and the table contains more than four columns.

   Most intersect tables contain just the four columns necessary to support the many-to-many relationship. They're not useful. Intersect tables with more than four columns are not common and more interesting.

To view information about all tables in your environment, see [Browse tables definitions in your environment](../browse-your-metadata.md).

## Dynamics 365 products table reference

Dynamics 365 products use Dataverse. When you create an environment for Dynamics 365 products, the environment has a common set of tables for all Dynamics 365 products. See the [Dynamics 365 Enabled apps table/entity reference](/dynamics365/developer/reference/about-entity-reference).

Each specific Dynamics 365 product can add more tables. The following table shows the table reference for specific Dynamics 365 products:

|Product Documentation |Product Table reference|
|---------|---------|
|[Sales](/dynamics365/sales/)|[Sales table/entity reference](/dynamics365/sales/developer/about-entity-reference)|
|[Field Service](/dynamics365/field-service/)|[Field Service table/entity reference](/dynamics365/field-service/developer/reference/about-entity-reference)|
|[Customer Service](/dynamics365/customer-service/)|[Customer Service table/entity reference](/dynamics365/customer-service/develop/reference/about-entity-reference)|


## Properties

This section includes selected entity properties rather than all of them. It includes only those properties that are most useful for developers. You can change some entity property values.

## Columns

Columns are listed in two separate sections:

| Section | Description |
| --- | --- |
| **Writable columns/attributes** | Columns you can set when creating or updating rows in a table. These columns return `true` for either the **[`AttributeMetadata.IsValidForCreate`](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForCreate)** or **[`AttributeMetadata.IsValidForUpdate`](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForUpdate)** properties, usually both. If either property returns `false`, this condition is indicated. |
| **Read-only columns/attributes** | Columns you can retrieve but can't set when creating or updating rows in a table. These columns always return `false` for both the **[`AttributeMetadata.IsValidForCreate`](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForCreate)** and **[`AttributeMetadata.IsValidForUpdate`](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForUpdate)** properties. |


### Choice column options

Choice column options in this reference documentation come from a deployment where English is the base language. Some choice options can vary depending on the base language selected when the environment is created. These differences more closely align to options that best suit the language or culture. You can customize these options by changing the labels or adding and removing options as needed.

## Relationships

The [EntityMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata) includes three properties to represent relationships:

| Property | Type | Description |
|---------|---------|---------|
|[OneToManyRelationships](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OneToManyRelationships)|[OneToManyRelationshipMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata)[]|Gets the array of one-to-many relationships for the entity.|
|[ManyToOneRelationships](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToOneRelationships)|[OneToManyRelationshipMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata)[]|Gets the array of many-to-one relationships for the entity.|
|[ManyToManyRelationships](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToManyRelationships)|[ManyToManyRelationshipMetadata](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata)[]|Gets the array of many-to-many relationships for the entity.|

> [!NOTE]
> While each table lists the relationships that apply to it, each relationship is shared by both tables. The relationships exist *between* the tables. While one-to-many relationships exist, *many-to-one* relationships are simply a view of a one-to-many relationship from the referencing table.

### Many-to-one relationships

Includes these [`OneToManyRelationshipMetadata` class](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata) properties:

| Property | Description |
|---------|---------|
|[`ReferencedEntity`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencedEntity)|The logical name of the related table.|
|[`ReferencedAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencedAttribute)|The logical name of primary key of the related table.|
|[`ReferencingEntity`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingEntity)|The logical name of the related table that has the lookup column.|
|[`ReferencingAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingAttribute)|The logical name of the lookup column in the related table that contains a reference to primary key of the primary table.|
|[`IsHierarchical`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.IsHierarchical)|Whether the relationship represents a self-referential hierarchical relationship|
|[`CascadeConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.CascadeConfiguration)|Data that describes which operations performed on the parent entity cascade down to related entities.<br />For more information, see [Cascade configuration](../entity-relationship-metadata.md#cascade-configuration).|



### One-to-many relationships

Includes these [`OneToManyRelationshipMetadata` class](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata) properties:

| Property | Description |
|---------|---------|
|[`ReferencingEntity`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingEntity)|The logical name of the related table.|
|[`ReferencingAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingAttribute)|The logical name of the column in the related table that contains a reference to primary key of the primary table.|
|[`IsCustomizable`](xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.IsCustomizable)|Whether you can change the properties of the relationship.|
|[`ReferencedEntityNavigationPropertyName`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencedEntityNavigationPropertyName)|The name of the Web API collection-valued navigation property for this relationship.<br />For more information, see [Web API Navigation Properties](../webapi/web-api-navigation-properties.md).|
|[`AssociatedMenuConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.AssociatedMenuConfiguration)|Data used by model-driven apps to control whether and how the related entity data can be accessed in the UI from the primary entity.|


### Many-to-many relationships

Each many-to-many relationship includes [Entity1LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1LogicalName) and [Entity2LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2LogicalName). For this documentation, relationship details are provided in the context of the current table. Whether it is `Entity1` or `Entity2` isn't really important.

For each many-to-many relationship, the following [`ManyToManyRelationshipMetadata` class](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata) properties are included:

| Property | Description |
|---------|---------|
|[`IntersectEntityName`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.IntersectEntityName)|The logical name of the intersect table that supports this many-to-many relationship.|
|[`IsCustomizable`](xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.IsCustomizable)|Whether you can change the properties of the relationship.|
|[`SchemaName`](xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName)|The schema name of the relationship.|
|`IntersectAttribute` ([`Entity1IntersectAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1IntersectAttribute) or [`Entity2IntersectAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2IntersectAttribute))|The name of the column in the intersect table that is the primary key for records of this type.|
|`NavigationPropertyName` ([`Entity1NavigationPropertyName`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1NavigationPropertyName) or [`Entity2NavigationPropertyName`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2NavigationPropertyName))|The name of the Web API collection-valued navigation property for this relationship.<br />More information: [Web API Navigation Properties](../webapi/web-api-navigation-properties.md)|
|`AssociatedMenuConfiguration` ([`Entity1AssociatedMenuConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1AssociatedMenuConfiguration) or [`Entity2AssociatedMenuConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2AssociatedMenuConfiguration))|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table.|


In the rare case where a many-to-many relationship is self-referencing, such as for [Connection Role (ConnectionRole) connectionroleassociation_association](entities/connectionrole.md#BKMK_connectionroleassociation_association), `Entity1` or `Entity2` is prepended to the property.

|Property|Value|
|---|---|
|[`Entity1IntersectAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1IntersectAttribute)|The name of the column in the intersect table that is the primary key for records of this type as the first table.|
|[`Entity2IntersectAttribute`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2IntersectAttribute)|The name of the column in the intersect table that is the primary key for records of this type as the second table.|
|[`Entity1NavigationPropertyName`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1NavigationPropertyName)|The name of the Web API collection-valued navigation property for this relationship as the first table.|
|[`Entity2NavigationPropertyName`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2NavigationPropertyName)|The name of the Web API collection-valued navigation property for this relationship as the second table.|
|[`Entity1AssociatedMenuConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1AssociatedMenuConfiguration)|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table as the first table.|
|[`Entity2AssociatedMenuConfiguration`](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2AssociatedMenuConfiguration)|Data used by model-driven apps to control whether and how the second table data can be accessed in the UI from this table as the second table.|

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
