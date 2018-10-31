---
title: "addPreSearch (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d69a432a-1d74-4782-bedd-f9f30d3d7d9c
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addPreSearch (Client API reference)



Applies changes to lookups based on values current just as the user is about to view results for the lookup.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addPreSearch(myFunction)`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes| The function that will be run just before the search to provide results for a lookup occurs. You can use this function to call one of the other lookup control functions and improve the results to be displayed in the lookup. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[PreSearch event](../events/PreSearch.md)

[removePreSearch](removePreSearch.md) 


