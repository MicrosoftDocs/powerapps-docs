---
title: EntityReference (Power Apps component framework API reference)| Microsoft Docs
description: Learn how to use different methods and properties available for EntityReference in Power Apps component framework.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
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

| Name   | Type     | Description                          |
| ------ | -------- | ------------------------------------ |
| `guid` | `string` | 00000000-0000-0000-0000-000000000000 |

### name

The name of the table reference. Read-only.

**Type**: `string`

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
