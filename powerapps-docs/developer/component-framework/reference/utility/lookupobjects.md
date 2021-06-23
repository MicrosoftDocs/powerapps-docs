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
|lookupOptions|`UtilityApi.LookupOptions`|Yes|Defines the options for opening the lookup dialog. The LookupOptions has the following elements:<br/>- **allowMultiSelect**: `Boolean`. Indicates whether the lookup allows more than one item to be selected.<br/>- **defaultEntityType**: `String`. The default table type to use.<br/>- **defaultViewId**: `String`. The default view to use.<br/>- **entityTypes**: `String[]`. The table types to display.<br/>- **viewIds**: `String[]`. The views to be available in the view picker. Only System views are supported (not user views).|

## Return Value

Type: LookupValue[]


### Related topics

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]