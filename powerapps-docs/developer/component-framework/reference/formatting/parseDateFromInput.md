---
title: parseDateFromInput | Microsoft Docs
description: Returns parsed string as Date.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/01/2022
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 148964b5-106e-4f2e-8038-9086d29dc54f
---

# parseDateFromInput

[!INCLUDE [parseDateFromInput-description](includes/parseDateFromInput-description.md)]

## Syntax

`context.formatting.parseDateFromInput(input, controlAttributes);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type                                           | Required | Description                                                   |
| -------------- | ---------------------------------------------- | -------- | ------------------------------------------------------------- |
| input          | `string`                                       | Yes      | User input.                                                   |
| behavior       | [`ControlAttributes`](../Controlattributes.md) | Yes      | `controlAttributes` control attributes used by the formatter. |

## Return Value

Type: `Date`

### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
