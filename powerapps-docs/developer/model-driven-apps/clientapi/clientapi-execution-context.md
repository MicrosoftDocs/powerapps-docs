---
title: "Client API execution context in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 1fcbf0fd-4e47-4352-a555-9315f7e57331
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Client API execution context



The execution context defines the event context in which your code executes. The execution context is passed when an event occurs on a form or grid, which you can use it in your event handler to perform various tasks such as determine [formContext](clientapi-form-context.md) or [gridContext](clientapi-grid-context.md), or manage the save event. 

The execution context is passed in one of the following ways:

- **Defining event handlers using UI**: The execution context is an *optional* parameter that can be passed to a JavaScript library function through an event handler. Use the **Pass execution context as first parameter** option in the **Handler Properties** dialog while specify the name of the function to pass the event execution context. The execution context is the first parameter passed to a function.<br/><br/>
![Pass execution context](../media/ClientAPI-PassExecutionContext.png)<br/><br/>

- **Defining event handlers using code**: The execution context is automatically passed as the first parameter to functions set using code. For a list of methods that can be used to define event handlers in code, see [Add or remove functions to events using code](events-forms-grids.md#add-or-remove-event-handler-function-to-event-using-code). 

The execution context object provides a number of methods to further work with the context. More information: [Execution context (Client API reference)](reference/execution-context.md)


### Related topics

 [Client API form context](clientapi-form-context.md)<br>
 [Client API grid context](clientapi-grid-context.md)<br>
 [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions)


