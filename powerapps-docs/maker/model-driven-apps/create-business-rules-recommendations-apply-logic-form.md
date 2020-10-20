---
title: "Create model-driven app business rules and recommendations | MicrosoftDocs"
description: Learn how to create a business rule for a specific form in Power Apps
ms.custom: ""
ms.date: 03/30/2020
ms.reviewer: ""
ms.service: powerapps
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
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create business rules and recommendations to apply logic in a model-driven app form

This topic shows you how to create business rules and recommendations to apply form logic in a model-driven app without writing JavaScript code or creating plug-ins. Business rules provide a simple interface to implement and maintain fast-changing and commonly used rules. They can be applied to Main and Quick Create forms, and they work in model-driven apps, legacy web apps, Dynamics 365 for tablets, and Dynamics 365 for Outlook (online or offline mode).
 
 By combining conditions and actions, you can do any of the following with business rules:  
  
-   Set field values  
  
-   Clear field values  
  
-   Set field requirement levels  
  
-   Show or hide fields  
  
-   Enable or disable fields  
  
-   Validate data and show error messages  
  
-   Create business recommendations based on business intelligence.  

> [!NOTE]
> To define a business rule for an entity so that it applies to all forms, see [Create a business rule for an entity](/powerapps/maker/common-data-service/data-platform-create-business-rule).
>
> Business rules don’t work with multi-select option sets.
  
## Create a business rule or business recommendation

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Entities**, select the entity you want, and then select the **Business rules** tab.

3.  On the command bar, select **Add business rule**.

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
  
    2.  To set properties for the condition, select the **Condition** component in the designer window, and then set the properties in the **Properties** tab on the right side of the screen. As you set properties, an expression is created at the bottom of the **Properties** tab.  
  
    3.  To add an additional clause (an AND or OR)  to the  condition, select **New** in the **Properties** tab to create a new rule, and then set the properties for that rule. In the **Rule Logic** field, you can specify whether to add the new rule as an AND or an OR.  
  
        ![Add a new rule to a condition](media/add-new-rule-condition.png "Add a new rule to a condition")  
  
    4.  When you're done setting properties for the condition, select **Apply**.  
  
7. **Add actions.** To add an action:  
  
    1.  Drag one of the action components from the **Components** tab to a plus sign next to **Condition** component. Drag the action to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.  
  
        ![Drag an action to a business rule](media/drag-an-action-business-rule.png "Drag an action to a business rule")  
  
    2.  To set properties for the action, select the **Action** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3.  When you're done setting properties, select **Apply**.  
  
8. **Add a business recommendation.** To add a business recommendation:  
  
    1.  Drag the **Recommendation** component from the **Components** tab to a plus sign next to a **Condition** component. Drag the **Recommendation** component to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.  
  
    2.  To set properties for the recommendation, select the **Recommendation** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3.  To add more actions to the recommendation, drag them from the **Components** tab, and then set properties for each action in the **Properties** tab.  
  
        > [!NOTE]
        >  When you create a recommendation, a single action is added by default. To see all the actions in a recommendation, select **Details** on the **Recommendation** component.  
  
    4.  When you're done setting properties, select **Apply**.  
  
9. To validate the business rule, select **Validate** on the action bar.  
  
10. To save the business rule, select **Save** on the action bar.  
  
11. To activate the business rule, select it in the Solution Explorer window, and then select **Activate**. You can't activate the business rule from the designer window.  
  
> [!TIP]
>  Here are a few tips to keep in mind as you work on business rules in the designer window:  
>   
> - To take a snapshot of everything in the Business Rule window, select **Snapshot** on the action bar. This is useful, for example, if you want to share and get comments on the business rule from a team member.  
> - Use the mini-map to navigate quickly to different parts of the process. This is useful when you have a complicated process that scrolls off the screen.  
> - As you add conditions, Actions, and business recommendations to your business rule, code for the business rule is built and appears at the bottom of the designer window. This code is read-only.  
  
<a name="BKMK_LocalizingErrorMessages"></a>   
## Localize error messages used in business rules  
 If you have more than one language provisioned for your organization, you will want to localize any error messages that you have set. Each time you set a message, a label is generated by the system. If you export the translations in your organization, you can add localized versions of your messages and then import those labels back into the system, so that people using languages other than your base language can view the translated messages.  

## Common issues
This section describes common issues that may occur when you use business rules. 

### Full Name field and Address field not supported with Unified Interface apps
Actions or conditions that use a composite field like the **Full Name** (fullname) field or an **Address** field aren't supported in apps based on the Unified Interface.  Alternatively, you can use actions or conditions with the constituent fields. For example, for the **Full Name** field, you can use actions or conditions on the  **First Name** (firstname) and **Last Name** (lastname) fields. 

### Business rules don't fire on editable grid on a dashboard
Entity scoped business rules will not fire on an editable grid when the editable grid is configured on a dashboard page.

### Is your business rule not firing for a form?
A business rule may not execute because the field referenced in the business rule isn't included with the form. 
1.    Open solution explorer. Expand the entity that you want and then select **Forms**. 
2.    Open the form that you want and then on the form designer ribbon select **Business Rules**. 
3.    In the form designer, open the business rule. 
4.    In the business rule designer select each condition and action to verify all the fields referenced in each condition and action. 

        > [!div class="mx-imgBorder"] 
        > ![Field referenced in business rule exists in entity](media/business-rule-field.png "Field referenced in business rule exists in entity")

 5.    Verify that each field referenced in the business rule is also included on the form. If not, add the missing field to the form.

        > [!div class="mx-imgBorder"] 
        > ![Account name field on form](media/account-name-on-form.png "Account name field on form")

A business rule may also not execute because a field referenced in the business rule is a composite field. You can use the constituent fields of the composite field instead.
## Frequently asked questions (FAQ)
*Can business rules unlock fields on a read-only form?*
- Yes, a business rule can unlock fields and edit actions on a read-only form.

*How do I troubleshoot a business rule that isn't working?* 
- See [Is your business rule not firing for a form?](#is-your-business-rule-not-firing-for-a-form) in this topic.

## See also  
 [Create custom business logic through processes](guide-staff-through-common-tasks-processes.md)   
 [Create a business process flow](/flow/create-business-process-flow)   

