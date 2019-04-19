---
title: CSS Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
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

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`path`|Place where CSS files are located|`string`|Yes|
|`order`|The order in which the webresource must load|`Positive integer`|Optional|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Example

```xml
<css path="css/JS_HelloWorldControl.css" order="1" />
```

### Related topics

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)
