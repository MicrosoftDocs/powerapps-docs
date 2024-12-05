---
title: "close (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the close method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# close (Client API reference)



[!INCLUDE[./includes/close-description.md](./includes/close-description.md)]

## Syntax

`formContext.ui.close();`

## Remarks

The HTML **Window.close** method is suppressed. To close a form window, you must use this method. If there are any unsaved changes in the form, the user will be prompted whether they want to save their changes before the window closes.

For Microsoft Dynamics 365 for tablets, this method mimics the behavior of the back navigation button.

### Related articles

[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
