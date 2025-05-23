---
title: "getViewSelector (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getViewSelector method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getViewSelector (Client API reference)

[!INCLUDE[./includes/getViewSelector-description.md](./includes/getViewSelector-description.md)]

## Grid types supported

Read-only grid

## Syntax

`gridContext.getViewSelector();`

## Return Value

**Type**: [ViewSelector](../viewselector.md)

**Description**: The **ViewSelector** object.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
