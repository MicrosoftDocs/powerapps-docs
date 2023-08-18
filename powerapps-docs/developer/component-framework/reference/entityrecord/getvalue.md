---
title: EntityRecord.getValue (Power Apps component framework API reference) | Microsoft Docs
description: Gets the value of the record's column.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 04/21/2023
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
| `columnName`   | `string` | Yes      | The logical name of the column. |

## Return Value

Type: `string` | `Date` | `number` | `number[]` | `boolean` | [EntityReference](./../entityreference.md) | `EntityReference[]` | [FileObject](./../fileobject.md) | [ImageObject](./../imageobject.md)

> [!NOTE]
> For Canvas apps the [fileSize](../fileobject.md#filesize) and [mimeType](../fileobject.md#mimetype) properties for file columns will be missing on the first call, but the call initiates an asynchronous process to cache these values. After these values are cached, the next `getValue` call will return all attribute values.

### Related articles

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
