---
title: "openAlertDialog (Client API Reference) in Model-Driven Apps"
description: Learn how to use the openAlertDialog method in model-driven apps to display an alert dialog, including syntax, parameters, and a JavaScript example.
author: sriharibs-msft
ms.author: srihas
ms.date: 10/29/2026
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# openAlertDialog (Client API reference)

[!INCLUDE[./includes/openAlertDialog-description.md](./includes/openAlertDialog-description.md)]

## Syntax

`Xrm.Navigation.openAlertDialog(alertStrings,alertOptions).then(successCallback,errorCallback);`

## Parameters

> [!NOTE]
> When you enable the *[new look](../../../../../user/modern-fluent-design.md)*, the dialog height resizes automatically if you don't set the **height** value of the dialog options.

|Name |Type |Required |Description |
|---|---|---|---|
|`alertStrings`|Object|Yes|The strings to use in the alert dialog. The object contains the following values:<br/>- **`confirmButtonLabel`**: (Optional) String. The confirm button label. If you don't specify the button label, **OK** is used as the button label.<br/>- **text**: String. The message to display in the alert dialog.<br/>- **`title`**: (Optional) String. The title of the alert dialog.|
|`alertOptions`|Object|No|The height and width options for alert dialog. The object contains the following values:<br/>- **`height`**: (Optional) Number. Height of the alert dialog in pixels.<br/>- **`width`**: (Optional) Number. Width of the alert dialog pixels.<br><br> When you enable the *[new look](../../../../../user/modern-fluent-design.md)*, the dialog height resizes automatically if you don't set the **`height`** value of the dialog options.|
|`successCallback`|function|No|A function to execute when the alert dialog closes either by clicking the confirm button or by pressing ESC.|
|`errorCallback`|function|No|A function to execute when the operation fails.|

## Example

The following sample code displays an alert dialog. Selecting **Yes** in the alert dialog or canceling the alert dialog by pressing ESC calls the `close` function:

```JavaScript
var alertStrings = { confirmButtonLabel: "Yes", text: "This is an alert.", title: "Sample title" };
var alertOptions = { height: 120, width: 260 };
Xrm.Navigation.openAlertDialog(alertStrings, alertOptions).then(
    function (success) {
        console.log("Alert dialog closed");
    },
    function (error) {
        console.log(error.message);
    }
);
```

### Related articles

[Xrm.navigation](../xrm-navigation.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
