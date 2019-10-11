---
title: Type | Microsoft Docs
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
ms.assetid: d9fb178c-6cc6-48cc-99c0-9972e37dec3e
---

# type

[!INCLUDE [type-description](includes/type-description.md)]

## Available for

Model-driven apps

## Parent Elements

|Element|Description|
|--|--|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|

## Value element

This element contains a `string` with one of the following values:

[!INCLUDE [type-table](includes/type-table.md)]

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

[PowerApps component framework Manifest Schema reference](index.md)<br/>
[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework overview](../overview.md)