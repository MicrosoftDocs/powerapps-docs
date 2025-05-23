---
title: "Understand the Client API object model in model-driven apps"
description: "The Client API object model for model-driven apps provides you objects and methods that you can use to apply custom business logic in model-driven apps using JavaScript."
author: sriharibs-msft
ms.author: srihas
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: concept-article
applies_to: 
  - "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Understand the Client API object model

The Client API object model for model-driven apps provides you objects and methods that you can use to apply custom business logic in model-driven apps using JavaScript, such as:

- Get or set column values.
- Show and hide user interface elements.
- Reference multiple controls per column.
- Access multiple forms per table.
- Manipulate form navigation items.
- Interact with the business process flow control.

Its important that you understand the model-driven apps Client API object model to effectively write and use your JavaScript code.

## Root objects in the Client API object model

At the root of the Client API object model are the following contexts and the Xrm object:

|Object|Description|
|--|--|
|`executionContext`|Represents the execution context for an event in model-driven apps forms and grids.<br/>More information: [Client API execution context](clientapi-execution-context.md)|
|`formContext` |Provides a reference to a form or an item on the form against which the current code executes. To get the `formContext` object, use the `executionContext`.[getFormContext](reference/executioncontext/getFormContext.md) method.<br/>More information: [Client API form context](clientapi-form-context.md)|
|`gridContext`|Provides a reference to a grid or a subgrid on a form against which the current code executes.<br/>More information: [Client API grid context](clientapi-grid-context.md)|
|`Xrm`| Provides a global object for performing operations that do not directly impact the data and UI in forms, grids, subgrids, controls, or columns. For example, navigate forms, create and manage records using Web API.<br/>More information: [Client API Xrm object](clientapi-xrm.md)|

### Related articles

[Client API global context](clientapi-xrm.md#client-api-global-context)<br/>
[Client API reference](reference.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
