---
title: condition element
description: Use this element to specify a condition to be evaluated as part of a filter for each row in the containing entity or link-entity elements to be returned.
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
# condition element

[!INCLUDE [condition-description](includes/condition-description.md)]

[Learn how to filter rows using FetchXml](../filter-rows.md).

## Example

This query returns account records where `address1_city` equals 'Redmond'.

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
|`attribute`|No|The name of the column with the value to apply the filter.|
|`entityname`|No|Specify the [link-entity](link-entity.md) `name` or `alias` that the condition should be applied to after the outer join. [Learn more about filters on link-entity](../filter-rows.md#filters-on-link-entity)|
|`operator`|Yes|The [operator](operators.md) to apply with the filter.|
|`value`|No|The value to test the column value with the operator.|
|`valueof`|No|The name of the column in the same table that has the value to test the column value with the operator. [Learn more about filtering on other column values](../filter-rows.md#filter-on-column-values-in-the-same-row). |


## Parent elements

|Name|Description|
|---------|---------|
|[filter](filter.md)|[!INCLUDE [filter-description](includes/filter-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[value](value.md)|0 or Many|[!INCLUDE [value-description](includes/value-description.md)]|

## Remarks

- Use the `value` attribute for all operators that compare to a single value. For example, `eq`.
- Use the [value element](value.md) for operators that compare to multiple values For example: `in`.
- Some operators require neither the `value` attribute or the [value element](value.md). For example: `null`.

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]