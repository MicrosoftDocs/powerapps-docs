---
title: openAlertDialog | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4acd3f17-74c0-4de1-9326-3778ff413f1e
---

# openAlertDialog

[!INCLUDE [openalertdialog-description](includes/openalertdialog-description.md)]

## Syntax

`openAlertDialog(alertStrings, options)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|alertStrings|`AlertDialogStrings`|yes|Strings to be used in alert dialog. The AlertDialogStrings has the following attributes:<br/>- **text**: `string`. The message to be displayed in the alert dialog. <br/>- **confirmButtonLabel**:`string`. The confirm button label. if you do not specify the button label, OK (in user's preferred language) is used as the button label.|
|options|`AlertDialogOptions`|yes|Dialog options. The AlertDialogOptions has the following attributes:<br/>- **height**: `number`. Height of the alert dialog in pixels. <br/>- **width**: `number`. Width of the alert dialog in pixels|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)

### Related topics

[Navigation](../navigation.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../../overview.md)<br />
