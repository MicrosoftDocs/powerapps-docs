---
title: formatUTCDateTimeToUserDate | Microsoft Docs
description: Returns a date that represents the UTC value after being formatted.
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

# formatUTCDateTimeToUserDate

[!INCLUDE [formatUTCDateTimeToUserDate-description](includes/formatUTCDateTimeToUserDate-description.md)]

## Syntax

`context.formatting.formatUTCDateTimeToUserDate(utcDateTime, behavior);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                                   | Required | Description                                          |
| -------------- | ------------------------------------------------------ | -------- | ---------------------------------------------------- |
| utcDateTime         | `Date`                                               | Yes      | The date to be formatted.                            |
| behavior       | [`DateTimeFieldBehavior`](../DateTimeFieldBehavior.md) | No       | The behavior of the datetime object to be formatted. |

## Return Value

Type: `Date`

### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
