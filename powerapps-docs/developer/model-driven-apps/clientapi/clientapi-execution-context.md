---
title: "Client API Execution Context in Model-Driven Apps"
description: "Learn how to use the client API execution context in model-driven apps to handle form and grid events, get form context, and avoid async issues. Read more."
author: sriharibs-msft
ms.author: srihas
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: article
ai-usage: ai-assisted
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
  - tahoon-ms
  - fafuxa-ms
---
# Client API execution context in model-driven apps

The execution context defines the event context in which your code runs. The system passes the execution context when an event occurs on a form or grid. Use it in your event handler to perform various tasks such as determining the [formContext](clientapi-form-context.md) or [gridContext](clientapi-grid-context.md), or managing the save event.

You can pass the execution context in the following ways:

- **Defining event handlers using the UI**: The execution context is an *optional* parameter that you can pass to a JavaScript library function through an event handler. Use the **Pass execution context as first parameter** option in the **Handler Properties** dialog while specifying the name of the function to pass the event execution context. The execution context is the first parameter passed to a function.

   ### [Unified Interface](#tab/pass-execution-context-unified-interface)

     :::image type="content" source="../media/pass-execution-context-as-first-parameter.png" alt-text="Screenshot of the Unified Interface Handler Properties dialog with the Pass execution context as first parameter option.":::

   ### [Legacy](#tab/pass-execution-context-legacy)

     :::image type="content" source="../media/legacy-handler-properties-pass-execution-context.png" alt-text="Screenshot of the legacy Handler Properties dialog with the Pass execution context as first parameter option.":::

   ---

- **Defining event handlers using code**: The system automatically passes the execution context as the first parameter to functions set by using code. For a list of methods that you can use to define event handlers in code, see [Add or remove event handler functions by using Client API code](events-forms-grids.md#add-or-remove-event-handler-functions-by-using-client-api-code).

The execution context object provides methods to work with the context. For more information, see [Client API execution context methods reference](reference/execution-context.md).

## Use context objects asynchronously

The context that the system passes to an event only works as expected during the event. When you keep a reference to a context after the event ends, actions might occur that cause context methods to behave in an unexpected way.

For example, if your event handler dispatches an async action that takes a long time while you're holding on to a reference to the execution context, the end user might navigate away from the current page by the time the promise resolves and you invoke the context method. This situation might cause methods like `formContext.getAttribute(<name>).getValue()` to return `null`, even though at the time the original event handler executed, the attribute had a value.

The following examples show where you should add more checks and take caution because the event handler function uses the execution context after the event finishes.

### Access context in a promise

The context might change in unexpected ways after a [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) resolves.

```JavaScript
function onLoad(executionContext) {
  const formContext = executionContext.getFormContext();
  fetch("https://www.contoso.com/").then((result) => {
    // Using formContext or executionContext here may not work as expected
    // because onLoad has already completed when the promise is resolved.
    formContext.getAttribute("name").setValue(result);
  });
}
```

### Access context after an await statement

The context might change in unexpected ways after using [await](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/await) within an [async function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/async_function). 

```JavaScript
async function onLoad(executionContext) {
  const formContext = executionContext.getFormContext();
  const result = await fetch("https://www.contoso.com/");
    // Using formContext or executionContext here might not work as expected
    // because the synchronous part of onLoad has already completed.
    formContext.getAttribute("name").setValue(result);
}
```

### Access context in a timeout function

The context might change in unexpected ways after using [setTimeout](https://developer.mozilla.org/docs/Web/API/setTimeout) or [setInterval](https://developer.mozilla.org/docs/Web/API/setInterval) to defer executing some code.

```JavaScript
function onLoad(executionContext) {
  const formContext = executionContext.getFormContext();
    if (notReady) {
    setTimeout(() => {
            // Using formContext or executionContext here may not work as expected
            // because onLoad has already completed when this delayed function executes.
            const name = formContext.getAttribute("name").getValue();
        }, 100);
    } else {
        formContext.getAttribute("name").setValue("abc");
    }
}
```


### Related articles

 [Client API form context](clientapi-form-context.md)<br>
 [Client API grid context](clientapi-grid-context.md)<br>
 [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
