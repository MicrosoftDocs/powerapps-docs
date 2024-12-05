---
title: "quickViewControl.getVisible (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the quickViewControl.getVisible method.
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
# quickViewControl.getVisible (Client API reference)

[!INCLUDE[./includes/getVisible-description.md](./includes/getVisible-description.md)]

>[!NOTE]
>If the containing **section** or **tab** for this control isn't visible, this method can still return **true**. To make certain that the control is actually visible; you need to also check the visibility of the containing elements.

## Syntax

`quickViewControl.getVisible();`

## Return Value

**Type**: Boolean.

**Description**: true if the control is visible; false otherwise.

### Related articles

[setVisible](setVisible.md)   
[formContext.ui.quickForms](../formContext-ui-quickForms.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
