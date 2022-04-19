---
title: addColumn | Microsoft Docs
description: Adds column to the column set.
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

# addColumn

[!INCLUDE[./includes/addColumn-description.md](./includes/addcolumn-description.md)]

## Available for

Model-driven apps

## Syntax

`context.parameters.dataset.addColumn(name, columnAlias)`

## Parameters

| Parameter Name | Type     | Required | Description                                                                                                                          |
| -------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| name           | `string` | Yes      | Name of the column. For linked entities concatenate linking entity alias and the column name, for instance "contact_alias.firstname" |
| columnAlias    | `string` | No       | Alias of the column.                                                                                                                 |

## Return value

Type: Promise

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
