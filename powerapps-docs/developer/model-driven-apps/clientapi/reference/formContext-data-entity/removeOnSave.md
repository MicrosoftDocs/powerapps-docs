---
title: "removeOnSave (Client API reference) in model-driven apps"
description: Removes a function to be called when the record is saved.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOnSave (Client API reference)



[!INCLUDE[./includes/removeOnSave-description.md](./includes/removeOnSave-description.md)]

## Syntax

`formContext.data.entity.removeOnSave(myFunction)`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be removed for the **OnSave** event.

### Related articles

[addOnSave](addOnSave.md)   
[Form OnSave event](../events/form-onsave.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
