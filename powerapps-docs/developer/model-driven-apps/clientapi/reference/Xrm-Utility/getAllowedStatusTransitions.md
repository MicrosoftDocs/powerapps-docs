---
title: "getAllowedStatusTransitions (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 28c36741-0070-435c-a42f-49f4dda2ef7f
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---

# getAllowedStatusTransitions (Client API reference)



[!INCLUDE[./includes/getAllowedStatusTransitions-description.md](./includes/getAllowedStatusTransitions-description.md)] 

## Syntax

`Xrm.Utility.getAllowedStatusTransitions(entityName,stateCode).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|entityName|String|Yes|The logical name of the entity.|
|stateCode|Number|Yes|The state code to find out the allowed status transition values.|
|successCallback|Function|No|The function to execute when the operation succeeds.|
|errorCallback|Function|No|The function to execute when the operation fails.|


### Related topics

[Xrm.Utility](../xrm-utility.md)



