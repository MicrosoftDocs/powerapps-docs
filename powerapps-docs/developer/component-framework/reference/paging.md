---
title: Paging | Microsoft Docs
description: Provides properties and methods to work with paging.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/12/2021

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 12891e96-972c-4289-bbde-2bc261cd1f12
---

# Paging

[!INCLUDE [paging-description](includes/paging-description.md)]

## Available for

Model-driven and canvas apps

## Properties

## firstPageNumber

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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
