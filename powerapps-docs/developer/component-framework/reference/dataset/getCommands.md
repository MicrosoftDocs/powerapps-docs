---
title: getCommands | Microsoft Docs
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

# delete

[!INCLUDE[./includes/getCommands-description.md](./includes/getCommands-description.md)]

## Available for

Model-driven and canvas apps (test on canvas)

## Syntax

`context.parameters.dataset.getCommands(ids)`

## Parameters

| Parameter Name | Type       | Required | description |
| -------------- | ---------- | -------- | ----------- |
| ids            | `string[]` | Yes      |             |

## Return value

Type: `[ICommand]()`

ADD TYPE COMMAND
/\*\*

- A command button control
  \*/
  export type ICommand = ButtonControl | FlyoutControl | SplitButtonControl;

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
