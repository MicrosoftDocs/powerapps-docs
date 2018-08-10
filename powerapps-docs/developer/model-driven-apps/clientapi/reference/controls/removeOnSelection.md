---
title: "removeOnSelection (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 3ca41e3e-af2b-4aa8-8233-64a8c276d0ef
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# removeOnSelection (Client API reference)



Removes an event handler from the [OnSelection](../events/onselection.md) event. 

## Control types supported

Knowledge base search control

## Syntax

```
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.removeOnSelection(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to remove from the **OnSelection** event.| 

### Related topics

[addOnSelection](addOnSelection.md)


