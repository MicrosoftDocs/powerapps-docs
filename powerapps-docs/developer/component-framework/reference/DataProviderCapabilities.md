---
title: DataProviderCapabilities | Microsoft Docs
description: Provides methods to use dataset capabilities.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 12/13/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8907f07a-ad45-47e4-a503-8eaae9bba5f7
---

# DataProviderCapabilities

Provides access to all the properties of a file.

## Available for

Canvas apps

## Properties

### isEditable

If the data provider has edit capabilities.

**Type**: `boolean`

### isFilterable

If the dataset can be filtered.

**Type**: boolean

### isSortable

If the dataset can be sorted.

**Type**: `boolean`

### canPaginate

If the dataset records can be paged.

**Type**: `boolean`

### canCreateNewRecords

Whether adding new records is supported or not.

**Type** `boolean`

## Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
