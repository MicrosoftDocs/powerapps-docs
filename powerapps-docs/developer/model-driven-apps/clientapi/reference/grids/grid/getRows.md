---
title: "getRows (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getRows method.
ms.date: 09/22/2021
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
