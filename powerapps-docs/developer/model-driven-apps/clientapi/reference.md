---
title: "Client API Reference for model-driven apps "
description: "The topic provides client API reference for model-driven apps."
ms.date: 05/13/2024
author: sriharibs-msft
ms.author: srihas
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Client API Reference for model-driven apps



This section contains reference documentation for client API object model that can be used with JavaScript libraries.

> [!IMPORTANT]
> - The Client API object model also contains the **Xrm.Internal** namespace, and use of the objects/methods in this namespace isn't supported. These objects, and any parts of the HTML Document Object Model (DOM), are subject to change without notice. We recommend that you don't use these functions or any script that depends on the DOM.
> - Also, while debugging, you may find methods and objects in the Client API object model that aren't documented. Only documented objects and methods are supported.
> - Most of the client scripting APIs available in this documentation also apply to Dynamics 365 Customer Engagement (on-premises). For a list of client scripting APIs not available for Customer Engagement (on-premises), see [Client scripting reference for Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/developer/clientapi/reference).

The topics under this section are organized as follows:

- Starts with reference for all the events, collections, context objects and save event.
   - [Events](reference/events.md)
   - [Collections](reference/collections.md)
   - [GetGlobalContext function and ClientGlobalContext.js.aspx](reference/GetGlobalContext-ClientGlobalContext.js.aspx.md)
   - [Execution context](reference/execution-context.md)
   - [Save event arguments](reference/save-event-arguments.md)

- Continues on to provide information about methods for **attributes** and **controls** in model-driven apps that are actually collections that appear under different objects in the Client API object model.

   - [Attributes](reference/attributes.md)
   - [Controls](reference/controls.md)

- Provides reference for properties and methods for the **formContext** and **gridContext** objects.

   - [formContext.data ](reference/formContext-data.md)
   - [formContext.data.entity ](reference/formContext-data-entity.md)
   - [formContext.data.process ](reference/formContext-data-process.md)
   - [formContext.ui ](reference/formContext-ui.md)
   - [Grids and subgrids in model-driven apps ](reference/grids.md)

- Finally provides reference for namespaces in the **Xrm** object model.

   - [Xrm.App](reference/xrm-app.md)
   - [Xrm.Device](reference/xrm-device.md)
   - [Xrm.Encoding](reference/xrm-encoding.md)
   - [Xrm.Navigation](reference/xrm-navigation.md)
   - [Xrm.Panel](reference/xrm-panel.md)
   - [Xrm.Utility](reference/xrm-utility.md)
   - [Xrm.WebApi](reference/xrm-webapi.md)



### Related articles

[Apply business logic using client scripting in model-driven apps](../client-scripting.md)   
[Understand the Client API object model](understand-clientapi-object-model.md)   
[Model-driven apps Developer Overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
