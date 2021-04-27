---
title: openAlertDialog | Microsoft Docs
description: Displays an alert dialog containing a message and a button.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4acd3f17-74c0-4de1-9326-3778ff413f1e
---

# openAlertDialog

[!INCLUDE [openalertdialog-description](includes/openalertdialog-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openAlertDialog(alertStrings, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|alertStrings|`AlertDialogStrings`|Yes|The strings to be used in alert dialog. The AlertDialogStrings has the following attributes:<br/>- **text**: `string`. The message to be displayed in the alert dialog. <br/>- **confirmButtonLabel**:`string`. The confirm button label. If you do not specify the button label, **OK** (in user's preferred language) is used as the button label.|
|options|`AlertDialogOptions`|Yes|Dialog options. The AlertDialogOptions has the following attributes:<br/>- **height**: `number`. Height of the alert dialog in pixels. <br/>- **width**: `number`. Width of the alert dialog in pixels|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)

## Example 

```TypeScript
context.navigation.openAlertDialog({text:"This is an alert.", confirmButtonLabel : "Yes",}).then(
		function success()
		{
			document.getElementById("openAlertDialogButton")!.innerHTML = "Alert dialog closed";
		},
		function()
		{
			document.getElementById("openAlertDialogButton")!.innerHTML = "Error in Alert Dialog";
		}
	);
```

### Related topics

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]