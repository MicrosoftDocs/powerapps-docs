---
title: "openConfirmDialog (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openConfirmDialog method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9c82028d-cbc9-4d40-9987-6ce1ea01fde2
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# openConfirmDialog (Client API reference)



[!INCLUDE[./includes/openConfirmDialog-description.md](./includes/openConfirmDialog-description.md)]

## Syntax

`Xrm.Navigation.openConfirmDialog(confirmStrings,confirmOptions).then(successCallback,errorCallback);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|confirmStrings|Object|Yes|The strings to be used in the confirmation dialog. The object contains the following values:<br/>- **cancelButtonLabel**: (Optional) String. The cancel button label. If you do not specify the cancel button label, **Cancel** is used as the button label.<br/>- **confirmButtonLabel**: (Optional) String. The confirm button label. If you do not specify the confirm button label, **OK** is used as the button label.<br/>- **subtitle**: (Optional) String. The subtitle to be displayed in the confirmation dialog.<br/>- **text**: String. The message to be displayed in the confirmation dialog.<br/>- **title**: (Optional) String. The title to be displayed in the confirmation dialog.|
|confirmOptions|Object|No|The height and width options for confirmation dialog. The object contains the following values:<br/>- **height**: (Optional) Number. Height of the confirmation dialog in pixels.<br/>- **width**: (Optional) Number. Width of the confirmation dialog in pixels.|
|successCallback|function|No|A function to execute when the confirmation dialog is closed by clicking the confirm, cancel, or **X** in the top-right corner of the dialog. An object with the **confirmed** (Boolean) attribute is passed that indicates whether the confirm button was clicked to close the dialog.|
|errorCallback|function|No|A function to execute when the operation fails.|

## Example

The following code sample displays a confirmation dialog box. Appropriate message is logged in the console depending on whether confirm or cancel/**X** was clicked to close the dialog.

```JavaScript
var confirmStrings = { text:"This is a confirmation.", title:"Confirmation Dialog" };
var confirmOptions = { height: 200, width: 450 };
Xrm.Navigation.openConfirmDialog(confirmStrings, confirmOptions).then(
function (success) {    
    if (success.confirmed)
        console.log("Dialog closed using OK button.");
    else
        console.log("Dialog closed using Cancel button or X.");
});

```

### Related topics

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]