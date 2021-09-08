---
title: PickFile | Microsoft Docs
description: Opens a dialog box to select files for the upload.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/08/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: aae27c64-33c4-47f1-b833-4c04161c01e2
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

See [Web service error codes](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/org-service/web-service-error-codes)

### Related topics

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
