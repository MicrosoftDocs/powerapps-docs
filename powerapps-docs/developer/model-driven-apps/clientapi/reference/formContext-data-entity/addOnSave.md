---
title: "addOnSave (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1a66f93d-a47c-4316-91f1-dcf5d09f9d19
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addOnSave (Client API reference)



[!INCLUDE[./includes/addOnSave-description.md](./includes/addOnSave-description.md)]

## Syntax

`formContext.data.entity.addOnSave(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be executed when the record is saved. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.

### Related topics

[removeOnSave](removeOnSave.md)

[Form OnSave event](../events/form-onsave.md)

