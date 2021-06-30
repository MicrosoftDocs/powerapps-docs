---
title: "removeOnLoad (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnLoad method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0b97afc4-1208-4c1b-8599-424d594ea69f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnLoad (Client API reference)



[!INCLUDE[./includes/removeOnLoad-description.md](./includes/removeOnLoad-description.md)]

## Syntax

`formContext.ui.removeOnLoad(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be removed from the form [OnLoad](../events/form-onload.md) event.

### Related topics

[addOnLoad](addOnLoad.md)

[Form data OnLoad event](../events/form-onload.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]