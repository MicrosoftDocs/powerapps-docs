---
title: "getText (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getText method.
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
# getText (Client API reference)

Returns a string value of the text for the currently selected option for a **choice** or **choices** column. 

## Column types supported

choice, choices

## Syntax

`formContext.getAttribute(arg).getText()`

## Return Value

**Type**: String. 

**Description**: The **text** value of the selected option.

> [!NOTE]
> When no option is selected, it will return null.

### Related articles

[getInitialValue (Client API reference)](getInitialValue.md)   
[getOption (Client API reference)](getOption.md)   
[getOptions (Client API reference)](getOptions.md)   
[getSelectedOption (Client API reference)](getSelectedOption.md) 


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
