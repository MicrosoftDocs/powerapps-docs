---
title: "GridRowData (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/10/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8139c622-e4d9-478f-9510-414d140e5556
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# GridRowData (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

GridRowData is returned by the [GridRow](gridrow.md).[getData](gridrow/getData.md) method.

GridRowData also provides methods for retrieving information specific to a record displayed in an editable grid row, including a collection of all the attributes included in the row. Attribute data is limited to the columns presented by the editable grid. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

```JavaScript
var myRows = gridContext.getGrid().getRows();
var myRow = myRows.get(arg);
var gridRowData = myRow.getData();
```

## Properties

|Name|Description|Available for|
|--|--|--|
|entity|Returns the [GridEntity](gridentity.md) for the GridRowData.|Read-only and editable grids|


## Methods

|Name|Description|Available for|
|--|--|--|
|[getEntity](gridrowdata/getEntity.md)|[!INCLUDE[gridrowdata/includes/getEntity-description.md](gridrowdata/includes/getEntity-description.md)]|Read-only and editable grids|


