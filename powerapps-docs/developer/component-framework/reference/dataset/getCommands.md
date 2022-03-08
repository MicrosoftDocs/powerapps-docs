---
title: getCommands | Microsoft Docs
description: The commands for this dataset.
keywords:
author: adrianorth
ms.date: 03/07/2022
ms.author: jdaly
ms.reviewer: jdaly
manager: kvivek

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 35d94cf8-eab3-4dee-82af-336f6b33b789
---

# getCommands

[!INCLUDE[./includes/getCommands-description.md](./includes/getcommands-description.md)]

## Available for

Canvas apps

## Syntax

`context.parameters.dataset.getCommands(ids)`

## Parameters

| Parameter Name | Type       | Required | description                                      |
| -------------- | ---------- | -------- | ------------------------------------------------ |
| ids            | `string[]` | Yes      | Array of IDs for which to command should be run. |

## Return value

Type: [ICommand](../icommand.md)

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
