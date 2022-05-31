---
title: Paging | Microsoft Docs
description: Provides properties and methods to work with paging.
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
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

**Type**: `number`

## Methods

| Method                                         | Description                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [loadExactPage](paging/loadExactPage.md)       | [!INCLUDE [loadexactpage-description](paging/includes/loadexactpage-description.md)]       |
| [loadNextPage](paging/loadnextpage.md)         | [!INCLUDE [loadnextpage-description](paging/includes/loadnextpage-description.md)]         |
| [loadPreviousPage](paging/loadpreviouspage.md) | [!INCLUDE [loadpreviouspage-description](paging/includes/loadpreviouspage-description.md)] |
| [reset](paging/reset.md)                       | [!INCLUDE [reset-description](paging/includes/reset-description.md)]                       |
| [setPageSize](paging/setpagesize.md)           | [!INCLUDE [setpagesize-description](paging/includes/setpagesize-description.md)]           |

## Limitations

For Canvas Apps `totalResultCount` is working in 500 divisible stages. When entity has total amount of records more than 500 (and let assume that page size is 100), for page range: from `firstPage`: 1 to `lastPage`: 5, `totalResultCount` will be showing 500. Then for a `lastPage`: 6, `totalResultCount`: will show 1000 in case there are more than 1000 records or will show specific number that indicates total records for the entity.

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)
[Data source delegation limitations](/powerapps-docs/maker/canvas-apps/delegation-overview#changing-the-limit)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
