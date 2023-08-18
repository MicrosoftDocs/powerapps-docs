---
title: openFile (Power Apps component framework API reference) | Microsoft Docs
description: Opens a file.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 08/22/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# openFile

[!INCLUDE [openfile-description](includes/openfile-description.md)]

## Available for

Model-driven apps

## Syntax

`context.navigation.openFile(file, options)`

## Parameters

| Parameter Name|Type|Required|Description|
|----|----|----|----|
| `file`| `FileObject` | Yes| An object describing the file to open. The `FileObject` has the following attributes: <br/>- **fileContent**: `String`. Contents of the file. <br/>- **fileName**: `String`. Name of the file.<br/>- **fileSize**: `Number`. Size of the file in KB. <br/>- **mimeType**: `String`. File MIME type. |
| `options`| `Object`| No| An object describing whether to open or save the file. The object has the following attribute: <br/>- **openMode**: Specify 1 to open; 2 to save. <br />If you do not specify this parameter, by default 1 (open) is passed. This parameter is only supported on Unified Interface. |

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [FileObject](../fileobject.md)

### Related articles

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
