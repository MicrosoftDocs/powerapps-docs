---
title: "getTotalRecordCount (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getTotalRecordCount method.
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

# getTotalRecordCount (Client API reference)

[!INCLUDE[./includes/getTotalRecordCount-description.md](./includes/getTotalRecordCount-description.md)]

- When the Dynamics 365 for Outlook client isn't connected to the server, this number is limited to those records that the user has selected to take offline.
- For Dynamics 365 mobile clients, this method will return the number of records in the subgrid.

## Grid types supported

Read-only and editable grids

## Syntax

`let filteredRecordCount = gridContext.getGrid().getTotalRecordCount();`

## Return Value

**Type**: Number

**Description**: Total number of records that match the filter criteria of the view.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

See [Collections (Client API reference)](../../collections.md) for information on the methods available to access data in a collection.

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
