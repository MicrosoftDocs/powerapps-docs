---
title: FormatCurrency | Microsoft Docs
description: Returns a formatted string that represents the currency value after being formatted.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 87e433e6-573f-414f-b49d-1213f2bd8cf4
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


### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]