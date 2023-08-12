---
title: entity element
description: Use this element to specify the entity of the query.
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
# entity element

[!INCLUDE [entity-description](includes/entity-description.md)]

[Learn how to query data using FetchXml](../overview.md).

## Example

```xml
TODO
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|TODO|
|`forceseek`|No|TODO|
|`enableprefiltering`|No|TODO|
|`prefilterparametername`|No|TODO|

## Parent elements

|Name|Description|
|---------|---------|
|[fetch element](fetch.md)|[!INCLUDE [fetch-description](includes/fetch-description.md)]|


## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes element](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute element](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order element](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity element](link-entity.md)|0 or many|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|
|[filter element](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
