---
title: "getActiveProcess (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a977a250-b79f-4c88-a6af-776350b110f7
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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
 


