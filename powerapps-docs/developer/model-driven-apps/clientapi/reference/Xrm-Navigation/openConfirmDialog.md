---
title: "openConfirmDialog (Client API Reference) in Model-Driven Apps"
description: Learn how to use the openConfirmDialog method in model-driven apps to display a confirmation dialog. Review syntax, parameters, and a JavaScript example.
author: sriharibs-msft
ms.author: srihas
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ai-usage: ai-assisted
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# openConfirmDialog (Client API reference)



[!INCLUDE[./includes/openConfirmDialog-description.md](./includes/openConfirmDialog-description.md)]

## Syntax

`Xrm.Navigation.openConfirmDialog(confirmStrings,confirmOptions).then(successCallback,errorCallback);`

## Parameters

> [!NOTE]
> When you enable the *[new look](../../../../../user/modern-fluent-design.md)*, the dialog height resizes automatically if you don't set the **height** value of the dialog options.



|Name |Type |Required |Description |
|---|---|---|---|
|`confirmStrings`|[confirmStrings](#confirmstrings)|Yes|The strings to use in the confirmation dialog.|
|`confirmOptions`|[confirmOptions](#confirmoptions)|No|The height and width options for the confirmation dialog.|
|`successCallback`|function|No|A function to execute when the confirmation dialog is closed by clicking the confirm, cancel, or **X** in the top-right corner of the dialog. An object with the **confirmed** (Boolean) attribute is passed that indicates whether the confirm button was clicked to close the dialog.|
|`errorCallback`|function|No|A function to execute when the operation fails.|

### confirmStrings

| Name | Type | Description |
| --- | --- | --- |
| `cancelButtonLabel` | String | (Optional) The cancel button label. If you don't specify the cancel button label, **Cancel** is used as the button label. |
| `confirmButtonLabel` | String | (Optional) The confirm button label. If you don't specify the confirm button label, **OK** is used as the button label. |
| `subtitle` | String | (Optional) The subtitle to display in the confirmation dialog. |
| `text` | String | The message to display in the confirmation dialog. |
| `title` | String | (Optional) The title to display in the confirmation dialog. |

### confirmOptions

| Name | Type | Description |
| --- | --- | --- |
| `height` | Number | (Optional) Height of the confirmation dialog in pixels. With the *new look* enabled, the dialog height resizes automatically if you don't set the `height` value of the dialog options. |
| `width` | Number | (Optional) Width of the confirmation dialog in pixels. |

## Example

The following code sample displays a confirmation dialog box. It logs an appropriate message in the console depending on whether the user selects confirm or cancel/**X** to close the dialog.

```JavaScript
const confirmStrings = {
  text: "This is a confirmation.",
  title: "Confirmation Dialog"
};
const confirmOptions = { height: 200, width: 450 };

Xrm.Navigation.openConfirmDialog(confirmStrings, confirmOptions).then(({ confirmed }) => {
  if (confirmed) {
        console.log("Dialog closed using OK button.");
  } else {
        console.log("Dialog closed using Cancel button or X.");
  }
});
```

### Related articles

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
