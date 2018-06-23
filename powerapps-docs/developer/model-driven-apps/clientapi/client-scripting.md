---
title: "Client scripting in model-driven apps using JavaScript| MicrosoftDocs"
description: "Learn how to use Client API in model-driven apps to apply custom business process logic for displaying data on a form."
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 16271bd8-cfa8-4a7f-802a-60fbff7c3722
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Client scripting in model-driven apps using JavaScript



Client-side scripting using JavaScript is one of the ways to apply custom business process logic for displaying data on a form in model-driven apps. 

> [!NOTE]
> You can also use business rules, which provides a way for someone who does not know JavaScript and is not a developer, to apply business process logic in a form. More information: [Create business rules and recommendations to apply logic in a form](/dynamics365/customer-engagement/customize/create-business-rules-recommendations-apply-logic-form.md)  

Forms in model-driven apps help display data to the user. A form in model-driven apps can contain items such as fields, a quick form, or a grid. An [event](events-forms-grids.md) occurs in model-driven apps forms whenever:
- A form loads
- Data is changed in a field or an item within the form
- Data is saved in a form

You can attach your JavaScript code to "react" to these events so that your code gets executed when the event occurs on the form. You attach your JavaScript code (scripts) to these events by using a [Script web resource](../script-jscript-web-resources.md) in model-driven apps. 

model-driven apps provides you a rich set of **client APIs** to interact with form objects and events to control what and when to display on a form.

> [!NOTE]
> Some client APIs are deprecated in the current release of model-driven apps. Ensure that you are aware of these APIs as you write your client-side code for model-driven apps. More information: [Deprecated client APIs](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated)

## Get Started

[Events in forms and grids](events-forms-grids.md)

[Understand the Client API object model](understand-clientapi-object-model.md)

[Walkthrough: Write your first client script](walkthrough-write-your-first-client-script.md)

## Reference

[Client API reference](reference.md)


## Related topics

[Web resources for model-driven apps](../web-resources.md)

[Customize commands and the ribbon](../customize-commands-ribbon.md)