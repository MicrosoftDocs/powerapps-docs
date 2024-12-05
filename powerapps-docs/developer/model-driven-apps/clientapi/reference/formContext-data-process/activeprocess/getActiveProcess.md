---
title: "getActiveProcess (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getActiveProcess method.
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
# getActiveProcess (Client API reference)

[!INCLUDE[./includes/getActiveProcess-description.md](./includes/getActiveProcess-description.md)]

## Syntax

`var activeProcess = formContext.data.process.getActiveProcess();`

## Return Value

**Type**: Process | null

**Description**: The currently active process or null if there is no active process. See [Process methods](../../formContext-data-process.md#process-methods) for the methods to access the properties of the process returned.

### Related articles

[setActiveProcess](setActiveProcess.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
