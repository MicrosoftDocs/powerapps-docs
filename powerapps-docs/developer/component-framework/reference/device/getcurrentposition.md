---
title: CaptureImageOptions (Power Apps component framework API reference) | Microsoft Docs
description: Returns the current location using the device geo location capability.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getCurrentPosition

[!INCLUDE[./includes/getcurrentposition-description.md](./includes/getcurrentposition-description.md)]

## Available for

Model-driven (mobile client) and canvas apps

## Syntax

`context.device.getCurrentPosition()`

## Return Value

Type: `Promise<Position>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [Position](../position.md)

## Exceptions

See [Web service error codes](../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
