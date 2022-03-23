---
title: "data.getIsDirty (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets a boolean value indicating whether any columns in the form have been modified.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# data.getIsDirty (Client API reference)

[!INCLUDE[./includes/getIsDirty-description.md](./includes/getIsDirty-description.md)]

## Syntax

`formContext.data.getIsDirty();`

## Return Type

**Type**: Boolean

**Description**: true if the form data has changed; false otherwise.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

### Related topics

[formContext.data.entity.getIsDirty](../formContext-data-entity/getIsDirty.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]