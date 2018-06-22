---
title: "removePreSearch (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 2451c4ac-527c-4487-8f52-bde1690c5bde
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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


