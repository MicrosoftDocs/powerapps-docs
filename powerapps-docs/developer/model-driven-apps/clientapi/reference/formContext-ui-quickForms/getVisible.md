---
title: "getVisible (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 72c7ec48-1d27-499c-b56c-b7a449a347b8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getVisible (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

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



