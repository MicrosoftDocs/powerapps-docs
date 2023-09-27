---
title: setControlState (Power Apps component framework API reference) | Microsoft Docs
description: Set component state so that it will be stored in one session.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# setControlState

[!INCLUDE [setcontrolstate-description](includes/setcontrolstate-description.md)]

## Syntax

`context.mode.setControlState(state);`

## Available for

Model-driven apps, canvas apps, & portals.

## Parameters

| Parameter Name | Type         | Required | Description                                          |
| -------------- | ------------ | -------- | ---------------------------------------------------- |
| state          | `Dictionary` | Yes      | Data that persists in one session for a single user. |

## Example

Sample control: [Implementing control state API component](../../sample-controls/control-state-api.md).

## Return Value

Type: `boolean`

### Related articles

[Mode](../mode.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
