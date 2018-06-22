---
title: "GridAttribute (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/10/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8139c622-e4d9-478f-9510-414d140e5556
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# GridAttribute (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

GridAttribute is only supported for editable grids.

GridAttribute represents the data in the cell of an editable grid, and contains a reference to all the cells associated with the attribute. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

GridAttribute also supports the **controls** collection for attributes of a selected grid row, which provides methods to work with a collection of cells associated with the attribute. Each cell ([GridCell](gridcell.md)) of a selected grid row is analogous to a control on a form that is tied to an attribute in an editable grid. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

>[!TIP]
>For performance reasons, a row (record) in an editable grid is not editable until the record is selected. Users must select a single record in a grid to edit it. Once a record is selected in an editable grid, Dynamics 365 internally evaluates a number of things including user access to the record, whether the record is active, and field validations to ensure that data security and validity are honored when you edit data. Consider using the [OnRecordSelect](../events/grid-onrecordselect.md) event with the [getFormContext](../executioncontext/getFormContext.md) method to access records in the grid that are in the editable state.

## Methods

GridAttribute supports the following methods for attributes of a selected grid row.

|Name|Description|
|--|--|
|[getName](../attributes/getName.md)|Returns the logical name of the attribute of a selected grid row.|
|[getRequiredLevel](../attributes/getRequiredLevel.md)| Returns a string value indicating whether a value for the attribute is required or recommended.|
|[setRequiredLevel](../attributes/setRequiredLevel.md)| Sets whether data is required or recommended for the attribute of a selected grid row before the record can be saved.|
|[getValue](../attributes/getValue.md)| Retrieves the data value for an attribute.|
|[setValue](../attributes/setValue.md)| Sets the data value for an attribute.|

>[!NOTE]
>To select a row in an editable grid, use the [Grid](grid.md).[getSelectedRows](grid/getSelectedRows.md)

### Related topics

[GridCell](gridcell.md)

[Grids and subgrids in Customer Engagement](../grids.md)

[Controls collection](../attributes/controls-collection.md)


