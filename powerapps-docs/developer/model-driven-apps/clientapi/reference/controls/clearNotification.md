---
title: "control.clearNotification (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the control.clearNotification method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# control.clearNotification (Client API reference)

Remove a message already displayed for a control.

## Control types supported

All

## Syntax

`formContext.getControl(arg).clearNotification(uniqueId);`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|uniqueId |String |No|The ID to use to clear a specific message that was set using **setNotification** or **addNotification**. If the **uniqueId** parameter isn’t specified, the currently displayed notification will be cleared.| 


## Return Value

**Type**: Boolean 

**Description**: Indicates whether the method succeeded. 

### Related topics

[addNotification](addNotification.md)

[setNotification](setNotification.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]