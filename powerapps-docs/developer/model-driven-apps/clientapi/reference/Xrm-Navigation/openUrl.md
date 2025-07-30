---
title: "openUrl (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the openUrl method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# openUrl (Client API reference)



[!INCLUDE[./includes/openUrl-description.md](./includes/openUrl-description.md)]

## Syntax

`Xrm.Navigation.openUrl(url,openUrlOptions)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|`url`|String|Yes|URL to open.|
|`openUrlOptions`|Object|No|Options to open the URL.The object contains the following values:<br/>- **`height`**: (Optional) Number. Height of the window to display the resultant page in pixels.<br/>- **`width`**: (Optional) Number. Width of the window to display the resultant page in pixels.|

## Remarks

This method is especially helpful for mobile clients to open a URL in a browser outside of shim.

 ### Related articles

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
