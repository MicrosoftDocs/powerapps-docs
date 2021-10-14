---
title: getTimeZoneOffsetMinutes | Microsoft Docs
description: Gets the offset in minutes from UTC for the given date.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 86290d20-7dbb-4932-adaa-31121ae7a3f6
---

# getTimeZoneOffsetMinutes

[!INCLUDE [gettimezoneoffsetminutes-description](includes/gettimezoneoffsetminutes-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`context.usersettings.getTimeZoneOffsetMinutes(date)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|date|`Date`|Yes|date to get the offset from utc for.|

## Return Value

Type: `Number`
Description: Time zone offset in minutes.


### Related topics

[User Settings](../usersettings.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]