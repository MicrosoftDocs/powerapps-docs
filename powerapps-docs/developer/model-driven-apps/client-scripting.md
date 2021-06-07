---
title: Apply business logic using client scripting in model-driven apps using JavaScript | Microsoft Docs
description: Learn how developers can use JavaScript in client-side scripts to apply custom business logic in model-driven apps.
services: ''
suite: powerapps
author: KumarVivek
ms.service: powerapps
ms.custom: "intro-internal"
ms.topic: article
ms.date: 04/15/2021
ms.author: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Apply business logic using client scripting in model-driven apps using JavaScript

Client-side scripting using JavaScript is one of the ways to apply custom business process logic for displaying data on a form in a model-driven app.

> [!IMPORTANT]
> All the client scripting concepts and APIs explained in this documentation also apply to [Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/overview) users.

Client scripting shouldn't be your first choice though for applying custom business process logic in model-driven app forms. *Business rules* provide a way for someone, who does not know JavaScript and is not a developer, to apply business process logic in a form. More information: [Create business rules to apply logic](../../maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form.md). You will find the business rule designer within the **Data** > **Tables** > [table_name] area on [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). When you view table, look for the **Business rules** tab.

However, if your business requirement can't be achieved using a business rule, you will find that client-scripting using the client API object model provides a powerful way to extend the behavior of the application and enable automation in the client.

## Use client scripting in model-driven apps

Forms in model-driven apps help display data to the user. A form in model-driven apps can contain items such as columns, a quick form, or a grid. An [event](clientapi/events-forms-grids.md) occurs in model-driven apps forms whenever:

- A form loads.
- Data is changed in a column or an item within the form.
- Data is saved in a form.

You can attach your JavaScript code to "react" to these events so that your code gets executed when the event occurs on the form. You attach your JavaScript code (scripts) to these events by using a [Script web resource](script-jscript-web-resources.md) in model-driven apps. 

Model-driven apps provides you a rich set of **client APIs** to interact with form objects and events to control what and when to display on a form.

> [!NOTE]
> Some client APIs are deprecated in the current release of model-driven apps. Ensure that you are aware of these APIs as you write your client-side code for model-driven apps. More information: [Deprecated client APIs](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated)

## Get started here

[Events in forms and grids](clientapi/events-forms-grids.md)<br/>
[Understand the Client API object model](clientapi/understand-clientapi-object-model.md)<br/>
[Walkthrough: Write your first client script](clientapi/walkthrough-write-your-first-client-script.md)

## Reference

[Client API reference](clientapi/reference.md)


### Related topics

[Web resources for model-driven apps](web-resources.md)<br/>
[Customize commands and the ribbon](customize-commands-ribbon.md)<br/>




[!INCLUDE[footer-include](../../includes/footer-banner.md)]