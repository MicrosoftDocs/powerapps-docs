---
title: "getCategory (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 2849a9e1-b2fb-464c-8fc7-90b0df027c86
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getCategory (Client API reference)



[!INCLUDE[./includes/getCategory-description.md](./includes/getCategory-description.md)]

## Syntax

`var stageCategoryNumber = stageObj.getCategory().getValue();`

## Return Value

**Type**: Number. 

**Description**: Here is the list of possible values.

|Value |Description|
|--|--|
|0|Qualify|
|1|Develop|
|2|Propose|
|3|Close|
|4|Identify|
|5|Research|
|6|Resolve|

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 


