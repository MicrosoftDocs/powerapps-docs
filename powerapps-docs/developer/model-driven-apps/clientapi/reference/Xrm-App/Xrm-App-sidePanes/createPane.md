---
title: "createPane (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the createPane method.
author: adrianorth
ms.author: aorth
ms.date: 04/04/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# createPane (Client API reference)

Provides all the information to create side panes.

## Syntax

`Xrm.App.sidePanes.createPane(paneOptions);`

## paneOptions object

The `paneOptions` object has the following values:

|Parameter Name| Type| Required|Description|
|-------------|------|---------|------------|
|`title`|string|No|The title of the pane. Used in pane header and for tooltip.|
|`paneId`|string|No| The ID of the new pane. If the value is not passed, the ID value is auto-generated.|
|`canClose`|Boolean|No| Whether the pane header will show a close button or not.|
|`imageSrc`|string|No| The path of the icon to show in the panel switcher control.|
|`hideHeader`|Boolean|No| Hides the header pane, including the title and close button. Default value is false.|
|`isSelected`|Boolean|No| When set to false, the created pane is not selected and leaves the existing pane selected. It also does not expand the pane if collapsed.|
|`width`|Number|No| The width of the pane in pixels.|
|`hidden`|Boolean|No| Hides the pane and tab.|
|`alwaysRender`|Boolean| No|Prevents the pane from unmounting when it is hidden.|
|`keepBadgeOnSelect`|Boolean|No| Prevents the badge from getting cleared when the pane becomes selected.|


### Related articles

[sidePanes](../../xrm-app-sidepanes.md)

[Creating side panes using client API](../../../create-app-side-panes.md)
