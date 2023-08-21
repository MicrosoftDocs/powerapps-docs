---
title: ImageObject (Power Apps component framework API reference) | Microsoft Docs
description: Provides access to all the properties of an image.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 08/31/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# ImageObject

[!INCLUDE [imageobject-description](includes/imageobject-description.md)]

## Available for

Canvas apps

## Properties

### fileContent

Contents of the file.

**Type**: `string`

### fileName

Name of the file.

**Type**: `string`

### fileSize

Size of the file in KB.

**Type**: `number`

### mimeType

File MIME type.

**Type**: `string`

### thumbnailUrl

URL pointing to the thumbnail version of the image, if available.

**Type**: `string`

## Sample controls

[Image upload component](../sample-controls/image-upload-control.md)

## Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
