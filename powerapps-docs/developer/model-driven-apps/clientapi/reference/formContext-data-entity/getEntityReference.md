---
title: entity.getEntityReference (Client API reference)
description: Returns a lookup value that references a record.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# entity.getEntityReference (Client API reference)

[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Syntax

`formContext.data.entity.getEntityReference();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Lookup object.

**Description**: The returned object has following three parameters:

- **`entityType`**: String. Logical name of the table record. For example, "account".
- **`id`**: String. GUID value of the table record.
- **`name`**: (Optional) String. Name of the table record. 


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
