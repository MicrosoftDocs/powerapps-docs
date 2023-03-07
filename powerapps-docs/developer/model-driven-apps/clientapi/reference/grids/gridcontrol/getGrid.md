---
title: "getGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGrid method.
author: jasongre
ms.author: jasongre
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

# getGrid (Client API reference)

[!INCLUDE[./includes/getGrid-description.md](./includes/getGrid-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`let grid = gridContext.getGrid();`

## Return Value

**Type**: [Grid](../grid.md)

**Description**: The **Grid** object.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
