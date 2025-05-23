---
title: Image Element | Microsoft Docs
description: The img web resource allows you to add images for the code components.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
