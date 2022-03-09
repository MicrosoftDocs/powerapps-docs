---
title: formatDecimal | Microsoft Docs
description: Returns a formatted string that represents the decimal value after being formatted.
keywords:
author: adrianorth
ms.date: 03/07/2022
ms.author: jdaly
ms.reviewer: jdaly
manager: kvivek

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 05c1c54d-14b5-4dad-9cd8-eec07e750c00
---

# formatDecimal

[!INCLUDE [formatdecimal-description](includes/formatdecimal-description.md)]

## Syntax

`context.formatting.formatDecimal(value, precision);`

## Available for 

Model-driven and canvas apps

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`number`|Yes|The date to be formatted.|
|precision|`number`|Yes|The number of digits after decimal point.|

## Return Value

Type: `string`


### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]