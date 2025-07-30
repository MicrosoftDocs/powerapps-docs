---
title: "GridRowData (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the GridRowData method.
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
# GridRowData (Client API reference)

GridRowData is returned by the [GridRow](gridrow.md).[getData](gridrow/getData.md) method.

GridRowData also provides methods for retrieving information specific to a record displayed in an editable grid row, including a collection of all the columns included in the row. Column data is limited to the columns presented by the editable grid. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

```JavaScript
var myRows = gridContext.getGrid().getRows();
var myRow = myRows.get(arg);
var gridRowData = myRow.data;
```

## Properties

|Name|Description|Available for|
|--|--|--|
|`entity`|Returns the [GridEntity](gridentity.md) for the GridRowData.|Read-only and editable grids|


## Methods

|Name|Description|Available for|
|--|--|--|
|[getEntity](gridrowdata/getEntity.md)|[!INCLUDE[gridrowdata/includes/getEntity-description.md](gridrowdata/includes/getEntity-description.md)]|Read-only and editable grids|


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
