---
title: save (Power Apps component framework API reference) | Microsoft Docs
description: Saves the record
ms.author: noazarur
author: noazarur-microsoft
ms.date: 04/21/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# save

[!INCLUDE[./includes/save-description.md](./includes/save-description.md)]

## Available for

Model-driven and canvas [experimental](../../../../maker/canvas-apps/working-with-experimental-preview.md#feature-roll-out-stages) apps

## Syntax

`save()`

## Return Value

Type: `Promise`

## Remarks

You can get an error saying `Invalid snapshot with id undefined` when the incorrect column name parameter was used with [setValue](setValue.md). Make sure to use the logical name of the column.


### Related articles

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
