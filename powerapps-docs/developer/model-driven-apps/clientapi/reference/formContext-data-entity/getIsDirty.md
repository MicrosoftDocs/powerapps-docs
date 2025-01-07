---
title: entity.getIsDirty (Client API reference)
description: Gets a boolean value indicating whether any attributes of the entity have been modified.
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
# entity.getIsDirty (Client API reference)



[!INCLUDE[./includes/getIsDirty-description.md](./includes/getIsDirty-description.md)]

## Syntax

`formContext.data.entity.getIsDirty();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Type

**Type**: Boolean

**Description**: true if any columns in the form have been changed; false otherwise.

### Related articles

[formContext.data.getIsDirty](../formContext-data/getIsDirty.md)   
[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
