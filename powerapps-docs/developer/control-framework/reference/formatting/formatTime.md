---
title: formatTime | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 148964b5-106e-4f2e-8038-9086d29dc54f

---

# formatTime

[!INCLUDE [formattime-description](includes/formattime-description.md)]

## Syntax

`formatTime(value, behavior)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Date`|yes|The date to be formatted.|
|behavior|`DateTimeFieldBehavior`|yes|The behavior of the datetime object to be formatted. The `DateTimeFieldBehavior` has the following attributes:<br/>- `None =0`: Unknown DateTime behavior <br/>- `UserLocal =1`: Respect user local time. Dates stored as UTC<br/>- `TimeZoneIndependent =3`: Dates and time stored without conversion to UTC|

## Return Value

Type: `string`

### Related topics

[Formatting](../formatting.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../../powerapps-control-framework-overview.md)<br />
