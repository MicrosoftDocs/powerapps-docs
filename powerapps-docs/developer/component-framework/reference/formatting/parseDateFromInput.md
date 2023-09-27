---
title: parseDateFromInput (Power Apps component framework API reference) | Microsoft Docs
description: Returns parsed string as date.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# parseDateFromInput

[!INCLUDE [parseDateFromInput-description](includes/parseDateFromInput-description.md)]

## Syntax

`context.formatting.parseDateFromInput(input, controlAttributes);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                           | Required | Description   |
| -------------- | ------------------ | -------- | ------------------------------- |
| input          | `string`                                       | Yes      | User input.  |
| behavior       | [`ControlAttributes`](../Controlattributes.md) | Yes      | `controlAttributes` control attributes used by the formatter. |

## Return Value

Type: `Date`

### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
