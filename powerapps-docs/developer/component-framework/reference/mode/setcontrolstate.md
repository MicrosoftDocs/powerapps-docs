---
title: setControlState | Microsoft Docs
description: Set component state so that it will be stored in one session.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
---

# setControlState

[!INCLUDE [setcontrolstate-description](includes/setcontrolstate-description.md)]

## Syntax

`context.mode.setControlState(state);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type         | Required | Description                                          |
| -------------- | ------------ | -------- | ---------------------------------------------------- |
| state          | `Dictionary` | Yes      | Data that persists in one session for a single user. |

## Example

Sample control: [Implementing control state API component](../../sample-controls/control-state-api.md).

## Return Value

Type: `boolean`

### Related topics

[Mode](../mode.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
