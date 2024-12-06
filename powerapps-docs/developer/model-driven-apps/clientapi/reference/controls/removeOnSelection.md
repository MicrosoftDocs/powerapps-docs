---
title: "removeOnSelection (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOnSelection method.
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
# removeOnSelection (Client API reference)

Removes an event handler from the [OnSelection](../events/onselection.md) event.

## Control types supported

Knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.removeOnSelection(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|`myFunction` |Function |Yes|The function to remove from the **OnSelection** event.| 

### Related articles

[addOnSelection](addOnSelection.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
