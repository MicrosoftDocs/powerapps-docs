---
title: "addOnLookupTagClick (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnLookupTagClick method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to add to the **OnLookupTagClick** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function along with eventArgs that contain the tag value. More information: [OnLookupTagClick event](../events/onlookuptagclick.md).<br/><br/>You should use a reference to a named function rather than an anonymous function if you later want to remove the event handler.|

### Related topics
 
[removeOnLookupTagClick](removeOnLookupTagClick.md)

[OnLookupTagClick event](../events/onlookuptagclick.md)
 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]