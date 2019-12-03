---
title: DataSet | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0202d51f-e9a9-4a2e-b3e9-0bfd7f6afb86
---

# DataSet

[!INCLUDE [dataset-description](includes/dataset-description.md)]

## Available for 

Model-driven apps

## Properties

### addColumn()

Adds  a column to the columnset

### Remarks

This method accept two parameters.

|Name|Type|Required|Description|
|------|-----|------|-----|
|name|`string`|Yes|Column name to be added to the dataset.|
|entityAlias|`string`|No| Entity alias for which the column name needs to be added.|

### columns

The set of columns available in this dataset.

**Type**: [Column](column.md)[]

### error

Whether an error occurred in data retrieval.

**Type**: `boolean`

### errorMessage

The error message associated with the last encountered error, if applicable.

**Type**: `string`

### filtering

The column filtering for the current query.

**Type**: [Filtering](filtering.md)

### linking

Defines the linked entity information.

**Type**: [Linking](linking.md)

### loading

Indicates whether the dataset is loading or not.

**Type**: `boolean`

### paging

Pagination status and actions.

**Type**: [Paging](paging.md)

### records

Map of IDs to the full record object.

**Type**: [EntityRecord](entityrecord.md)

### sortedRecordIds

IDs of the records in the dataset, order by the query response result.

**Type**: `string[]`

### sorting

The sorting status for the current query.

**Type**: [SortStatus](sortstatus.md)

## Methods

|Method | Description | 
| ------------- |-------------|
|[clearSelectedRecordIds](dataset/clearselectedrecordids.md)|[!INCLUDE [clearselectedrecordids-description](dataset/includes/clearselectedrecordids-description.md)]| 
|[getSelectedRecordIds](dataset/getselectedrecordids.md)|[!INCLUDE [getselectedrecordids-description](dataset/includes/getselectedrecordids-description.md)]| 
|[getTargetEntityType](dataset/gettargetentitytype.md)|[!INCLUDE [gettargetentitytype-description](dataset/includes/gettargetentitytype-description.md)]| 
|[getTitle](dataset/gettitle.md)|[!INCLUDE [gettitle-description](dataset/includes/gettitle-description.md)]| 
|[getViewId](dataset/getviewid.md)|[!INCLUDE [getviewid-description](dataset/includes/getviewid-description.md)]| 
|[openDatasetItem](dataset/opendatasetitem.md)|[!INCLUDE [opendatasetitem-description](dataset/includes/opendatasetitem-description.md)]| 
|[refresh](dataset/refresh.md)|[!INCLUDE [refresh-description](dataset/includes/refresh-description.md)]| 
|[setSelectedRecordIds](dataset/setselectedrecordids.md)|[!INCLUDE [setselectedrecordids-description](dataset/includes/setselectedrecordids-description.md)]| 

## Example

To learn more about how to implement the dataset methods, see [DataSet Grid component](../sample-controls/data-set-grid-control.md)

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)