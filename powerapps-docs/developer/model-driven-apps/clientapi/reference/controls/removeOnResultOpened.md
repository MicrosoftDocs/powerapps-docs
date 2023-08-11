---
title: "removeOnResultOpened (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnResultOpened method.
author: chmoncay
ms.author: chmoncay
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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
