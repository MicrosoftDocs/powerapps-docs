---
title: "Apply custom business logic with business rules and flows in model-driven apps | MicrosoftDocs"
description: "Learn about the types of business logic you can use in your app"
ms.custom: intro-internal
ms.date: 08/02/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 0b4e6602-5701-4859-81cc-6f6fe50901b2
caps.latest.revision: 44
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Apply custom business logic with business rules and flows in model-driven apps

## The importance of business processes in model-driven apps

Defining and enforcing consistent business processes is one of the main reasons people use model-driven apps. Consistent processes help ensure that people using a model-driven app can focus on their work and not on remembering how to perform a set of manual steps in order to reach their objectives.

These fall into 2 major categories natively within model-driven apps.  **Business rules** and **Business process flows**.  Business process flows fall within the functionality delivered by Power Automate.

## Business rules

Business rules provide a simple interface to implement and maintain fast-changing and commonly used rules. The *scope* of a business rule defines where the business rule will run:

|||  
|-|-|  
|**If you select this item...**|**The scope is set to...**|  
|**Table**|All forms and server|  
|**All Forms**|All forms|  
|Specific form (**Account** form, for example)|Just that form|

For more information about defining business rules for a form in a model-driven app, see [Create business rules to apply logic in a model-driven app form](create-business-rules-recommendations-apply-logic-form.md)

> [!NOTE]
> To define a business rule for a table so that it applies at the server level to both *canvas apps* and *model-driven apps*, see [Create a business rule for a table](../data-platform/data-platform-create-business-rule.md).

## Power Automate Flows  
  
Power Automate includes several types of processes, each designed for a different purpose:  

-   Business process flows.  Ensure that people enter data consistently and follow the same steps every time they work in an app by creating a business process flow. These flows are authored in Power Automate, however they are only ever applicable to model-driven apps.  More information: [Business process flows overview](/flow/business-process-flows-overview)

:::image type="content" source="../../user/media/business-process.png" alt-text="Sample model-driven app":::

-   Workflows and actions. Dynamics 365 customizers may be familiar with the classic Microsoft Dataverse processes, which are workflows and actions. More information: [Use Workflow processes](/flow/workflow-processes) and [Actions overview](../data-platform/actions.md)

-   Automated flows. Create a Power Automate cloud flow that performs one or more tasks automatically after it's triggered by an event. These have the added advantage of being able to reach into the connector framework within your environment and therefore connect to other data sources such as SQL, SharePoint or any of the other 400 data sources and services. More information: [Create a flow](/flow/get-started-logic-flow)
    
-   Button flows. Create a Power Automate cloud flow that perform repetitive tasks simply by tapping a button on your mobile device. More information: [Introducing button flows](/flow/introduction-to-button-flows)
  
-   Scheduled flows. Create a flow that performs one or more tasks on a schedule such as once a day, on a specific date, or after a certain time. More information: [Run flows on a schedule](/flow/run-scheduled-tasks)
  
## Next steps

[Create business rules to apply logic in a model-driven app form](create-business-rules-recommendations-apply-logic-form.md)

[Learn about business process flows](/flow/business-process-flows-overview)

### See also

[Apply business logic with Dataverse](../data-platform/processes.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]