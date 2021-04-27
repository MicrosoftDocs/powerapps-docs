---
title: "addOnResultOpened (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnResultOpened method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5f0eabe1-985a-4e89-b23a-72657208ae7e
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnResultOpened (Client API reference)

Adds an event handler to the [OnResultOpened](../events/onresultopened.md) event. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.addOnResultOpened(myFunction);
```
[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to add to the **OnResultOpened** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[OnResultOpened event](../events/onresultopened.md)

[removeOnResultOpened](removeOnResultOpened.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]