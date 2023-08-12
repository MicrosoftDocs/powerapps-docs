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
TODO
```


## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`type`|No|TODO|
|`hint`|No|TODO|
|`isquickfindfields`|No|TODO|

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
