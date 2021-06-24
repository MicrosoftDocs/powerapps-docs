---
title: "getText (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getText method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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

### Related topics
[getInitialValue (Client API reference)](getInitialValue.md)

[getOption (Client API reference)](getOption.md)

[getOptions (Client API reference)](getOptions.md)

[getSelectedOption (Client API reference)](getSelectedOption.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]