---
title: "addOnSelection (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 66cfb2ff-4d78-4bb9-8dc0-e214ae1d2880
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnSelection (Client API reference)



Adds an event handler to the [OnSelection](../events/onselection.md) event. 

## Control types supported

Knowledge base search control

## Syntax

```
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.addOnSelection(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to add to the **OnSelection** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[OnSelection event](../events/onselection.md)

[removeOnSelection](removeOnSelection.md)