---
title: "Apply business logic using client scripting in model-driven apps: JavaScript"
description: Learn how to apply custom business logic in model-driven apps using JavaScript client-side scripts. Discover best practices and implementation strategies.
suite: powerapps
author: sriharibs-msft
ms.author: srihas
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.collection: get-started
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Apply business logic using client scripting in model-driven apps with JavaScript

JavaScript client-side scripting provides a powerful way to apply custom business logic for displaying data on forms in model-driven apps.

> [!IMPORTANT]
> All the client scripting concepts and APIs explained in this documentation also apply to [Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/overview) users.

However, don't use client scripting as your first choice for applying custom business process logic in model-driven app forms. *Business rules* provide a way for someone who doesn't know JavaScript and isn't a developer to apply business process logic in a form. For more information, see [Create business rules to apply logic](../../maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form.md). You find the business rule designer within the **Data** > **Tables** > [table_name] area on [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). When you view table, look for the **Business rules** tab.

However, if your business requirement can't be achieved by using a business rule, client scripting by using the client API object model provides a powerful way to extend the behavior of the application and enable automation in the client.

## Use client scripting in model-driven apps

Forms in model-driven apps help display data to the user. A form in model-driven apps can contain items such as columns, a quick form, or a grid. An [event](clientapi/events-forms-grids.md) occurs in model-driven apps forms whenever:

- A form loads.
- Data changes in a column or an item within the form.
- Data is saved in a form.

You can attach your JavaScript code to "react" to these events so that your code gets executed when the event occurs on the form. You attach your JavaScript code (scripts) to these events by using a [Script web resource](script-jscript-web-resources.md) in model-driven apps. 

Model-driven apps provide you with a rich set of **client APIs** to interact with form objects and events to control what and when to display on a form.

> [!NOTE]
> Some client APIs are deprecated in the current release of model-driven apps. Ensure that you're aware of these APIs as you write your client-side code for model-driven apps. For more information, see [Deprecated client APIs](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated).

## Next steps

> [!div class="nextstepaction"]
> [Events in forms and grids](clientapi/events-forms-grids.md)

> [!div class="nextstepaction"]
> [Understand the Client API object model](clientapi/understand-clientapi-object-model.md)

> [!div class="nextstepaction"]
> [Walkthrough: Write your first client script](clientapi/walkthrough-write-your-first-client-script.md)


## Reference

[Client API reference](clientapi/reference.md)


### Related articles

[Web resources for model-driven apps](web-resources.md)<br/>
[Customize commands and the ribbon](customize-commands-ribbon.md)<br/>




[!INCLUDE[footer-include](../../includes/footer-banner.md)]
