---
title: "Client API grid context in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f884d7d4-31e6-4080-acd9-493e81e6b278
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Client API grid context



The grid context object provides a reference to the grid or a subgrid on a form against which the current code is executed.

Depending on where your JavaScript code is executed, you get the **gridContext** object in one of the following ways:

- **Executing code on a form event**: Use the [formContext](clientapi-form-context.md) object to get an instance of the form where the code is executed, and then retrieve the subgrid control on the form. For example, when you know the name of a subgrid control (say **Contacts** subgrid in the default account form), you can access it using the following code:

    ```JavaScript
    function doSomething(executionContext) {
       var formContext = executionContext.getFormContext(); // get the form Context
       var gridContext = formContext.getControl("Contacts"); // get the grid context

       // Perform operations on the subgrid
    }
    ```

- **Executing code on a grid event**: Use the [getFormContext](reference/executioncontext/getFormContext.md) method of the passed in execution context object to directly return reference to the grid where the code is executed. The grid events include [OnChange](reference/events/grid-onchange.md), [OnRecordSelect](reference/events/grid-onrecordselect.md), and [OnSave](reference/events/grid-onsave.md).

    ```JavaScript
    function doSomething(executionContext) {
        var gridContext = executionContext.getFormContext(); // get the grid context

        // Perform operations on the grid
    }
    ```

For more information about working with methods and events available for grids and subgrids, see [Grids and subgrids](reference/grids.md).

> [!NOTE]
> Getting the **gridContext** object for JavaScript functions for ribbon actions is different from how you get it in form scripting. More information: [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)

## Related topics

[Client API form context](clientapi-form-context.md)

[Client API execution context](clientapi-execution-context.md)

[Understand the Client API object model](understand-clientapi-object-model.md)

[Grids and subgrids](reference/grids.md)

 

