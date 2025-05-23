---
title: "addOnSave (Client API reference) in model-driven apps"
description: Adds a function to be called when the OnSave event is triggered.
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
# addOnSave (Client API reference)

[!INCLUDE[./includes/addOnSave-description.md](./includes/addOnSave-description.md)]

## Syntax

`formContext.data.entity.addOnSave(myFunction)`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be executed when the record is saved. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.

### Related articles

[removeOnSave](removeOnSave.md)   
[Form OnSave event](../events/form-onsave.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
