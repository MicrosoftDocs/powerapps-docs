---
title: EntityMetadata | Microsoft Docs
description: Information about methods and properties for entity metadata.
keywords:
ms.author: nabuthuk
manager: kvivek
author: nkrb
ms.date: 10/01/2020
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad8659f7-f566-43db-bed1-c8484c114a59
---

# EntityMetadata

Returns the entity metadata for the specified entity.

## Available for

Model-driven apps

## Properties

|Name| Type| Description|
|-------|--------|--------|
|attributeNames|string[]|List of attribute names of the entity.|
|description|string|Entity description.|
|displayName|string| Display name of the entity.|
|entityPluralName|string|The plural name of the entity.|
|logicalName|string| The logical name of the entity.|
|metadata|Dictionary<[AttributeMetadata](attributemetadata.md)>|Attribute metadata for specific attributes indexed by attribute name.|
|primaryImageAttribute|string|Entity's primary image attribute name.|
|primaryIdAttribute|string|Entity's primary id attribute name.|
|primaryNameAttribute|string|Entity's primary field name.|
|privilegesByType|Dictionary<[securityPrivilegeMetadata](securityprivilegesmetadata.md)>|The privileges for the entity indexed by type.|
||||

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]