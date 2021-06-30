---
title: "addOnSelection (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnSelection method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 66cfb2ff-4d78-4bb9-8dc0-e214ae1d2880
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.addOnSelection(myFunction);
```
[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to add to the **OnSelection** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[OnSelection event](../events/onselection.md)

[removeOnSelection](removeOnSelection.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]