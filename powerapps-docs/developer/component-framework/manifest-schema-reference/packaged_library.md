---
title: Packaged Library Element | Microsoft Docs
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
ms.assetid: 41c50db2-3096-4990-ac2b-e702c161bf4f
---

# packaged_library element

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [packaged_library-description](includes/packaged_library-description.md)]

## Available for

Model-driven apps

## Attributes

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`path`|Place where packaged library files are located|`string`|Yes|Model-driven apps|
|`version`|The current version of the packaged library|`string`|Yes|Model-driven apps|

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

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)
