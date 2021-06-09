---
title: "GridRowData (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the GridRowData method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8139c622-e4d9-478f-9510-414d140e5556
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
|entity|Returns the [GridEntity](gridentity.md) for the GridRowData.|Read-only and editable grids|


## Methods

|Name|Description|Available for|
|--|--|--|
|[getEntity](gridrowdata/getEntity.md)|[!INCLUDE[gridrowdata/includes/getEntity-description.md](gridrowdata/includes/getEntity-description.md)]|Read-only and editable grids|




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
