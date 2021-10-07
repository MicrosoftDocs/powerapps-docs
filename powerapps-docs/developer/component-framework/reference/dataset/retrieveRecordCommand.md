---
title: retrieveRecordCommand | Microsoft Docs
description:
keywords:
ms.author: vilesyk
author: Nkrb
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec4d6f14-d08b-410f-aad7-6a040c2b1c6a
---

# retrieveRecordCommand

[!INCLUDE[./includes/retrieveRecordCommand-description.md](./includes/retrieveRecordCommand-description.md)]

## Available for

Model-driven apps

## Syntax

`context.parameters.dataset.retrieveRecordCommand(recordIds)`

## Parameters

| Parameter Name   | Type       | Required | description |
| ---------------- | ---------- | -------- | ----------- |
| recordIds        | `string[]` | Yes      |             |
| specificCommands | `string[]` | No       |             |
| filterByPriority | `boolean`  | No       |             |
| useNestedFormat  | `boolean`  | No       |             |
| refreshAllRules  | `boolean`  | No       |             |

## Return value

TODO ADD NEW TYPE
Type: [`ICommandObjectWrapper`]

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
