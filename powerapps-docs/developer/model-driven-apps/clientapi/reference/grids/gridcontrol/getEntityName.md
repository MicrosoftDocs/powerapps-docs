---
title: "gridContext.getEntityName (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the gridContext.getEntityName method.
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
# gridContext.getEntityName (Client API reference)

[!INCLUDE[./includes/getEntityName-description.md](./includes/getEntityName-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.getEntityName();`

## Return Value

**Type**: String

**Description**: The logical name of the table data displayed in the grid.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext). 

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
