---
title: "captureVideo| MicrosoftDocs"
ms.date: 10/31/2018
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


## Syntax

`Xrm.Device.captureVideo().then(successCallback, errorCallback)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|successCallback |Function | Yes|A function to call when Video is returned. A base64 encoded Video object with the following attributes is passed to the function:<br/>- **fileContent**: Contents of the Video file. String <br/>- **fileName**: Name of the Video file. String.<br/>- **fileSize**: Size of the Video file in KB. Number.<br/>- **mimeType**: Video file MIME type. String.|
|errorCallback |Function | Yes|A function to call when the operation fails. |
 

## Return Value
On success, returns a base64 encoded Video object with the attributes specified earlier.

## Remarks
This method is supported only for the mobile clients.

### Related topics
[Xrm.Device](../xrm-device.md)

