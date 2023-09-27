---
title: FormatCurrency (Power Apps component framework API reference) | Microsoft Docs
description: Returns a formatted string that represents the currency value after being formatted.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# formatCurrency

[!INCLUDE [formatcurrency-description](includes/formatcurrency-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`context.formatting.formatCurrency(value, precision, symbol)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`number`|yes| A value to be formatted.|
|precision|`number`|yes| The number of digits after decimal point.|
|symbol|`string`|yes| The currency symbol/code to be added with currency value.|

## Return Value

Type: `string`


### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
