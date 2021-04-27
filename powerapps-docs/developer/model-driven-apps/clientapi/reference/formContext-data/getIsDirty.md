---
title: "getIsDirty (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets a boolean value indicating whether any columns in the form have been modified.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 93908c95-c813-4f55-9d19-8fd27a0126d7
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getIsDirty (Client API reference)

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