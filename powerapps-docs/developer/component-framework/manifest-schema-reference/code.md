---
title: Code Element | Microsoft Docs
description: Refers to the path where the resource files are located.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
