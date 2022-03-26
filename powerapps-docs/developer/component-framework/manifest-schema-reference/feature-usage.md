---
title: feature-usage | Microsoft Docs
description: The feature-usage element acts as a wrapper around the uses-feature elements, which themselves allow developers to declare which features their component wants to use.
keywords:
ms.subservice: pcf
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly
ms.topic: "reference"
---

# feature-usage element

[!INCLUDE [feature-usage-description](includes/feature-usage-description.md)]

## Available for

Model-driven apps

## Parent Element

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Child Element

|Element|Description|Available for|
|--|--|-----|
|[uses-feature](uses-feature.md)|Indicates which feature their components want to use.|Model-driven apps|


## Example

```XML
<feature-usage>
    <uses-feature name="Device.captureAudio" required="true" />
    <uses-feature name="Device.captureImage" required="true" />
    <uses-feature name="Device.captureVideo" required="true" />
    <uses-feature name="Device.getBarcodeValue" required="true" />
    <uses-feature name="Device.getCurrentPosition" required="true" />
    <uses-feature name="Device.pickFile" required="true" />
    <uses-feature name="Utility" required="true" />
    <uses-feature name="WebAPI" required="true" />
 </feature-usage>
```


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]