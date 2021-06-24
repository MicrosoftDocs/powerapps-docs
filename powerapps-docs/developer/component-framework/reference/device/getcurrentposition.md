---
title: CaptureImageOptions | Microsoft Docs
description: Returns the current location using the device geo location capability. This method is supported only for the mobile clients.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 98f341b4-1d5d-4ad2-849d-5ea1d7e143b0
---

# getCurrentPosition

[!INCLUDE[./includes/getcurrentposition-description.md](./includes/getcurrentposition-description.md)]

## Syntax

`context.device.getCurrentPosition()`

## Available for 

Model-driven and canvas apps

## Return Value

Type: `Promise<Position>`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [Position](../position.md)

### Related topics

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]