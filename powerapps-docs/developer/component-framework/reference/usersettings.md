---
title: UserSettings | Microsoft Docs
description: Provides information about the current user settings.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c237ff96-9268-4068-9d61-aea0bdc79fc2
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

Current user roles. This is supported only in model-driven apps.

**Type**: `string[]`

### userId

The id of the current user. This is supported only in model-driven apps.

**Type**: `string`

### userName

The username of the current user. This is supported only in model-driven apps.

**Type**: `string`

## Methods

|Method | Description | 
| ------|-------------|
|[getTimeZoneOffsetMinutes](usersettings/gettimezoneoffsetminutes.md)|[!INCLUDE [gettimezoneoffsetminutes-description](usersettings/includes/gettimezoneoffsetminutes-description.md)]|

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]