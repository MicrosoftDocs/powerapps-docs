---
title: DataSet (Power Apps component framework API reference) | Microsoft Docs
description: Learn how to use different methods and properties available for DatSet in Power Apps component framework.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# DataSet

[!INCLUDE [dataset-description](includes/dataset-description.md)]

## Available for

Model-driven and canvas apps.

## Properties

### columns

The set of columns available in this dataset. Supported in both model-driven and canvas apps.

**Type**: [Column](column.md)[]

### error

Whether an error occurred in data retrieval. Supported in both model-driven and canvas apps.

**Type**: `boolean`

### errorCode

The error code associated with the last encountered error, if applicable.

### errorMessage

The error message associated with the last encountered error, if applicable.

**Type**: `number | string`

### filtering

The column filtering for the current query. Supported in both model-driven and canvas apps. Filtering can be configured for a dataset by setting `context.parameters.[dataset_property_name].filtering.setFilter(<filterExpression>)`. Once filter is set, calling `context.parameters.[dataset_property_name].refresh()` retrieves the filtered data from the data source.

| Value | Conditional operator  | Model-driven apps | Canvas apps |
| ----- | --------------------- | ----------------- | ----------- |
| -1    | None                  | Yes               | Yes         |
| 0     | Equal                 | Yes               | Yes         |
| 1     | NotEqual              | Yes               | Yes         |
| 2     | GreaterThan           | Yes               | Yes         |
| 3     | LessThan              | Yes               | Yes         |
| 4     | GreaterEqual          | Yes               | Yes         |
| 5     | LessEqual             | Yes               | Yes         |
| 6     | Like                  | Yes               | Yes         |
| 7     | NotLike               | No                | Yes         |
| 8     | In                    | Yes               | Yes         |
| 12    | Null                  | Yes               | Yes         |
| 13    | NotNull               | No                | Yes         |
| 14    | Yesterday             | Yes               | No          |
| 15    | Today                 | Yes               | No          |
| 16    | Tomorrow              | Yes               | No          |
| 17    | Last7Days             | Yes               | No          |
| 18    | Next7Days             | Yes               | No          |
| 19    | LastWeek              | Yes               | No          |
| 20    | ThisWeek              | Yes               | No          |
| 22    | LastMonth             | Yes               | No          |
| 23    | ThisMonth             | Yes               | No          |
| 25    | On                    | Yes               | No          |
| 26    | OnOrBefore            | Yes               | No          |
| 27    | OnOrAfter             | Yes               | No          |
| 28    | LastYear              | Yes               | No          |
| 29    | ThisYear              | Yes               | No          |
| 33    | LastXDays             | Yes               | No          |
| 34    | NextXDays             | Yes               | No          |
| 37    | LastXMonths           | Yes               | No          |
| 38    | NextXMonths           | Yes               | No          |
| 49    | Contains              | Yes               | Yes         |
| 54    | BeginWith             | No                | Yes         |
| 55    | DoesNotBeginWidth     | No                | Yes         |
| 56    | EndsWidth             | No                | Yes         |
| 57    | DesNotEndWith         | No                | Yes         |
| 70    | InFiscalPeriodAndYear | Yes               | No          |
| 75    | Above                 | Yes               | Yes         |
| 76    | Under                 | Yes               | Yes         |
| 77    | NotUnder              | Yes               | Yes         |
| 78    | AboveOrEqual          | Yes               | Yes         |
| 79    | UnderOrEqual          | Yes               | Yes         |
| 87    | ContainValues         | Yes               | Yes         |
| 88    | DoesNotContainValues  | No                | Yes         |

> [!NOTE]
> Filtering feature is only available to Dataverse data source.

**Type**: [Filtering](filtering.md)

### linking

Defines the linked table information. Supported only in model-driven apps.

**Type**: [Linking](linking.md)

### loading

Indicates whether the dataset is loading or not. Supported in both model-driven and canvas apps.

**Type**: `boolean`

### paging

Pagination status and actions. Supported in both model-driven and canvas apps. Paging info can be accessed and configured for a dataset using `context.parameters.[dataset_property_name].paging `.

> [!NOTE]
> Dataverse data source does not return the `totalRecordCount` in paging object for canvas apps. Instead, it uses `hasNextPage` and `hasPreviousPage` to check if there are more records to be fetched.

Dataset components can use `context.parameters.[dataset_property_name].paging.setPageSize(pageSize)` to change the number of records retrieved per page.

**Type**: [Paging](paging.md)

### records

Map of IDs to the full record object. Supported in both model-driven and canvas apps.

**Type**: [EntityRecord](entityrecord.md)

### sortedRecordIds

IDs of the records in the dataset, order by the query response result. Supported in both model-driven and canvas apps.

**Type**: `string[]`

### sorting

The sorting status for the current query. Supported in both model-driven and canvas apps. Sorting can be configured for a dataset by setting `context.parameters.[dataset_property_name].sorting = [SortStatus]`. Once sorting is configured, calling `context.parameters.[dataset_property_name].refresh()` retrieves the sorted data from the data source.

> [!NOTE]
> Sorting feature is only available to Dataverse data source.
> Also, if sorting is re-configured it will reset the filter `context.parameters.[dataset_property_name].filtering`

**Type**: [SortStatus](sortstatus.md)[]

## Methods

| Method                                                      | Description                                                                                             | Available for                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [addColumn](dataset/addcolumn.md)                           | [!INCLUDE [addcolumn-description](dataset/includes/addcolumn-description.md)]                           | Model-driven apps            |
| [clearSelectedRecordIds](dataset/clearselectedrecordids.md) | [!INCLUDE [clearselectedrecordids-description](dataset/includes/clearselectedrecordids-description.md)] | Model-driven and Canvas apps |
| [delete](dataset/delete.md)                                 | [!INCLUDE [delete-description](dataset/includes/delete-description.md)]                                 | Canvas apps                  |
| [getCommands](dataset/getCommands.md)                       | [!INCLUDE [getcommands-description](dataset/includes/getcommands-description.md)]                       | Canvas apps                  |
| [getDataSetCapabilities](dataset/getDataSetCapabilities.md) | [!INCLUDE [getcatasetcapabilities-description](dataset/includes/getdatasetcapabilities-description.md)] | Canvas apps                  |
| [getSelectedRecordIds](dataset/getSelectedRecordIds.md)     | [!INCLUDE [getselectedrecordids-description](dataset/includes/getselectedrecordids-description.md)]     | Model-driven and Canvas apps |
| [getTargetEntityType](dataset/getTargetEntityType.md)       | [!INCLUDE [gettargetentitytype-description](dataset/includes/gettargetentitytype-description.md)]       | Model-driven and Canvas apps |
| [getTitle](dataset/getTitle.md)                             | [!INCLUDE [gettitle-description](dataset/includes/gettitle-description.md)]                             | Model-driven and Canvas apps |
| [getViewId](dataset/getViewId.md)                           | [!INCLUDE [getviewid-description](dataset/includes/getviewId-description.md)]                           | Model-driven and Canvas apps |
| [newRecord](dataset/newRecord.md)                           | [!INCLUDE [newrecord-description](dataset/includes/newrecord-description.md)]                           | Canvas apps                  |
| [openDatasetItem](dataset/openDatasetItem.md)               | [!INCLUDE [opendatasetitem-description](dataset/includes/opendatasetitem-description.md)]               | Model-driven and Canvas apps |
| [refresh](dataset/refresh.md)                               | [!INCLUDE [refresh-description](dataset/includes/refresh-description.md)]                               | Model-driven and Canvas apps |
| [retrieveRecordCommand](dataset/retrieveRecordCommand.md)   | [!INCLUDE [retrieverecordcommand-description](dataset/includes/retrieverecordcommand-description.md)]   | Model-driven                 |
| [setSelectedRecordIds](dataset/setselectedrecordids.md)     | [!INCLUDE [setselectedrecordids-description](dataset/includes/setselectedrecordids-description.md)]     | Model-driven and Canvas apps |

## Lookup columns

Dataverse table's lookup columns can now be retrieved. For canvas apps, if a lookup column is included in the dataset, all columns in the referred record are retrieved. `GetFormattedValue` returns the JSON string for this column. `GetValue` method returns the JSON object directly.

## Example

To learn more about how to implement the dataset methods, see [DataSet Grid component](../sample-controls/data-set-grid-control.md)

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
