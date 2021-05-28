---
title: openConfirmDialog | Microsoft Docs
description: Displays a confirmation dialog box containing a message and two buttons.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 83f2c208-696c-48b1-b65c-2ba7374d6cfc
---

# openConfirmDialog

[!INCLUDE [openconfirmdialog-description](includes/openconfirmdialog-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openConfirmDialog(confirmStrings, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|confirmStrings|`ConfirmDialogStrings`|Yes|The strings used in the dialog. The ConfirmDialogStrings has the following attributes:<br/>- **title**: `String`. The title to be displayed in the confirmation dialog. <br/>- **subtitle**: `String`. The subtitle to be used displayed in the confirmation dialog.<br/>- **text**: `String`. The message to be displayed in the confirmation dialog.<br/>- **confirmButtonLabel**: `String`. The confirm button label. If you do not specify the button label, **OK** (in user's preferred language) is used as the button label.<br/>- **cancelButtonLabel**: `String` The cancel button label. If you do not specify the cancel button label, **Cancel** is used as the button label.|
|options|`ConfirmDialogOptions`|No|Options for the dialog. The ConfirmDialogOptions has the following attributes:<br/>- **height**: `Number`. Height of the confirmation dialog in pixels. <br/>- **width**:`Number`. Width of the confirmation dialog in pixels|

## Return Value

Type: `Promise<ConfirmDialogResponse>`

Description: Returns an object with the confirmed (Boolean) attribute is passed that indicates whether the confirm button was clicked to close the dialog.

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) 


### Related topics

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]