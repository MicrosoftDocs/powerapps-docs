---
title: Event Element | Microsoft Docs
description: Defines a Power FX expression that can be configured within Power Apps Studio, then triggered within the component code.
author: anuitz
ms.author: anuitz
ms.reviewer: jdaly
ms.date: 03/24/2025
ms.topic: reference
ms.subservice: pcf
contributors:
 - OliverDumrique
---

# event element

[!INCLUDE [event-description](includes/event-description.md)]

## Available for

Canvas and model-driven apps

## Properties

|Name |Description |Type |Required | Available for|
|------|------|------|-------|------------|
|`name` |Name of the event |`string` |Yes |Canvas and model-driven apps|
|`display-name-key` |Used in the customization screens as localized strings that describe the name of the event. |`string` |Yes |Canvas apps|
|`description-key` |Used in the customization screens as localized strings that describe the description of the event. |`string` |Optional |Canvas apps|
|`pfx-default-value` |The default Power Fx expression value provided to the component. |See [Remarks](#remarks) |Optional |Canvas apps|

### Remarks

[!INCLUDE [pfx-default-value-description](includes/pfx-default-value-description.md)]

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Example

```xml
<event name="OnSelectCustomButton"
   pfx-default-value='SubmitForm(%MyFormName.ID%); Back(%ScreenTransition.RESERVED%.Cover)'
   display-name-key="OnSelectCustomButton_Display_Key"
   description-key="OnSelectCustomButton_Desc_Key" />
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
