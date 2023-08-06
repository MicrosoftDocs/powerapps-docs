---
title: all-attributes element
description: Use this element to specify that all columns in the containing entity or link-entity element should be returned.
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
# all-attributes element

[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]

> [!IMPORTANT]
> It is not recommended to request all columns for a table for performance reasons. You should always use [attribute elements](attribute.md) to specify which columns you want to return.

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