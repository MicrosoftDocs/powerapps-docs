---
title: saveMultipleRecords | Microsoft Docs
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

# saveMultipleRecords

[!INCLUDE[./includes/saveMultipleRecords-description.md](./includes/saveMultipleRecords-description.md)]

## Available for

Model-driven apps

## Syntax

`context.parameters.dataset.saveMultipleRecords(records)`

## Parameters

| Parameter Name | Type                                 | Required | description |
| -------------- | ------------------------------------ | -------- | ----------- |
| records        | `[EntityRecord](../entityrecord.md)` | Yes      |             |

## Return value

Type: `Promise<string>`

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
