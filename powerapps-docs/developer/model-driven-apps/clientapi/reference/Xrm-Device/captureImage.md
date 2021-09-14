---
title: "captureImage | MicrosoftDocs"
description: Includes description and supported parameters for the captureImage method.
ms.date: 09/08/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1b24e8b2-20af-4e75-8c00-1aa393c07aef
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
---

# captureImage (Client API reference)

[!INCLUDE[./includes/captureImage-description.md](./includes/captureImage-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.captureImage(imageOptions).then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                                                               |
| --------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| imageOptions    | Object   | No       | An object with the following values:<br/>- **allowEdit**: Indicates whether to edit the image before saving. Boolean.<br/>- **quality**: Quality of the image file in percentage. Number.<br/>- **height**: Height of the image to capture. Number.<br/>- **width**: Width of the image to capture. Number.<br/>**Note**: Both the height and width dimensions must be specified if used. |
| successCallback | Function | Yes      | A function to call when image is returned. A base64 encoded image object with the following values is passed to the function:<br/>- **fileContent**: Contents of the image file. String <br/>- **fileName**: Name of the image file. String.<br/>- **fileSize**: Size of the image file in KB. Number.<br/>- **mimeType**: Image file MIME type. String.                                  |
| errorCallback   | Function | Yes      | A function to call when the operation fails.                                                                                                                                                                                                                                                                                                                                              |

## Return Value

On success, returns a base64 encoded image object with the values specified earlier.

## Exceptions

See [Web service error codes](../../../../data-platform/org-service/web-service-error-codes.md)

### Related topics

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
