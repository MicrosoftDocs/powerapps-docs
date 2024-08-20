---
title: "Client API execution context in model-driven apps| MicrosoftDocs"
description: "Learn about the model-driven application client API execution context"
author: adrianorth
ms.author: aorth
ms.date: 08/20/2024
ms.reviewer: jdaly
ms.topic: conceptual
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
  - tahoon-ms
---
# Client API execution context

The execution context defines the event context in which your code executes. The execution context is passed when an event occurs on a form or grid. Use it in your event handler to perform various tasks such as determine [formContext](clientapi-form-context.md) or [gridContext](clientapi-grid-context.md), or manage the save event.

The execution context is passed in one of the following ways:

- **Defining event handlers using UI**: The execution context is an *optional* parameter that can be passed to a JavaScript library function through an event handler. Use the **Pass execution context as first parameter** option in the **Handler Properties** dialog while specify the name of the function to pass the event execution context. The execution context is the first parameter passed to a function.

   ### [Legacy](#tab/pass-execution-context-legacy)

     ![Pass execution context.](../media/ClientAPI-PassExecutionContext.png "Pass execution context")

   ### [Unified Interface](#tab/pass-execution-context-unified-interface)

     ![Pass execution context as parameter.](../media/pass-execution-context-as-first-parameter.png "Pass execution context as parameter")

   ---

- **Defining event handlers using code**: The execution context is automatically passed as the first parameter to functions set using code. For a list of methods that can be used to define event handlers in code, see [Add or remove functions to events using code](events-forms-grids.md#add-or-remove-event-handler-function-to-event-using-code).

The execution context object provides many methods to further work with the context. More information: [Execution context (Client API reference)](reference/execution-context.md)

## Common mistakes in accessing contexts

The context passed to an event is only valid during the event. Don't keep a reference to a context after the event ends. The following are common anti-patterns because they access the context after the event handler finishes:

### Accessing context in a promise

The context isn't valid after a [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) resolves.

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

The context isn't valid after using [await](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/await) within an [async function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/async_function). 

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

The context isn't valid after using [setTimeout](https://developer.mozilla.org/docs/Web/API/setTimeout) or [setInterval](https://developer.mozilla.org/docs/Web/API/setInterval) to defer executing some code.

```JavaScript
function onLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    if (notReady) {
        setTimeout(function () {
            // Using formContext or executionContext here is not supported
            // because onLoad has already completed when this delayed function executes.
            var name = formContext.getAttribute("name").getValue();
        }, 100);
    } else {
        formContext.getAttribute("name").setValue("abc");
    }
}
```

### Accessing context in a stored variable

Don't cache the context as a variable.

```JavaScript
function onLoad(executionContext) {
    window.__myExecutionContext = executionContext;
}

// This function is called any time later.
function customFunction() {
    // Using formContext or executionContext here is not supported
    // because onLoad has already completed when customFunction executes.
    var formContext = window.__myExecutionContext.getFormContext();
    formContext.getAttribute("name").setValue("abc");
}
```


### Related articles

 [Client API form context](clientapi-form-context.md)<br>
 [Client API grid context](clientapi-grid-context.md)<br>
 [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
