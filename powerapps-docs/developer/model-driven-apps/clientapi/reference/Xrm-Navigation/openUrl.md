---
title: "openUrl (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 29cb3685-21aa-42fc-8e84-0074dcc69197
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# openUrl (Client API reference)



[!INCLUDE[./includes/openUrl-description.md](./includes/openUrl-description.md)]

## Syntax

`Xrm.Navigation.openUrl(url,openUrlOptions)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|url|String|Yes|URL to open.|
|openUrlOptions|Object|No|Options to open the URL.The object contains the following attributes:<br/>- **height**: (Optional) Number. Height of the window to display the resultant page in pixels.<br/>- **width**: (Optional) Number. Width of the window to display the resultant page in pixels.|

## Remarks

This method is especially helpful for mobile clients to open a URL in a browser outside of shim.

 ### Related topics

[Xrm.Navigation](../xrm-navigation.md)

