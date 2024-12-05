---
title: "getRows (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getRows method.
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

# getRows (Client API reference)

[!INCLUDE[./includes/getRows-description.md](./includes/getRows-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`let allRows = gridContext.getGrid().getRows();`

## Return Value

**Type**: [Collection](./../../collections.md)

**Description**: A collection of rows in the grid.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

See [Collections (Client API reference)](../../collections.md) for information on the methods available to access data in a collection.

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
