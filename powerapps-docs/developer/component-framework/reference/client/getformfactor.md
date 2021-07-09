---
title: getFormFactor | Microsoft Docs
description: Returns information about the kind of device the user is using.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0ad24866-08c3-4584-8964-decff50e716e
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