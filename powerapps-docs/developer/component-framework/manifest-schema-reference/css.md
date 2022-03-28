---
title: CSS Element | Microsoft Docs
description: CSS describes how code components are to be displayed on UI.
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

# css element

[!INCLUDE [css-description](includes/css-description.md)]

## Available for

Model-driven and canvas apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-----|
|`path`|Relative path w.r.t manifest where CSS files are located|`string`|Yes|Model-driven and canvas apps |
|`order`|The order in which the CSS files Should load|`Positive integer`|Optional|Model-driven and canvas apps |

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Example

```xml
<resources>
  <code path="TS_LocalizationAPI.js" order="1" />
	<css path="css/TS_LocalizationAPI.css" order="1" />
 </resources>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]