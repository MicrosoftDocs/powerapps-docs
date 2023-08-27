---
title: loadExactPage (Power Apps component framework API reference) | Microsoft Docs
description: Request the exact page of results to be loaded.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# loadExactPage

[!INCLUDE [loadexactpage-description](includes/loadexactpage-description.md)]

> [!NOTE]
> `loadExactPage` does not support parallel execution.
> Executing `loadExactPage` will trigger `updateView` on the control with newly fetched results.

## Available for

Model-driven and canvas apps

## Syntax

`loadExactPage(pageNumber)`

## Parameters

| Parameter Name | Type     | Required | Description            |
| -------------- | -------- | -------- | ---------------------- |
| pageNumber     | `Number` | Yes      | Pagesize to be loaded. |

### Related articles

[Paging](../paging.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
