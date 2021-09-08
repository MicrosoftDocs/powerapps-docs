---
title: "captureVideo| MicrosoftDocs"
description: Includes description and supported parameters for the captureVideo method.
ms.date: 09/08/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9580d05a-a91f-4126-b94b-4d1068da35fa
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
---

# captureVideo (Client API reference)

[!INCLUDE[./includes/captureVideo-description.md](./includes/captureVideo-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.captureVideo().then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                              |
| --------------- | -------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| successCallback | Function | Yes      | A function to call when Video is returned. A base64 encoded Video object with the following values is passed to the function:<br/>- **fileContent**: Contents of the Video file. String <br/>- **fileName**: Name of the Video file. String.<br/>- **fileSize**: Size of the Video file in KB. Number.<br/>- **mimeType**: Video file MIME type. String. |
| errorCallback   | Function | Yes      | A function to call when the operation fails.                                                                                                                                                                                                                                                                                                             |

## Return Value

On success, returns a base64 encoded Video object with the values specified earlier.

## Exceptions

See [Web service error codes](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/org-service/web-service-error-codes)

### Related topics

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
