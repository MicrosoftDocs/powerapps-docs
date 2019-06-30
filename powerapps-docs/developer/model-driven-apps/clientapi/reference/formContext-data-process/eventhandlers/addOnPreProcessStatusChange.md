---
title: "addOnPreProcessStatusChange (Client API reference) in Dynamics 365 for Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: crm-online
ms.topic: reference
applies_to: Dynamics 365 for Customer Engagement (online)
ms.assetid: 
author: KumarVivek
ms.author: kvivek
manager: amyla
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# addOnPreProcessStatusChange (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/addOnPreProcessStatusChange-description.md](./includes/addOnPreProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.addOnPreProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be executed when the business process flow status changes. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

### Related topics

[removeOnProcessStatusChange](removeOnProcessStatusChange.md)

[formContext.data.process](../../formContext-data-process.md)
