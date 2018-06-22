---
title: "Understand the Client API object model in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3335aec5-6b48-4ef6-8d49-2833b177f318
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Understand the Client API object model

[!INCLUDE[](../../includes/cc_applies_to_update_9_0_0.md)]

The Client API object model for Customer Engagement provides you objects and methods that you can use to apply custom business logic in Customer Engagement using JavaScript, such as:
- Get or set attribute values.
- Show and hide user interface elements.
- Reference multiple controls per attribute.
- Access multiple forms per entity.
- Manipulate form navigation items.
- Interact with the business process flow control.

Its important that you understand the Customer Engagement Client API object model to effectively write and use your JavaScript code in Customer Enagagement.

## Root objects in the Client API object model

At the root of the Client API object model are the following contexts and the Xrm object:

|Object|Description|
|--|--|
|**executionContext**|Represents the execution context for an event in Customer Engagement forms and grids.<br/>More information: [Client API execution context](clientapi-execution-context.md)|
|**formContext** |Provides a reference to a form or an item on the form against which the current code executes. To get the **formContext** object, use the **executionContext**.[getFormContext](reference/executioncontext/getFormContext.md) method.<br/>More information: [Client API form context](clientapi-form-context.md)|
|**gridContext** |Provides a reference to a grid or a subgrid on a form against which the current code executes.<br/>More information: [Client API grid context](clientapi-form-context.md)|
|**Xrm**| Provides a global object for performing operations that do not directly impact the data and UI in forms, grids, subgrids, controls, or attributes. For example, navigate forms, create and manage records using Web API.<br/>More information: [Client API Xrm object](clientapi-xrm.md)|

### Related topics

[Client API global context](clientapi-xrm.md#client-api-global-context)

[Client API reference](reference.md)








