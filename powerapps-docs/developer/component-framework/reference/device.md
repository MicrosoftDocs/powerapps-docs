---
title: Device (Power Apps component framework API reference) | Microsoft Docs
description: Provides methods to use native device capabilities.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Device

[!INCLUDE [device-description](includes/device-description.md)]

> [!IMPORTANT]
> If you want to use the device API methods, you need to declare the usage of these method in [feature-usage](../manifest-schema-reference/feature-usage.md) node in the manifest file.

## Available for

Model-driven and canvas apps

## Syntax

`context.device`

## Methods

| Method                                             | Description                                                                                    |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [captureAudio](device/captureaudio.md)             | [!INCLUDE [captureaudio-description](device/includes/captureaudio-description.md)]             |
| [captureImage](device/captureimage.md)             | [!INCLUDE [captureimage-description](device/includes/captureimage-description.md)]             |
| [captureVideo](device/capturevideo.md)             | [!INCLUDE [capturevideo-description](device/includes/capturevideo-description.md)]             |
| [getBarcodeValue](device/getbarcodevalue.md)       | [!INCLUDE [getbarcodevalue-description](device/includes/getbarcodevalue-description.md)]       |
| [getCurrentPosition](device/getcurrentposition.md) | [!INCLUDE [getcurrentposition-description](device/includes/getcurrentposition-description.md)] |
| [pickFile](device/pickfile.md)                     | [!INCLUDE [pickfile-description](device/includes/pickfile-description.md)]                     |

## Example

```TypeScript
 private onUploadButtonClick(event: Event): void {
    this._context.device.pickFile().then(this.processFile.bind(this), this.showError.bind(this));
  }
```

## Sample controls

[Device API component](../sample-controls/device-api-control.md)  
[Image upload component](../sample-controls/image-upload-control.md)

### Related articles
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
