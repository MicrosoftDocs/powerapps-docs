---
title: getClient (Power Apps component framework API reference) | Microsoft Docs
description: Returns a value to indicate which client the script is executing in.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# getClient

[!INCLUDE [getclient-description](includes/getclient-description.md)]

## Syntax

`context.client.getClient()`

## Available for 

Model-driven apps, canvas apps, & portals.



## Return Value

Type: `String`

Returns a value to indicate in which client the script is executing.

|Client type|Description|
|-----|-----|
|Web| Web application, or Unified Interface|
|Outlook| Outlook|
|Mobile| Mobile app|



### Related articles

[Client](../client.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
