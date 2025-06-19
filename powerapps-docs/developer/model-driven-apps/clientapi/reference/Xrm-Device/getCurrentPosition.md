---
title: "getCurrentPosition (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getCurrentPosition method.
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

# getCurrentPosition (Client API reference)

[!INCLUDE[./includes/getCurrentPosition-description.md](./includes/getCurrentPosition-description.md)]

## Available for

This method is supported only for the mobile clients.

## Syntax

`Xrm.Device.getCurrentPosition().then(successCallback, errorCallback)`

## Parameters

| Parameter Name  | Type     | Required | Description|
| --------------- | -------- | -------- | -----------|
| `successCallback` | Function | Yes      | A function to call when the current geolocation information is returned. A geolocation object with the following values is passed to the function.:<br/>- **`coords`**: Contains a set of geographic coordinates along with associated accuracy and a set of other optional values such as altitude and speed. <br/>- **`timestamp`**: Represents the time when the object was acquired and is represented as DOMTimeStamp.|
| `errorCallback`   | Function | Yes      | A function to call when the operation fails. An object with the following properties is passed: <br/>- **`code`**: The error code. Number. <br/>- **`message`**: Localized message describing the error details. String.<br/><br/>If the user location setting isn't enabled on your mobile device, the error message indicates the same. If you're using an earlier version of the model-driven apps mobile client or if geolocation capability isn't available on your mobile device, null is passed to the error callback. |

## Return Value

On success, returns a geolocation object with the values specified earlier in the **successCallback** function.

## Exceptions

See [Web service error codes](../../../../data-platform/reference/web-service-error-codes.md)

## Remarks

For the **getCurrentPosition** method to work, the geolocation capability must be enabled on your mobile device, and the model-driven apps mobile clients must have permissions to access the device location, which isn't enabled by default.

## Example

```JavaScript
Xrm.Device.getCurrentPosition().then(
    function success(location) {
        Xrm.Navigation.openAlertDialog({
            text: "Latitude: " + location.coords.latitude +
            ", Longitude: " + location.coords.longitude
        });
    },
    function (error) {
        Xrm.Navigation.openAlertDialog({ text: error.message });
    }
);
```

### Related articles

[Xrm.Device](../xrm-device.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
