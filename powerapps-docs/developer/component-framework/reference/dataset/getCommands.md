---
title: getCommands (Power Apps component framework API reference) | Microsoft Docs
description: The commands for this dataset.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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
| IDs            | `string[]` | Yes      | Array of IDs for which to command should be run. |

## Return value

Type: [ICommand](../icommand.md)

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
