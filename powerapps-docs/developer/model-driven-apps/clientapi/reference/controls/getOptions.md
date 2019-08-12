---
title: "getOptions (Client API reference)| MicrosoftDocs"
ms.date: 08/13/2019
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 83347491-68d2-4844-bda4-0cd0abde2edf
author: "nkrb"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getOptions (Client API reference)

Returns an array of option objects representing valid options available for a control, including a blank option and excluding any options that have been removed from the control using [removeOption](removeOption.md). 

## Control types supported

OptionSet, MultiSelectOptionSet

## Syntax

`formContext.getControl(arg).getOptions()`

## Return Value

**Type**: Array of option objects. 

**Description**: The array of option objects representing valid options where each option object has the following attributes:
- **text**: String. Label of the option.
- **value**: Number. Enumeration value of the option.

