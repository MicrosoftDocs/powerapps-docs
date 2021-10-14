---
title: "GridRow (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the GridRow method.
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
# GridRow (Client API reference)



A collection of GridRow is returned by [Grid](grid.md).[getRows](grid/getRows.md) and [Grid](grid.md).[getSelectedRows](grid/getSelectedRows.md) methods.

```JavaScript
var myRows = gridContext.getGrid().getRows();
var gridRow = myRows.get(arg);
```

## Properties

|Name|Description|Available for|
|--|--|--|
|data|An object containing the [GridRowData](gridrowdata.md) for the GridRow.|Read-only and editable grids|


## Methods

|Name|Description|Available for|
|--|--|--|
|[getData](gridrow/getData.md)|[!INCLUDE[gridrow/includes/getData-description.md](gridrow/includes/getData-description.md)]|Read-only and editable grids|

### Related topics

[GridRowData](gridrowdata.md)

[Grids and subgrids in model-driven apps](../grids.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]