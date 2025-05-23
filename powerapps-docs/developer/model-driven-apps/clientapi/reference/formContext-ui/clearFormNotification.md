---
title: "ui.clearFormNotification (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the ui.clearNotification method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# ui.clearFormNotification (Client API reference)



[!INCLUDE[./includes/clearFormNotification-description.md](./includes/clearFormNotification-description.md)]

## Syntax

`formContext.ui.clearFormNotification(uniqueId)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`uniqueId`|String|Yes|A unique identifier for the message to be cleared that was set using the [setFormNotification](setFormNotification.md) method.|

## Return Value

**Type**: Boolean

**Description**: true if the method succeeded, false otherwise. 


### Related articles

[setFormNotification](setFormNotification.md)   
[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
