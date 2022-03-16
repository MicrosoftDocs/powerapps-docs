---
title: getClient | Microsoft Docs
description: Returns a value to indicate which client the script is executing in.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
---
# getClient

[!INCLUDE [getclient-description](includes/getclient-description.md)]

## Syntax

`context.client.getClient()`

## Available for 

Model-driven and canvas apps 



## Return Value

Type: `String`

Returns a value to indicate in which client the script is executing.

|Client type|Description|
|-----|-----|
|Web| Web application, or Unified Interface|
|Outlook| Outlook|
|Mobile| Mobile app|



### Related topics

[Client](../client.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]