---
title: Device | Microsoft Docs
description: Provides methods to use native device capabilities.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a0f9abc5-c605-4433-bf5a-f8253eeeda3b
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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
