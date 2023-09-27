---
title: EntityMetadata (Power Apps component framework API reference)| Microsoft Docs
description: Information about methods and properties for table definitions.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# EntityMetadata

Returns the table definitions for the specified table.

## Available for

Model-driven apps

## Properties

|Name| Type| Description|
|-------|--------|--------|
|attributeNames|string[]|List of column names of the table.|
|description|string|Entity description.|
|displayName|string| Display name of the table.|
|entityPluralName|string|The plural name of the table.|
|logicalName|string| The logical name of the table.|
|metadata|Dictionary<[AttributeMetadata](attributemetadata.md)>|Colum definitions for specific columns indexed by column name.|
|primaryImageAttribute|string|Table's primary image column name.|
|primaryIdAttribute|string|Table's primary id column name.|
|primaryNameAttribute|string|Table's primary column name.|
|privilegesByType|Dictionary<[securityPrivilegeMetadata](securityprivilegesmetadata.md)>|The privileges for the table indexed by type.|
||||

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
