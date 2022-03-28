---
title: "quickViewControl.getControlType (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getControlType method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# quickViewControl.getControlType (Client API reference)



[!INCLUDE[./includes/getControlType-description.md](./includes/getControlType-description.md)]

## Syntax

`quickViewControl.getControlType();`

## Return Value

**Type**: String.

**Description**: For a quick view control, the method returns "quickform". 

For a constituent control in a quick view control, the method returns the actual category of the control. For more information about possible return values, see [getControlType](../controls/getControlType.md)..

### Related topics

[formContext.ui.quickForms](../formContext-ui-quickForms.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]