---
title: HTML Element | Microsoft Docs
description: Use HTML web resources to create user interface elements for client extensions. 
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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