---
title: PickFile | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: aae27c64-33c4-47f1-b833-4c04161c01e2
---

# pickFile

[!INCLUDE[./includes/pickfile-description.md](./includes/pickfile-description.md)]

## Syntax

`pickFile(options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|`options`|`object`|no|Options to pick file.|

## Return Value

Type: `Promise<File[]>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)

## Remarks

The `options` parameter object has the following properties:

|Name|Type|Description|
|--|--|--|
|`accept`|`string`|Image file type to select. Valid values are "audio", "video", or "image"|
|`allowMultipleFiles`|`boolean`|Indicates whether to allow select multiple files|
|`maximumAllowedFileSize`|`number`|Maximum size of the files(s) to be selected|

### Related topics

[Device](../device.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../../powerapps-control-framework-overview.md)<br />
