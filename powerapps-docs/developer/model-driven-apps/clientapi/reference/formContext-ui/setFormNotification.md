---
title: "setFormNotification (Client API Reference) in Model-Driven Apps"
description: Learn how to use setFormNotification to display error, warning, and info notifications on model-driven app forms. Review syntax and parameters.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setFormNotification (Client API reference)



[!INCLUDE[./includes/setFormNotification-description.md](./includes/setFormNotification-description.md)]

By using setFormNotification, you can display any number of form-level notifications in model-driven apps. They stay visible until you remove them by using [clearFormNotification](clearFormNotification.md). The height of the notification area is limited, so each new message is added to the top. Users can scroll down to view older messages that aren't removed yet.

## Syntax

`formContext.ui.setFormNotification(message, level, uniqueId);`

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|`message`|String|Yes|The text of the message.|
|`level`|String|Yes|The level of the message, which defines how the message is displayed. Specify one of the following values:<br>`ERROR` : Notification uses the system error icon.<br/>`WARNING` : Notification uses the system warning icon.<br/>`INFO` : Notification uses the system info icon.|
|`uniqueId`|String|Yes|A unique identifier for the message that you can use later with [clearFormNotification](clearFormNotification.md) to remove the notification.|

## Return value

**Type**: Boolean

**Description**: true if the method succeeded; otherwise, false. 


### Related articles

[clearFormNotification](clearFormNotification.md)   
[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
