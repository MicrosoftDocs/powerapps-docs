---
title: "removeOnLookupTagClick (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnLookupTagClick method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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