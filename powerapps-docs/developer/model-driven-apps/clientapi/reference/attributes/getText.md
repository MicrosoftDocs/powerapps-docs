---
title: "getText (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 1/10/2019
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getText (Client API reference)



Returns a string value of the text for the currently selected option for an **optionset** or **multiselectoptionset** attribute. 

## Attribute types supported

optionset, multiselectoptionset

## Syntax

`formContext.getAttribute(arg).getText()`

## Return Value

**Type**: String. 

**Description**: The **text** value of the selected option.

> [!NOTE]
> When no option is selected, it will return null.

### Related topics
[getInitialValue (Client API reference)](getInitialValue.md)

[getOption (Client API reference)](getOption.md)

[getOptions (Client API reference)](getOptions.md)

[getSelectedOption (Client API reference)](getSelectedOption.md) 


