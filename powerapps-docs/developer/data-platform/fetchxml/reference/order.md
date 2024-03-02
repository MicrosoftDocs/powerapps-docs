---
title: order element
description: Use this element to specify the sort order of rows from the containing entity or link-entity element.
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
# order element

[!INCLUDE [order-description](includes/order-description.md)]

[Learn how to order rows using FetchXml](../order-rows.md).

## Example

This example return account records in ascending order by `createdon`, `name`, and `accountnumber` values.

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <order attribute='createdon' />
    <order attribute='name' />
    <order attribute='accountnumber' />
  </entity>
</fetch>
```

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`attribute`|Yes|The `name` of the [attribute element](attribute.md) to sort the data by.|
|`alias`|No|The `alias` of the [attribute element](attribute.md) to sort the data by|
|`descending`|No|Whether to sort the data in descending order.|
|`entityname`|No|Use this attribute to specify sort order for `link-entity` elements so that they aren't applied last. In an `order` within an `entity` element, set `entityname` to the  `alias` value of a `link-entity`. [Learn how to apply `link-entity` orders first](../order-rows.md#process-link-entity-orders-first)|

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
