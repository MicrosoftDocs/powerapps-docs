---
title: Resx Element | Microsoft Docs
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
ms.assetid: 38acfda3-4adc-4aa2-bb8b-f29ba572a6e5
---

# resx element

[!INCLUDE [resx-description](includes/resx-description.md)]

## Available for

Model-driven apps and canvas apps (experimental preview)

## Attributes

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

### Related topics

[PowerApps component framework Manifest Schema reference](index.md)<br/>
[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework overview](../overview.md)
