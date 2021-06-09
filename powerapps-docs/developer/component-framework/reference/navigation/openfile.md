---
title: openFile | Microsoft Docs
description: Opens a file.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ae94e467-d12c-4a74-96f0-05a09e03c5f8
---
# openFile

[!INCLUDE [openfile-description](includes/openfile-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openFile(file, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|file|`FileObject`|Yes|An object describing the file to open.The FileObject has the following attributes: <br/>- **fileContent**: `String`. Contents of the file. <br/>- **fileName**: `String`. Name of the file.<br/>- **fileSize**: `Number`. Size of the file in KB. <br/>- **mimeType**: `String`. File MIME type.|
|options|`Object`|No|An object describing whether to open or save the file. The object has the following attribute: <br/>- **openMode**: Specify 1 to open; 2 to save. 
If you do not specify this parameter, by default 1 (open) is passed. This parameter is only supported on Unified Interface.|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [FileObject](../fileobject.md)


### Related topics

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]