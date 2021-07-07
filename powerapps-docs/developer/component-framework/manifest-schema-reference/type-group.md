---
title: Type Group Element | Microsoft Docs
description: The type-group node defines a set of types identified by a single name. This information can be used to identify the data types supported by a specific property.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec7c1ad4-b834-4755-8a04-2c8940f75674
---

# type-group element

[!INCLUDE [type-group-description](includes/type-group-description.md)]

## Available for

Model-driven and canvas apps

## Parameters

|Name|Description|Type|Required|
|--|--|--|--|
|`name`|Name of the data type|`string`|Yes|

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|


## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[type](type.md)|[!INCLUDE [type-description](includes/type-description.md)]|1 or more|


The `type-group` has a limited support for canvas apps. Only the following types are compatible:
   - **Strings**: SingleLine.Text, Multiple, SingleLine.TextArea, SingleLine.Email, SingleLine.Phone, SingleLine.URL, SingleLine.Ticker.
   - **Numbers**: Decimal, FP, Whole.None, Currency.
   - **Dates**: DateAndTime.DateAndTime, DateAndTime.DateOnly.

If the types listed in the `type-group` are mix of compatible and non compatible types, then the first compatible type from `type-group` is considered.

### Example

```XML
<type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
