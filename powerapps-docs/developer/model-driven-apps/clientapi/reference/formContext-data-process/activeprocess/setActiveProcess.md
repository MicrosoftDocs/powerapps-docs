---
title: "setActiveProcess (Client API reference) in model-driven apps"
description: Sets a process as the active process.
author: matthidinger
ms.author: mahiding
ms.date: 06/28/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setActiveProcess (Client API reference)

[!INCLUDE[./includes/setActiveProcess-description.md](./includes/setActiveProcess-description.md)]

If the business process being set as active already has an instance, the instance will be marked as active and the primary record form will be reloaded to show it. If no instance exists for the process, a new instance is created, marked as active, and the primary record form will be reloaded to show it.

If multiple instances of the process exist, one of these will be chosen as per the defaulting logic to be marked as active. Typically, this is the most recently used process instance by the current user.

> [!NOTE]
> - The `setActiveProcess` method should be used while creating or editing a record. Use the `setActiveProcess` method to set the active process for a business process flow instead of `processId` and `processInstanceId` with `Xrm.Navigation.openForm` method . 
> - The `setActiveProcess` method will reload the form and any unsaved data will be lost.

## Syntax

`formContext.data.process.setActiveProcess(processId, callbackFunction);`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`processId`|String|Yes|The Id of the process to set as the active process.|
|`callbackFunction`|Function|No|A function to call when the operation is complete. This callback function is passed one of the following string values to indicate whether the operation succeeded:<br/>- **`success`**: The operation succeeded.<br/>- **`invalid`**: The processId isn't valid or the process isn't enabled.|

### Related articles

[getActiveProcess](getActiveProcess.md)   
[setActiveProcessInstance](../setActiveProcessInstance.md)   
[formContext.data.process](../../formContext-data-process.md)
 

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
