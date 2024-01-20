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
|`hint`|No|TODO See new section in [Filter rows using FetchXml](../filter-rows.md)[TODO: using the hint attribute](../filter-rows.md#todo-using-the-hint-attribute)|****
|`isquickfindfields`|No|Use this to tell Dataverse to execute the query like a Quick find query. [Quick find queries](#quick-find-queries) |
|`overridequickfindrecordlimitenabled`|No|Use this when the quick find limit **is not enabled**, but you want to apply at limit to this query for better performance|
|`overridequickfindrecordlimitdisabled`|No|Use this when the quick find **limit is enabled**, but you want to apply at limit to this query for better usability, avoiding the error that would otherwise be returned.|

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


## Quick find queries

**TODO**: Add information about how quick find queries *may* increase query performance and the error that can occur due to them. See https://learn.microsoft.com/en-us/power-apps/developer/data-platform/quick-find-limit

### Quick Find limit

TODO: 
 - Setting to turn it on or off in the UI?
 - Set the quick find query limit for the org. Is it in the UI?

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
