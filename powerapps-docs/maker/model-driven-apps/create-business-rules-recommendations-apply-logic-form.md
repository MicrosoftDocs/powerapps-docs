---
title: "Create model-driven app business rules and recommendations | MicrosoftDocs"
ms.custom: ""
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 00e62904-2ce9-4730-a113-02b1fedbf22e
caps.latest.revision: 31
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
tags: 
 - "PowerApps maker portal impact"
---
# Tutorial: Create business rules and recommendations to apply logic in a model-driven app form

This tutorial shows you how to create business rules and recommendations to apply form logic without writing JavaScript code or creating plug-ins.  Business rules provide a simple interface to implement and maintain fast-changing and commonly used rules. They can be applied to Main and Quick Create forms, and they work in PowerApps apps, Dynamics 365 customer engagement web apps, Dynamics 365 for tablets, and Dynamics 365 for Outlook (online or offline mode).  
  
 By combining conditions and actions, you can do any of the following with business rules:  
  
-   Set field values  
  
-   Clear field values  
  
-   Set field requirement levels  
  
-   Show or hide fields  
  
-   Enable or disable fields  
  
-   Validate data and show error messages  
  
-   Create business recommendations based on business intelligence.  
  
## Create a business rule or business recommendation
  
1. Open [solution explorer](advanced-navigation.md#solution-explorer).  
  
2.  Open the entity you want to create the business rule for (for example, open the **Account** entity), and then double-click **Business Rules**.  
  
 ![Create a business rule in the default solution](media/create-business-rule-the-default-solution.png "Create a business rule in the default solution")  
  
3.  Select **New**.  
  
     The Business Rule designer window opens with a single condition already created for you. Every rule starts with a condition. The business rule takes one or more actions based on that condition.  
  
 ![Business Rules design window](media/business-rules-design-window.png "Business Rules design window")  
  
   > [!TIP]
> If you want to modify an existing business rule, you must deactivate it before you can modify it.

4.  Add a description, if you want, in the description box in the upper-left corner of the window.  
  
5.  Set the scope, according to the following:  
  
    |||  
    |-|-|  
    |**If you select this item...**|**The scope is set to...**|  
    |**Entity**|All forms and server|  
    |**All Forms**|All forms|  
    |Specific form (**Account** form, for example)|Just that form|  
  
6. **Add conditions.** To add more conditions to your business rule:  
  
    1.  Drag the **Condition** component from the **Components** tab to a plus sign in the designer.  
  
        ![Add a condition in a business rule](media/add-condition-business-rule.png "Add a condition in a business rule")  
  
    2.  To set properties for the condition, click the **Condition** component in the designer window, and then set the properties in the **Properties** tab on the right side of the screen. As you set properties, an expression is created at the bottom of the **Properties** tab.  
  
    3.  To add an additional clause (an AND or OR)  to the  condition, click **New** in the **Properties** tab to create a new rule, and then set the properties for that rule. In the **Rule Logic** field, you can specify whether to add the new rule as an AND or an OR.  
  
        ![Add a new rule to a condition](media/add-new-rule-condition.png "Add a new rule to a condition")  
  
    4.  When you're done setting properties for the condition, click **Apply**.  
  
7. **Add actions.** To add an action:  
  
    1.  Drag one of the action components from the **Components** tab to a plus sign next to **Condition** component. Drag the action to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.  
  
        ![Drag an action to a business rule](media/drag-an-action-business-rule.png "Drag an action to a business rule")  
  
    2.  To set properties for the action, click the **Action** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3.  When you're done setting properties, click **Apply**.  
  
8. **Add a business recommendation.** To add a business recommendation:  
  
    1.  Drag the **Recommendation** component from the **Components** tab to a plus sign next to a **Condition** component. Drag the **Recommendation** component to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.  
  
    2.  To set properties for the recommendation, click the **Recommendation** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3.  To add more actions to the recommendation, drag them from the **Components** tab, and then set properties for each action in the **Properties** tab.  
  
        > [!NOTE]
        >  When you create a recommendation, a single action is added by default. To see all the actions in a recommendation, click **Details** on the **Recommendation** component.  
  
    4.  When you're done setting properties, click **Apply**.  
  
9. To validate the business rule, click **Validate** on the action bar.  
  
10. To save the business rule, click **Save** on the action bar.  
  
11. To activate the business rule, select it in the Solution Explorer window, and then click **Activate**. You can't activate the business rule from the designer window.  
  
> [!TIP]
>  Here are a few tips to keep in mind as you work on business rules in the designer window:  
>   
> - To take a snapshot of everything in the Business Rule window, click **Snapshot** on the action bar. This is useful, for example, if you want to share and get comments on the business rule from a team member.  
> - Use the mini-map to navigate quickly to different parts of the process. This is useful when you have a complicated process that scrolls off the screen.  
> - As you add conditions, Actions, and business recommendations to your business rule, code for the business rule is built and appears at the bottom of the designer window. This code is ready only.  
  
<a name="BKMK_LocalizingErrorMessages"></a>   
## Localize error messages used in business rules  
 If you have more than one language provisioned for your organization, you will want to localize any error messages that you have set. Each time you set a message, a label is generated by the system. If you export the translations in your organization, you can add localized versions of your messages and then import those labels back into the system, so that people using languages other than your base language can view the translated messages.  
  
## Next steps  
 [Create custom business logic through processes](guide-staff-through-common-tasks-processes.md)   
 [Create a business process flow](create-business-process-flow.md)   

