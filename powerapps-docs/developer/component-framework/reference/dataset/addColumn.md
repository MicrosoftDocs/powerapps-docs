---
title: addColumn | Microsoft Docs
description: Adds column to the column set.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/12/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec4d6f14-d08b-410f-aad7-6a040c2b1c6a
---

# addColumn

[!INCLUDE[./includes/addColumn-description.md](./includes/addcolumn-description.md)]

## Available for

Model-driven apps

## Syntax

`context.parameters.dataset.addColumn(name, columnAlias)`

## Parameters

| Parameter Name | Type     | Required | description |
| -------------- | -------- | -------- | ----------- |
| name           | `string` | Yes      | Name of the column.          |
| columnAlias    | `string` | No       | Alias of the column.         |

## Return value

Type: Promise

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
