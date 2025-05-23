---
title: "GridControl (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the GridControl method.
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
# GridControl (Client API reference)

GridControl or the gridContext is the instance of grid or subgrid on a form against which you want to execute your script. Use the form context to get GridControl [(gridContext)](../grids.md#bkmk_gridcontext) on a form.

## Methods for grids

|Name|Description|Available for|
|--|--|--|
|[addOnLoad](gridcontrol/addOnLoad.md)|[!INCLUDE[gridcontrol/includes/addOnLoad-description.md](gridcontrol/includes/addOnLoad-description.md)]|Read-only grid|
|[getEntityName](gridcontrol/getEntityName.md)|[!INCLUDE[gridcontrol/includes/getEntityName-description.md](gridcontrol/includes/getEntityName-description.md)]|Read-only and editable grids|
|[getFetchXml](gridcontrol/getFetchXml.md)|[!INCLUDE[gridcontrol/includes/getFetchXml-description.md](gridcontrol/includes/getFetchXml-description.md)]|Read-only and editable grids|
|[getGrid](gridcontrol/getGrid.md)|[!INCLUDE[gridcontrol/includes/getGrid-description.md](gridcontrol/includes/getGrid-description.md)]|Read-only and editable grids|
|[getGridType](gridcontrol/getGridType.md)|[!INCLUDE[gridcontrol/includes/getGridType-description.md](gridcontrol/includes/getGridType-description.md)]|Read-only and editable grids|
|[getRelationship](gridcontrol/getRelationship.md)|[!INCLUDE[gridcontrol/includes/getRelationship-description.md](gridcontrol/includes/getRelationship-description.md)]|Read-only and editable grids|
|[getUrl](gridcontrol/getUrl.md)|[!INCLUDE[gridcontrol/includes/getUrl-description.md](gridcontrol/includes/getUrl-description.md)]|Read-only and editable grids|
|[getViewSelector](gridcontrol/getViewSelector.md)|[!INCLUDE[gridcontrol/includes/getViewSelector-description.md](gridcontrol/includes/getViewSelector-description.md)]|Read-only grid|
|[openRelatedGrid](gridcontrol/openRelatedGrid.md)|[!INCLUDE[gridcontrol/includes/openRelatedGrid-description.md](gridcontrol/includes/openRelatedGrid-description.md)]|Read-only and editable grids|
|[refresh](gridcontrol/refresh.md)|[!INCLUDE[gridcontrol/includes/refresh-description.md](gridcontrol/includes/refresh-description.md)]|Read-only and editable grids|
|[refreshRibbon](gridcontrol/refreshRibbon.md)|[!INCLUDE[gridcontrol/includes/refreshRibbon-description.md](gridcontrol/includes/refreshRibbon-description.md)]|Read-only and editable grids|
|[removeOnLoad](gridcontrol/removeOnLoad.md)|[!INCLUDE[gridcontrol/includes/removeOnLoad-description.md](gridcontrol/includes/removeOnLoad-description.md)]|Read-only grid|

## Additional methods for subgrids

Along with the methods mentioned above, subgrid also have the following methods:

|Name|Description|Available for|
|--|--|--|
|[getControlType](../controls/getControlType.md)|Returns a value that categorizes controls.|Read-only and editable grids|
|[getDisabled](../controls/getDisabled.md)|Returns whether the control is disabled.|Read-only and editable grids|
|[getName](../controls/getName.md)|Returns the name assigned to the control.|Read-only and editable grids|
|[getParent](../controls/getParent.md)|Returns a reference to the section object that contains the control.|Read-only and editable grids|
|[getVisible](../controls/getVisible.md)|Returns a value that indicates whether the control is currently visible.|Read-only and editable grids|
|[setDisabled](../controls/setDisabled.md)|Sets whether the control is disabled.|Read-only and editable grids|
|[setFocus](../controls/setFocus.md)|Sets the focus on the control.|Read-only and editable grids|
|[setVisible](../controls/setVisible.md)|Sets a value that indicates whether the control is visible.|Read-only and editable grids|

### Related articles

[Grid](grid.md)   
[Grids and subgrids in model-driven apps](../grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
