---
title: "getFetchXml (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getFetchXml (Client API reference)



[!INCLUDE[./includes/getFetchXml-description.md](./includes/getFetchXml-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`var result = gridContext.getfetchXml();`

## Return Value

**Type**: String

**Description**: The FetchXML query.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext) 

## Example

The following example displays the retrieved Fetch XNL of the Contacts subgrid in the Console:

```JavaScript
function myFunction(executionContext) {
    var formContext = executionContext.getFormContext(); // get the form context
    var gridContext = formContext.getControl("Contacts"); // get the grid context
    var retrieveFetchXML = function () {
        var result = gridContext.getFetchXml();
        console.log(result)
    };
    gridContext.addOnLoad(retrieveFetchXML);    
}
```


