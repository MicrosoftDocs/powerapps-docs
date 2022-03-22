---
title: "addPreSearch (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnPreSearch method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addPreSearch (Client API reference)

Applies changes to lookups based on values current just as the user is about to view results for the lookup.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addPreSearch(myFunction)`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes| The function that will be run just before the search to provide results for a lookup occurs. You can use this function to call one of the other lookup control functions and improve the results to be displayed in the lookup. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[PreSearch event](../events/PreSearch.md)

[removePreSearch](removePreSearch.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]