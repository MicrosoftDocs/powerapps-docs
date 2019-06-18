---
title: FilterExpression | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 19ad54b8-e044-4f07-a18e-b00d26b75832
---

# FilterExpression

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [filterexpression-description](includes/filterexpression-description.md)]

## Properties

## conditions

The set of conditions associated with this filter.

**Type**: [ConditionExpression](conditionexpression.md)[]

## filterOperator

The operator used to combine conditions in this filter.

**Type**: `enum`

The `filterOperator` value is an enum with the following possible values

|Value|Member|
|--|--|
|0|And|
|1|Or|

## filters

Any child filters that should be evaluated after evaluating this filter.

**Type**: [FilterExpression](filterexpression.md)[]<br />

### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)