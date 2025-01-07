---
title: "loadPanel"
description: Includes description and supported parameters for the loadPanel method.
ms.date: 04/17/2022
ms.service: powerapps
ms.topic: reference
applies_to: "Dynamics 365 (online)"
author: sriharibs-msft
ms.author: srihas
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# loadPanel (Client-side reference)

[!INCLUDE[./includes/loadPanel-description.md](./includes/loadPanel-description.md)]


## Syntax

`Xrm.Panel.loadPanel(url, title)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|`url` |String | Yes|URL of the page to be loaded in the side pane static area.|
|`title` |String | Yes|Title of the side pane static area. |


## Remarks

This API is being replaced with Xrm.App.sidePanes.createPane.  See [Use with Xrm.App.panels.loadPanel](../../create-app-side-panes.md#use-with-xrmapppanelsloadpanel) for more details on the interaction of `loadPanel` and `createPane`.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
