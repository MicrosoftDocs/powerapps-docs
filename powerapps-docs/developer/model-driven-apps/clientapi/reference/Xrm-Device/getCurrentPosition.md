---
title: "getCurrentPosition| MicrosoftDocs"
description: Includes description and supported parameters for the getCurrentPosition method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 062a52d8-170c-4e98-b48a-ac99ec759f83
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getCurrentPosition (Client API reference)



[!INCLUDE[./includes/getCurrentPosition-description.md](./includes/getCurrentPosition-description.md)]


## Syntax

`Xrm.Device.getCurrentPosition().then(successCallback, errorCallback)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|successCallback |Function | Yes|A function to call when the current geolocation information is returned. A geolocation object with the following values is passed to the function.:<br/>- **coords**: Contains a set of geographic coordinates along with associated accuracy as well as a set of other optional values such as altitude and speed. <br/>- **timestamp**: Represents the time when the object was acquired and is represented as DOMTimeStamp.|
|errorCallback |Function | Yes|A function to call when the operation fails. An object with the following properties will be passed: <br/>- **code**: The error code. Number. <br/>- **message**: RLocalized message describing the error details. String.<br/><br/>If the user location setting is not enabled on your mobile device, the error message indicates the same. If you are using an earlier version of the model-driven apps mobile client or if geolocation capability is not available on your mobile device, null is passed to the error callback.|
 

## Return Value
On success, returns a geolocation object with the values specified earlier in the **successCallback** function.

## Remarks
For the **getCurrentPosition** method to work, the geolocation capability must be enabled on your mobile device, and the model-driven apps mobile clients must have permissions to access the device location, which isn't enabled by default.

This method is supported only for the mobile clients.

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

### Related topics
[Xrm.Device](../xrm-device.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]