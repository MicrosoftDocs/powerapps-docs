---
title: Property Element | Microsoft Docs
description: The property node defines a specific, configurable piece of data that the component expects from the Microsoft Dataverse.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 45f4872d-c1d2-4c5a-8721-251b96ede370
---

# property element

[!INCLUDE [property-description](includes/property-description.md)]

## Available for

Model-driven apps and canvas apps (public preview)

## Properties

|Name |Description |Type |Required |
|------|------|------|-------|
|name |Name of the property |string |Yes |
|display-name-key |Used in the customization screens as localized strings that describes the name of the property. |string |Yes |
|of-type| Defines the data type of the property| See [Remarks](#remarks)|Optional|
|usage |The usage property identifies if the property is meant to represent a column that the component can change (bound) or read-only values (input)|bound or input |Yes |
|required |Whether the property is required or not |boolean |Optional |
|of-type-group |Name of the type-group as defined in manifest| string |Optional |
|description-key |Used in the customization screens as localized strings that describes the description of the property. |string |Optional |
|default-value |The default configuration value provided to the component. In model-driven apps, this property is only allowed on inputs since the bound parameters expect to have a column associated. |string |Optional |

### Remarks

The `of-type` property value must be one of the following:

[!INCLUDE [type-table](includes/type-table.md)]

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|


## Example

```xml
<property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key"
description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]