---
title: "getControlType (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getControlType method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 72d6c761-bcc7-4de6-b73f-5f2833297825
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getControlType (Client API reference)



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