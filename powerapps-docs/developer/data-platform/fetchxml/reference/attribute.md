---
title: attribute element
description: Use this element to specify which columns in the containing entity or link-entity element should be returned.
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
# attribute element

[!INCLUDE [attribute-description](includes/attribute-description.md)]

[Learn how to select columns using FetchXml](../select-columns.md).

## Example

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <link-entity name='contact'
      from='contactid'
      to='primarycontactid'
      link-type='inner'
      alias='contact'>
      <attribute name='fullname' />
    </link-entity>
  </entity>
</fetch>
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`addedby`|No|REMOVE?|
|`aggregate`|No|The [aggregate function](#aggregate-functions) to apply. [Learn how to aggregate data with FetchXml](../aggregate-data.md)|
|`alias`|No|The name of the column to return. Each column must have a unique name. Usually used when retrieving aggregate values. [Learn more about column aliases](../select-columns.md#column-aliases).|
|`build`|No|REMOVE?|
|`dategrouping`|No|When grouping data by a datetime value, specifies the date part to use. See [Date grouping options](#date-grouping-options)|
|`distinct`|No|When using the aggregate `countcolumn` function, specifies that only unique values for the column are returned. [Learn more about distinct column values](../aggregate-data.md#distinct-column-values).|
|`groupby`|No|When aggregating data, specifies the column to use to group the data. [Learn more about grouping](../aggregate-data.md#grouping).|
|`latematerialize`|No|Boolean attribute to direct the server to apply late materialization strategy to improve preformance. [Learn how to use this attribute](../optimize-performance.md#late-materialize-query).|
|`name`|Yes|The logical name of the column.|
|`rowaggregate`|No|When this value is set to `CountChildren` a value that includes the total number of child records for the record is included in the results. [Learn how to use this attribute](../../query-hierarchical-data.md#retrieve-the-number-of-hierarchically-related-child-records).|
|`usertimezone`|No|REMOVE?|


## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|


## Aggregate functions

These are the aggregate functions you can use. [Learn how to aggregate data with FetchXml](../aggregate-data.md)

[!INCLUDE [aggregate-function-table](includes/aggregate-function-table.md)]

## Date grouping options

[Learn more about grouping by parts of a date](../aggregate-data.md#grouping-by-parts-of-a-date)

[!INCLUDE [dategrouping-table](includes/dategrouping-table.md)]

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]