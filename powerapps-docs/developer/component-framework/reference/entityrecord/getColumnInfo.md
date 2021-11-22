---
title: getColumnInfo | Microsoft Docs
description:
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 74992f97-89b7-401e-ac95-9c8a47f990d1
---

# getColumnInfo

TODO: this API basically gets security roles that can be setup here: https://docs.microsoft.com/en-us/power-platform/admin/set-up-security-permissions-field

[!INCLUDE[./includes/getColumnInfo-description.md](./includes/getColumnInfo-description.md)]

## Available for

Model-driven apps and Canvas

## Syntax

`getColumnInfo(columnName)`

## Parameters

| Parameter Name | Type     | Required | description |
| -------------- | -------- | -------- | ----------- |
| columnName     | `string` | Yes      |             |

## Return Value

**Type**: `ColumnInfo`

ADD new TYPE

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

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
