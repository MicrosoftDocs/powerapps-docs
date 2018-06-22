---
title: "close (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1261a94d-4f5c-446d-8c29-a326e819696b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# close (Client API reference)



[!INCLUDE[./includes/close-description.md](./includes/close-description.md)]

## Syntax

`formContext.ui.close();`

## Remarks

The HTML **Window.close** method is suppressed. To close a form window, you must use this method. If there are any unsaved changes in the form, the user will be prompted whether they want to save their changes before the window closes.

For Microsoft Dynamics 365 for tablets, this method mimics the behavior of the back navigation button.

### Related topics

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)

