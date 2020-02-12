---
title: "addOnLookupTagClick (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 02/11/2020
ms.service: powerapps
ms.topic: "reference"
ms.assetid: d18136d2-a3cf-4440-8e6b-1703594acd79
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnLookupTagClick (Client API reference)

Adds an event handler to the [OnLookupTagClick](../events/onlookuptagclick.md) event.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addOnLookupTagClick(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to add to the **OnLookupTagClick** event. The [execution context](../../../clientapi-execution-context.md) is automatically passed as the first parameter to this function along with eventArgs that contain the tag value. More information: [OnLookupTagClick event](../events/onlookuptagclick.md).<br/><br/>You should use a reference to a named function rather than an anonymous function if you later want to remove the event handler.|

### Related topics
 
[removeOnLookupTagClick](removeOnLookupTagClick.md)

[OnLookupTagClick event](../events/onlookuptagclick.md)
 


