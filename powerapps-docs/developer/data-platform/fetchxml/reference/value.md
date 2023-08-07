---
title: value element
description: Use this element to specify the values to evaluate with a condition.
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
# value element

[!INCLUDE [value-description](includes/value-description.md)]

To learn how to use this element, see [Filter rows using FetchXml](../filter-rows.md).

## Example

```xml
<filter>
   <condition attribute="numberofemployees" operator="between">
      <value>6</value>
      <value>20</value>
   </condition>
</filter>
```

## Parent elements

|Name|Description|
|---------|---------|
|[condition element](condition.md)|[!INCLUDE [condition-description](includes/condition-description.md)]|
