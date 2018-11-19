---
title: Resx Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 38acfda3-4adc-4aa2-bb8b-f29ba572a6e5
---

# resx element

[!INCLUDE [resx-description](includes/resx-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`path`|Place where resx files are located|`string`|yes|
|`version`|The current version of the resx file|`string`|yes|

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

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
