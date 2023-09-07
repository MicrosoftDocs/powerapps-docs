---
title: getEntityMetadata (Power Apps component framework API reference) | Microsoft Docs
description: Returns the table definitions for the specified table.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getEntityMetadata (Component Framework)

[!INCLUDE [getentitymetadata-description](includes/getentitymetadata-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.utils.getEntityMetadata(entityName, attributes)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|entityName|`String`|Yes|The logical name of the table.|
|attributes|`String[]`|No|The columns to get metadata for.|

## Return Value

Type: Promise<[EntityMetadata](../entitymetadata.md)>


### Related articles

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
