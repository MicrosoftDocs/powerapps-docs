---
title: Packaged Library Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 41c50db2-3096-4990-ac2b-e702c161bf4f
---

# packaged_library element

[!INCLUDE [packaged_library-description](includes/packaged_library-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`path`|Place where packaged library files are located|`string`|yes|
|`version`|The current version of the packaged library|`string`|yes|

## Parent Elements

|Element|Description|
|--|--|
|[library](library.md)|[!INCLUDE [library-description](includes/library-description.md)]|

## Example

```xml
<resources>
			<library name="AngularJSCore" version=">=1" order="1">
				<packaged_library path="libs/angular.min.js" version="1.5.8" />
			</library>
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
