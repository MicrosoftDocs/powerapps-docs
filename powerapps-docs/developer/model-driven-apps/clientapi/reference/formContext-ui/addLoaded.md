---
title: "ui.addLoaded (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the ui.addLoaded method.
author: MitiJ
ms.author: mijosh
ms.date: 07/08/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# ui.addLoaded (Client API reference)

Adds a function to be called on the form [Loaded](../events/form-loaded.md) event that happens after the form completes the load process.

## Syntax

`formContext.ui.addLoaded(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be executed on the form [Loaded](../events/form-loaded.md) event. The function is added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. For more information, see [Execution context](../../clientapi-execution-context.md).|

### Related articles

[removeLoaded](removeloaded.md)   
[Form Loaded event](../events/form-loaded.md)   
[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
