---
title: gridEntity.getEntityReference (Client API reference)
description: Includes description and supported parameters for the gridEntity.getEntityReference method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# gridEntity.getEntityReference (Client API reference)

[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridEntity.getEntityReference();`

## Return Value

**Type**: Lookup

**Description**: Lookup object that references the record in the row. The object has the following values:

- **`entityType`**: String. The logical name for the record in the row. The same data returned by the **GridEntity**.[getEntityName](getEntityName.md) method.
- **`id`**: String. The Id for the record in the row. The same data returned by the **GridEntity**.[getId](getId.md) method.
- **`name`**: String. The primary column value for the record in the row. The same data returned by the **GridEntity**.[getPrimaryAttributeValue](getPrimaryAttributeValue.md) method.

## Remarks

To get the `gridEntity` object, see [GridEntity](../gridentity.md). 


[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
