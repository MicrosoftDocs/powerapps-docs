---
title: "sidePanes (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the sidePanes method.
ms.date: 08/31/2021
ms.service: powerapps
ms.topic: "reference"
author: "aorth"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
---
# sidePanes (Client API reference)

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../../includes/cc-beta-prerelease-disclaimer.md)]

Provides methods for managing side panes.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc-preview-features-definition](../../../../includes/cc-preview-features-definition.md)]

## Methods

|Methods|Description|
|--------|----------|
|[createPane](Xrm-App/Xrm-App-sidePanes/createPane.md)|Add empty pane to SideBar. Need to call `pane.navigateTo()` to load the page.|
|[getAllPanes](Xrm-App/Xrm-App-sidePanes/getAllPanes.md)|Returns a collection containing all active panes.|
|[getSelectedPane](Xrm-App/Xrm-App-sidePanes/getSelectedPane.md)|Returns the current selected pane.|
|[getPane](Xrm-App/Xrm-App-sidePanes/getPane.md)|Returns the pane corresponding to the input ID. If pane doesn't exist, undefined is returned.|

## Parameter

|Parameter Name|Description|
|--------------|-----------|
|state|Returns whether the selected pane is collapsed or expanded.|

### Related topics

[Creating side panes using client API](../create-app-side-panes.md)

