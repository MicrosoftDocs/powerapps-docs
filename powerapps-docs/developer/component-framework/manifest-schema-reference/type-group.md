---
title: Type Group Element | Microsoft Docs
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
ms.assetid: ec7c1ad4-b834-4755-8a04-2c8940f75674
---

# type-group element

[!INCLUDE [type-group-description](includes/type-group-description.md)]

## Available for

Model-driven apps and canvas apps (public preview)

## Attributes

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


Type-group has a limited support for canvas apps in this experimental preview . The following issues occur when you try to import components:

1. If all types listed in the type group are of compatible javascript types, the developer attempt to choose the most generic option listed. The types that are considered compatible are :
   - Strings: SingleLine.Text, Multiple, SingleLine.TextArea, SingleLine.Email, SingleLine.Phone, SingleLine.URL, SingleLine.Ticker.
   - Numbers: Decimal, Floating Point, Whole.None, Currency.
   - Dates: DateAndTime.DateAndTime, DateAndTime.DateOnly.

2. If the types listed in the group are not considered compatible, then the parameter will be treated as the first type listed in the type-group.

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