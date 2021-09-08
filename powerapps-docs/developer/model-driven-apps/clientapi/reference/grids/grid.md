---
title: "Grid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the grid method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 02fef0b4-b895-4277-b604-3f525c29dca3
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Grid (Client API reference)



Grid is returned by the **gridContext**.[getGrid](gridcontrol/getGrid.md) method. Use Grid methods to access information about data in the grid.

`var myGrid = gridContext.getGrid();`

## Methods

|Name|Description|Available for|
|--|--|--|
|[getRows](grid/getRows.md)|[!INCLUDE[grid/includes/getRows-description.md](grid/includes/getRows-description.md)]|Read-only and editable grids|
|[getSelectedRows](grid/getSelectedRows.md)|[!INCLUDE[grid/includes/getSelectedRows-description.md](grid/includes/getSelectedRows-description.md)]|Read-only and editable grids|
|[getTotalRecordCount](grid/getTotalRecordCount.md)|[!INCLUDE[grid/includes/getTotalRecordCount-description.md](grid/includes/getTotalRecordCount-description.md)]|Read-only and editable grids|

### Related topics

[GridRow](gridrow.md)

[Grids and subgrids in model-driven apps](../grids.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]