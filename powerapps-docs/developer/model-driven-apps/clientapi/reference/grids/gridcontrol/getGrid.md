---
title: "getGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGrid method.
ms.date: 04/21/2021
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
# getGrid (Client API reference)



[!INCLUDE[./includes/getGrid-description.md](./includes/getGrid-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`var grid = gridContext.getGrid();`

## Return Value

**Type**: [Grid](../grid.md)

**Description**: The **Grid** object.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext). 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]