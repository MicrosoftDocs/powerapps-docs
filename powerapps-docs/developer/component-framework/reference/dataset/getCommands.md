---
title: getCommands | Microsoft Docs
description: The commands for this dataset.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
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
