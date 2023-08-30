---
title: filter element
description: Use this element to specify a set of conditions to be evaluated for each row of the containing entity or link-entity element that will determine if the row is returned.
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
|`hint`|No|TODO?|
|`isquickfindfields`|No|REMOVE?|

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[condition element](condition.md)|0 to 500|[!INCLUDE [condition-description](includes/condition-description.md)]|
|[filter element](filter.md)|0 or many|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
