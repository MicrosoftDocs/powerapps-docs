---
title: DataSet | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0202d51f-e9a9-4a2e-b3e9-0bfd7f6afb86
---

# DataSet

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [dataset-description](includes/dataset-description.md)]

## Available for 

Model-driven apps

## Properties

### addColumn

The function to add a column to the dataset

**Type**: `function`<br />
**Optional**

### Remarks

This function must accept two parameters.

|Name|Type|Required|Description|
|-|-|-|-|
|name|string|Yes|Column name to be added to the dataset|
|entityalias|string|No| Alias for which the column name needs to be added|

### columns

The set of columns available in this dataset.

**Type**: [Column](column.md)[]

### error

Whether an error occurred in data retrieval.

**Type**: `boolean`

### errorMessage

The error message associated with the last encountered error.

**Type**: `string`

### filtering

Placeholder description: IDataSetExposedParameter.name
<!-- 
QUESTION: This description doesn't seem right
'The column sorting for the current query.' 
-->

**Type**: [Filtering](filtering.md)

### linking

Placeholder description: IDataSetExposedParameter.name

**Type**: [Linking](linking.md)

### loading

Whether the dataset is loading.

**Type**: `boolean`

### paging

Pagination status and actions.

**Type**: [Paging](paging.md)

### records

Map of IDs to the full record object.

**Type**: `object`

### sortedRecordIds

IDs of the records in the dataset, in order.

**Type**: `string[]`

### sorting

The column sorting for the current query.

**Type**: [Sort](sortstatus.md)

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


### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)