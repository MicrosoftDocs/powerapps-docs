---
title: delete | Microsoft Docs
description: Delete the records from data source.
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

# delete

[!INCLUDE[./includes/delete-description.md](./includes/delete-description.md)]

## Available for

Limited support for canvas apps

## Syntax

`context.parameters.dataset.delete(ids)`

## Parameters

| Parameter Name | Type       | Required | description                 |
| -------------- | ---------- | -------- | --------------------------- |
| ids            | `string[]` | Yes      | Array of IDs to be deleted. |

## Return value

Type: Promise

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
