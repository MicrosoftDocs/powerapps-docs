---
title: "addOnStageSelected (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5982770c-d5a4-415a-a32d-3734b6210bb9
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addOnStageSelected (Client API reference)



[!INCLUDE[./includes/addOnStageSelected-description.md](./includes/addOnStageSelected-description.md)]

## Syntax

`formContext.data.process.addOnStageSelected(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be executed when the business process flow stage is selected. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

### Related topics

[removeOnStageSelected](removeOnStageSelected.md)
 
[formContext.data.process](../../formContext-data-process.md)
 


