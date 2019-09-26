---
title: lookupObjects | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
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
|lookupOptions|`UtilityApi.LookupOptions`|Yes|Defines the options for opening the lookup dialog. The LookupOptions has the following attributes:<br/>- **allowMultiSelect**: `Boolean`. Indicates whether the lookup allows more than one item to be selected.<br/>- **defaultEntityType**: `String`. The default entity type to use.<br/>- **defaultViewId**: `String`. The default view to use.<br/>- **entityTypes**: `String[]`. The entity types to display.<br/>- **viewIds**: `String[]`. The views to be available in the view picker. Only System views are supported (not user views).|

## Return Value

Type: [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[EntityReference](../entityreference.md)[]>


### Related topics

[Utility](../utility.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)