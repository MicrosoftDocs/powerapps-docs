---
title: openUrl | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
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

`openUrl(url, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|url|`string`|yes|Url to be opened.|
|options|`OpenUrlOptions`|yes|Window options for the url. The OpenUrlOptions has the following parameters: <br/>- **height**: `number`. Height of the window to display the resultant page in pixels.<br/>- **width**: `number`. Width of the window to display the resultant page in pixels.|


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)