---
title: addColumn (Power Apps component framework API reference) | Microsoft Docs
description: Adds column to the column set.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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
| name           | `string` | Yes      | Name of the column. For linked entities concatenate linking entity alias and the column name, for example: `contact_alias.firstname`. |
| columnAlias    | `string` | No       | Alias of the column.                                                                                                                 |

## Return value

Type: Promise

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
