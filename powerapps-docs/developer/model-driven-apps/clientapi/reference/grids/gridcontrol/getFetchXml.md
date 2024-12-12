---
title: "getFetchXml (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getFetchXml method.
author: clromano
ms.author: clromano
ms.date: 06/29/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getFetchXml (Client API reference)

[!INCLUDE[./includes/getFetchXml-description.md](./includes/getFetchXml-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`var result = gridContext.getFetchXml();`

## Return Value

**Type**: String

**Description**: The FetchXML query.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext) 

## Example

The following example displays the retrieved Fetch XML of the Contacts subgrid in the console:

```JavaScript
function myFunction(executionContext) {
    var formContext = executionContext.getFormContext(); // get the form context
    var gridContext = formContext.getControl("Contacts"); // get the grid context
    var retrieveFetchXML = function (exeCtx) {
        var gridCtx = exeCtx.getFormContext().getControl("Contacts");
        var result = gridCtx.getFetchXml();
        console.log(result)
    };
    gridContext.addOnLoad(retrieveFetchXML);
}
```

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
