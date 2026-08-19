---
title: "Use Client API Grid Context in Model-Driven Apps"
description: "Learn how to use the Client API grid context to access subgrids on model-driven app forms, understand its limitations, and start coding."
author: Hillaryyaory-microsoft
ms.author: hillaryyaory
ms.date: 08/18/2026
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
  - fikaradz
  - tahoon-ms
  - clromano
---
# Client API grid context

The Client API grid context helps you access and work with tabular data in grids and subgrids on a form. Grids can span the entire form or appear as form items called **subgrids**.

The Client API grid context provides reference to a subgrid on a form against which the current code is executed. 

Use the [formContext](clientapi-form-context.md) to get an instance of the form where the code is executed, and then retrieve the subgrid control on the form. For example, when you know the name of a subgrid control (say **Contacts** subgrid in the default account form), you can access it using the following code:

```JavaScript
function doSomething(executionContext) {
   var formContext = executionContext.getFormContext(); // get the form Context
   var gridContext = formContext.getControl("Contacts"); // get the grid context

   // Perform operations on the subgrid
}
```

## Limitations

- Getting the context of a grid (spanning the entire form) is only supported in ribbon commands. For more information, see [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions).
- Calls to `getControl()` aren't supported when you use `gridContext`.
- Grid contexts have the same validity as their execution context. Once the event handler for the execution context finishes, these contexts require extra care to use. See [Using context objects asynchronously](clientapi-execution-context.md#using-context-objects-asynchronously).


## Related articles

[Client API form context](clientapi-form-context.md)   
[Client API execution context](clientapi-execution-context.md)   
[Understand the Client API object model](understand-clientapi-object-model.md)  
[Grids and subgrids](reference/grids.md)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
