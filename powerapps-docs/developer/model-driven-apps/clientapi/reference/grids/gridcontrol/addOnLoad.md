---
title: "addOnLoad (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 11/10/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 24f34ac9-2a15-478e-980c-588a79d84e8d
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addOnLoad (Client API reference)



[!INCLUDE[./includes/addOnLoad-description.md](./includes/addOnLoad-description.md)]

## Grid types supported

Read-only grids

## Syntax

`gridContext.addOnLoad(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be executed when the subgrid loads. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [execution context](../../../clientapi-execution-context.md) for more information.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

## Example

Add the myContactsGridOnloadFunction function to the Contacts subgrid **OnLoad** event.

```JavaScript
function myFunction(executionContext) {
    var formContext = executionContext.getFormContext(); // get the form context
    var gridContext = formContext.getControl("Contacts");// get the grid context
    var myContactsGridOnloadFunction = function () { console.log("Contacts Subgrid OnLoad event occurred") };
    gridContext.addOnLoad(myContactsGridOnloadFunction);
}
```

### Related topics

[removeOnLoad](removeOnLoad.md)



