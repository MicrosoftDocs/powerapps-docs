---
title: "getActiveProcess (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getActiveProcess method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# getActiveProcess (Client API reference)



[!INCLUDE[./includes/getActiveProcess-description.md](./includes/getActiveProcess-description.md)]

## Syntax

`var activeProcess = formContext.data.process.getActiveProcess();`

## Return Value

**Type**: Process. 

**Description**: The currently active process. See [Process methods](../../formContext-data-process.md#process-methods) for the methods to access the properties of the process returned.

### Related topics

[setActiveProcess)](setActiveProcess.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]