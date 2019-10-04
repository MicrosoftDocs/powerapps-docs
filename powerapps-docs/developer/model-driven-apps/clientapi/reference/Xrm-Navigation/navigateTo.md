---
title: "navigateTo (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/4/2019
ms.service: powerapps
ms.topic: "reference"
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# navigateTo (Client API reference)



[!INCLUDE[./includes/navigateTo-description.md](./includes/navigateTo-description.md)]

## Syntax

`Xrm.Navigation.navigateTo(pageInput).then(successCallback,errorCallback);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|pageInput|Object|Yes|The page to navigate to. The object contains the following attributes:<br/>- **pageType**: Specify entitylist.<br/>- **confirmButtonLabel**: (Optional) String. The confirm button label. If you do not specify the confirm button label, **OK** is used as the button label.<br/>- **subtitle**: (Optional) String. The subtitle to be displayed in the confirmation dialog.<br/>- **text**: String. The message to be displayed in the confirmation dialog.<br/>- **title**: (Optional) String. The title to be displayed in the confirmation dialog.|
|confirmOptions|Object|No|The height and width options for confirmation dialog. The object contains the following attributes:<br/>- **height**: (Optional) Number. Height of the confirmation dialog in pixels.<br/>- **width**: (Optional) Number. Width of the confirmation dialog in pixels.|
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

