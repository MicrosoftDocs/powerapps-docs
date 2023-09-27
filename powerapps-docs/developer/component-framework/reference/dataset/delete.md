---
title: delete (Power Apps component framework API reference) | Microsoft Docs
description: Delete the records from data source.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# delete

[!INCLUDE[./includes/delete-description.md](./includes/delete-description.md)]

## Available for

Canvas apps

## Syntax

`context.parameters.dataset.delete(ids)`

## Parameters

| Parameter Name | Type       | Required | description                 |
| -------------- | ---------- | -------- | --------------------------- |
| ids            | `string[]` | Yes      | Array of IDs to be deleted. |

## Return value

Type: Promise

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
