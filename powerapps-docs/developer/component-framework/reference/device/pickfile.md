---
title: PickFile (Power Apps component framework API reference) | Microsoft Docs
description: Opens a window to select files for the upload.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# pickFile

[!INCLUDE[./includes/pickfile-description.md](./includes/pickfile-description.md)]

## Available for

Model-driven and canvas apps

## Syntax

`context.device.pickFile(options)`

## Parameters

| Parameter Name | Type     | Required | Description           |
| -------------- | -------- | -------- | --------------------- |
| `options`      | `Object` | No       | Options to pick file. |

The `options` parameter object has the following properties:

| Name                     | Type      | Description                                                                |
| ------------------------ | --------- | -------------------------------------------------------------------------- |
| `accept`                 | `String`  | Image file types to select. Valid values are _audio_, _video_, or _image_. |
| `allowMultipleFiles`     | `Boolean` | Indicates whether to allow select multiple files                           |
| `maximumAllowedFileSize` | `Number`  | Maximum size of the file(s) to be selected                                 |

## Return Value

Type: `Promise<FileObject[]>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [FileObject](../fileobject.md)

## Exceptions

See [Web service error codes](../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
