---
title: "ViewSelector methods (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the ViewSelector method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 37fbabaf-e2ce-4e46-a54e-e46bd884197b
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ViewSelector methods (Client API reference)



Provides methods to get or set information about the view selector of the subgrid control. If the subgrid control is not configured to display the view selector, calling the **ViewSelector** methods will throw an error.

ViewSelector is returned by the **gridContext**.[getViewSelector](gridcontrol/getViewSelector.md) method.

```JavaScript
var viewSelector = gridContext.getViewSelector();
```

Methods

|Name|Description|Available for|
|--|--|--|
|[getCurrentView](viewselector/getCurrentView.md)|[!INCLUDE[viewselector/includes/getCurrentView-description.md](viewselector/includes/getCurrentView-description.md)]|Read-only grid|
|[isVisible](viewselector/isVisible.md)|[!INCLUDE[viewselector/includes/isVisible-description.md](viewselector/includes/isVisible-description.md)]|Read-only grid|
|[setCurrentView](viewselector/setCurrentView.md)|[!INCLUDE[viewselector/includes/setCurrentView-description.md](viewselector/includes/setCurrentView-description.md)]|Read-only grid|


### Related topics

[gridContext](../grids.md#bkmk_gridcontext)

[Grids and subgrids in model-driven apps](../grids.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]