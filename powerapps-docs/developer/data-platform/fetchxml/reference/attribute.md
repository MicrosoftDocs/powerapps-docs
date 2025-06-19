---
title: attribute element
description: Use this element to specify which columns in the containing entity or link-entity element should be returned.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 07/12/2024
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
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
|`aggregate`|No|The [aggregate function](#aggregate-functions) to apply. [Learn how to aggregate data with FetchXml](../aggregate-data.md)|
|`alias`|No|The name of the column to return. Each column must have a unique name. You'll use aliases when you retrieve aggregate values. [Learn more about column aliases](../select-columns.md#column-aliases).|
|`dategrouping`|No|When you group data by a datetime value, this attribute specifies the date part to use. See [Date grouping options](#date-grouping-options)|
|`distinct`|No|When you use the aggregate `countcolumn` function, this attribute specifies that only unique values for the column are returned. [Learn more about distinct column values](../aggregate-data.md#distinct-column-values).|
|`groupby`|No|When you aggregate data, this attribute specifies the column to use to group the data. [Learn more about grouping](../aggregate-data.md#grouping).|
|`name`|Yes|The logical name of the column.|
|`rowaggregate`|No|When this value is set to `CountChildren` a value that includes the total number of child records for the record is included in the results. [Learn how to use this attribute](../../query-hierarchical-data.md#retrieve-the-number-of-hierarchically-related-child-records).|
|`usertimezone`|No|Used by aggregate queries that group by datetime columns. Depending on the time zone, the same datetime value can fall in different days. [Learn about grouping by parts of a date](../aggregate-data.md#grouping-by-parts-of-a-date)<br /><br />Use this attribute with a `false` value to force the grouping to use UTC value. When you don't set this attribute, the default value is `true`, and the user's time zone is used.<br /><br />**Note**: With QueryExpression, the grouping always uses UTC. When using the SDK [FetchXmlToQueryExpressionRequest class](/dotnet/api/microsoft.crm.sdk.messages.fetchxmltoqueryexpressionrequest), this setting is lost. There's [no way to set this using QueryExpression](../../org-service/queryexpression/aggregate-data.md#time-zone-when-grouping-by-date).|

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|


## Aggregate functions

Use these aggregate functions. [Learn how to aggregate data with FetchXml](../aggregate-data.md)

[!INCLUDE [aggregate-function-table](includes/aggregate-function-table.md)]

## Date grouping options

[Learn more about grouping by parts of a date](../aggregate-data.md#grouping-by-parts-of-a-date)

[!INCLUDE [dategrouping-table](includes/dategrouping-table.md)]

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]