---
title: "openFile (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openFile method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 6a2497fe-08ad-4953-b3ff-44c72bc25082
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# openFile (Client API reference)

[!INCLUDE[./includes/openFile-description.md](./includes/openFile-description.md)]

## Syntax

`Xrm.Navigation.openFile(file,openFileOptions)`

## Parameters

| Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|file |Object | Yes|An object describing the file to open. The object has the following values:<br/>- **fileContent**: String. Contents of the file.  <br/>- **fileName**: String. Name of the file.<br/>- **fileSize**: Number. Size of the file in KB.<br/>- **mimeType**: String. MIME type of the file.|
|openFileOptions |Object | No|An object describing whether to open or save the file. The object has the following values:<br/>- **openMode**: Specify `1` to open; `2` to save. <br/>If you do not specify this parameter, by default `1` (open) is passed.<br/>This parameter is only supported on Unified Interface.|

### Related topics

[Xrm.Navigation](../xrm-navigation.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]