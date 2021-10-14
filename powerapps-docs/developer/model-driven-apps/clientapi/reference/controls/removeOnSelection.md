---
title: "removeOnSelection (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnSelection method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 3ca41e3e-af2b-4aa8-8233-64a8c276d0ef
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
|myFunction |Function |Yes|The function to remove from the **OnSelection** event.| 

### Related topics

[addOnSelection](addOnSelection.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]