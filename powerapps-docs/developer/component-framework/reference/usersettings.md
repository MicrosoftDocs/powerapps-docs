---
title: UserSettings | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c237ff96-9268-4068-9d61-aea0bdc79fc2
---

# UserSettings

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [usersettings-description](includes/usersettings-description.md)]

## Properties

## dateFormattingInfo

Date formatting information as retrieved from the server.

**Type**: `DateFormattingInfo`

## isRTL

Whether the language is right to left

**Type**: `boolean`

## languageId

Current user's language id

**Type**: `number`

## numberFormattingInfo

Number formatting information as retrieved from the server.

**Type**: `NumberFormattingInfo`

## securityRoles

Current user roles

**Type**: `string[]`

## userId

The id of the current user

**Type**: `string`

## userName

The name of the current user

**Type**: `string`

## Methods

|Method | Description | 
| ------|-------------|
|[getTimeZoneOffsetMinutes](usersettings/gettimezoneoffsetminutes.md)|[!INCLUDE [gettimezoneoffsetminutes-description](usersettings/includes/gettimezoneoffsetminutes-description.md)]|

### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)