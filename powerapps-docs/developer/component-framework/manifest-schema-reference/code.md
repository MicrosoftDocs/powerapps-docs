---
title: Code Element | Microsoft Docs
description: Refers to the path where the resource files are located.
keywords:
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 44d9fcfb-0cd8-48cc-aace-dd589099dd79
---

# code element

[!INCLUDE [code-description](includes/code-description.md)]

## Available for

Model-driven and canvas apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-----|
|`path`|Place where the resource files are located|`String`|Yes|Model-driven and canvas apps |
|`order`|The order in which the resource files should load|`Positive integer`|Yes|Model-driven and canvas apps |

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

### Example

```XML
<code path="TS_IncrementControl.js" order="1" />
	    <css path="css/TS_IncrementControl.css" order="1" />
      <resx path="strings/TSIncrementControl.1033.resx" version="1.0.0" />
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]