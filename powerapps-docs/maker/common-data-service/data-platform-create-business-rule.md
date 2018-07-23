---
title: Create a business rule in Common Data Service for Apps | Microsoft Docs
description: Step-by-step instructions for how to create a business rule in Common Data Service (CDS) for Apps.
author: clwesene
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 03/21/2018
ms.author: clwesene
---

# Create a business rule

You can create business rules and recommendations to apply logic and validations without writing code or creating plug-ins.  Business rules provide a simple interface to implement and maintain fast-changing and commonly used rules. 
  
By combining conditions and actions, you can do any of the following with business rules:  
  
* Set field values  
* Clear field values  
* Set field requirement levels  
* Show or hide fields  
* Enable or disable fields  
* Validate data and show error messages  
* Create business recommendations based on business intelligence.  
  
## Differences between Canvas and Model driven apps

Model driven apps can use all actions available on business rules, however not all business rule actions are available on Canvas apps at this time. The following actions are **not** available on Canvas apps :

* Show or hide fields  
* Enable or disable fields  
* Create business recommendations based on business intelligence.  

## Prerequisites
To follow this topic, you must switch to an [environment](../canvas-apps/working-with-environments.md) in which you can create and edit entities.

## Create a business rule
  
1. Sign in to [PowerApps](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then click or tap the down arrow for **Data** near the left edge.

2. In the list that appears, click or tap **Entities**.
  
3. Open the entity you want to create the business rule for (for example, open the **Account** entity), and then click the **Business Rules** tab.  

4. Click **New**.  
  
    The Business Rule designer window opens with a single condition already created for you. Every rule starts with a condition. The business rule takes one or more actions based on that condition.  

    > [!TIP]
    > If you want to modify an existing business rule, you must deactivate it before you can modify it.  
  
5. Add a description, if you want, in the description box in the upper-left corner of the window.
  
6. Set the scope, according to the following:  
  
    |||  
    |-|-|  
    |**If you select this item...**|**The scope is set to...**|  
    |**Entity**|Model Driven forms and server|  
    |**All Forms**|Model Driven forms|  
    |Specific form (**Account** form, for example)|Just that Model Driven form|  

    > [!TIP]
    > If you're building a Canvas app, you must use Entity as the scope.
  
7. **Add conditions.** To add more conditions to your business rule:  
  
    1. Drag the **Condition** component from the **Components** tab to a plus sign in the designer.  
  
        ![Add a condition in a business rule](./media/data-platform-cds-create-business-rule/add-condition-business-rule.png "Add a condition in a business rule")  
  
    2. To set properties for the condition, click the **Condition** component in the designer window, and then set the properties in the **Properties** tab on the right side of the screen. As you set properties, the Common Data Service creates an expression at the bottom of the **Properties** tab.  
  
    3. To add an additional clause (an AND or OR)  to the  condition, click **New** in the **Properties** tab to create a new rule, and then set the properties for that rule. In the **Rule Logic** field, you can specify whether to add the new rule as an AND or an OR.  
  
        ![Add a new rule to a condition](./media/data-platform-cds-create-business-rule/add-new-rule-condition.png "Add a new rule to a condition")  
  
    4. When you're done setting properties for the condition, click **Apply**.  
  
8. **Add actions.** To add an action:  
  
    1. Drag one of the action components from the **Components** tab to a plus sign next to **Condition** component. Drag the action to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.
  
        ![Drag an action to a business rule](./media/data-platform-cds-create-business-rule/drag-an-action-business-rule.png "Drag an action to a business rule")  
  
    2. To set properties for the action, click the **Action** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3. When you're done setting properties, click **Apply**.  
  
9. **Add a business recommendation. (Model Driven only)** To add a business recommendation:  
  
    1. Drag the **Recommendation** component from the **Components** tab to a plus sign next to a **Condition** component. Drag the **Recommendation** component to a plus sign next to a check mark if you want the business rule to take that action when the condition is met, or to a plus sign next to an  x if you want the business rule to take that action if the condition is not met.  
  
    2. To set properties for the recommendation, click the **Recommendation** component in the designer window, and then set the properties in the **Properties** tab.  
  
    3. To add more actions to the recommendation, drag them from the **Components** tab, and then set properties for each action in the **Properties** tab.  
  
        > [!NOTE]
        >  When you create a recommendation, the Common Data Service adds a single action by default. To see all the actions in a recommendation, click **Details** on the **Recommendation** component.  
  
    4. When you're done setting properties, click **Apply**.  
  
10. To validate the business rule, click **Validate** on the action bar.  
  
11. To save the business rule, click **Save** on the action bar.  
12. To activate the business rule, select it in the Solution Explorer window, and then click **Activate**. You can't activate the business rule from the designer window.  
  
    > [!TIP]
    >  Here are a few tips to keep in mind as you work on business rules in the designer window:  
    >   
    > - To take a snapshot of everything in the Business Rule window, click **Snapshot** on the action bar. This is useful, for example, if you want to share and get comments on the business rule from a team member.  
    > - Use the mini-map to navigate quickly to different parts of the process. This is useful when you have a complicated process that scrolls off the screen.  
    > - As you add conditions, Actions, and business recommendations to your business rule, Common Data Service builds the code for the business rule at the bottom of the designer window. This code is read only.  
  
## Localize error messages used in business rules  
 If you have more than one language provisioned for your organization, you will want to localize any error messages that you have set. Each time you set a message, a label is generated by the system. If you export the translations in your organization, you can add localized versions of your messages and then import those labels back into the Common Data Service, so that people using languages other than your base language can view the translated messages.  
  