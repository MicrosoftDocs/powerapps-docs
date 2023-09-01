---
title: fetch element
description: Use this element as the root element in the query.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 08/31/2023
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# fetch element

[!INCLUDE [fetch-description](includes/fetch-description.md)]

[Learn how to query data using FetchXml](../overview.md).

## Example

```xml
<fetch>
  <entity name='account' />
</fetch>
```


## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`aggregate`|No|Boolean value to specify that the query returns aggregate values. [Learn about aggregating data](../aggregate-data.md)|
|`aggregatelimit`|No|TODO?|
|`count`|No|Positive integer value to specify the number of records to return in a page. [Learn about paging results](../page-results.md) |
|`distinct`|No|Boolean value to specify that duplicate rows not be included in the results. [Learn more about returning distinct results](../filter-rows.md#returning-distinct-results)|
|`mapping`|No|REMOVE?|
|`min-active-row-version`|No|REMOVE?|
|`no-lock`|No|Boolean value to specify that read locks not be placed on the tables in the query.|
|`options`|No|A string value to apply one or more SQL optimizations. See [Options](#options)|
|`output-format`|No|REMOVE?|
|`page`|No|Positive integer value to specify the page number to return. [Learn about paging results](../page-results.md)|
|`paging-cookie`|No|String value from a previous page of data to make retrieving the next page of data more efficient. [Learn about paging results](../page-results.md) |
|`returntotalrecordcount`|No|Boolean value to specify whether the total number of records matching the criteria is returned. |
|`top`|No|Positive integer value to specify the number of records to return. This value cannot exceed 5,000. L[earn more about limiting the number of rows](../filter-rows.md#limit-the-number-of-rows)|
|`utc-offset`|No|TODO?|
|`version`|No|REMOVE?|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[entity element](entity.md)|1|[!INCLUDE [entity-description](includes/entity-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]

## Options

Use these values with the `options` attribute to specify these SQL Server hints are applied to the query. When more than one option is set, separate them by commas.

```text
options='OptimizeForUnknown,DisableRowGoal,Recompile'
``````

> [!IMPORTANT]
> These options are only recommended to be used by developers who fully understand how FetchXml is translated to SQL. Incorrect use of these options can damage the performance of a query.


|FetchXML option|SQL Server hint|
|---------|---------|
|`OptimizeForUnknown`|[Optimize for unknown](/sql/t-sql/queries/hints-transact-sql-query#optimize-for-unknown)|
|`ForceOrder`|[Force Order](/sql/t-sql/queries/hints-transact-sql-query#force-order)|
|`Recompile`|[recompile](/sql/t-sql/queries/hints-transact-sql-query#recompile)|
|`DisableRowGoal` |[Hint: `DISABLE_OPTIMIZER_ROWGOAL`](/sql/t-sql/queries/hints-transact-sql-query#use_hint)|
|`EnableOptimizerHotfixes`|[Hint: `ENABLE_QUERY_OPTIMIZER_HOTFIXES`](/sql/t-sql/queries/hints-transact-sql-query#use_hint)|
|`LoopJoin`|[Loop Join](/sql/t-sql/queries/hints-transact-sql-query#-loop--merge--hash--join)|
|`MergeJoin`|[Merge Join](/sql/t-sql/queries/hints-transact-sql-query#-loop--merge--hash--join)|
|`HashJoin`|[Hash Join](/sql/t-sql/queries/hints-transact-sql-query#-loop--merge--hash--join)|
|`NO_PERFORMANCE_SPOOL`|[NO_PERFORMANCE_SPOOL](/sql/t-sql/queries/hints-transact-sql-query#no_performance_spool)|
|`ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS`|[Hint: `ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS`](/sql/t-sql/queries/hints-transact-sql-query#use_hint)|

More information: [Hints (Transact-SQL) - Query](/sql/t-sql/queries/hints-transact-sql-query)

