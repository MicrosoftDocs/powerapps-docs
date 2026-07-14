---
title: Property Element | Microsoft Docs
description: The property node defines a specific, configurable piece of data that the component expects from the Microsoft Dataverse.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# property element

[!INCLUDE [property-description](includes/property-description.md)]

## Available for

Model-driven and canvas apps

## Properties

|Name |Description |Type |Required | Available for|
|------|------|------|-------|------------|
|default-value |The default configuration value provided to the component. In model-driven apps, this property is only allowed on inputs since the bound parameters expect to have a column associated. |string |Optional |Model-driven apps|
|description-key |Used in the customization screens as localized strings that describes the description of the property. |string |Optional |Model-driven and canvas apps|
|display-name-key |Used in the customization screens as localized strings that describes the name of the property. |string |Yes |Model-driven apps|
|name |Name of the property |string |Yes |Model-driven and canvas apps|
|of-type-group |Name of the type-group as defined in manifest| string |Optional |Model-driven apps|
|of-type| Defines the data type of the property| See [Using of-type](#using-of-type)|Optional|Model-driven and canvas apps|
|pfx-default-value |The default PFX expression value provided to the component. |See [Using pfx-default-value](#using-pfx-default-value) |Optional |Canvas apps|
|required |Whether the property is required or not |boolean |Optional |Model-driven apps|
|usage |The usage property identifies if the property is meant to represent a column that the component can change (bound), read-only (input) or output values|bound, input or output |Yes|Model-driven apps|

### Remarks

This section contains guidance about using the Property element attributes.

#### Using of-type

The `of-type` property value must be one of the following:

[!INCLUDE [type-table](includes/type-table.md)]

#### Using pfx-default-value

[!INCLUDE [pfx-default-value-description](includes/pfx-default-value-description.md)]

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|


## Example

```xml
<property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key"
description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
