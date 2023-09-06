---
title: "addPreSearch (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnPreSearch method.
author: chmoncay
ms.author: chmoncay
ms.date: 08/12/2023
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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
|myFunction |Function |Yes| The function that is run just before the search to provide results for a lookup occurs. You can use this function to call one of the other lookup control functions and improve the results to be displayed in the lookup. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

## Example

<!-- Added from https://github.com/MicrosoftDocs/powerapps-docs/issues/4252 -->

In the following example, the `onLoad` function is set for the form onload event. It modifies the search filter for all the lookup controls associated with the `primaryid` lookup attribute because there may be more than one.

It adds the `myPreSearchCallBack` function using the `addPreSearch` method. This example requires all the contact records returned to have the `firstname` value of 'Eric'.

```javascript
function onLoad(executionContext) {
   var fromContext = executionContext.getFormContext()
   var attribute = fromContext.getAttribute("primarycontactid") 
   attribute.controls.forEach(control => control.addPreSearch(myPreSearchCallBack))
}

function myPreSearchCallBack (executionContext){
   var control = executionContext.getEventSource();
   var filter = "<filter><condition attribute='firstname' operator='eq' value='Eric' /></filter>";
   control.addCustomFilter(filter);
}
```

### Related articles

[PreSearch event](../events/PreSearch.md)

[removePreSearch](removePreSearch.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
