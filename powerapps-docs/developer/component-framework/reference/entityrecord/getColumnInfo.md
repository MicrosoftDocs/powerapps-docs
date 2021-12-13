---
title: getColumnInfo | Microsoft Docs
description: Gets the current state of the column for the record.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/12/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 74992f97-89b7-401e-ac95-9c8a47f990d1
---

# getColumnInfo

[!INCLUDE[./includes/getColumnInfo-description.md](./includes/getcolumninfo-description.md)]

## Available for

Canvas apps

## Syntax

`getColumnInfo(columnName)`

## Parameters

| Parameter Name | Type     | Required | description |
| -------------- | -------- | -------- | ----------- |
| columnName     | `string` | Yes      |  Name of the column.           |

## Return Value

**Type**: `ColumnInfo`

```
ColumnInfo{
readonly error: boolean;
	readonly errorMessage?: string;
	readonly security?: SecurityValues;
	readonly type: string;
}
```

### Related topics

[Entityrecord](../entityrecord.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)
[Set up security permissions for a field](/power-platform/admin/set-up-security-permissions-field)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
