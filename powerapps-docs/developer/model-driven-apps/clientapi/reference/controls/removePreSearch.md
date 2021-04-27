---
title: "removePreSearch (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removePreSearch method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 2451c4ac-527c-4487-8f52-bde1690c5bde
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removePreSearch (Client API reference)



Removes event handler functions that have previously been set for the [PreSearch](../events/PreSearch.md) event.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).removePreSearch(myFunction)`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes| The function to remove. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[PreSearch event](../events/PreSearch.md)

[addPreSearch](addPreSearch.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]