---
title: CSS Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
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
|`path`|Place where CSS files are located|`string`|yes|
|`order`|The order in which the webresource must load|`Positive integer`|yes|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Example

```xml
<css path="css/JS_HelloWorldControl.css" order="1" />
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
