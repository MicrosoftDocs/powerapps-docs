---
title: "GridRow (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 02fef0b4-b895-4277-b604-3f525c29dca3
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
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


