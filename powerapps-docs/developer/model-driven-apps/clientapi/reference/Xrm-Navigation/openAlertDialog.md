---
title: "openAlertDialog (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8615a284-41b4-479c-81bd-577b3b7c79ad
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# openAlertDialog (Client API reference)



[!INCLUDE[./includes/openAlertDialog-description.md](./includes/openAlertDialog-description.md)]

## Syntax

`Xrm.Navigation.openAlertDialog(alertStrings,alertOptions).then(closeCallback,errorCallback);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|alertStrings|Object|Yes|The strings to be used in the alert dialog. The object contains the following attributes:<br/>- **confirmButtonLabel**: (Optional) String. The confirm button label. If you do not specify the button label, **OK** is used as the button label.<br/>- **text**: String. The message to be displyed in the alert dialog.|
|alertOptions|Object|No|The height and width options for alert dialog. The object contains the following attributes:<br/>- **height**: (Optional) Number. Height of the alert dialog in pixels.<br/>- **width**: (Optional) Number. Width of the alert dialog pixels.|
|successCallback|function|No|A function to execute when the alert dialog is closed by either clicking the confirm button or canceled by pressing ESC.|
|errorCallback|function|No|A function to execute when the operation fails.|


## Example

The following sample code displays an alert dialog. Clicking **Yes** button in the alert dialog or canceling the alert dialog by pressing ESC calls the `close` function::

```JavaScript
var alertStrings = { confirmButtonLabel: "Yes", text: "This is an alert." };
var alertOptions = { height: 120, width: 260 };
Xrm.Navigation.openAlertDialog(alertStrings, alertOptions).then(
    function success(result) {
        console.log("Alert dialog closed");
    },
    function (error) {
        console.log(error.message);
    }
);
```

### Related topics

[Xrm.navigation](../xrm-navigation.md)

