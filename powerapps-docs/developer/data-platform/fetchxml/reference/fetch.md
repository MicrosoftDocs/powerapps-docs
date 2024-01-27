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
|`aggregatelimit`|No|Set a limit below the standard 50,000  record aggregate limit. [Learn about aggregate limits](../aggregate-data.md#limitations) |
|`count`|No|Positive integer value to specify the number of records to return in a page. [Learn about paging results](../page-results.md) |
|`distinct`|No|Boolean value to specify that duplicate rows not be included in the results. [Learn more about returning distinct results](#returning-distinct-results)|
|`latematerialize`|No|Boolean value to direct the query to be broken up into smaller parts and reassemble the results before returning them. This may improve performance for some long-running queries. [Learn more about using Late Materialize query](../optimize-performance.md#late-materialize-query). |
|`no-lock`|No|Legacy setting to prevent shared locks on records. [No longer necessary](../optimize-performance.md#no-lock). |
|`options`|No|A string value to apply one or more SQL optimizations. See [Options](#options)|
|`page`|No|Positive integer value to specify the page number to return. [Learn about paging results](../page-results.md)|
|`paging-cookie`|No|String value from a previous page of data to make retrieving the next page of data more efficient. [Learn about paging results](../page-results.md) |
|`returntotalrecordcount`|No|Boolean value to specify whether the total number of records matching the criteria is returned. [Learn how to count rows using FetchXml](../count-rows.md)|
|`top`|No|Positive integer value to specify the number of records to return. This value cannot exceed 5,000. [Learn more about limiting the number of rows](../overview.md#limit-the-number-of-rows)|
|`datasource`|No|When using Dataverse long term data retention, set this to `'retained'` to indicate the query is for retained rows only. [Learn more about Dataverse long term data retention](../../../../maker/data-platform/data-retention-overview.md)|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[entity](entity.md)|1|[!INCLUDE [entity-description](includes/entity-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]

## Options

> [!IMPORTANT]
> Only apply these options when recommended by Microsoft technical support. Incorrect use of these options can damage the performance of a query.

Use these values with the `options` attribute to specify these SQL Server hints are applied to the query. When more than one option is set, separate them by commas.

```text
options='OptimizeForUnknown,DisableRowGoal,Recompile'
```

[!INCLUDE [fetch-options-table](includes/fetch-options-table.md)]


## Returning distinct results

Use the [fetch element](reference/fetch.md) `distinct` attribute to require the query to exclude any duplicate values in the results.

If you use the `distinct` attribute, you must add at least one order element to have consistent paging.

When you use the `distinct` attribute, the results returned don't include primary key values for each record because they represent an aggregation of all the distinct values.

