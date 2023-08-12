---
title: condition element
description: Use this element to specify a condition to be evaluated as part of a filter for each row in the containing entity or link-entity elements to be returned.
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
# condition element

[!INCLUDE [condition-description](includes/condition-description.md)]

[Learn how to filter rows using FetchXml](../filter-rows.md).

## Example

```xml
TODO
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`aggregate`|No|TODO|
|`alias`|No|TODO|
|`attribute`|No|TODO|
|`column`|No|TODO|
|`entityname`|No|TODO|
|`operator`|Yes|TODO|
|`rowaggregate`|No|TODO|
|`uihidden`|No|TODO|
|`uiname`|No|TODO|
|`uitype`|No|TODO|
|`value`|No|TODO|
|`valueof`|No|TODO|


## Parent elements

|Name|Description|
|---------|---------|
|[filter](filter.md)|[!INCLUDE [filter-description](includes/filter-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[value element](value.md)|0 or Many|[!INCLUDE [value-description](includes/value-description.md)]|

## Remarks

- Use the `value` attribute for all operators that compare to a single value. For example, `eq`.
- Use the [value element](value.md) for operators that compare to multiple values For example: `in`.
- Some operators require neither the `value` attribute or the [value element](value.md). For example: `null`.

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]