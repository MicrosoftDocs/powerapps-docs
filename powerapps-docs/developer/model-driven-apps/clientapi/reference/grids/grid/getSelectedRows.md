---
title: "getSelectedRows (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getSelectedRows method.
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

# getSelectedRows (Client API reference)

[!INCLUDE[./includes/getSelectedRows-description.md](./includes/getSelectedRows-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`let allSelectedRows = gridContext.getGrid().getSelectedRows();`

## Return Value

**Type**: [Collection](./../../collections.md)

**Description**: A collection of selected rows in the grid.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

See [Collections (Client API reference)](../../collections.md) for information on the methods available to access data in a collection.

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
