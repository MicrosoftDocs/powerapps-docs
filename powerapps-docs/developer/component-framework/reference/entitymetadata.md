---
title: EntityMetadata | Microsoft Docs
description: Information about methods and properties for table metadata.
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

Returns the table metadata for the specified table.

## Available for

Model-driven apps

## Properties

|Name| Type| Description|
|-------|--------|--------|
|attributeNames|string[]|List of column names of the table.|
|description|string|Table description.|
|displayName|string| Display name of the table.|
|entityPluralName|string|The plural name of the table.|
|logicalName|string| The logical name of the table.|
|metadata|Dictionary<[AttributeMetadata](attributemetadata.md)>|Column metadata for specific columns indexed by column name.|
|primaryImageAttribute|string|Table's primary image column name.|
|primaryIdAttribute|string|Table's primary id column name.|
|primaryNameAttribute|string|Table's primary column name.|
|privilegesByType|Dictionary<[securityPrivilegeMetadata](securityprivilegesmetadata.md)>|The privileges for the table indexed by type.|
||||

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)
