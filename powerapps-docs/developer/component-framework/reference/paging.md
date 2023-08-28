---
title: Paging (Power Apps component framework API reference) | Microsoft Docs
description: Provides properties and methods to work with paging.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 06/14/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Paging

[!INCLUDE [paging-description](includes/paging-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### firstPageNumber

First page number.

**Type**: `number`

### hasNextPage

Whether the result set can be paged forwards.

**Type**: `boolean`

### hasPreviousPage

Whether the result set can be paged backwards.

**Type**: `boolean`

### lastPageNumber

Last page number.

**Type**: `number`

### pageNumber

Page Number. Same as firstPageNumber. Used in exposed interfaces where firstPageNumber and lastPageNumber is not available.

**Type**: `number`

### pageSize

The pageSize of the paging.

**Type**: `number`

### totalResultCount

Total number of results on the server for the current query.
In case when value is not available `-1` is sent.

**Type**: `number`

> [!NOTE]
> For Canvas Apps `totalResultCount` will not always show the total number of records a table has. Because of [delegation](../../../maker/canvas-apps/delegation-overview.md), it will return a value divisible by 500 until the last set of records is reached.
>
>Let's say that a table has 1022 records in it. Your page size is 100. The following table shows the `totalResultCount` value you can expect for each page:
>
>|Page  |Value  |
>|----|----|
>|1|500|
>|2|500|
>|3|500|
>|4|500|
>|5|500|
>|6|1000|
>|7|1000|
>|8|1000|
>|9|1000|
>|10|1000|
>|11|1022|

## Methods

| Method                                         | Description                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [loadExactPage](paging/loadExactPage.md)       | [!INCLUDE [loadexactpage-description](paging/includes/loadexactpage-description.md)]       |
| [loadNextPage](paging/loadnextpage.md)         | [!INCLUDE [loadnextpage-description](paging/includes/loadnextpage-description.md)]         |
| [loadPreviousPage](paging/loadpreviouspage.md) | [!INCLUDE [loadpreviouspage-description](paging/includes/loadpreviouspage-description.md)] |
| [reset](paging/reset.md)                       | [!INCLUDE [reset-description](paging/includes/reset-description.md)]                       |
| [setPageSize](paging/setpagesize.md)           | [!INCLUDE [setpagesize-description](paging/includes/setpagesize-description.md)]           |

## Limitations

> [!NOTE]
> `loadExactPage`, `loadNextPage`, `loadPreviousPage` do not support parallel execution.
> Executing any of them will trigger `updateView` on the control with newly fetched results.

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)<br/>
[Data source delegation limitations](../../../maker/canvas-apps/delegation-overview.md#changing-the-limit)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
