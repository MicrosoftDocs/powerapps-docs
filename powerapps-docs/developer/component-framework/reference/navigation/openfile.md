---
title: openFile | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ae94e467-d12c-4a74-96f0-05a09e03c5f8
---
# openFile

[!INCLUDE [openfile-description](includes/openfile-description.md)]

## Available for 

Model-driven apps only

## Syntax

`openFile(file, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|file|`FileObject`|yes|An object describing the file to open.The FileObject has the following attributes: <br/>- **fileContent**: `string`. Contents of the file. <br/>- **fileName**: `string`. Name of the file.<br/>- **fileSize**: `number`. Size of the file in KB. <br/>- **mimeType**: `string`. File MIME type.|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)