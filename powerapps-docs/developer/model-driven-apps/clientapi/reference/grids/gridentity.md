---
title: "GridEntity (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the GridEntity method.
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
# GridEntity (Client API reference)

GridEntity is returned by the [GridRowData](gridrowdata.md).[getEntity](gridrowdata/getEntity.md) method or by directly accessing the [GridRowData](gridrowdata.md).**entity** object. Use the GridEntity methods to access data about the specific records in the rows.

```JavaScript
var myRows = gridContext.getGrid().getRows();
var myRow = myRows.get(arg);
var gridEntity = myRow.data.entity;
```

GridEntity also supports the **columns** collection that provides methods of working with a collection of columns for a table in the editable grid. Each column ([GridAttribute](gridattribute.md)) represents the data in the cell of an editable grid, and contains a reference to all the cells associated with the column. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

## Methods

|Name|Description|Available for|
|--|--|--|
|[getEntityName](gridentity/getEntityName.md)|[!INCLUDE[gridentity/includes/getEntityName-description.md](gridentity/includes/getEntityName-description.md)]|Read-only and editable grids|
|[getEntityReference](gridentity/getEntityReference.md)|[!INCLUDE[gridentity/includes/getEntityReference-description.md](gridentity/includes/getEntityReference-description.md)]|Read-only and editable grids|
|[getId](gridentity/getId.md)|[!INCLUDE[gridentity/includes/getId-description.md](gridentity/includes/getId-description.md)]|Read-only and editable grids|
|[getPrimaryAttributeValue](gridentity/getPrimaryAttributeValue.md)|[!INCLUDE[gridentity/includes/getPrimaryAttributeValue-description.md](gridentity/includes/getPrimaryAttributeValue-description.md)]|Read-only grid|

### Related articles

[GridAttribute](gridattribute.md)   
[Grids and subgrids in model-driven apps](../grids.md)   
[Columns](../attributes.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
