---
title: ControlAttributes in Microsoft Dataverse| Microsoft Docs
description: Attributes of control that necessary for formatting.
keywords:
ms.author: nabuthuk
manager: kvivek
author: nkrb
ms.date: 11/23/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad8659f7-f566-43db-bed1-c8484c114a59
---

# ControlAttributes

[!INCLUDE [ControlAttributes-description](includes/controlattributes-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### Type

The column type.

**Type**: `[ControlAttributesType](../controlattributestype.md) | string`

### Precision

The precision of the column.

**Type**: `number`

### PrecisionSource

The precision source of the column.

**Type**: `[MoneyPrecisionSource](./moneyprecisionsource.md)`

### Format

The format of the string column.
**Type**: `string`

### Behavior

The behavior of the datetime column.
**Type**: `[DateTimeFieldBehavior](./DateTimeFieldBehavior.md)`

### OptionSet

The optionset/choice object of this column.
**Type**: `[OptionDescriptor](./optiondescriptor.md)`

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
