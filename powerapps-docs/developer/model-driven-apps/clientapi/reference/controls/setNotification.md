---
title: "setNotification (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setNotification method.
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
---
# setNotification (Client API reference)

Displays an error message for the control to indicate that data isn’t valid. When this method is used,  a red "X" icon appears next to the control. On Dynamics 365 mobile clients, tapping on the icon will display the message. 

## Control types supported

Standard, lookup, choices and choice control types.

## Syntax

`formContext.getControl(arg).setNotification(message,uniqueId);`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|message |String |Yes|The message to display.| 
|uniqueId |String |No|The ID to use to clear this message when using the **clearNotification** method.
| | |

## Return Value
**Type**: Boolean 

**Description**: Indicates whether the method succeeded.

## Remarks

Setting an error notification on a control will block the form from saving.

### Related topics

[addNotification](addNotification.md)

[clearNotification](clearNotification.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]