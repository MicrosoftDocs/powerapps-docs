---
title: "getOptions (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 83347491-68d2-4844-bda4-0cd0abde2edf
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getOptions (Client API reference)

Returns an array of option objects representing valid options currently available including a blank option and excluding any options that have been removed from the control using [removeOption](removeOption.md). 

## Attribute types supported

OptionSet, MultiSelectOptionSet

## Syntax

`formContext.getControl(arg).getOptions()`

## Return Value

**Type**: Array of option objects. 

**Description**: The array of option objects representing valid options with the name of the option (string) and the value (number).

