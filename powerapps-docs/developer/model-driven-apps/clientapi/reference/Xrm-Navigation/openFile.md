---
title: "openFile (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the openFile method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# openFile (Client API reference)

[!INCLUDE[./includes/openFile-description.md](./includes/openFile-description.md)]

## Syntax

`Xrm.Navigation.openFile(file,openFileOptions)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|`file` |Object | Yes|An object describing the file to open. The object has the following values:<br/>- **`fileContent`**: String. Contents of the file.  <br/>- **`fileName`**: String. Name of the file.<br/>- **`fileSize`**: Number. Size of the file in KB.<br/>- **`mimeType`**: String. MIME type of the file.|
|`openFileOptions` |Object | No|An object describing whether to open or save the file. The object has the following values:<br/>- **`openMode`**: Specify `1` to open; `2` to save. <br/>If you do not specify this parameter, by default `1` (open) is passed.<br/>This parameter is only supported on Unified Interface.|

### Related articles

[Xrm.Navigation](../xrm-navigation.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
