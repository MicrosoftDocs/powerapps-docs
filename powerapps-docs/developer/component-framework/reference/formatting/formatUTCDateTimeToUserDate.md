---
title: formatUTCDateTimeToUserDate | Microsoft Docs
description: Returns a date that represents the UTC value after being formatted.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 11/04/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 148964b5-106e-4f2e-8038-9086d29dc54f
---

# formatTime

[!INCLUDE [formatUTCDateTimeToUserDate-description](includes/formatUTCDateTimeToUserDate-description.md)]

## Syntax

`context.formatting.formatUTCDateTimeToUserDate(utcDateTime, behavior);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                                   | Required | Description                                          |
| -------------- | ------------------------------------------------------ | -------- | ---------------------------------------------------- |
| value          | `string`                                               | Yes      | The date to be formatted.                            |
| behavior       | [`DateTimeFieldBehavior`](../DateTimeFieldBehavior.md) | No       | The behavior of the datetime object to be formatted. |

## Return Value

Type: `Date`

### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
