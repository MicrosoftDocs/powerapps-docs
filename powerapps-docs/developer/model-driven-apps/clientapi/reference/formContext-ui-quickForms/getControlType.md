---
title: "getControlType (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 72d6c761-bcc7-4de6-b73f-5f2833297825
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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