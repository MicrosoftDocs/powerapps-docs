---
title: Property Set Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 996f10e5-8057-40ea-9680-555e4cd682ff
---

# property-set element

[!INCLUDE [property-set-description](includes/property-set-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`name`|Name of the field|`string`|Yes|
|`display-name-key`|Used in customization screens as localized strings that describe the name of the property|`string`|Yes|
|`description-key`|Used in customization screens as localized strings that describe the description of the property|`string`|Optional|

## Parent Elements

|Element|Description|
|--|--|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[types](types.md)||0 or more|


### Related topics

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)