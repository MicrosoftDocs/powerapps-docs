---
title: "removeOnResultOpened (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnResultOpened method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnResultOpened (Client API reference)



Removes an event handler from the [OnResultOpened](../events/onresultopened.md) event. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.removeOnResultOpened(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to remove from the **OnResultOpened** event.|

### Related topics

[OnResultOpened event](../events/onresultopened.md)

[addOnResultOpened](addOnResultOpened.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]