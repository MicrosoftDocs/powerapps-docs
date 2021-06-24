---
title: getString| Microsoft Docs
description: Returns the localized string for a given key associated with the specified resource (resx) defined in the manifest file.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f28117a1-5d88-4c52-999c-1e07b09c0fe0
---

# getString

[!INCLUDE [getstring-description](includes/getstring-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`context.resources.getString(id)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|id|`String`|Yes|Name of the resource in the component manifest.|

## Return Value

Type: `String`


### Related topics

[Resources](../resources.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]