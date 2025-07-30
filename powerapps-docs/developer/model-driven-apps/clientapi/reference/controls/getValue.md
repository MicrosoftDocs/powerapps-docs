---
title: "control.getValue (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getValue method.
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
# control.getValue (Client API reference)

Gets the latest value in a control as the user types characters in a specific text or number column. This method helps you to build interactive experiences by validating data and alerting users as they type characters in a control.

The `getValue` method is different from the column [getValue](../attributes/getvalue.md) method because the control method retrieves the value from the control as the user is typing in the control as opposed to the column `getValue` method that retrieves the value after the user commits (saves) the column. 

## Syntax

`formContext.getControl(arg).getValue();`

## Return Value

**Type**: String

**Description**:  The latest data value for a control.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
