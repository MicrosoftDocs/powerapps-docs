---
title: "setShowTime (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setShowTime method.
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
# setShowTime (Client API reference)

Specify whether a date control should show the time portion of the date. 

## Control types supported

standard control for **datetime** attributes.

## Syntax

`formContext.getControl(arg).setShowTime(bool);`

## Parameter

|Name|Type|Required|Description|
|----|----|----|----|
|`bool`|Boolean|Yes|Specify true to show the time portion of the date; false otherwise.|

## Remarks

This method will show or hide the time component of a date control where the attribute uses the **DateAndTime** format. This method will have no effect when the **DateOnly** format is used.

### Related articles

[getShowTime](getShowTime.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
