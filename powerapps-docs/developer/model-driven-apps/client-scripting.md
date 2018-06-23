---
title: Use client scripting with model-driven apps | Microsoft Docs
description: Learn how developers can use JavaScript in client-side scripts and model-driven apps
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/13/2018
ms.author: jdaly
---

# Client scripting with model-driven apps

Client-side scripting using JavaScript is one of the ways to apply custom business process logic for displaying data on a form in a model-driven app, but it shouldn't be your first choice. *Business rules* provides provides a way for someone who does not know JavaScript and is not a developer, to apply business process logic in a form. More information: [Common Data Service for Apps Customization Guide Create business rules and recommendations to apply logic in a form](/dynamics365/customer-engagement/customize/create-business-rules-recommendations-apply-logic-form)

> [!TIP]
> You will find the business rule designer within the **Common Data Service** area on [powerapps.com](http://web.powerapps.com). When you view an entity, look for the **Business rules** tab.

If your business requirement can't be achieved using a business rule, you will find that client-scripting using the client API object model provides a powerful way to extend the behavior of the application and enable automation in the client.

## Resources

The following resources for client scripting are available in the Common Data Service for Apps Developer guide.

- [Client scripting with model-driven apps](client-scripting.md)
- [Events in forms and grids in model-driven apps](clientapi/events-forms-grids.md)
- [Understand the Client API object model](clientapi/understand-clientapi-object-model.md)
- [Tutorial: Write your first client script](clientapi/walkthrough-write-your-first-client-script.md)
- [Debug your JavaScript code](/dynamics365/customer-engagement/developer/clientapi/debug-javascript-code)
- [Best practices: Client scripting](/dynamics365/customer-engagement/developer/clientapi/client-scripting-best-practices)
- [Client API Reference](/dynamics365/customer-engagement/developer/clientapi/reference)

