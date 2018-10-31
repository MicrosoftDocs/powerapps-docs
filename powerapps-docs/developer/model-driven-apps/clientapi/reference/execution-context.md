---
title: "Client API execution context in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 1fcbf0fd-4e47-4352-a555-9315f7e57331
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Execution context (Client API reference)



The execution context defines the event context in which your code executes. More information: [Client API execution context](../clientapi-execution-context.md).

The execution context object provides the following methods.

|Method |Description |
|---|---|
|[getDepth](executioncontext/getDepth.md)|Returns a value that indicates the order in which this handler is executed.|
|[getEventArgs](executioncontext/getEventArgs.md)|Returns an object with methods to manage the **OnSave** event.|
|[getEventSource](executioncontext/getEventSource.md)|Returns a reference to the object that the event occurred on.|
|[getFormContext](executioncontext/getFormContext.md)|Returns a reference to the form or an item on the form depending on where the method was called.|
|[getSharedVariable](executioncontext/getSharedVariable.md)|Retrieves a variable set using the [setSharedVariable](executioncontext/setSharedVariable.md) method.|
|[setSharedVariable](executioncontext/setSharedVariable.md)|Sets the value of a variable to be used by a handler after the current handler completes.|

### Related topics

[Client API execution context](../clientapi-execution-context.md)

[Save event arguments](save-event-arguments.md)

[Understand Client API object model](../understand-clientapi-object-model.md) 

