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
|`name`|Yes|[!INCLUDE [link-entity-name-description](includes/link-entity-name-description.md)]|
|`to`|Yes|[!INCLUDE [link-entity-to-description](includes/link-entity-to-description.md)]|
|`from`|Yes|[!INCLUDE [link-entity-name-from-description](includes/link-entity-from-description.md)]|
|`alias`|No|[!INCLUDE [link-entity-name-alias-description](includes/link-entity-alias-description.md)]|
|`link-type`|No|[!INCLUDE [link-entity-name-link-type-description](includes/link-entity-link-type-description.md)]|
|`intersect`|No|[!INCLUDE [link-entity-name-intersect-description](includes/link-entity-intersect-description.md)]|
|`forceseek`|No|[!INCLUDE [link-entity-name-forceseek-description](includes/link-entity-forceseek-description.md)]|
|`enableprefiltering`|No|[!INCLUDE [link-entity-name-enableprefiltering-description](includes/link-entity-enableprefiltering-description.md)]|
|`prefilterparametername`|No|[!INCLUDE [link-entity-name-prefilterparametername-description](includes/link-entity-prefilterparametername-description.md)]|

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

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
