---
title: uses-feature | Microsoft Docs
description: Indicates which feature their components want to use.
ms.author: hemantg
author: HemantGaur
ms.date: 05/27/2022
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

## Parent Element

|Element|Description|
|--|--|
|feature-usage|The feature-usage element acts as a wrapper around the uses-feature elements, which themselves allow developers to declare which features their component wants to use. If there are no uses-feature elements defined, the feature-usage element is not required.|

## Child Elements

|Element|Description|Type|Required|
|--|--|---|----|
|name|Name of the feature that is declared in the component|`string`|Yes|
|required|Indicates if the component requires that feature or not|`boolean`|Yes|

### Example 

```XML
<feature-usage>
    <uses-feature name="WebAPI" required="true" />
</feature-usage>
```

The table below shows the relationship of these settings to what happens in the code at runtime whether the feature function will be available to call based upon the uses-feature settings defined in the manifest.

|Manifest|If Host supports|If Host doesn't support|
|----|----|-----|
|`uses-feature name="device.captureImage" required="true"`|`Context.device.captureImage != null`, no check needed.|Warning at design time. Component load will  fail at runtime.|
|`uses-feature name="device.captureImage" required="false"`|`Context.device.captureImage != null`|`Context.device.captureImage == null`, component can adaptively check this at runtime. |
|(none)|`Context.device.captureImage == null` |`Context.device.captureImage == null` |

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
