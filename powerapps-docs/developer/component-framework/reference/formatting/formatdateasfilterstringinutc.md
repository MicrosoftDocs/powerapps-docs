---
title: formatDateAsFilterStringUTC (Power Apps component framework API reference) | Microsoft Docs
description: Returns a formatted string that represents a date in YYYY-MM-DD standard UTC format. Results pattern is based on standard UTC format.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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


### Related articles

[Formatting](../formatting.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
