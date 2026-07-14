---
title: entity element
description: Use this element to specify the entity of the query.
author: MsSQLGirl
ms.author: jukoesma
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
# entity element

[!INCLUDE [entity-description](includes/entity-description.md)]

[Learn how to query data using FetchXml](../overview.md).

## Example

```xml
<fetch>
  <entity name='account'>
    <attribute name='accountclassificationcode' />
    <attribute name='createdby' />
    <attribute name='createdon' />
    <attribute name='name' />
  </entity>
</fetch>
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|The logical name of the table that the query is based on.|

## Parent elements

|Name|Description|
|---------|---------|
|[fetch](fetch.md)|[!INCLUDE [fetch-description](includes/fetch-description.md)]|


## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity](link-entity.md)|0 or many|Joins a table related to the [entity](entity.md) or [link-entity](link-entity.md) to return more columns with the result.|
|[filter](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
