---
title: formatUserInput | Microsoft Docs
description: Returns formatter user input based on the passed in attribute type. If type is not recognized, returns the input itself.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 11/23/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 148964b5-106e-4f2e-8038-9086d29dc54f
---

# formatUserInput

[!INCLUDE [formatUserInput-description](includes/formatuserinput-description.md)]

## Syntax

`context.formatting.formatUserInput(input, controlAttributes);`

## Available for

Model-driven and canvas apps

## Parameters

| Parameter Name | Type   | Required | Description   |
| -------------- | ----------------- | -------- | ---------------- |
| input          | `unknown`  | Yes      | User input. |
| behavior       | [`ControlAttributes`](../Controlattributes.md) | Yes | `controlAttributes`  used by the formatter. |

## Return Value

Type: `string`

## Example

```ts
const controlAttributes = {
  Type: "double",
  Precision: 2,
  PrecisionSource: 0,
  Behavior: null,
  OptionSet: null,
  Format: null,
} as ControlAttributes;

context.formatter.formatUserInput("22", controlAttributes);
```

### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
