---
title: "setUtcValue (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e7f770ac-ee19-46dd-babb-44127c299411
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setUtcValue (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Sets a UTC date and time value for a **datetime** type of attribute. UTC stands for Coordinated Universal Time.

> [!NOTE]
> Attributes on quick create forms won't save values set using this method. 

## Attribute types supported

datetime

## Syntax

`formContext.getAttribute(arg).setUtcValue(value)`

## Parameters

**Type**: datetime. 

**Description**: The UTC date and time value.

### Related topic
[getUtcValue (Client API reference)](getUtcValue.md)

