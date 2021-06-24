---
title: getEntityMetadata | Microsoft Docs
description: Returns the table definitions for the specified table.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6a334af7-ca5b-449c-b90f-0901824654d2
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