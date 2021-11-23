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

[!INCLUDE [ControlAttributes-description](includes/ControlAttributes-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### Type

The attribute type
**Type**: `[ControlAttributesType](./ControlAttributesType.md) | string`

### Precision

The Precision of the attribute
**Type**: `number`

### PrecisionSource

The Precision source of the attribute
**Type**: `[MoneyPrecisionSource?](./MoneyPrecisionSource.md)`

### Format

The format of the string attribute
**Type**: `string?`

### Behavior

The behavior of the datetime attribute
**Type**: `[DateTimeFieldBehavior?](./DateTimeFieldBehavior.md)`

### OptionSet

The optionset object of this attribute
**Type**: `[OptionDescriptor\[\]?](./OptionDescriptor.md)`

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
