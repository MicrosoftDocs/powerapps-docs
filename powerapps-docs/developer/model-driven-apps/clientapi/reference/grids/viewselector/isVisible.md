---
title: "isVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isVisible method.
author: adrianorth
ms.author: aorth
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
# isVisible (Client API reference)



[!INCLUDE[./includes/isVisible-description.md](./includes/isVisible-description.md)]

## Grid types supported

Read-only grid

## Syntax

`viewSelector.isVisible();`

## Return Value

**Type**: Boolean

**Description**: true if visible; false otherwise.

## Remarks

If the subgrid control is not configured to display the view selector, calling this method on the **ViewSelector** returned by the GridControl.getViewSelector method will throw an error.

To get the `viewSelector` object, see [ViewSelector](../viewselector.md).





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]