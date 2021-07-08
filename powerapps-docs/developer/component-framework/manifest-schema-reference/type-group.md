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

The `type-group` node has a limited support for canvas apps. When the type groups can easily resolve to a common type, the "most compatible" type (generally the least specific type) will be chosen for the type of the given field. The resolvable type groupings are as follows:

   - **Strings**: SingleLine.Text, Multiple, SingleLine.TextArea, SingleLine.Email, SingleLine.Phone, SingleLine.URL, SingleLine.Ticker.
   - **Numbers**: Decimal, FP, Whole.None, Currency.
   - **Dates**: DateAndTime.DateAndTime, DateAndTime.DateOnly.

For example, the following type group:

```XML
<type-group name="numeric">
       <type>FP</type>
       <type>Decimal</type>
       <type>Whole.None</type>
</type-group>
```

would result in the control receiving the value **Decimal** as the type for the given parameter's Type.

When a `type-group` includes a value not included in any of the above groupings, or includes values from more than one grouping, the first value listed in the `type-group` is always chosen as the type for that parameter.

For example, for the following type group:
```XML
<type-group name="example1">
       <type>TwoOptions</type>
       <type>Decimal</type>
       <type>FP</type>
</type-group>
```

Would result in the control receiving the value **TwoOptions** for the given parameter's type, while the following:

```XML
<type-group name="example2">
       <type>Decimal</type>
       <type>TwoOptions</type>
       <type>FP</type>
</type-group>
```
would again receive "Decimal".

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
