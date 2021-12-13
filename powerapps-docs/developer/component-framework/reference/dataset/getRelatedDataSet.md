---
title: getRelatedDataSet | Microsoft Docs
description: Gets the related dataset for this column (only if this is related table column like lookup).
keywords:
manager: kvivek
ms.date: 06/12/2021
ms.service: "powerapps"
ms.reviewer: "nabuthuk"
ms.author: nabuthuk
author: Nkrb
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 35d94cf8-eab3-4dee-82af-336f6b33b789
---

# getRelatedDataSet

[!INCLUDE[./includes/getRelatedDataSet-description.md](./includes/getrelateddataset-description.md)]

## Available for

Canvas apps

## Syntax

`context.parameters.dataset.getRelatedDataSet(columnName, updateCallback, targetEntityName)`

## Parameters

| Parameter Name   | Type                       | Required | description |
| ---------------- | -------------------------- | -------- | ----------- |
| columnName       | `string`                   | Yes      |             |
| updateCallback   | `onDataSetUpdatedCallback` | Yes      |             |
| targetEntityName | `string`                   | No       |             |

## Return value

Type: `[Dataset](../../dataset.md)`

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
