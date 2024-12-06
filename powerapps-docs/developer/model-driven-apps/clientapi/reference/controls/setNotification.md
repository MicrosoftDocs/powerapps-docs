---
title: "setNotification (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setNotification method.
author: MitiJ
ms.author: mijosh
ms.date: 11/27/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setNotification (Client API reference)

Displays an error message for the control to indicate that data isn't valid. When this method is used,  a red "X" icon appears next to the control. On Dynamics 365 mobile clients, tapping on the icon will display the message.

> [!NOTE]
> Always make sure that the control you are using `setNotification` with is visible on the form.
>
>`setNotification` will not return an error if you use it on a control that is visible but is within a section or tab that isn't visible. When saving a record `setNotification` will display a message at the top of the form as a validation error. If the control is not visible because it is within a hidden parent section or tab, the user cannot fix this.

## Control types supported

Standard, lookup, choices and choice control types.

## Syntax

`formContext.getControl(arg).setNotification(message,uniqueId);`

## Parameters

|Name | Type | Required | Description|
|----|----|----|----|
|`message` |String |Yes|The message to display.|
|`uniqueId` |String |No|The ID to use to clear this message when using the **clearNotification** method.

## Return Value

**Type**: Boolean

**Description**: Indicates whether the method succeeded.

## Remarks

Setting an error notification on a control will block the form from saving.

### Related articles

[addNotification](addNotification.md)   
[clearNotification](clearNotification.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
