---
title: EntityRecord.getValue | Microsoft Docs
description: Gets the value of the record's column.
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# EntityRecord.getValue

[!INCLUDE[./includes/getvalue-description.md](./includes/getvalue-description.md)]

## Available for

Model-driven and canvas apps

## Syntax

`getValue(columnName)`

## Parameters

| Parameter Name | Type     | Required | Description         |
| -------------- | -------- | -------- | ------------------- |
| `columnName`   | `string` | Yes      | Name of the column. |

## Return Value

Type: `string` | `Date` | `number` | `number[]` | `boolean` | [EntityReference](./../entityreference.md) | `EntityReference[]` | [FileObject](./../fileobject.md) | [ImageObject](./../ImageObject.md)

> [!NOTE]
> For Canvas apps some attributes for file columns will be missing on the first call, since they depend on some async functions. After async functions resolve they will caches values and next `getValue` call will fetch all existing attributes.

### Related topics

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
