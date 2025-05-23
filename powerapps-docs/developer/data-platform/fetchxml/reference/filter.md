---
title: filter element
description: Use this element to specify a set of conditions to be evaluated for each row of the containing entity or link-entity element that determines if the row is returned.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 02/29/2024
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
# filter element

[!INCLUDE [filter-description](includes/filter-description.md)]

[Learn how to filter rows using FetchXml](../filter-rows.md).

## Example

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <filter type='and'>
      <condition attribute='address1_city'
        operator='eq'
        value='Redmond' />
    </filter>
  </entity>
</fetch>
```


## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`type`|No|Use `and` or `or`. Whether all (`and`) or any (`or`) [conditions](condition.md) within the filter must be met.|
|`hint`|No|Use this attribute to set the `union` hint to get a performance benefit for a specific type of query. [Learn how to use the union hint](../optimize-performance.md#union-hint)|
|`isquickfindfields`|No| Use this attribute to tell Dataverse to execute the query as a quick find query. [About quick find queries](../../quick-find.md)|
|`overridequickfindrecordlimitenabled`|No|See [Quick find record limits](../../quick-find.md#quick-find-record-limits) and [Apply the quick find record limit](../../quick-find.md#apply-the-quick-find-record-limit)|
|`overridequickfindrecordlimitdisabled`|No|See [Quick find record limits](../../quick-find.md#quick-find-record-limits) and [Bypass the quick find record limit](../../quick-find.md#bypass-the-quick-find-record-limit)|

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[condition](condition.md)|0 to 500|[!INCLUDE [condition-description](includes/condition-description.md)]|
|[filter](filter.md)|0 or many|[!INCLUDE [filter-description](includes/filter-description.md)]|
|[link-entity](link-entity.md)|0 or many|Used when [filtering on values in related records](../filter-rows.md#filter-on-values-in-related-records)|


[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
