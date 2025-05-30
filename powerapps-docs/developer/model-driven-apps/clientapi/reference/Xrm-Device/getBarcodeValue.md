---
title: "getBarcodeValue (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getBarCodeValue method.
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

# getBarcodeValue (Client API reference)

[!INCLUDE[./includes/getBarcodeValue-description.md](./includes/getBarcodeValue-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.getBarcodeValue().then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description|
| --------------- | -------- | -------- | -----------|
| `successCallback` | Function | Yes      | A function to call when the barcode value is returned as a String.                                                                                   |
| `errorCallback`   | Function | Yes      | A function to call when the operation fails. An error object with the **message** property (String) will be passed that describes the error details. |

## Return Value

On success, returns a string containing the scanned barcode value.

## Exceptions

See [Web service error codes](../../../../data-platform/reference/web-service-error-codes.md)

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

### Related articles

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
