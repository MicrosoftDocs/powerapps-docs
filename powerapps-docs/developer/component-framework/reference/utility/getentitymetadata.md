---
title: getEntityMetadata | Microsoft Docs
description: Returns the table definitions for the specified table.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# getEntityMetadata

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


### Related topics

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]