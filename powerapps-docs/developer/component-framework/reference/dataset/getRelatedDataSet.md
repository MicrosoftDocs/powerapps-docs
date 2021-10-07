---
title: getRelatedDataSet | Microsoft Docs
description:
keywords:
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.reviewer: "nabuthuk"
ms.author: vilesyk
author: Nkrb
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 35d94cf8-eab3-4dee-82af-336f6b33b789
---

# getRelatedDataSet

[!INCLUDE[./includes/getRelatedDataSet-description.md](./includes/getRelatedDataSet-description.md)]

## Available for

Model-driven

## Syntax

`context.parameters.dataset.getRelatedDataSet(columnName, updateCallback, targetEntityName)`

## Parameters

| Parameter Name   | Type                       | Required | description |
| ---------------- | -------------------------- | -------- | ----------- |
| columnName       | `string`                   | Yes      |             |
| columnName       | `onDataSetUpdatedCallback` | Yes      |             |
| targetEntityName | `string`                   | No       |             |

## Return value

Type: `[Dataset](../../dataset.md)`

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
