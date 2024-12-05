---
title: "GridRow (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the GridRow method.
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
# GridRow (Client API reference)

A collection of GridRow is returned by [Grid](grid.md).[getRows](grid/getRows.md) and [Grid](grid.md).[getSelectedRows](grid/getSelectedRows.md) methods.

```JavaScript
var myRows = gridContext.getGrid().getRows();
var gridRow = myRows.get(arg);
```

## Properties

|Name|Description|Available for|
|--|--|--|
|`data`|An object containing the [GridRowData](gridrowdata.md) for the GridRow.|Read-only and editable grids|


## Methods

|Name|Description|Available for|
|--|--|--|
|[getData](gridrow/getData.md)|[!INCLUDE[gridrow/includes/getData-description.md](gridrow/includes/getData-description.md)]|Read-only and editable grids|

### Related articles

[GridRowData](gridrowdata.md)   
[Grids and subgrids in model-driven apps](../grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
