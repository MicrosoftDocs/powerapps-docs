---
title: "gridContext.addOnLoad (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the gridContext.addOnLoad method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# gridContext.addOnLoad (Client API reference)

[!INCLUDE[./includes/addOnLoad-description.md](./includes/addOnLoad-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.addOnLoad(myFunction);`

## Parameter

|Name|Type|Required|Description|
|---|---|---|---|
|`myFunction`| function reference | Yes| The function to be executed when the subgrid loads. The function will be added to the bottom of the event handler pipeline. The execution context is automatically passed as the first parameter to the function. See [execution context](../../../clientapi-execution-context.md) for more information. |

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

## Example

Add the myContactsGridOnloadFunction function to the Contacts subgrid **OnLoad** event.

```JavaScript
function myFunction(executionContext) {
    let formContext = executionContext.getFormContext(); // get the form context
    let gridContext = formContext.getControl("Contacts");// get the grid context
    let myContactsGridOnloadFunction = function () { console.log("Contacts Subgrid OnLoad event occurred") };
    gridContext.addOnLoad(myContactsGridOnloadFunction);
}
```

### Related articles

[removeOnLoad](removeOnLoad.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
