---
title: getBarcodeValue (Power Apps component framework API reference) | Microsoft Docs
description: Invokes the device camera to scan the barcode information, such as product number.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getBarcodeValue

[!INCLUDE[./includes/getbarcodevalue-description.md](./includes/getbarcodevalue-description.md)]

## Available for

Model-driven (mobile client) and canvas apps (mobile client)

## Syntax

`context.device.getBarcodeValue()`

## Return Value

Type: `Promise<string>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise)

## Exceptions

See [Web service error codes](../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Device](../device.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
