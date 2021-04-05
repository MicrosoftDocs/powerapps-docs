---
title: ConditionExpression in Microsoft Dataverse| Microsoft Docs
description: Learn how to use different methods and properties available for ConditionExpression in Power Apps component framework.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bd90b3fd-a4b4-4999-8b53-d2a5dce4966b
---

# ConditionExpression

[!INCLUDE [conditionexpression-description](includes/conditionexpression-description.md)]

## Available for 

Model-driven apps

## Properties

### attributeName

The name of the dataset column to apply the filter on.

**Type**: `string`

### conditionOperator

The operator used to evaluate the condition.

**Type**: `enum`

The `conditionOperator` value is an enum with the following possible values

|Value|Member|
|--|--|
|-1|None|
|0|Equal|
|1|NotEqual|
|2|GreaterThan|
|3|LessThan|
|4|GreaterEqual|
|5|LessEqual|
|6|Like|
|8|In|
|12|Null|
|14|Yesterday|
|15|Today|
|16|Tomorrow|
|17|Last7Days|
|18|Next7Days|
|19|LastWeek|
|20|ThisWeek|
|22|LastMonth|
|23|ThisMonth|
|25|On|
|26|OnOrBefore|
|27|OnOrAfter|
|28|LastYear|
|29|ThisYear|
|33|LastXDays|
|34|NextXDays|
|37|LastXMonths|
|38|NextXMonths|
|49|Contains|
|70|InFiscalPeriodAndYear|
|75|Above|
|76|Under|
|77|NotUnder|
|78|AboveOrEqual|
|79|UnderOrEqual|
|87|ContainValues|

### entityAliasName

Table alias name so filtering can be used on linked tables.

**Type**: `string`

### value

The value evaluated by the condition.

**Type**: `string | string[]`

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]