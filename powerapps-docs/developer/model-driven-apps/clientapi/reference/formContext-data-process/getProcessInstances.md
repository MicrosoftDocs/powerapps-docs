---
title: "getProcessInstances (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getProcessInstances method.
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
# getProcessInstances (Client API reference)



[!INCLUDE[./includes/getProcessInstances-description.md](./includes/getProcessInstances-description.md)]

## Syntax

`formContext.data.process.getProcessInstances(callbackFunction(object));`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`callbackFunction`|Function|Yes|The callback function is passed an object with the following columns and their corresponding values as the key: value pair. All returned values are of String type except for **CreatedOnDate**, which is of [Date](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) type. <br/>- CreatedOn (deprecated)<br/>- CreatedOnDate<br/>- ProcessDefinitionID<br/>- ProcessDefinitionName<br/>- ProcessInstanceID<br/>- ProcessInstanceName<br/>- StatusCodeName<br/><br/>The process instances are filtered according to the user's privileges.|

### Related articles

[setActiveProcessInstance](setActiveProcessInstance.md)   
[formContext.data.process](../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
