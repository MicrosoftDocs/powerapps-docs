---
title: "setIsValid (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setIsValid method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# setIsValid (Client API reference)

Sets a value for a column to determine whether it is valid or invalid with a message.

## Column types supported

All

## Syntax 

`formContext.getAttribute(arg).setIsValid(bool, message);` 

## Parameters

|Name|Type|Required|Description|
|----|----|------|------------|
|`bool`|Boolean|Yes|Specify false to set the column value to invalid and true to set the value to valid.|
|`message`|String|No|The message to display.| 


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
