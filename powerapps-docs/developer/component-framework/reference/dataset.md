---
title: DataSet in Microsoft Dataverse| Microsoft Docs
description: Learn how to use different methods and properties available for DatSet in Power Apps component framework.
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

Model-driven and canvas apps.

## Properties

### addColumn

Adds  a column to the columnset. This is supported only in model-driven apps. Dataset components can request additional columns on top of already selected `fields` in the dataset.

`context.parameters.[dataset_property_name].addColumn("columnName")`

### Remarks

This method accept two parameters.

|Name|Type|Required|Description|
|------|-----|------|-----|
|name|`string`|Yes|Column name to be added to the dataset.|
|entityAlias|`string`|No| Table alias for which the column name needs to be added.|

### columns

The set of columns available in this dataset. This is supported in both model-driven and canvas apps.

**Type**: [Column](column.md)[]

### error

Whether an error occurred in data retrieval. This is supported in both model-driven and canvas apps.

**Type**: `boolean`

### errorMessage

The error message associated with the last encountered error, if applicable. This is supported in both model-driven and canvas apps.

**Type**: `string`

### filtering

The column filtering for the current query. This is supported in both model-driven and canvas apps. Filtering can be configured for a dataset by setting `context.parameters.[dataset_property_name].filtering.setFilter(<filterExpression>)`. Once filter is set, calling `context.parameters.[dataset_property_name].refresh()`  retrieves the filtered data from the data source.  

|Value|Conditional operator|Model-driven apps| Canvas apps|
|------|--------|-------------------|----------------|
|-1|None|Yes|Yes|
|0|Equal|Yes|Yes|
|1|NotEqual|Yes|Yes|
|2|GreaterThan|Yes|Yes|
|3|LessThan|Yes|Yes|
|4|GreaterEqual|Yes|Yes|
|5|LessEqual|Yes|Yes|
|6|Like|Yes|Yes|
|7|NotLike|No|Yes|
|8|In|Yes|Yes|
|12|Null|Yes|Yes|
|13|NotNull|No|Yes|
|14|Yesterday|Yes|No|
|15|Today|Yes|No|
|16|Tomorrow|Yes|No|
|17|Last7Days|Yes|No|
|18|Next7Days|Yes|No|
|19|LastWeek|Yes|No|
|20|ThisWeek|Yes|No|
|22|LastMonth|Yes|No|
|23|ThisMonth|Yes|No|
|25|On|Yes|No|
|26|OnOrBefore|Yes|No|
|27|OnOrAfter|Yes|No|
|28|LastYear|Yes|No|
|29|ThisYear|Yes|No|
|33|LastXDays|Yes|No|
|34|NextXDays|Yes|No|
|37|LastXMonths|Yes|No|
|38|NextXMonths|Yes|No|
|49|Contains|Yes|Yes|
|54|BeginWith|No|Yes|
|55|DoesNotBeginWidth|No|Yes|
|56|EndsWidth|No|Yes|
|57|DesNotEndWith|No|Yes|
|70|InFiscalPeriodAndYear|Yes|No|
|75|Above|Yes|Yes|
|76|Under|Yes|Yes|
|77|NotUnder|Yes|Yes|
|78|AboveOrEqual|Yes|Yes|
|79|UnderOrEqual|Yes|Yes|
|87|ContainValues|Yes|Yes|
|88|DoesNotContainValues|No|Yes|


> [!NOTE]
> Filtering feature is only available to Dataverse data source. 

**Type**: [Filtering](filtering.md)

### getTargetEntity

Allows the component to retrieve the logical name of the current Dataverse table. If the current data source is not a Dataverse table , this method returns null.

### linking

Defines the linked table information. This is supported only in model-driven  apps.

**Type**: [Linking](linking.md)

### loading

Indicates whether the dataset is loading or not. This is supported in both model-driven and canvas apps.

**Type**: `boolean`

### paging

Pagination status and actions. This is supported in both model-driven and canvas apps. Paging info can be accessed and configured for a dataset using `context.parameters.[dataset_property_name].paging `.

> [!NOTE]
> Dataverse data source  does not return the `totalRecordCount` in paging object for canvas apps. Instead, it uses `hasNextPage` and `hasPreviousPage` to check if there are more records to be fetched.  

Dataset components can use `context.parameters.[dataset_property_name].paging.setPageSize(pageSize)` to change the number of records retrieved per page.  

**Type**: [Paging](paging.md)

### records

Map of IDs to the full record object. This is supported in both model-driven and canvas apps.

**Type**: [EntityRecord](entityrecord.md)

### sortedRecordIds

IDs of the records in the dataset, order by the query response result. This is supported in both model-driven and canvas apps.

**Type**: `string[]`

### sorting

The sorting status for the current query. This is supported in both model-driven and canvas apps. Sorting can be configured for a dataset by setting `context.parameters.[dataset_property_name].sorting = [SortStatus]`. Once sorting is configured, calling `context.parameters.[dataset_property_name].refresh()` retrieves the sorted data from the data source.  

> [!NOTE]
> Sorting feature is only available to Dataverse data source.
> Also, if sorting is re-configured it will reset the filter `context.parameters.[dataset_property_name].filtering`

**Type**: [SortStatus](sortstatus.md)

### Lookup columns

Dataverse table's lookup columns can now be retrieved.For canvas apps if a lookup column is included in the dataset , all columns in the referred record will be retrieved.  `GetFormattedValue` returns the JSON string for this column. `GetValue` method returns the JSON object directly.

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

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
