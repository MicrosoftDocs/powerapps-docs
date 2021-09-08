---
title: "GridAttribute (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the GridAttribute method.
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
# GridAttribute (Client API reference)



GridAttribute is supported for both read-only and editable grids.

GridAttribute represents the data in the cell of an editable grid, and contains a reference to all the cells associated with the column. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

GridAttribute also supports the **controls** collection for columns of a selected grid row, which provides methods to work with a collection of cells associated with the column. Each cell ([GridCell](gridcell.md)) of a selected grid row is analogous to a control on a form that is tied to a column in an editable grid. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

>[!TIP]
>For performance reasons, a row (record) in an editable grid is not editable until the record is selected. Users must select a single record in a grid to edit it. Once a record is selected in an editable grid, Dynamics 365 internally evaluates a number of things including user access to the record, whether the record is active, and column validations to ensure that data security and validity are honored when you edit data. Consider using the [OnRecordSelect](../events/grid-onrecordselect.md) event with the [getFormContext](../executioncontext/getFormContext.md) method to access records in the grid that are in the editable state.

## Methods

GridAttribute supports the following methods for columns of a selected grid row.

|Name|Description|
|--|--|
|[getName](../attributes/getName.md)|Returns the logical name of the column of a selected grid row.|
|[getRequiredLevel](../attributes/getRequiredLevel.md)| Returns a string value indicating whether a value for the column is required or recommended.|
|[setRequiredLevel](../attributes/setRequiredLevel.md)| Sets whether data is required or recommended for the column of a selected grid row before the record can be saved.|
|[getValue](../attributes/getValue.md)| Retrieves the data value for a column.|
|[setValue](../attributes/setValue.md)| Sets the data value for a column.|

>[!NOTE]
>To select a row in an editable grid, use the [Grid](grid.md).[getSelectedRows](grid/getSelectedRows.md)

### Related topics

[GridCell](gridcell.md)

[Grids and subgrids in model-driven apps](../grids.md)

[Controls collection](../attributes/controls-collection.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
