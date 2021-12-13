---
title: retrieveRecordCommand | Microsoft Docs
description: Retrieve record's associated commands.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/12/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec4d6f14-d08b-410f-aad7-6a040c2b1c6a
---

# retrieveRecordCommand

[!INCLUDE[./includes/retrieveRecordCommand-description.md](./includes/retrieverecordcommand-description.md)]

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
