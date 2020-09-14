---
title: "getValue (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
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
# getValue (Client API reference)



Gets the latest value in a control as the user types characters in a specific text or number field. This method helps you to build interactive experiences by validating data and alerting users as they type characters in a control.

The getValue method is different from the attribute [getValue](../attributes/getvalue.md) method because the control method retrieves the value from the control as the user is typing in the control as opposed to the attribute getValue method that retrieves the value after the user commits (saves) the field. 

## Syntax

`formContext.getControl(arg).getValue();`

## Return Value

**Type**: String

**Description**:  The latest data value for a control.

