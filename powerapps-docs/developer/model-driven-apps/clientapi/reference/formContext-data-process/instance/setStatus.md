---
title: "setStatus (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setStatus method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# setStatus (Client API reference)



[!INCLUDE[./includes/setStatus-description.md](./includes/setStatus-description.md)]

## Syntax

`formContext.data.process.setStatus(status, callbackFunction);`

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|status|String|Yes|The new status. The values can be **active**, **aborted**, **finished**, or **invalid**. |
|callbackFunction|Function|No|A function to call when the operation is complete. This callback function is passed the new status as a string value.|

**Type**: String. 

**Description**:Returns one of the following values: **active**, **aborted**, or **finished**. It returns **invalid** if the setStatus API fails.

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
