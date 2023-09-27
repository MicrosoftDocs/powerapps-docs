---
title: loadNextPage (Power Apps component framework API reference) | Microsoft Docs
description: Request the next page of results to be loaded.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# loadNextPage

[!INCLUDE [loadnextpage-description](includes/loadnextpage-description.md)]

> [!NOTE]
> `loadNextPage` does not support parallel execution.
> Executing `loadNextPage` will trigger `updateView` on the control with newly fetched results.

## Available for

Model-driven and canvas apps

## Syntax

`loadNextPage()`

### Related articles

[Paging](../paging.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
