---
title: Resx Element | Microsoft Docs
description: The resx web resource is used to manage the localized strings you define.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# resx element

[!INCLUDE [resx-description](includes/resx-description.md)]

## Available for

Model-driven and canvas apps

## Parameters

|Name|Description|Type|Required|
|--|--|--|--|
|`path`|Relative path w.r.t manifest where resx files are located|`string`|Yes|
|`version`|The current version of the resx file|`string`|Yes|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

## Example

```xml
<resources>
      <code path="TS_LocalizationAPI.js" order="1" />
       <css path="css/TS_LocalizationAPI.css" order="1" />
      <resx path="strings/TSLocalizationAPI.1033.resx" version="1.0.0" />
      <resx path="strings/TSLocalizationAPI.1035.resx" version="1.0.0" />
      <resx path="strings/TSLocalizationAPI.3082.resx" version="1.0.0" />
    </resources>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
