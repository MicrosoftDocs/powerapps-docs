---
title: formatUserDateTimeToUTC | Microsoft Docs
description: Returns a formatted string that represents the datetime value after being formatted.
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

# formatUserDateTimeToUTC

[!INCLUDE [formatUserDateTimeToUTC-description](includes/formatUserDateTimeToUTC-description.md)]

## Syntax

`context.formatting.formatUserDateTimeToUTC(userDateTime, behavior);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                                   | Required | Description                                          |
| -------------- | ------------------------------------------------------ | -------- | ---------------------------------------------------- |
| userDateTime   | `Date`                                                 | Yes      | The date to be formatted.                            |
| behavior       | [`DateTimeFieldBehavior`](../DateTimeFieldBehavior.md) | No       | The behavior of the datetime object to be formatted. |

## Return Value

Type: `string`

### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
