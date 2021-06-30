---
title: "isVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isVisible method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d22cd046-064c-47ef-9e46-5cc4c8b6e280
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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