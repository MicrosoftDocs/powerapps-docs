---
title: "getGridType (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getGridType method.
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

# getGridType (Client API reference)

[!INCLUDE[./includes/getGridType-description.md](./includes/getGridType-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`let gridType = gridContext.getGridType();`

## Return Value

**Type**: Number

**Description**: Returns one of the following values:

| Value | Description  |
| ----- | ------------ |
| 1     | HomePageGrid |
| 2     | Subgrid      |

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
