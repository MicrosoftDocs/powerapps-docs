---
title: getFormFactor | Microsoft Docs
description: Returns information about the kind of device the user is using.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# getFormFactor

[!INCLUDE [getformfactor-description](includes/getformfactor-description.md)]

## Syntax

`context.client.getFormFactor()`

## Available for 

Model-driven and canvas apps

## Return Value

Type: `Number`

|Value|Form Factor|
|---|---|
|0|Unknown|
|1|Desktop|
|2|Tablet|
|3|Phone|


### Related topics

[Client](../client.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]