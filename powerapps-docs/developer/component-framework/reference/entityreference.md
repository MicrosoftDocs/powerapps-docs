---
title: EntityReference in Microsoft Dataverse| Microsoft Docs
description: Learn how to use different methods and properties available for EntityReference in Power Apps component framework.
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

# EntityReference

[!INCLUDE [entityreference-description](includes/entityreference-description.md)]

## Available for 

Model-driven apps

## Properties

### etn

The table type name. Read-only.

**Type**: `string`

### id

The record id. Read-only.

**Type**: `object`

The `id` object contains the following property:

|Name|Type|Description|
|--|--|--|
|`guid`|`string`|00000000-0000-0000-0000-000000000000|

### name

The name of the table reference. Read-only.

**Type**: `string`

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]