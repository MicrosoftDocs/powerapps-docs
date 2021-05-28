---
title: "addOnStageChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnStageChange method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d18136d2-a3cf-4440-8e6b-1703594acd79
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnStageChange (Client API reference)



[!INCLUDE[./includes/addOnStageChange-description.md](./includes/addOnStageChange-description.md)]

## Syntax

`formContext.data.process.addOnStageChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be executed when the business process flow stage changes. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../../clientapi-execution-context.md) for more information.<br/><br/>You should use a reference to a named function rather than an anonymous function if you may later want to remove the event handler.|

### Related topics
 
[removeOnStageChange](removeOnStageChange.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]