---
title: setValue | Microsoft Docs
description: Set value for the column.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/12/2021

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5928055f-784f-496d-bd96-6921d9574d2f
---

# setValue

[!INCLUDE[./includes/setValue-description.md](./includes/setValue-description.md)]

## Available for

Model-driven and canvas apps

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
