---
title: CSS Element | Microsoft Docs
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
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: b6119424-c0a4-4412-b25c-8239da6cbe36
---

# css element

[!INCLUDE [css-description](includes/css-description.md)]

## Available for

Model-driven apps and canvas apps (experimental preview)

## Attributes

|Name|Description|Type|Required|Available for|
|--|--|--|--|-----|
|`path`|Relative path w.r.t manifest where CSS files are located|`string`|Yes|Model-driven apps and canvas apps (experimental preview) |
|`order`|The order in which the CSS files Should load|`Positive integer`|Optional|Model-driven apps and canvas apps (experimental preview) |

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Example

```xml
<css path="css/JS_HelloWorldControl.css" order="1" />
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)
