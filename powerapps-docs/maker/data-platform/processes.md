---
title: "Apply business logic in Microsoft Dataverse | MicrosoftDocs"
description: "Learn about the different types of business logic you can use in your app"
ms.custom: intro-internal
ms.date: 12/20/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 0b4e6602-5701-4859-81cc-6f6fe50901b2
caps.latest.revision: 44
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Apply business logic in Microsoft Dataverse
[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

There are several choices available for applying business logic in Dataverse. 

## Business rules
You can create business rules and recommendations to apply logic and validations without writing code or creating plug-ins. Business rules provide a simple interface to implement and maintain fast-changing and commonly used rules.

Define *business rules* for a table that apply to all the table forms and at the server level. Business rules defined for a table apply to both *canvas apps* and *model-driven apps* if the table is used in the app. More information: [Create a business rule for a table](data-platform-create-business-rule.md)

> [!NOTE]
> To define a business rule that applies to a form in a model-driven app, see [Create business rules for a model-driven app form](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)

## Dataverse processes
You can also use the following Dataverse processes:

- [Real-time workflows](overview-realtime-workflows.md)

- [Actions](actions.md).

## Power Automate
Power Automate has several different flows you can use to create automated workflows within Dataverse or between Dataverse and another app or service that can be used to synchronize files, get notifications, collect data, and more. 


|Flow type  |Description  |More information  |
|---------|---------|---------|
|Business process flows     | Define a set of steps that run in a Power Apps model-driven app for people to follow to take them to a desired outcome.        | [Learn more](/power-automate/create-business-process-flow)     |
|Cloud flows     |  Create a flow that performs one or more tasks automatically after it's triggered by an event.    | [Learn more](/power-automate/get-started-logic-flow)        |
|Instant flows   | Run repetitive tasks from anyplace, at any time, via a flow app on your mobile device.        | [Learn more](/power-automate/introduction-to-button-flows)        |
|Scheduled flows   | Create a flow that performs one or more tasks on a schedule.    | [Learn more](/power-automate/run-scheduled-tasks)        |
|Desktop flows   | Row and automate the playback of manual steps on legacy software.    | [Learn more](/power-automate/desktop-flows/overview)     |


### See also

[Apply business logic in model-driven apps](../model-driven-apps/guide-staff-through-common-tasks-processes.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]