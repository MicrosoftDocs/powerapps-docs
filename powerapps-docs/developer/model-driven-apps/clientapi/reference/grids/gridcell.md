---
title: "GridCell (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the GridCell method.
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
# GridCell (Client API reference)

GridCell is only supported for editable grids.

GridCell of a selected grid row is analogous to a control on a form that is tied to a column in an editable grid. See [Collections (Client API reference)](../collections.md) for information on the methods available to access data in a collection.

## Methods

GridCell supports the following methods.

|Name |Description |
|--|--|
|[clearNotification](../controls/clearNotification.md)| Clears notification for a cell.|
|[getDisabled](../controls/getDisabled.md)| Returns whether the cell is disabled (read-only).|
|[setDisabled](../controls/setDisabled.md)| Sets whether the cell is disabled.<br/><br/>**NOTE**: Enabling a read-only cell for editing can cause an error when the record is saved. If the column is considered read-only by the server, an error may occur if the value is modified. This may happen in scenarios where the user doesn't have write privileges to the record, the record is disabled, or the user doesn't have the necessary field-level security privileges.| 
|[setNotification](../controls/setNotification.md)|Displays an error message for a cell to indicate that data isn't valid.|
|[getLabel](../controls/getLabel.md)|Returns the label of the column that contains the cell.|


### Related articles

[Grids and subgrids in model-driven apps](../grids.md)   
[Controls](../controls.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
