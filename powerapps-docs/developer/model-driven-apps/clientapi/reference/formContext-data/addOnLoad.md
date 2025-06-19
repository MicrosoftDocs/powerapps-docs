---
title: "data.addOnLoad (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the data.addOnLoad method.
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
# data.addOnLoad (Client API reference)



[!INCLUDE[./includes/addOnLoad-description.md](./includes/addOnLoad-description.md)]

## Syntax

`formContext.data.addOnLoad(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be executed when the form data loads. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [Execution context](../../clientapi-execution-context.md) for more information.

### Related articles

[removeOnLoad](removeOnLoad.md)   
[Form data OnLoad event](../events/form-data-onload.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
