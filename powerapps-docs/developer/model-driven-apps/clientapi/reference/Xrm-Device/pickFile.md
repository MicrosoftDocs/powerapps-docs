---
title: "pickFile| MicrosoftDocs"
description: Opens a dialog box to select files for the upload
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---

# pickFile (Client API reference)

[!INCLUDE[./includes/pickFile-description.md](./includes/pickFile-description.md)]

## Available for

This method is supported for both web and mobile clients.

## Syntax

`Xrm.Device.pickFile(pickFileOptions).then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                           |
| --------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pickFileOptions | Object   | No       | An object with the following values:<br/>- **accept**: Image file types to select. Valid values are "audio", "video", or "image". String.<br/>- **allowMultipleFiles**: Indicates whether to allow selecting multiple files. Boolean.<br/>- **maximumAllowedFileSize**: Maximum size of the files(s) to be selected. Number.                          |
| successCallback | Function | Yes      | A function to call when selected files are returned. An array of objects with _each_ object having the following values is passed to the function:<br/>- **fileContent**: Contents of the file. String <br/>- **fileName**: Name of the file. String.<br/>- **fileSize**: Size of the file in KB. Number.<br/>- **mimeType**: File MIME type. String. |
| errorCallback   | Function | Yes      | A function to call when the operation fails.                                                                                                                                                                                                                                                                                                          |

## Return Value

On success, returns a promise with array of objects as specified earlier for the **successCallback** function.

## Exceptions

See [Web service error codes](../../../../data-platform/org-service/web-service-error-codes.md)

### Related topics

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
