---
title: "addOnPostSearch (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c398dbca-0ead-487a-8a92-35b1f2953bf6
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# removeOnPostSearch (Client API reference)



Removes an event handler from the [PostSearch](../events/postsearch.md) event. 

## Control types supported

knowledge base search control

## Syntax

```
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


