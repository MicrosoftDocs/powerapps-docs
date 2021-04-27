---
title: "addTabStateChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addTabStateChange method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 51b0dbf3-28bd-4eea-9ee9-50b322e9af9b
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]