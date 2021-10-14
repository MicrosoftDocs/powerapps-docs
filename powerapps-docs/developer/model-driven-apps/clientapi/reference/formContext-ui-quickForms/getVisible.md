---
title: "getVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getVisible method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 72c7ec48-1d27-499c-b56c-b7a449a347b8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getVisible (Client API reference)



[!INCLUDE[./includes/getVisible-description.md](./includes/getVisible-description.md)]

>[!NOTE]
>If the containing **section** or **tab** for this control isn’t visible, this method can still return **true**. To make certain that the control is actually visible; you need to also check the visibility of the containing elements.

## Syntax

`quickViewControl.getVisible();`

## Return Value

**Type**: Boolean.

**Description**: true if the control is visible; false otherwise.

### Related topics

[setVisible](setVisible.md)

[formContext.ui.quickForms](../formContext-ui-quickForms.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]