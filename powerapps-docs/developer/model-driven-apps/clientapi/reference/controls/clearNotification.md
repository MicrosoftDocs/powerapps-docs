---
title: "clearNotification (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the clearNotification method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# clearNotification (Client API reference)

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