---
title: getFormFactor (Power Apps component framework API reference) | Microsoft Docs
description: Returns information about the kind of device the user is using.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getFormFactor

[!INCLUDE [getformfactor-description](includes/getformfactor-description.md)]

## Syntax

`context.client.getFormFactor()`

## Available for 

Model-driven apps, canvas apps, & portals.

## Return Value

Type: `Number`

|Value|Form Factor|
|---|---|
|0|Unknown|
|1|Desktop|
|2|Tablet|
|3|Phone|


### Related articles

[Client](../client.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
