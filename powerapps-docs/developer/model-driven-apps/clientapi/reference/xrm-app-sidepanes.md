---
title: "sidePanes (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the sidePanes method.
author: adrianorth
ms.author: aorth
ms.date: 04/04/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# sidePanes (Client API reference)

Provides methods for managing side panes.

## Methods

|Methods|Description|
|--------|----------|
|[createPane](Xrm-App/Xrm-App-sidePanes/createPane.md)|Add empty pane to sidePanes collection. Need to call `pane.navigateTo()` to load the page.|
|[getAllPanes](Xrm-App/Xrm-App-sidePanes/getAllPanes.md)|Returns a collection containing all active panes.|
|[getSelectedPane](Xrm-App/Xrm-App-sidePanes/getSelectedPane.md)|Returns the current selected pane.|
|[getPane](Xrm-App/Xrm-App-sidePanes/getPane.md)|Returns the pane corresponding to the input ID. If pane doesn't exist, undefined is returned.|

## Parameter

|Parameter Name|Description|
|--------------|-----------|
|state|Returns whether the selected pane is collapsed or expanded.|

### Related topics

[Creating side panes using client API](../create-app-side-panes.md)

