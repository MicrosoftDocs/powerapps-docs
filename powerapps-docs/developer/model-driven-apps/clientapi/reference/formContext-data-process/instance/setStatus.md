---
title: "setStatus (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setStatus (Client API reference)



[!INCLUDE[./includes/setStatus-description.md](./includes/setStatus-description.md)]

## Syntax

`formContext.data.process.setStatus(status, callbackFunction);`

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|status|String|Yes|The new status. The values can be **active**, **aborted**, or **finished**.|
|callbackFunction|Function|No|A function to call when the operation is complete. This callback function is passed the new status as a string value.|

**Type**: String. 

**Description**:Returns one of the following values: **active**, **aborted**, or **finished**.

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 


