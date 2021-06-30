---
title: "addOnPreProcessStatusChange (Client API reference) in model-driven apps in Power Apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnPreProcessStatusChange method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: reference
ms.assetid: 
author: KumarVivek
ms.author: kvivek
manager: annbe
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# addOnPreProcessStatusChange (Client API reference)

[!INCLUDE[](../../../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/addOnPreProcessStatusChange-description.md](./includes/addOnPreProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.addOnPreProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be executed when the business process flow status changes. The function will be added to the start of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

This client API is only supported on the Unified Client. The legacy web client does not support this client API.

### Related topics

[removeOnPreProcessStatusChange](removeOnPreProcessStatusChange.md)

[formContext.data.process](../../formContext-data-process.md)


[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]