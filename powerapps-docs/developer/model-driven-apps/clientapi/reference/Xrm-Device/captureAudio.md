---
title: "captureAudio (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the captureAudio method.
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

# captureAudio (Client API reference)

[!INCLUDE[./includes/captureAudio-description.md](./includes/captureAudio-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.captureAudio().then(successCallback, errorCallback)`

## Parameters

| Parameter Name| Type| Required | Description|
|---| --- | --- | ---|
| `successCallback` | Function | Yes      | A function to call when audio is returned. A base64 encoded audio object with the following values is passed to the function:<br/>- **`fileContent`**: Contents of the audio file. String <br/>- **`fileName`**: Name of the audio file. String.<br/>- **`fileSize`**: Size of the audio file in KB. Number.<br/>- **`mimeType`**: Audio file MIME type. String. |
| `errorCallback`   | Function | Yes      | A function to call when the operation fails.|

## Return Value

On success, returns a base64 encoded audio object with the values specified earlier.

## Exceptions

See [Web service error codes](../../../../data-platform/reference/web-service-error-codes.md)

### Related articles

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
