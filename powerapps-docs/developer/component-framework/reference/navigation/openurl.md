---
title: openUrl | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 590078f3-c604-4bd0-ac74-9cf6d8806802

---

# openUrl

[!INCLUDE [openurl-description](includes/openurl-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openUrl(url, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|url|`string`|Yes|Url to be opened.|
|options|`OpenUrlOptions`|No|Options to open the URL. The OpenUrlOptions has the following parameters: <br/>- **height**: `Number`. Height of the window to display the resultant page in pixels.<br/>- **width**: `Number`. Width of the window to display the resultant page in pixels.|


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)