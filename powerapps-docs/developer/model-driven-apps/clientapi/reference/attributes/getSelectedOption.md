---
title: "Xrm.Device| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: ce572df6-aae6-431a-aa95-73eee544c7e9
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getSelectedOption (Client API reference)



Returns the option object or an array of option objects selected in an **optionset** or **multiselectoptionset** attribute respectively. 

## Attribute types supported

optionset, multiselectoptionset

## Syntax

`formContext.getAttribute(arg).getSelectedOption()`

## Return Value

**Type**: Option object for optionset; array of option objects for multiselectoptionset. 

**Description**: Returns the object with text and value properties.

### Related topics
[getInitialValue (Client API reference)](getInitialValue.md)

[getOption (Client API reference)](getOption.md)

[getOptions (Client API reference)](getOptions.md)

[getText (Client API reference)](getText.md)

