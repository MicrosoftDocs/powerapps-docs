---
title: formatDecimal | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 05c1c54d-14b5-4dad-9cd8-eec07e750c00
---

# formatDecimal

[!INCLUDE [formatdecimal-description](includes/formatdecimal-description.md)]

## Available for 

Model-driven apps and canvas apps (experimental preview)

## Syntax

`context.formatting.formatDecimal(value, precision)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`number`|yes|The date to be formatted.|
|precision|`number`|yes|The number of digits after decimal point.|

## Return Value

Type: `string`


### Related topics

[Formatting](../formatting.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)