---
title: openUrl (Power Apps component framework API reference) | Microsoft Docs
description: Opens a url, including file urls.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# openUrl

[!INCLUDE [openurl-description](includes/openurl-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`context.navigation.openUrl(url, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|url|`string`|Yes|Url to be opened.|
|options|`OpenUrlOptions`|No|Options to open the URL. The OpenUrlOptions has the following parameters: <br/>- **height**: `Number`. Height of the window to display the resultant page in pixels.<br/>- **width**: `Number`. Width of the window to display the resultant page in pixels.|


### Related articles

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
