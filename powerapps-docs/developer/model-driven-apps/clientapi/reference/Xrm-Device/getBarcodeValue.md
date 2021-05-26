---
title: "getBarcodeValue| MicrosoftDocs"
description: Includes description and supported parameters for the getBarCodeValue method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0218b96c-2809-4f2d-9f9f-d8ee8f8e3b7b
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getBarcodeValue (Client API reference)



[!INCLUDE[./includes/getBarcodeValue-description.md](./includes/getBarcodeValue-description.md)]


## Syntax

`Xrm.Device.getBarcodeValue().then(successCallback, errorCallback)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|successCallback |Function | Yes|A function to call when the barcode value is returned as a String.|
|errorCallback |Function | Yes|A function to call when the operation fails. An error object with the **message** property (String) will be passed that describes the error details.|
 

## Return Value
On success, returns a string containing the scanned barcode value.

## Remarks
This method is supported only for the mobile clients.

## Example

```JavaScript
Xrm.Device.getBarcodeValue().then(
    function success(result) {
        Xrm.Navigation.openAlertDialog({ text: "Barcode value: " + result });
    },
    function (error) {
        Xrm.Navigation.openAlertDialog( {text: error.message} );
    }
);
``` 

### Related topics
[Xrm.Device](../xrm-device.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]