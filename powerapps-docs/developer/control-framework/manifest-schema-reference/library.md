---
title: Library Element | Microsoft Docs
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
ms.assetid: 90f2b4c9-7396-4ab9-bc9f-810189dc18b7
---

# library element

[!INCLUDE [library-description](includes/library-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`name`|Name of the library|`string`|yes|
|`version`|The current library version|Positive integer|yes|
|`order`|The order in which the library files must load|Positive integer|yes|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[packaged_library](packaged_library.md)|[!INCLUDE [packaged_library-description](includes/packaged_library-description.md)]|0 or more|

## Example

```xml
<resources>
<library name="AngularJSCore" version=">=1" order="1">
<packaged_library path="libs/angular.min.js" version="1.5.8" />
</library>
  </resources>
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
