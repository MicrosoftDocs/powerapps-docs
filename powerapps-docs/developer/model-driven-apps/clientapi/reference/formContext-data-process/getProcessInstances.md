---
title: "getProcessInstances (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 12/04/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4ed6c991-59c9-4a69-90d4-635f3f1d397b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getProcessInstances (Client API reference)



[!INCLUDE[./includes/getProcessInstances-description.md](./includes/getProcessInstances-description.md)]

## Syntax

`formContext.data.process.getProcessInstances(callbackFunction(object));`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|callbackFunction|Function|Yes|The callback function is passed an object with the following attributes and their corresponding values as the key: value pair. All returned values are of String type except for **CreatedOnDate**, which is of [Date](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) type. <br/>- CreatedOn (deprecated)<br/>- CreatedOnDate<br/>- ProcessDefinitionID<br/>- ProcessDefinitionName<br/>- ProcessInstanceID<br/>- ProcessInstanceName<br/>- StatusCodeName<br/><br/>The process instances are filtered according to the user’s privileges.|

### Related topics

[setActiveProcessInstance](setActiveProcessInstance.md)

[formContext.data.process](../formContext-data-process.md)
 


