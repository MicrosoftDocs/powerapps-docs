---
title: openErrorDialog (Power Apps component framework API reference) | Microsoft Docs
description: Displays an error dialog.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# openErrorDialog

[!INCLUDE [openerrordialog-description](includes/openerrordialog-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openErrorDialog(options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|options|`ErrorDialogOptions`|Yes|Error dialog options. The ErrorDialogOptions has the following attributes: <br/>- **details**: `String`. Details about the error. When you specify this, the **Download Log File** button is available in the error message, and clicking it will let users download a text file with the content specified in this attribute.<br/>- **errorCode**: `Number`. The error code. If you just set errorCode, the message for the error code is automatically retrieved from the server and displayed in the error dialog. If you specify an **errorCode** value, an error dialog with a default error message is displayed.<br/>- **message**: `String`. The message to be displayed in the error dialog. You must set either the **errorCode** or **message** attribute.|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)


### Related articles

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
