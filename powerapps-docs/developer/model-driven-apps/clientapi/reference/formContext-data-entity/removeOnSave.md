---
title: "removeOnSave (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 04/07/2020
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 14a92f7c-f4c0-475d-8797-dcbb283db37a
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnSave (Client API reference)



[!INCLUDE[./includes/removeOnSave-description.md](./includes/removeOnSave-description.md)]

## Syntax

`formContext.data.entity.removeOnSave(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be removed for the **OnSave** event.

### Related topics

[addOnSave](addOnSave.md)

[Form OnSave event](../events/form-onsave.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]