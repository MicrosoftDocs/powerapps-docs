---
title: Aggregate data using OData
description: Learn how to use OData to retrieve aggregated data from Microsoft Dataverse Web API.
ms.date: 07/01/2024
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Aggregate data using OData

## Example

## Distinct column values

## Grouping

### Grouping by parts of a date

#### Fiscal period date grouping example


## OData aggregation limitations

This section describes capabilities that are available using aggregation with FetchXml that are not currently available using OData.

### Get distinct number with CountColumn

You can't get a distinct number of values using [CountColumn](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType.CountColumn) with OData. [Learn about distinct column values using FetchXml](../../fetchxml/aggregate-data.md#distinct-column-values)


### Time zone when grouping by date

Grouping by parts of a date always uses UTC time and there is no way to specify that the user's time zone should be used instead [available in FetchXml](../../fetchxml/aggregate-data.md#grouping-by-parts-of-a-date)


### Row aggregate

When a table has a [hierarchical relationship defined](../../../../maker/data-platform/query-visualize-hierarchical-data.md), you can't return a row aggregate on the lookup column for the hierarchical relationship. [Learn about row aggregates using FetchXml](../../fetchxml/aggregate-data.md#row-aggregate)



### Per query limit

There is no way to specify a configurable aggregate limit. [Learn about per query limits using FetchXml](../../fetchxml/aggregate-data.md#per-query-limit)


[!INCLUDE [cc-query-aggregation-limitations](../../includes/cc-query-aggregation-limitations.md)]

## Next steps

Learn how to count rows.

> [!div class="nextstepaction"]
> [Count rows](count-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]