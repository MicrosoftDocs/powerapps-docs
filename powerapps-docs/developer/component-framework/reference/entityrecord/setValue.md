---
title: setValue | Microsoft Docs
description: Set value for the column.
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

# setValue

[!INCLUDE[./includes/setValue-description.md](./includes/setValue-description.md)]

## Available for

Model-driven and canvas ([experimental](/powerapps-docs/maker/canvas-apps/working-with-experimental-preview#feature-roll-out-stages)) apps

## Syntax

`setValue(columnName, value)`

## Parameters

| Parameter Name | Type                                                                                                           | Required | Description               |
| -------------- | -------------------------------------------------------------------------------------------------------------- | -------- | ------------------------- |
| `columnName`   | `string`                                                                                                       | Yes      | Name of the column.       |
| `value`        | `string | Date | number | number[] | boolean | EntityReference | EntityReference[] | FileObject | ImageObject` | Yes      | New value for the record. |

## Return Value

Type: `Promise`

## Limitations

Canvas ([experimental](/powerapps-docs/maker/canvas-apps/working-with-experimental-preview#feature-roll-out-stages) apps do not support `Decimal Number` and `Floating Point Number` types.

### Related topics

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
