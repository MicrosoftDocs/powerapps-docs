---
title: getTimeZoneOffsetMinutes (Power Apps component framework API reference) | Microsoft Docs
description: Gets the offset in minutes from UTC for the given date.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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


### Related articles

[User Settings](../usersettings.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
