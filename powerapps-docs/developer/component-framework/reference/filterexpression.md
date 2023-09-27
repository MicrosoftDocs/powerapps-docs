---
title: FilterExpression (Power Apps component framework API reference) | Microsoft Docs
description: An expression used to represent a filter.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# FilterExpression

[!INCLUDE [filterexpression-description](includes/filterexpression-description.md)]

## Available for 

Model-driven apps

## Properties

### conditions

The set of conditions associated with this filter.

**Type**: [ConditionExpression](conditionexpression.md)[]

### filterOperator

The operator used to combine conditions in this filter.

**Type**: `enum`

The `filterOperator` value is an enum with the following possible values

|Value|Member|
|--|--|
|0|And|
|1|Or|

### filters

Any child filters that should be evaluated after evaluating this filter.

**Type**: [FilterExpression](filterexpression.md)[]<br />

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
