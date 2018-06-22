---
title: "setActiveProcess (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0d4c2d8a-a2fb-4cdd-9153-041646068992
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setActiveProcess (Client API reference)



[!INCLUDE[./includes/setActiveProcess-description.md](./includes/setActiveProcess-description.md)]

If there is an active instance of the process, the entity record is loaded with the process instance ID. If there is no active instance of the process, a new process instance is created and the entity record is loaded with the process instance ID. If there are multiple instances of the current process, the record is loaded with the first instance of the active process as per the defaulting logic, that is the most recently used process instance per user.

## Syntax

`formContext.data.process.setActiveProcess(processId, callbackFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|processInstanceId|String|Yes|The Id of the process to set as the active process.|
|callbackFunction|Function|No|A function to call when the operation is complete. This callback function is passed one of the following string values to indicate whether the operation succeeded:<br/>- **success**: The operation succeeded.<br/>- **invalid**: The processId isn’t valid or the process isn’t enabled.|

### Related topics

[getActiveProcess](getActiveProcess.md)

[setActiveProcessInstance](../setActiveProcessInstance.md)

[formContext.data.process](../../formContext-data-process.md)
 


