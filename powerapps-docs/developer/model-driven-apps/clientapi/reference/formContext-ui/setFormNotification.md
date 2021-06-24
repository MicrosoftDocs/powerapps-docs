---
title: "setFormNotification (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setFormNotification method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 48749e32-8490-4c8f-917c-3f1f8b9c028b
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setFormNotification (Client API reference)



[!INCLUDE[./includes/setFormNotification-description.md](./includes/setFormNotification-description.md)]

You can display any number of notifications and they will be displayed until they are removed using [clearFormNotification](clearFormNotification.md). The height of the notification area is limited so each new message will be added to the top. Users can scroll down to view older messages that have not yet been removed.

## Syntax

`formContext.ui.setFormNotification(message, level, uniqueId);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|message|String|Yes|The text of the message.|
|level|String|Yes|The level of the message, which defines how the message will be displayed. Specify one of the following values:<br>`ERROR` : Notification will use the system error icon.<br/>`WARNING` : Notification will use the system warning icon.<br/>`INFO` : Notification will use the system info icon.|
|uniqueId|String|Yes|A unique identifier for the message that can be used later with [clearFormNotification](clearFormNotification.md) to remove the notification.|

## Return Value

**Type**: Boolean

**Description**: true if the method succeeded; false otherwise. 


### Related topics

[clearFormNotification](clearFormNotification.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]