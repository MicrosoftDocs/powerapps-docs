---
title: Paging | Microsoft Docs
description: Provides properties and methods to work with paging.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
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

### totalResultCount

Total number of results on the server for the current query.

**Type**: `number`

### hasNextPage

Whether the result set can be paged forwards.

**Type**: `boolean`

### hasPreviousPage

Whether the result set can be paged backwards.

**Type**: `boolean`

## Methods

|Method | Description |
| ------|-------------|
|[loadNextPage](paging/loadnextpage.md)|[!INCLUDE [loadnextpage-description](paging/includes/loadnextpage-description.md)]|
|[loadPreviousPage](paging/loadpreviouspage.md)|[!INCLUDE [loadpreviouspage-description](paging/includes/loadpreviouspage-description.md)]|
|[reset](paging/reset.md)|[!INCLUDE [reset-description](paging/includes/reset-description.md)]|
|[setPageSize](paging/setpagesize.md)|[!INCLUDE [setpagesize-description](paging/includes/setpagesize-description.md)]|
|pageSize|The number of records to return per dataset page. On forms, dataset pageSize goes with the formatting (Number of rows) and on others you can choose your personal options.|


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
