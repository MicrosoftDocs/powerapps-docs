---
title: "Client API Reference for Model-Driven Apps"
description: "Explore the client API reference for model-driven apps, including events, form and grid context, and Xrm namespaces. Learn how to use them in JavaScript."
ms.date: 10/29/2026
author: sriharibs-msft
ms.author: srihas
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Client API reference for model-driven apps



This section contains the client API reference for model-driven apps. Use these objects, methods, and events in JavaScript libraries to apply business logic to forms, grids, and app navigation.

> [!IMPORTANT]
> - The Client API object model also contains the **Xrm.Internal** namespace, and use of the objects and methods in this namespace isn't supported. These objects, and any parts of the HTML Document Object Model (DOM), are subject to change without notice. Don't use these functions or any script that depends on the DOM.
> - While debugging, you might find methods and objects in the Client API object model that aren't documented. Only documented objects and methods are supported.
> - Most of the client scripting APIs available in this documentation also apply to Dynamics 365 Customer Engagement (on-premises). For a list of client scripting APIs not available for Customer Engagement (on-premises), see [Client scripting reference for Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/developer/clientapi/reference).

The following list shows how the articles in this section are organized:

- Reference for all the events, collections, context objects, and save event.
   - [Events](reference/events.md)
   - [Collections](reference/collections.md)
   - [GetGlobalContext function and ClientGlobalContext.js.aspx](reference/GetGlobalContext-ClientGlobalContext.js.aspx.md)
   - [Execution context](reference/execution-context.md)
   - [Save event arguments](reference/save-event-arguments.md)

- Information about methods for **attributes** and **controls** in model-driven apps. These methods are collections that appear under different objects in the Client API object model.

   - [Attributes](reference/attributes.md)
   - [Controls](reference/controls.md)

- Reference for properties and methods for the **formContext** and **gridContext** objects.

   - [formContext.data ](reference/formContext-data.md)
   - [formContext.data.entity ](reference/formContext-data-entity.md)
   - [formContext.data.process ](reference/formContext-data-process.md)
   - [formContext.ui ](reference/formContext-ui.md)
   - [Grids and subgrids in model-driven apps ](reference/grids.md)

- Reference for namespaces in the **Xrm** object model.

   - [Xrm.App](reference/xrm-app.md)
   - [Xrm.Copilot](reference/xrm-copilot.md)
   - [Xrm.Device](reference/xrm-device.md)
   - [Xrm.Encoding](reference/xrm-encoding.md)
   - [Xrm.Navigation](reference/xrm-navigation.md)
   - [Xrm.Panel](reference/xrm-panel.md)
   - [Xrm.Utility](reference/xrm-utility.md)
   - [Xrm.WebApi](reference/xrm-webapi.md)



## Related articles

[Apply business logic using client scripting in model-driven apps](../client-scripting.md)   
[Understand the Client API object model](understand-clientapi-object-model.md)   
[Model-driven apps developer guide](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
