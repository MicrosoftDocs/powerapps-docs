---
title: "Grid (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the grid method.
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

# Grid (Client API reference)

Grid is returned by the [getGrid](gridcontrol/getGrid.md) method. Use Grid methods to access information about data in the grid.

`let myGrid = gridContext.getGrid();`

## Methods

|Name|Description|Available for|
|---|---|---|
|[getRows](grid/getRows.md)| [!INCLUDE[grid/includes/getRows-description.md](grid/includes/getRows-description.md)]| Read-only and editable grids|
|[getSelectedRows](grid/getSelectedRows.md)| [!INCLUDE[grid/includes/getSelectedRows-description.md](grid/includes/getSelectedRows-description.md)]| Read-only and editable grids |
|[getTotalRecordCount](grid/getTotalRecordCount.md) | [!INCLUDE[grid/includes/getTotalRecordCount-description.md](grid/includes/getTotalRecordCount-description.md)] | Read-only and editable grids |

### Related articles

[GridRow](gridrow.md)   
[Grids and subgrids in model-driven apps](../grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
