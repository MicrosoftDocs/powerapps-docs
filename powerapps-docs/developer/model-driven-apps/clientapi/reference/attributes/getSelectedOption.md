---
title: "getSelectedOption| MicrosoftDocs"
description: Includes description and supported parameters for the getSelectedOption method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: ce572df6-aae6-431a-aa95-73eee544c7e9
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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

### Related topics
[getInitialValue (Client API reference)](getInitialValue.md)

[getOption (Client API reference)](getOption.md)

[getOptions (Client API reference)](getOptions.md)

[getText (Client API reference)](getText.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]