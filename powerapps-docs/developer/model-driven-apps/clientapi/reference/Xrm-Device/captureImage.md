---
title: "captureImage (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the captureImage method.
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

# captureImage (Client API reference)

[!INCLUDE[./includes/captureImage-description.md](./includes/captureImage-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.captureImage(imageOptions).then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description|
| --------------- | -------- | -------- | -----------|
| `imageOptions` | Object| No | An object with the following values:<br/>- **`allowEdit`**: Indicates whether to edit the image before saving. Boolean.<br/>- **`quality`**: Quality of the image file in percentage. Number.<br/>- **`height`**: Height of the image to capture. Number.<br/>- **`width`**: Width of the image to capture. Number.<br/>**Note**: Both the height and width dimensions must be specified if used. |
| `successCallback` | Function | Yes | A function to call when image is returned. A base64 encoded image object with the following values is passed to the function:<br/>- **`fileContent`**: Contents of the image file. String <br/>- **`fileName`**: Name of the image file. String.<br/>- **`fileSize`**: Size of the image file in KB. Number.<br/>- **`mimeType`**: Image file MIME type. String.|
| `errorCallback`   | Function | Yes      | A function to call when the operation fails.|

## Return Value

On success, returns a base64 encoded image object with the values specified earlier.

## Exceptions

See [Web service error codes](../../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
