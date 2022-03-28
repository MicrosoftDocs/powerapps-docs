---
title: HTML Element | Microsoft Docs
description: 
keywords:
ms.subservice: pcf
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
---

# html element

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

## Example

```XML
<resources>
   <code path="TS_LocalizationAPI.js" order="1" />
	 <html path="html/default.html" order="1" />
  </resources>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]