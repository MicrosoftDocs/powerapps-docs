---
title: Property Set Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 996f10e5-8057-40ea-9680-555e4cd682ff
---

# property-set element

[!INCLUDE [property-set-description](includes/property-set-description.md)]

## Available for

Model-driven apps

## Attributes

|Name |Description |Type |Required |
|----- |------ |------ |---------- |
|name | Name of the field. |string |Yes |
|display-name-key  | Used in customization screens as localized strings that describe the name of the property. |string |Yes |
|description-key |Used in customization screens as localized strings that describe the description of the property. |string |Optional |
|of-type |Defines the data type of the property |See [Remarks](#remarks) |Optional |
|required|Indicates whether the property is required or not.|boolean |Optional |
|of-type-group |Name of the type-group as defined in manifest. |string|Optional |
|usage |The usage attribute identifies if the property is meant to represent an entity attribute that the component can change (bound) or read-only values (input). |bound or input |Yes |

## Parent Elements

|Element|Description|
|--|--|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[types](types.md)||0 or more|

### Remarks

The `of-type` attribute value must be one of the following:

[!INCLUDE [type-table](includes/type-table.md)]

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]