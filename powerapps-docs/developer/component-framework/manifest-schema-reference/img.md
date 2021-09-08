---
title: Image Element | Microsoft Docs
description: The img web resource allows you to add images for the code components.
keywords:
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 0e776647-a4a2-42c9-85e8-62718154052f
---

# img element

[!INCLUDE [img-description](includes/img-description.md)]

## Available for

Model-driven apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`path`|Relative path w.r.t manifest where the image files are located|`string`|Yes|Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|


### Example

```XML
<resources>
   <code path="index.ts" order="1" />
	  <img path="img/default.png" />
 </resources>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]