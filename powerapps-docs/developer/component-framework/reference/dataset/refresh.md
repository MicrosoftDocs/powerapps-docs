---
title: refresh (Power Apps component framework API reference) | Microsoft Docs
description: Refreshes the dataset based on filters, sorting, linking, new column.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# refresh

[!INCLUDE[./includes/refresh-description.md](./includes/refresh-description.md)]

> [!NOTE]
> `refresh` does not support parallel execution.
> Executing `refresh` will trigger `updateView` on the control with newly fetched results.

## Available for

Model-driven and canvas apps

## Syntax

`context.parameters.dataset.refresh()`

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
