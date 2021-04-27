---
title: "addOnPostSearch (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnPostSearch method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9d000628-5dbe-45bd-9c47-e19187ffdae7
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnPostSearch (Client API reference)

Adds an event handler to the [PostSearch](../events/postsearch.md) event. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>";
kbSearchControl.addOnPostSearch(myFunction);
```

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to add to the **PostSearch** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.| 

### Related topics

[PostSearch event](../events/postsearch.md)

[removeOnPostSearch](removeOnPostSearch.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]