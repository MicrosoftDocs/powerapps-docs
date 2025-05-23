---
title: "removeOnPostSearch (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOnPostSearch method.
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
|----|----|----|----|
|`myFunction`|Function |Yes|The function to remove from the **PostSearch** event.|

### Related articles

[PostSearch event](../events/postsearch.md)   
[addOnPostSearch](addOnPostSearch.md) 

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
