---
title: DataProviderCapabilities (Power Apps component framework API reference) | Microsoft Docs
description: Provides methods to use dataset capabilities.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# DataProviderCapabilities

[!INCLUDE [dataprovidercapabilities-description](includes/dataprovidercapabilities-description.md)]

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

**Type**: `boolean`

### hasRecordNavigation

Whether the dataset supports record navigation for lookup and primary fields.

**Type**: `boolean`

### hasCellImageInfo

Whether image info for record columns can be retrieved.

**Type** `boolean`

## Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
