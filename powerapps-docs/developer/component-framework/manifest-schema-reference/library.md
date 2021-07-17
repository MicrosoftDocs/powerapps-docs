---
title: Library Element | Microsoft Docs
description: 
keywords:
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 90f2b4c9-7396-4ab9-bc9f-810189dc18b7
---

# library element

[!INCLUDE [library-description](includes/library-description.md)]

## Parameters

|Name|Description|Type|Required|
|--|--|--|--|
|`name`|Name of the library|`string`|Yes|
|`version`|The current library version|Positive integer|Yes|
|`order`|The order in which the library files should load|Positive integer|Yes|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[packaged_library]||0 or more|

## Example

```xml
<resources>
<library name="AngularJSCore" version=">=1" order="1">
<packaged_library path="libs/angular.min.js" version="1.5.8" />
</library>
  </resources>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]