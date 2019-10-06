---
title: uses-feature | Microsoft Docs
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
ms.assetid: 87f5e921-4114-4710-a362-db741426a69b
---

# uses-feature element

Indicates which feature their components want to use.

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
|`uses-feature name="device.captureImage" required=”true"`|`Context.device.captureImage != null`, no check needed.|Warning at design time. Component load will  fail at runtime.|
|`uses-feature name="device.captureImage" required=”false"`|`Context.device.captureImage != null`|`Context.device.captureImage == null`, component can adaptively check this at runtime. |
|(none)|`Context.device.captureImage == null` |`Context.device.captureImage == null` |

### Related topics

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)