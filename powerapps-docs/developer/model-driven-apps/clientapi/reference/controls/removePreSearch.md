---
title: "removePreSearch (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removePreSearch method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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
|`myFunction` |Function |Yes| The function to remove. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related articles

[PreSearch event](../events/PreSearch.md)   
[addPreSearch](addPreSearch.md) 


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
