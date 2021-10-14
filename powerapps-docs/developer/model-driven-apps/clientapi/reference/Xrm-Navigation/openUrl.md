---
title: "openUrl (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openUrl method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 29cb3685-21aa-42fc-8e84-0074dcc69197
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# openUrl (Client API reference)



[!INCLUDE[./includes/openUrl-description.md](./includes/openUrl-description.md)]

## Syntax

`Xrm.Navigation.openUrl(url,openUrlOptions)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|url|String|Yes|URL to open.|
|openUrlOptions|Object|No|Options to open the URL.The object contains the following values:<br/>- **height**: (Optional) Number. Height of the window to display the resultant page in pixels.<br/>- **width**: (Optional) Number. Width of the window to display the resultant page in pixels.|

## Remarks

This method is especially helpful for mobile clients to open a URL in a browser outside of shim.

 ### Related topics

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]