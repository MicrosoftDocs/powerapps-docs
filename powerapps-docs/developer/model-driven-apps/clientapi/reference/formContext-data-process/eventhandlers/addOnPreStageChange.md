---
title: "addOnPreStageChange (Client API reference) in model-driven apps in Power Apps| MicrosoftDocs"
ms.date: 07/19/2019
ms.service: crm-online
ms.topic: reference
ms.assetid: 
author: msftman
ms.author: deonhe
manager: KVivek
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# addOnPreStageChange (Client API reference)

[!INCLUDE[./includes/addOnStageChange-description.md](./includes/AddOnPreStageChange-description.md)]

## Syntax

`formContext.data.process.addOnPreStageChange(myFunction);`

## Parameter

Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function that runs **before** the business process flow stage changes. The function will be added to the start of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

This client API is only supported on the Unified Client. The legacy web client does not support this client API.

### Related topics

- [addOnStageChange](addOnStageChange.md)
 
- [removeOnStageChange](removeOnStageChange.md)

- [formContext.data.process](../../formContext-data-process.md)
 


