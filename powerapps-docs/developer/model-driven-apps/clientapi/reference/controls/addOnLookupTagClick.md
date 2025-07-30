---
title: "addOnLookupTagClick (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOnLookupTagClick method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
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
|`myFunction`|Function reference|Yes|The function to add to the [OnLookupTagClick event](../events/onlookuptagclick.md). The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function along with eventArgs that contain the tag value.<br/><br/>You should use a reference to a named function rather than an anonymous function if you later want to remove the event handler.|

### Related articles
 
[removeOnLookupTagClick](removeOnLookupTagClick.md)   
[OnLookupTagClick event](../events/onlookuptagclick.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
