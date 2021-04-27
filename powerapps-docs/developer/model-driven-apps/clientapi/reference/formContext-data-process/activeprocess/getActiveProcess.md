---
title: "getActiveProcess (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getActiveProcess method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a977a250-b79f-4c88-a6af-776350b110f7
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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