---
title: all-attributes element
description: Use this element to specify that all columns in the containing entity or link-entity element should be returned.
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
# all-attributes element

[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]

> [!IMPORTANT]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors. You should always use [attribute elements](attribute.md) to specify which columns you want to return. More information: [Select columns using FetchXml](../select-columns.md)

## Example

```xml
<entity name="account">
   <all-attributes/>
</entity>
```

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
