---
title: value element
description: Use this element to specify the values to evaluate with a condition.
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
# value element

[!INCLUDE [value-description](includes/value-description.md)]

[Learn how to filter rows using FetchXml](../filter-rows.md).

## Example

This filter will will evaluate to true when the `numberofemployees` is between 6 and 20.

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
|[condition](condition.md)|[!INCLUDE [condition-description](includes/condition-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
