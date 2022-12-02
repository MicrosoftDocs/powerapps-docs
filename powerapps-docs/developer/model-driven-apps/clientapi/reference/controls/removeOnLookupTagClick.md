---
title: "removeOnLookupTagClick (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnLookupTagClick method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# removeOnLookupTagClick (Client API reference)

Removes an event handler from the [OnLookupTagClick](../events/onlookuptagclick.md) event.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).removeOnLookupTagClick(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be removed from the [OnLookupTagClick](../events/onlookuptagclick.md) event.|

### Related topics

[addOnLookupTagClick](addOnLookupTagClick.md)
 
[OnLookupTagClick event](../events/onlookuptagclick.md)
 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]