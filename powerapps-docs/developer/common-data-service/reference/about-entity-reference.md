---
title: "About Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Use this reference to understand the available operations that can be performed for specific entities, the default attributes attributes of each entity and the relationships between entities."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/12/2018
ms.author: jdaly
---
# About the Entity Reference

Use this reference to understand the available operations that can be performed for specific entities, the default attributes of each entity and the relationships between entities.

> [!NOTE]
> This reference includes only entities where:
>
> -  **IsPrivate** equals `false`
>    - This excludes entities where no external use cases exist.
> - **IsIntersect** equals `false`
>    - This excludes entities used to define Many-to-many relationships.
> - The entity supports some kind of direct data modification operation.
>    - This excludes entities which you can't work with directly. 
>
> To see all entity metadata information for your environment, see [Dynamics 365 Developers Guide : Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata).


## Entity Properties

This section includes selected entity properties rather than all of them. Only those properties expected to be most useful for developers are included. Some entity property values can be changed.

## Attributes
Attributes are listed in two separate sections: **Writable attributes** and **Read-only attributes**. The purpose of this separation is to focus on the attributes a developer can set when creating or updating an entity instance. Understanding these attributes helps a developer understand what they can do with the entity beyond simply retrieving the values. 

The attributes in the **Writable attributes** section return true for *either*  the **IsValidForCreate** or **IsValidForUpdate** properties, (usually both). If either of these properties return false, this is indicated.

**Read-only attributes** always return false for the **IsValidForCreate** *and* **IsValidForUpdate** properties.

## Relationships

The [EntityMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) class includes three properties to represent relationships:

|Property| Type  |Description  |
|---------|---------|---------|
|[OneToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.onetomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_OneToManyRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of one-to-many relationships for the entity.|
|[EntityMetadata.ManyToOneRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytoonerelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToOneRelationships)|[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)[]|Gets the array of many-to-one relationships for the entity.|
|[EntityMetadata.ManyToManyRelationships](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.manytomanyrelationships#Microsoft_Xrm_Sdk_Metadata_EntityMetadata_ManyToManyRelationships)|[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)[]|Gets the array of many-to-many relationships for the entity.|

> [!NOTE]
> It is important to keep in mind that while each entity lists those relationships which apply to it, each relationship is shared by both entities. The relationships exist *between* the entities. While One-To-Many relationships exist, *Many-to-One* relationships are simply a view of a One-To-Many relationship from the referencing entity.

### One-to-many relationships
In order to represent that there are no actual *Many-to-One* relationships with a minimum of confusion, the details of each relationship are only documented once. Each one-to-Many relationship is listed with the referenced entity and includes selected relationship details and a link to the corresponding *Many-to-One* relationship. Each *Many-to-One* relationship listed includes only a link to the corresponding One-to-Many relationship.

For each one-to-many relationship the following properties are included:

|Property|Description|
|---------|---------|
|`ReferencingEntity`|The logical name of the related entity.|
|`ReferencingAttribute`|The logical name of the attribute in the related entity that contains a reference to primary key of the primary entity.|
|`IsHierarchical`|Whether the relationship represents a self-referential hierarchical relationship|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|
|`ReferencedEntityNavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information:[Dynamics 365 Customer Engagement Developer Guide Navigation properties](/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#navigation-properties)|
|`AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the related entity data can be accessed in the UI from the primary entity.|
|`CascadeConfiguration`|Data that describes which operations performed on the parent entity will cascade down to related entities.<br />More information: [Cascade configuration](../entity-relationship-metadata.md#cascade-configuration)|


### Many-to-many relationships
Each many-to-many relationship includes [Entity1LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity1logicalname) and [Entity2LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata.entity2logicalname). For this documentation relationship details are only included in the topic for *Entity1*. Each Many-to-Many relationship where the entity is *Entity2* includes only a link to the details found in the topic for *Entity1*.

For each many-to-many relationship the following properties are included:

|Property|Description|
|---------|---------|
|`IntersectEntityName`|The logical name of the intersect entity that supports this many-to-many relationship|
|`Entity1LogicalName`|The logical name for the first entity in the relationship.|
|`Entity1IntersectAttribute`|The logical name of the intersect entity attribute that includes a reference to the primary key of the first entity.|
|`Entity1NavigationPropertyName`|The name of the Web API collection-valued navigation property for this relationship.<br />More information: [Dynamics 365 Customer Engagement Developer Guide Navigation properties](/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#navigation-properties)|
|`Entity1AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the first entity data can be accessed in the UI from the second entity.|
|`Entity2LogicalName`|The logical name for the second entity in the relationship.|
|`Entity2IntersectAttribute`|The logical name of the intersect entity attribute that includes a reference to the primary key of the second entity.|
|`Entity2NavigationPropertyName`|This is typically the same as the `Entity1NavigationPropertyName`|
|`Entity2AssociatedMenuConfiguration`|Data used by model-driven apps to control whether and how the second entity data can be accessed in the UI from the first entity.|
|`IsCustomizable`|Whether the properties of the relationship can be changed.|

