---
title: "Understand the Client API object model in model-driven apps"
description: "The Client API object model for model-driven apps provides you objects and methods that you can use to apply custom business logic in model-driven apps using JavaScript."
author: sriharibs-msft
ms.author: srihas
ms.date: 03/27/2026
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

The Client API object model for model-driven apps provides objects and methods that you can use to apply custom business logic in model-driven apps by using JavaScript, such as:

- Get or set column values.
- Show and hide user interface elements.
- Reference multiple controls per column.
- Access multiple forms per table.
- Manipulate form navigation items.
- Interact with the business process flow control.

It's important that you understand the model-driven apps Client API object model to effectively write and use your JavaScript code.

## Root objects in the Client API object model

At the root of the Client API object model are the following contexts and the Xrm object:

|Object|Description|
|--|--|
|[execution context](clientapi-execution-context.md)|Represents the execution context for an event in model-driven apps forms and grids.|
|[form context](clientapi-form-context.md) |Provides a reference to a form or an item on the form against which the current code executes. To get the form context object, use the execution context [getFormContext](reference/executioncontext/getFormContext.md) method.|
|[grid context](clientapi-grid-context.md)|Provides a reference to a grid or a subgrid on a form against which the current code executes.|
|[Xrm](clientapi-xrm.md)| Provides a global object for performing operations that don't directly impact the data and UI in forms, grids, subgrids, controls, or columns. For example, use it to navigate forms, and create and manage records by using Web API.|

### Related articles

[Client API global context](clientapi-xrm.md#client-api-global-context)<br/>
[Client API reference](reference.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
