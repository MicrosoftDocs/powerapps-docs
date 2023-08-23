---
title: formatUserDateTimeToUTC (Power Apps component framework API reference) | Microsoft Docs
description: Returns a formatted string that represents the UTC datetime value after being formatted.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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

### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
