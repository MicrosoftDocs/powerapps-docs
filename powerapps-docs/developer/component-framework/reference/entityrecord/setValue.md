---
title: setValue | Microsoft Docs
description: Set value for the column.
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

# setValue

[!INCLUDE[./includes/setValue-description.md](./includes/setValue-description.md)]

## Available for

Model-driven and canvas (experimental) apps

## Syntax

`setValue(columnName, value)`

## Parameters

| Parameter Name | Type     | Required | Description               |
| -------------- | -------- | -------- | ------------------------- |
| `columnName`   | `string` | Yes      | Name of the column. |
| `value`        | `string  | Date     | number | number[] | boolean | EntityReference | EntityReference[] | FileObject | ImageObject` | Yes | New value for the record. |

## Return Value

Type: `Promise`

### Related topics

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
