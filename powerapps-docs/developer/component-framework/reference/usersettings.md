---
title: UserSettings (Power Apps component framework API reference) | Microsoft Docs
description: Provides information about the current user settings.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# UserSettings

[!INCLUDE [usersettings-description](includes/usersettings-description.md)]

## Available for 

Model-driven and canvas apps

## Properties

### dateFormattingInfo

Date formatting information as retrieved from the server. This property is supported in both model-driven and canvas apps.

**Type**: [DateFormattingInfo](dateformattinginfo.md)

### isRTL

Returns true if the language is right to left. This property is supported in both model-driven and canvas apps.

**Type**: `boolean`

### languageId

Current user's language ID. This property is supported in both model-driven and canvas apps.

**Type**: `number`

### numberFormattingInfo

Number formatting information as retrieved from the server. This property is supported in both model-driven and canvas apps.

**Type**: [NumberFormattingInfo](numberformattinginfo.md)

### securityRoles

Current user roles. Supported only in model-driven apps.

**Type**: `string[]`

### userId

The id of the current user. Supported only in model-driven apps.

**Type**: `string`

### userName

The username of the current user. Supported only in model-driven apps.

**Type**: `string`

## Methods

|Method | Description | 
| ------|-------------|
|[getTimeZoneOffsetMinutes](usersettings/gettimezoneoffsetminutes.md)|[!INCLUDE [gettimezoneoffsetminutes-description](usersettings/includes/gettimezoneoffsetminutes-description.md)]|

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
