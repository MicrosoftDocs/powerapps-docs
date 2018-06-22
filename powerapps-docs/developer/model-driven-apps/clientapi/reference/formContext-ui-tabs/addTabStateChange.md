---
title: "addTabStateChange (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 51b0dbf3-28bd-4eea-9ee9-50b322e9af9b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addTabStateChange (Client API reference)



[!INCLUDE[./includes/addTabStateChange-description.md](./includes/addTabStateChange-description.md)].

## Syntax

`tabObj.addTabStateChange(myFunction);` 

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be executed on the [TabStateChange](../events/tabstatechange.md) event. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.|

### Related topics

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)


