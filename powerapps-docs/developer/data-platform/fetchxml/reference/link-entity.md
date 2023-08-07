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

To learn how to use this element, see [Join tables using FetchXml](../join-tables.md).

## Example

```xml
TODO
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|The logical name of the related table.|
|`to`|Yes|The logical name of the column in the parent element *to* match with the related table column specified in the `from` attribute.|
|`from`|Yes|The logical name of the column *from* the related table that matches the column specified in the `to` attribute.|
|`alias`|No|A string to represent the name of the related table.<br />-  If not set for a many-to-one relationship, it will default the logical name of the related table.<br />- If not set for a one-to-many relationship, an alias value is generated using the pattern `{LogicalName}+{N}`, where `N` is the number of link-entities for that table.|
|`link-type`|No|Whether to use an *inner* or *outer* join. Default behavior is *inner*.<br />- An inner join restricts results to rows with matching values in both tables.<br />- An outer join includes results from the parent element that don't have a matching value.|
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
