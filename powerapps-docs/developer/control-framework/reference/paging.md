---
title: Paging | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 12891e96-972c-4289-bbde-2bc261cd1f12
---

# Paging

[!INCLUDE [paging-description](includes/paging-description.md)]

## totalResultCount

Total number of results on the server for the current query.

**Type**: `number`

## hasNextPage

Whether the result set can be paged backwards.

**Type**: `boolean`

## hasPreviousPage

Whether the result set can be paged backwards.

**Type**: `boolean`

## Methods

|Method | Description |
| ------|-------------|
|[loadNextPage](paging/loadnextpage.md)|[!INCLUDE [loadnextpage-description](paging/includes/loadnextpage-description.md)]|
|[loadPreviousPage](paging/loadpreviouspage.md)|[!INCLUDE [loadpreviouspage-description](paging/includes/loadpreviouspage-description.md)]|
|[reset](paging/reset.md)|[!INCLUDE [reset-description](paging/includes/reset-description.md)]|
|[setPageSize](paging/setpagesize.md)|[!INCLUDE [setpagesize-description](paging/includes/setpagesize-description.md)]|

### Related topics

[PowerApps Control Framework API Reference](index.md)<br />
[PowerApps Control Framework Overview](../overview.md)
