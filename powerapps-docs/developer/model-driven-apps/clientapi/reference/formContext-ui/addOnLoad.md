---
title: "addOnLoad (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnLoad method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 31a146de-9e25-43be-ae3e-83a2a5c86543
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnLoad (Client API reference)



[!INCLUDE[./includes/addOnLoad-description.md](./includes/addOnLoad-description.md)]

## Syntax

`formContext.ui.addOnLoad(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be executed on the form [OnLoad](../events/form-onload.md) event. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.|

### Related topics

[removeOnLoad](removeOnLoad.md)

[Form OnLoad event](../events/form-onload.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]