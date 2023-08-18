---
title: retrieveRecordCommand (Power Apps component framework API reference) | Microsoft Docs
description: Retrieve record's associated commands.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# retrieveRecordCommand

[!INCLUDE[./includes/retrieveRecordCommand-description.md](./includes/retrieverecordcommand-description.md)]

## Available for

Model-driven apps

## Syntax

`context.parameters.dataset.retrieveRecordCommand(recordIds)`

## Parameters

| Parameter Name   | Type       | Required | Description |
| ---------------- | ---------- | -------- | ----------- |
| recordIds        | `string[]` | Yes      |             |
| specificCommands | `string[]` | No       |             |
| filterByPriority | `boolean`  | No       |             |
| useNestedFormat  | `boolean`  | No       |             |
| refreshAllRules  | `boolean`  | No       |             |

## Return value

Type: `ICommandObjectWrapper`

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
