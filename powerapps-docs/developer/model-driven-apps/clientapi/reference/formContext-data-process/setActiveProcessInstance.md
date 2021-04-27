---
title: "setActiveProcessInstance (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setActiveProcessInstance method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c01a9445-00b6-4152-a482-df830f91a3ea
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setActiveProcessInstance (Client API reference)



[!INCLUDE[./includes/setActiveProcessInstance-description.md](./includes/setActiveProcessInstance-description.md)]

## Syntax

`formContext.data.process.setActiveProcessInstance(processInstanceId, callbackFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|processInstanceId|String|Yes|The Id of the process instance to set as the active instance.|
|callbackFunction|Function|No|A function to call when the operation is complete. This callback function is passed one of the following string values to indicate whether the operation succeeded:<br/>- **success**: The operation succeeded.<br/>- **invalid**: The processInstanceId isn’t valid or the process isn’t enabled.|

### Related topics

[getProcessInstances](getProcessInstances.md)

[formContext.data.process](../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]