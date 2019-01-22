---
title: Property Set Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
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
|`name`|Name of the field|`string`|yes|
|`display-name-key`|Used in customization screens as localized strings that describe the name of the property|`string`|yes|
|`description-key`|Used in customization screens as localized strings that describe the description of the property|`string`|no|

## Parent Elements

|Element|Description|
|--|--|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[types](types.md)|[!INCLUDE [types-description](includes/types-description.md)]|0 or more|

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
