---
title: Property Element | Microsoft Docs
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
ms.assetid: 45f4872d-c1d2-4c5a-8721-251b96ede370
---

# property element

[!INCLUDE [property-description](includes/property-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`name`|Name of the property|`string`|yes|
|`display-name-key`|Used in the customization screens as localized strings that describes the name of the property.|`string`|yes|
|`of-type`|Defines the data type of the property|See [Remarks](#remarks)|no|
|`usage`|The usage attribute identifies if the property is meant to represent an entity attribute that the control can change (bound) or read-only values (input)|`bound`,`input` or `output`|no|
|`required`|Whether the property is required or not|`boolean`|no|
|`of-type-group`|Defines the set of related data types identified by a single name|`string`|no|
|`description-key`|Used in the customization screens as localized strings that describes the description of the property.|`string`|no|

### Remarks

The `of-type` attribute value must be one of the following:

[!INCLUDE [type-table](includes/type-table.md)]

## Parent Elements

|Element|Description|
|--|--|
|[manifest](manifest.md)|[!INCLUDE [manifest-description](includes/manifest-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[manifest](manifest.md)|[!INCLUDE [manifest-description](includes/manifest-description.md)]|0 or more|

## Example

```xml
<property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key" description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
