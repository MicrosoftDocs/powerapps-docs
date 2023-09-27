---
title: SortStatus (Power Apps component framework API reference) | Microsoft Docs
description: Current sort status of a dataset column.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# SortStatus

[!INCLUDE [sort-description](includes/sortstatus-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### name

The name of the column.

**Type**: `string`

### sortDirection

The current sort direction for the column.

**Type**: `enum`

The `sortDirection` value is an enum with the following possible values.

| Value | Member     |
| ----- | ---------- |
| -1    | None       |
| 0     | Ascending  |
| 1     | Descending |

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
