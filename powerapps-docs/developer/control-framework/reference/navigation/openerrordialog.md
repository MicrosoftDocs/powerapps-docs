---
title: openErrorDialog | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 10c154b9-45a0-44ee-a621-73d6a9009c6d
---
# openErrorDialog

[!INCLUDE [openerrordialog-description](includes/openerrordialog-description.md)]

## Syntax

`openErrorDialog(options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|options|`ErrorDialogOptions`|yes|Error dialog options. The ErrorDialogOptions has the following attributes: <br/>- **details**: `string`. Details about the error. When you specify this, the Download Log File button is available in the error message, and clicking it will let users download a text file with the content specified in this attribute.<br/>- **errorCode**: `number`. If you just set errorCode, the message for the error code is automatically retrieved from the server and displayed in the error dialog. If you specify an errorCode value, an error dialog with a default error message is displayed.<br/>- **message**: `string`. The message to be displayed in the error dialog.|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps Component Framework API Reference](../reference/index.md)<br/>
[PowerApps Component Framework Overview](../overview.md)