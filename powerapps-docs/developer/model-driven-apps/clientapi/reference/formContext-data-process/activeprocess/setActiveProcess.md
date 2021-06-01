---
title: "setActiveProcess (Client API reference) in model-driven apps| MicrosoftDocs"
description: Sets a process as the active process.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0d4c2d8a-a2fb-4cdd-9153-041646068992
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setActiveProcess (Client API reference)



[!INCLUDE[./includes/setActiveProcess-description.md](./includes/setActiveProcess-description.md)]

If there is an active instance of the process, the table record is loaded with the process instance ID. If there is no active instance of the process, a new process instance is created and the table record is loaded with the process instance ID. If there are multiple instances of the current process, the record is loaded with the first instance of the active process as per the defaulting logic, that is the most recently used process instance per user.

> [!NOTE]
> The `setActiveProcess` method should be used while creating or editing a record. Use the `setActiveProcess` method to set the active process for a business process flow instead of `processId` and `processInstanceId` with `Xrm.Navigation.openForm` method . 

## Syntax

`formContext.data.process.setActiveProcess(processId, callbackFunction);`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|processId|String|Yes|The Id of the process to set as the active process.|
|callbackFunction|Function|No|A function to call when the operation is complete. This callback function is passed one of the following string values to indicate whether the operation succeeded:<br/>- **success**: The operation succeeded.<br/>- **invalid**: The processId isn’t valid or the process isn’t enabled.|

### Related topics

[getActiveProcess](getActiveProcess.md)

[setActiveProcessInstance](../setActiveProcessInstance.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]