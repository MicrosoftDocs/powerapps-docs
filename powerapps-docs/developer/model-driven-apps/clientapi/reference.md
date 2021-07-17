---
title: "Client API Reference for model-driven apps | MicrosoftDocs"
description: "The topic provides client API reference for model-driven apps."
ms.date: 06/27/2019
ms.service: powerapps
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Client API Reference for model-driven apps



This section contains reference documentation for client API object model that can be used with JavaScript libraries.

> [!IMPORTANT]
> - The Client API object model also contains the **Xrm.Internal** namespace, and use of the objects/methods in this namespace isn’t supported. These objects, and any parts of the HTML Document Object Model (DOM), are subject to change without notice. We recommend that you don’t use these functions or any script that depends on the DOM.
> - Also, while debugging, you may find methods and objects in the Client API object model that aren’t documented. Only documented objects and methods are supported.
> - The client scripting APIs available in this documentation also apply to Dynamics 365 Customer Engagement (on-premises).

The topics under this section are organized as follows:
- Starts with reference for all the events, collections, and the execution context object.
- Continues on to provide information about methods for **attributes** and **controls** in Customer Engagement that are actually collections that appear under different objects in the Client API object model.
- Provides reference for properties and methods for the **formContext** and **gridContext** objects.
- Finally provides reference for namespaces in the **Xrm** object model. 

### Related topics

[Apply business logic using client scripting in model-driven apps](../client-scripting.md)<br/>
[Understand the Client API object model](understand-clientapi-object-model.md)<br/>
[Model-driven apps Developer Overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]