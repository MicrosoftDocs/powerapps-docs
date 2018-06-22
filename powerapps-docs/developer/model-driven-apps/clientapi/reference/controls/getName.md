---
title: "getName (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getName (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns the name assigned to the control.

>[!NOTE]
>The name assigned to a control is not determined until the form loads. Changes to the form may change the name assigned to a given control. 

## Control types supported

All

## Syntax

`formContext.getControl(arg).getName();`

## Return Value

**Type**: String

**Description**: The name of the control.

### Related topics

[Controls](../controls.md)

