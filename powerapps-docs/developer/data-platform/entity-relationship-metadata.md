---
title: Table relationship definitions | Microsoft Docs
description: Learn about the relationship definitions used in Microsoft Dataverse.
services: ''
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/11/2021
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Table relationship definitions

When you look at the solution explorer or the three relationship collections in the `EntityMetadata`, you might think that there are three types of relationships. Actually, there are only two, as shown in the following table.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

|Relationship Type|Description|
|--|--|
|One-to-Many<br />[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)|A relationship where one record for the **Primary Table** can be associated to many other **Related Table** records because of a lookup column on the related table.<br />When viewing a primary table record you can see a list of the related table records that are associated with it.|
|Many-to-Many<br />[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)|A relationship that depends on a special *Relationship Table*, sometimes called an *Intersect* table, so that many records of one table can be related to many records of another table.<br />When viewing records of either table in a Many-to-Many relationship you can see a list of any records of the other table that are related to it.|

The `EntityMetadata` `ManyToOneRelationships` collection contains [OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata) types. One-to-Many relationships exist between tables and refer to each table as either a *Primary Table* or *Related Table*. The related table, sometimes called the *child table*, has a lookup column that allows storing a reference to a record from the primary table, sometimes called the *parent table*. A Many-to-One relationship is just a One-to-Many relationship viewed from the related table.

> [!NOTE]
> Although related tables are sometimes called *child tables*, don't confuse these with [Child tables](entity-metadata.md#child-tables), which refers to how security is applied to related tables.

More information: [Create relationships between tables](../../maker/data-platform/data-platform-entity-lookup.md).

## Cascade configuration

When a one-to-many relationship exists, there are cascading behaviors that can be configured to preserve data integrity and automate business processes. More information: [Configure relationship cascading behavior](configure-entity-relationship-cascading-behavior.md).

## Create a hierarchy of tables

Within a self-referential One-to-Many relationship you can set a hierarchy by setting the `IsHierarchical` property to `true`.

With model-driven apps, this enables an experience that enables you to view and interact with the hierarchy. 

For developers, this enables new types of queries based on the hierarchy using the `Under` and `Not Under` operators.

More information: [Microsoft Dataverse Developer Guide : Query and visualize hierarchically related data](/dynamics365/customer-engagement/customize/query-visualize-hierarchical-data).

### See also

[Dataverse tables](entities.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]