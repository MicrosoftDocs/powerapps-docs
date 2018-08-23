---
title: Entity relationship metadata | Microsoft Docs
description: Learn about the entity relationship metadata used in Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/12/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Entity relationship metadata

When you look at the solution explorer or the three relationship collections in the `EntityMetadata`, you might think that there are three types of entity relationships. Actually, there are only two, as shown in the following table.

|Relationship Type|Description|
|--|--|
|One-to-Many<br />[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)|An entity relationship where one entity record for the **Primary Entity** can be associated to many other **Related Entity** records because of a lookup field on the related entity.<br />When viewing a primary entity record you can see a list of the related entity records that are associated with it.|
|Many-to-Many<br />[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)|An entity relationship that depends on a special *Relationship Entity*, sometimes called an *Intersect* entity, so that many records of one entity can be related to many records of another entity.<br />When viewing records of either entity in a Many-to-Many relationship you can see a list of any records of the other entity that are related to it.|

The `EntityMetadata` `ManyToOneRelationships` collection contains [OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata) types. One-to-Many relationships exist between entities and refer to each entity as either a *Primary Entity* or *Related Entity*. The related entity, sometimes called the *child entity*, has a lookup attribute that allows storing a reference to a record from the primary entity, sometimes called the *parent entity*. A Many-to-One relationship is just a One-to-Many relationship viewed from the related entity.

> [!NOTE]
> Although related entities are sometimes called *child entities*, don't confuse these with [Child entities](entity-metadata.md#child-entities), which refers to how security is applied to related entities.

More information:
- [Dynamics 365 Customer Engagement Customization Guide: Create and edit relationships between entities](/dynamics365/customer-engagement/customize/create-edit-entity-relationships)
- [Dynamics 365 Customer Engagement Developer Guide: Customize entity relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)

## Cascade configuration

When a one-to-many entity relationship exists, there are cascading behaviors that can be configured to preserve data integrity and automate business processes.

More information:

- [Dynamics 365 Customer Engagement Customization Guide: Create 1:N (one-to-many) or N:1 (many-to-one) relationships > Relationship behavior](/dynamics365/customer-engagement/customize/create-and-edit-1n-relationships#relationship-behavior)
- [Dynamics 365 Customer Engagement Developer Guide: Entity relationship behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior)


## Create a hierarchy of entities

Within a self-referential One-to-Many relationship you can set a hierarchy by setting the `IsHierarchical` property to `true`.

With model-driven apps, this enables an experience that enables you to view and interact with the hierarchy. 

For developers, this enables new types of queries based on the hierarchy using the `Under` and `Not Under` operators.

More information: [Dynamics 365 Customer Engagement Developer Guide : Query and visualize hierarchically related data](/dynamics365/customer-engagement/customize/query-visualize-hierarchical-data)

### See also

[Common Data Service for Apps entities](entities.md)
