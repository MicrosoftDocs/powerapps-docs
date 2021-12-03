---
title: "Client API grid context in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f884d7d4-31e6-4080-acd9-493e81e6b278
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Client API grid context

Grids present data in a tabular format. Grids can span the entire form or can be one of the items on a form; the latter are called **subgrids**.

The Client API grid context object provides reference to a subgrid on a form against which the current code is executed. 

> [!NOTE]
> Getting the context of a grid (spanning the entire form) is only supported in ribbon commands. More information: [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)

Use the [formContext](clientapi-form-context.md) object to get an instance of the form where the code is executed, and then retrieve the subgrid control on the form. For example, when you know the name of a subgrid control (say **Contacts** subgrid in the default account form), you can access it using the following code:

```JavaScript
function doSomething(executionContext) {
   var formContext = executionContext.getFormContext(); // get the form Context
   var gridContext = formContext.getControl("Contacts"); // get the grid context

   // Perform operations on the subgrid
}
```

## Related topics

[Client API form context](clientapi-form-context.md)<br/>
[Client API execution context](clientapi-execution-context.md)<br/>
[Understand the Client API object model](understand-clientapi-object-model.md)<br/>
[Grids and subgrids](reference/grids.md)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]