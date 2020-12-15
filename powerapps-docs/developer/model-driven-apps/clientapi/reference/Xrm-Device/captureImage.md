---
title: "captureImage | MicrosoftDocs"
ms.date: 10/31/2018
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


## Syntax

`Xrm.Device.captureImage(imageOptions).then(successCallback, errorCallback)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|imageOptions |Object | No|An object with the following attributes:<br/>- **allowEdit**: Indicates whether to edit the image before saving. Boolean.<br/>- **height**: Height of the image to capture. Number.<br/>- **quality**: Quality of the image file in percentage. Number.<br/>- **width**: Width of the image to capture. Number..|
|successCallback |Function | Yes|A function to call when image is returned. A base64 encoded image object with the following attributes is passed to the function:<br/>- **fileContent**: Contents of the image file. String <br/>- **fileName**: Name of the image file. String.<br/>- **fileSize**: Size of the image file in KB. Number.<br/>- **mimeType**: Image file MIME type. String.|
|errorCallback |Function | Yes|A function to call when the operation fails. |
 

## Return Value
On success, returns a base64 encoded image object with the attributes specified earlier.

## Remarks
This method is supported only for the mobile clients.

### Related topics
[Xrm.Device](../xrm-device.md)

