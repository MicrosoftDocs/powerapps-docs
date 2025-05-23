---
title: "addOnProcessStatusChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOnProcessStatusChange method.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addOnProcessStatusChange (Client API reference)

[!INCLUDE[./includes/addOnProcessStatusChange-description.md](./includes/addOnProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.addOnProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|Function reference|Yes|The function to be executed when the business process flow status changes. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

### Related articles

[removeOnProcessStatusChange](removeOnProcessStatusChange.md)   
[formContext.data.process](../../formContext-data-process.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
