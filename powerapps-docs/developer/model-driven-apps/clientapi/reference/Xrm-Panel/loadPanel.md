---
title: "loadPanel| MicrosoftDocs"
description: Includes description and supported parameters for the loadPanel method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5bc5295b-0232-4d1b-8583-f20417571c1f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# loadPanel (Client-side reference)



[!INCLUDE[./includes/loadPanel-description.md](./includes/loadPanel-description.md)]


## Syntax

`Xrm.Panel.loadPanel(url, title)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|url |String | Yes|URL of the page to be loaded in the side pane static area.|
|title |String | Yes|Title of the side pane static area. |


## Remarks
This API is being replaced with Xrm.App.sidePanes.createPane.  See [Create side panes working with loadPanel](../../create-app-side-panes#use-with-xrmapppanelsloadpanel.md) for more details on the interaction of loadPanel and createPane. 



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]