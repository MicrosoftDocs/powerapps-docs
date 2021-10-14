---
title: formatDateAsFilterStringUTC | Microsoft Docs
description: Returns a formatted string that represents a date in YYYY-MM-DD standard UTC format. Results pattern is based on standard UTC format.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a604fbbf-6d09-450d-b686-7a5cb3f3a2bc
---

# formatDateAsFilterStringInUTC

[!INCLUDE [formatdateasfilterstringinutc-description](includes/formatdateasfilterstringinutc-description.md)]

## Syntax

`context.formatting.formatDateAsFilterStringInUTC(value, includeTime)`

## Available for 

Model-driven and canvas apps

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Date`|yes|The date to be formatted.|
|includeTime|`boolean`|yes| If time component should be included in the return value.|

## Return Value

Type: `string`


### Related topics

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]