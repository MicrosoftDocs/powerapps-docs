---
title: setValue (Power Apps component framework API reference) | Microsoft Docs
description: Set value for the column.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 04/21/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# setValue

[!INCLUDE[./includes/setValue-description.md](./includes/setValue-description.md)]

## Available for

Model-driven and canvas [experimental](../../../../maker/canvas-apps/working-with-experimental-preview.md#feature-roll-out-stages) apps

## Syntax

`setValue(columnName, value)`

## Parameters

|Parameter Name |Type| Required | Description|
|----|----|----|----|
| `columnName`|`string`| Yes| The logical name of the column.|
| `value`|`string`<br />`Date`<br />`number`<br />`number[]`<br />`boolean`<br />[EntityReference](./../entityreference.md)<br />`EntityReference[]`<br />[FileObject](./../fileobject.md)<br />[ImageObject](./../imageobject.md)| Yes      | New value for the record. |

## Return Value

Type: `Promise`

## Limitations

Canvas [experimental](../../../../maker/canvas-apps/working-with-experimental-preview.md#feature-roll-out-stages) apps do not support `Decimal Number` and `Floating Point Number` types.

### Related articles

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
