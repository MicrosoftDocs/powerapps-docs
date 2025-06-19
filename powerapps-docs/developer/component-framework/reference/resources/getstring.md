---
title: getString (Power Apps component framework API reference) | Microsoft Docs
description: Returns the localized string for a given key associated with the specified resource (resx) defined in the manifest file.
author: anuitz
ms.author: anuitz
ms.date: 09/27/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getString

[!INCLUDE [getstring-description](includes/getstring-description.md)]

## Available for

Model-driven apps, canvas apps, & portals.

## Syntax

`context.resources.getString(id)`

> [!NOTE]
> If the `id` parameter doesn't match a key associated with the specified resource (resx) defined in the manifest file, this method returns the `id` parameter value.

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|`id`|String|Yes|Name of the resource in the component manifest.|

## Return Value

Type: `String`


### Related articles

[Resources](../resources.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
