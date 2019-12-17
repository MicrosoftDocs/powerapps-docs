---
title: CaptureImage | Microsoft Docs
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
ms.assetid: 1d9c0063-add2-4002-acab-1be07ca1f6b6
---

# captureImage

[!INCLUDE[./includes/captureimage-description.md](./includes/captureimage-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.device.captureImage(options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|`options`|`Object`|No|Options for capturing image.|

## Return Value

Type: `Promise<FileObject>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [FileObject](../fileobject.md)

## Remarks

The `options` parameter object has the following properties:

|Name|Type|Description|
| ---|----|-----------|
|`allowEdit`|`Boolean`|Indicates whether to edit the image before saving.|
|`height`|`Number`|Height of the image to capture.|
|`preferFrontCamera`|`Boolean`|Indicates whether to capture image using the front camera of the device.|
|`quality`|`Number`|Quality of the image file in percentage.|
|`width`|`Number`|Width of the image to capture.|


### Related topics

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)