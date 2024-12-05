---
title: "setActiveProcessInstance (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setActiveProcessInstance method.
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
# setActiveProcessInstance (Client API reference)

[!INCLUDE[./includes/setActiveProcessInstance-description.md](./includes/setActiveProcessInstance-description.md)]

## Syntax

`formContext.data.process.setActiveProcessInstance(processInstanceId, callbackFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`processInstanceId`|String|Yes|The Id of the process instance to set as the active instance.|
|`callbackFunction`|Function|No|A function to call when the operation is complete. This callback function is passed one of the following string values to indicate whether the operation succeeded:<br/>- **`success`**: The operation succeeded.<br/>- **`invalid`**: The processInstanceId isn't valid or the process isn't enabled.|

### Related articles

[getProcessInstances](getProcessInstances.md)   
[formContext.data.process](../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
