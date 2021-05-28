---
title: "getName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getName method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getName (Client API reference)



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



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]