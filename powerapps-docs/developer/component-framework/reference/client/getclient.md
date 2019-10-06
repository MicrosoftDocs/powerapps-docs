---
title: getClient | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 4b7c18f8-cd00-4f39-8f88-ed9306d6a055
---
# getClient

[!INCLUDE [getclient-description](includes/getclient-description.md)]

## Syntax

`context.client.getClient()`

## Available for 

Model-driven apps and canvas apps (experimental preview) 



## Return Value

Type: `String`

Returns a value to indicate in which client the script is executing.

|||
|-----|-----|
|Web| Web application, or Unified Interface|
|Outlook| Outlook|
|Mobile| Mobile app|



### Related topics

[Client](../client.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)