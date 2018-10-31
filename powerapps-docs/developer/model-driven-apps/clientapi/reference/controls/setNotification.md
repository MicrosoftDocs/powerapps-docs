---
title: "setNotification (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setNotification (Client API reference)



Displays an error message for the control to indicate that data isn’t valid. When this method is used,  a red "X" icon appears next to the control. On Dynamics 365 mobile clients, tapping on the icon will display the message. 

## Control types supported

All

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