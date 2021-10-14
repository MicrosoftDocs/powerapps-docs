---
title: "getSelectedRows (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getSelectedRows method.
ms.date: 09/22/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 49f39f0f-33ef-41d1-9ab3-14966ae075b5
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
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
