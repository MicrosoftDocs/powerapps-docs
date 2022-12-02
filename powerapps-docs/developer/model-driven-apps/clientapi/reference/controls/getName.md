---
title: "control.getName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the control.getName method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# control.getName (Client API reference)



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