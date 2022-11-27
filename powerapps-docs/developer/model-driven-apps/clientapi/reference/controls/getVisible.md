---
title: "control.getVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the control.getVisible method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 11/27/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# control.getVisible (Client API reference)

Returns a value that indicates whether the control is currently visible.

> [!NOTE]
> `getVisible` only returns whether the control is configured to be visible. `getVisible` will return true when the control is within a section or tab that is hidden.

## Control types supported

All

## Syntax

`formContext.getControl(arg).getVisible();`

## Return Value

**Type**: Boolean.

**Description**: true if the control is visible; false otherwise.

### Related topics

[setVisible](setVisible.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]