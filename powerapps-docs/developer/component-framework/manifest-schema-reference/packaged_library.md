---
title: Packaged Library Element | Microsoft Docs
description: 
keywords:
ms.subservice: pcf
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly
ms.topic: "reference"
---

# packaged_library element

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

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]