---
title: "addOnSelection (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOnSelection method.
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
# addOnSelection (Client API reference)

Adds an event handler to the [OnSelection](../events/onselection.md) event. 

## Control types supported

Knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.addOnSelection(myFunction);
```
[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|----|----|----|----|
|`myFunction` |Function |Yes|The function to add to the [OnSelection event](../events/onselection.md). The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related articles

[removeOnSelection](removeOnSelection.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
