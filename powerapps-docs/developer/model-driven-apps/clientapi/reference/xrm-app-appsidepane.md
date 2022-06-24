---
title: "AppSidePane (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the AppSidePane method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 04/21/2022
ms.reviewer: jdaly
ms.topic: "reference"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# AppSidePane (Client API reference)

Provides methods for managing a single side pane.

## Methods

|Methods|Description|
|--------|----------|
|close|Closes the side pane and removes it from the side bar.|
|select|Specify whether the pane should be selected or expanded.|
|navigate|Opens a page within the selected pane. This is similar to the [navigateTo](Xrm-Navigation/navigateTo.md) method.|

### Parameters

|Parameter Name| Type| Required|Description|
|-------------|------|---------|------------|
|title|string|No|The title of the pane. Used in pane header and for tooltip.|
|paneId|string|No| The ID of the new pane. If the value is not passed, the ID value is auto-generated.|
|canClose|Boolean|No| Whether the pane header will show a close button or not.|
|imageSrc|string|No| The path of the icon to show in the panel switcher control.|
|width|Number|No| The width of the pane in pixels.|
|hidden|Boolean|No| Hides the pane and tab.|
|alwaysRender|Boolean| No|Prevents the pane from unmounting when it is hidden.|
|keepBadgeOnSelect|Boolean|No| Prevents the badge from getting cleared when the pane becomes selected.|


### Related topics

[Creating side panes using client API](../create-app-side-panes.md)
