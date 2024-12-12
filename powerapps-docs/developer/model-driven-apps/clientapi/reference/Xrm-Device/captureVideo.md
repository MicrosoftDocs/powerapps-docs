---
title: "captureVideo (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the captureVideo method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# captureVideo (Client API reference)

[!INCLUDE[./includes/captureVideo-description.md](./includes/captureVideo-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.captureVideo().then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description|
| --------------- | -------- | -------- | ----|
| `successCallback` | Function | Yes | A function to call when Video is returned. A base64 encoded Video object with the following values is passed to the function:<br/>- **`fileContent`**: Contents of the Video file. String <br/>- **`fileName`**: Name of the Video file. String.<br/>- **`fileSize`**: Size of the Video file in KB. Number.<br/>- **`mimeType`**: Video file MIME type. String. |
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

On success, returns a base64 encoded Video object with the values specified earlier.

## Exceptions

See [Web service error codes](../../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
