---
title: ControlAttributes| Microsoft Docs
description: Attributes of control that necessary for formatting.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# ControlAttributes

[!INCLUDE [ControlAttributes-description](includes/controlattributes-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### Type

The column type.

**Type**: [ControlAttributesType](ControlAttributesType.md)

### Precision

The precision of the column.

**Type**: `number`

### PrecisionSource

The precision source of the column.

**Type**: [MoneyPrecisionSource](./moneyprecisionsource.md)

### Format

The format of the string column.
**Type**: `string`

### Behavior

The behavior of the datetime column.
**Type**: [DateTimeFieldBehavior](./DateTimeFieldBehavior.md)

### OptionSet

The optionset/choice object of this column.
**Type**: [OptionDescriptor](./optiondescriptor.md)

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
