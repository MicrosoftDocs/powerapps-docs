---
title: uses-feature | Microsoft Docs
description: Indicates which feature their components want to use.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# uses-feature element

[!INCLUDE [uses-feature-description](includes/uses-feature-description.md)]

## Available for

Model-driven apps

## Parameters

|Element|Description|Type|Required|
|--|--|---|----|
|`name`|Name of the feature that is declared in the component|`string`|Yes|
|`required`|Indicates if the component requires that feature or not|`boolean`|Yes|

## Parent Element

|Element|Description|
|--|--|
|[feature-usage](feature-usage.md)|[!INCLUDE [feature-usage-description](includes/feature-usage-description.md)]|



### Example 

```XML
<feature-usage>
    <uses-feature name="WebAPI" required="true" />
</feature-usage>
```

The following table shows the relationship of these settings to what happens in the code at runtime whether the feature function is available to call based upon the `uses-feature` settings defined in the manifest.

|Manifest|If Host supports|If Host doesn't support|
|----|----|-----|
|`uses-feature name="device.captureImage" required="true"`|`Context.device.captureImage != null`, no check needed.|Warning at design time. Component load fails at runtime.|
|`uses-feature name="device.captureImage" required="false"`|`Context.device.captureImage != null`|`Context.device.captureImage == null`, component can adaptively check this at runtime. |
|(none)|`Context.device.captureImage == null` |`Context.device.captureImage == null` |

### Related articles

[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
