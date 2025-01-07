---
title: "control.getOptions (Client API reference)"
description: Includes description and supported parameters for the control.getOptions method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# control.getOptions (Client API reference)

Returns an array of option objects representing valid options available for a control, including a blank option and excluding any options that have been removed from the control using [removeOption](removeOption.md).

## Control types supported

Choice, Choices

## Syntax

`formContext.getControl(arg).getOptions()`

## Return Value

**Type**: Array of option objects. 

**Description**: The array of option objects representing valid options where each option object has the following attributes:

- **`text`**: String. Label of the option.
- **`value`**: Number. Enumeration value of the option.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
