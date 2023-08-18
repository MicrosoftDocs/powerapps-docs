---
title: loadPreviousPage (Power Apps component framework API reference) | Microsoft Docs
description: Request the previous page of results to be loaded.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# loadPreviousPage

[!INCLUDE [loadpreviouspage-description](includes/loadpreviouspage-description.md)]

> [!NOTE]
> `loadPreviousPage` does not support parallel execution.
> Executing `loadPreviousPage` will trigger `updateView` on the control with newly fetched results.

## Available for

Model-driven and canvas apps

## Syntax

`loadPreviousPage()`

### Related articles

[Paging](../paging.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
