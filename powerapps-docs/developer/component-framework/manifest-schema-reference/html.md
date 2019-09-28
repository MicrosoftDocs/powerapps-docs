---
title: HTML Element | Microsoft Docs
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
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: dcb8e71d-9a2f-4789-9a84-34673ccfd5c1
---

# html element

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [html-description](includes/html-description.md)]

## Available for

Model-driven apps

## Attributes

|Name|Description|Type|Required|Available for|
|--|--|--|--|----------|
|`path`|Relative path w.r.t manifest where HTML files are located|`string`|Yes|Model-driven apps|
|`order`|The order in which HTML files should load|`Positive integer`|Optional|Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

### Related topics

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)