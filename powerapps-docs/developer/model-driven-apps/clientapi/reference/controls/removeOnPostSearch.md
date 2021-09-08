---
title: "addOnPostSearch (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnPostSearch method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c398dbca-0ead-487a-8a92-35b1f2953bf6
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnPostSearch (Client API reference)



Removes an event handler from the [PostSearch](../events/postsearch.md) event. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>";
kbSearchControl.removeOnPostSearch(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to remove from the **PostSearch** event.| 

### Related topics

[PostSearch event](../events/postsearch.md)

[addOnPostSearch](addOnPostSearch.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]