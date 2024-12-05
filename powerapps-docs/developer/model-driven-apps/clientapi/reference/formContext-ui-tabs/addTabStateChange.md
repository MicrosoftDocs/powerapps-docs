---
title: "addTabStateChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addTabStateChange method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addTabStateChange (Client API reference)

[!INCLUDE[./includes/addTabStateChange-description.md](./includes/addTabStateChange-description.md)].

## Syntax

`tabObj.addTabStateChange(myFunction);` 

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be executed on the [TabStateChange](../events/tabstatechange.md) event. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.|

### Related articles

[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
