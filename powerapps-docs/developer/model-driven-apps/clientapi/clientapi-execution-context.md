---
title: "Client API execution context in model-driven apps| MicrosoftDocs"
description: "Explains the client api execution context"
author: adrianorth
ms.author: aorth

ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Client API execution context

The execution context defines the event context in which your code executes. The execution context is passed when an event occurs on a form or grid, which you can use it in your event handler to perform various tasks such as determine [formContext](clientapi-form-context.md) or [gridContext](clientapi-grid-context.md), or manage the save event. 

The execution context is passed in one of the following ways:

- **Defining event handlers using UI**: The execution context is an *optional* parameter that can be passed to a JavaScript library function through an event handler. Use the **Pass execution context as first parameter** option in the **Handler Properties** dialog while specify the name of the function to pass the event execution context. The execution context is the first parameter passed to a function.

   ### [Legacy](#tab/pass-execution-context-legacy)
     ![Pass execution context.](../media/ClientAPI-PassExecutionContext.png "Pass execution context")

   ### [Unified Interface](#tab/pass-execution-context-unified-interface)
     ![Pass execution context as parameter.](../media/pass-execution-context-as-first-parameter.png "Pass execution context as parameter")

   ---

- **Defining event handlers using code**: The execution context is automatically passed as the first parameter to functions set using code. For a list of methods that can be used to define event handlers in code, see [Add or remove functions to events using code](events-forms-grids.md#add-or-remove-event-handler-function-to-event-using-code).

The execution context object provides a number of methods to further work with the context. More information: [Execution context (Client API reference)](reference/execution-context.md)

## Common mistakes in accessing contexts

Contexts are passed as part of lifecycle functions. These contexts are only valid during the event. Don't keep a reference to it after the event ends. The following are common errors because they access the context after the event handler finishes:

### Accessing context in a promise

```JavaScript
function onLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    fetch("https://www.contoso.com/").then(
        function (result) {
            // Using formContext or executionContext here is not supported
            // because onLoad has already completed when the promise is resolved.
            formContext.getAttribute("name").setValue(result);
        }
    );
}
```

### Accessing context after an await statement

```JavaScript
async function onLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    var result = await fetch("https://www.contoso.com/");
    // Using formContext or executionContext here is not supported
    // because the synchronous part of onLoad has already completed.
    formContext.getAttribute("name").setValue(result);
}
```

### Accessing context in a timeout function

```JavaScript
function onLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    if (notReady) {
        setTimeout(function () {
            // Using formContext or executionContext here is not supported
            // because onLoad has already completed when this delayed function executes.
            onLoad(executionContext);
        }, 100);
    } else {
        formContext.getAttribute("name").setValue("abc");
    }
}
```

### Accessing context in a stored variable

```JavaScript
function onLoad(executionContext) {
    window.__myContext = executionContext;
}

// This function is called any time later.
function customFunction() {
    // Using formContext or executionContext here is not supported
    // because onLoad has already completed when this function executes.
    var formContext = window.__myContext.getFormContext();
    formContext.getAttribute("name").setValue("abc");
}
```


### Related articles

 [Client API form context](clientapi-form-context.md)<br>
 [Client API grid context](clientapi-grid-context.md)<br>
 [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
