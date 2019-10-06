---
title: formatTime | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 148964b5-106e-4f2e-8038-9086d29dc54f

---

# formatTime

[!INCLUDE [formattime-description](includes/formattime-description.md)]

## Syntax

`context.formatting.formatTime(value, behavior);`

## Available for 

Model-driven apps and canvas apps (experimental preview)

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Date`|Yes|The date to be formatted.|
|behavior|`DateTimeFieldBehavior`|Yes|The behavior of the datetime object to be formatted. The `DateTimeFieldBehavior` has the following attributes:<br/>- `None =0`: Unknown DateTime behavior <br/>- `UserLocal =1`: Respect user local time. Dates stored as UTC<br/>- `TimeZoneIndependent =3`: Dates and time stored without conversion to UTC|

## Return Value

Type: `string`


### Related topics

[Formatting](../formatting.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)