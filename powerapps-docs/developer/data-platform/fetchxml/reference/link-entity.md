---
title: link-entity element
description: Use this element to join tables with the containing entity or link-entity element.
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
# link-entity element

[!INCLUDE [link-entity-description](includes/link-entity-description.md)]

## Example

```xml
TODO
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|TODO|
|`to`|Yes|TODO|
|`from`|Yes|TODO|
|`alias`|No|TODO|
|`link-type`|No|TODO|
|`intersect`|No|TODO|
|`forceseek`|No|TODO|
|`enableprefiltering`|No|TODO|
|`prefilterparametername`|No|TODO|

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes element](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute element](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order element](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity element](link-entity.md)|0 or many|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|
|[filter element](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|
