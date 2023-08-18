---
title: formatDecimal (Power Apps component framework API reference) | Microsoft Docs
description: Returns a formatted string that represents the decimal value after being formatted.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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


### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
