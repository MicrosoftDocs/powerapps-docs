---
title: "addOnPostSearch (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOnPostSearch method.
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
# addOnPostSearch (Client API reference)

Adds an event handler to the [PostSearch](../events/postsearch.md) event. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.addOnPostSearch(myFunction);
```

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|`myFunction` |Function |Yes|The function to add to the [PostSearch event](../events/postsearch.md). The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related articles

[removeOnPostSearch](removeOnPostSearch.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
