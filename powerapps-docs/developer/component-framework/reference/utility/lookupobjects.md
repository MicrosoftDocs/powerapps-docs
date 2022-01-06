---
title: lookupObjects | Microsoft Docs
description: Opens a lookup dialog allowing the user to select one or more items.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d213b401-cfc4-44df-b55c-f040fb6d7072
---

# lookupObjects

[!INCLUDE [lookupobjects-description](includes/lookupobjects-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.utils.lookupObjects(lookupOptions)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|lookupOptions|`UtilityApi.LookupOptions`|Yes|Defines the options for opening the lookup dialog. For a list of lookupOptions, see [lookupOptions](../../../model-driven-apps/clientapi/reference/Xrm-Utility/lookupObjects.md) |

## Return Value

Type: Promise<LookupValue[]>


### Related topics

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
