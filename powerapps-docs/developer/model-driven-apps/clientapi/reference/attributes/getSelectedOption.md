---
title: "getSelectedOption"
description: Includes description and supported parameters for the getSelectedOption method.
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
# getSelectedOption (Client API reference)

Returns the option object or an array of option objects selected in a **choice** or **choices** column respectively. 

## Column types supported

choice, choices

## Syntax

`formContext.getAttribute(arg).getSelectedOption()`

## Return Value

**Type**: Option object for choice; array of option objects for choices. 

**Description**: Returns the object with text and value properties.

### Related articles

[getInitialValue (Client API reference)](getInitialValue.md)   
[getOption (Client API reference)](getOption.md)   
[getOptions (Client API reference)](getOptions.md)   
[getText (Client API reference)](getText.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
