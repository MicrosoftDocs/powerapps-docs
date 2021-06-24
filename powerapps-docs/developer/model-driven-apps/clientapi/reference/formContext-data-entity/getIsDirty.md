---
title: "getIsDirty (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets a boolean value indicating whether any columns in the form have been modified.
ms.date: 10/31/2018
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

`formContext.data.entity.getIsDirty();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Type

**Type**: Boolean

**Description**: true if any columns in the form have been changed; false otherwise.

### Related topics

[formContext.data.getIsDirty](../formContext-data/getIsDirty.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]