---
title: lookupObjects | Microsoft Docs
description: Opens a lookup dialog allowing the user to select one or more items.
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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
