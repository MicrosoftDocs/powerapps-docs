---
title: openWebResource (Power Apps component framework API reference) | Microsoft Docs
description: Opens a HTML web resource.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# openWebResource

[!INCLUDE [openwebresource-description](includes/openwebresource-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openWebResource(name, options, data)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|name|`String`|Yes|The name of the HTML web resource to open.|
|options|`OpenWebResourceOptions`|No|Window options for opening the web resource. The OpenWebResourceOptions has the following attributes:<br/>- **height**: `Number`. Height of the window to display the resultant page in pixels.<br/>- **width**: `Number`. Width of the window to display the resultant page in pixels.<br/>- **openInNewWindow**: `Boolean`. Indicates whether to open the web resource in a new window.|
|data|`String`|No|Data to be passed into the data parameter.

### Related articles

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
