---
title: formatTime (Power Apps component framework API reference) | Microsoft Docs
description: Returns a formatted string that represents the datetime value after being formatted.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# formatTime

[!INCLUDE [formattime-description](includes/formattime-description.md)]

## Syntax

`context.formatting.formatTime(value, behavior);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                                   | Required | Description                                          |
| -------------- | ------------------------------------------------------ | -------- | ---------------------------------------------------- |
| value          | `Date`                                                 | Yes      | The date to be formatted.                            |
| behavior       | [`DateTimeFieldBehavior`](../DateTimeFieldBehavior.md) | Yes      | The behavior of the datetime object to be formatted. |

## Return Value

Type: `string`

### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
