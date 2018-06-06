---
title: "Create or edit a business unit to control access to records for Dynamics 365 Customer Engagement | MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: dea61b2c-a489-4d9a-9535-2e8eb6fe8943
caps.latest.revision: 38
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Create or edit a business unit to control access to records

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

A business unit is a logical grouping of related business activities. Use business units together with security roles to control data access so people see just the information they need to do their jobs.  
  
 Keep the following in mind when creating business units:  
  
-   The organization (also known as the root business unit) is the top level of a [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] business unit hierarchy. [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] automatically creates the organization when you install or provision [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)]. You can’t change or delete the organization name.  
  
-   Each business unit can have just one parent business unit.  
  
-   Each business unit can have multiple child business units.  
  
-   You must assign every user to one (and only one) business unit.  
  
-   You can assign a team to just one business unit, but a team can consist of users from one or many business units. Consider using a team if you have a situation where users from different business units need to work together on a shared set of records.  
  
<a name="bkmk1"></a>   
## Create a new business unit  
  
1.  Make sure you have the System Administrator or System Customizer role.  
  
    Check your security role  
  
    1. [!INCLUDE[proc_follow_steps_in_link](../../includes/proc-follow-steps-in-link.md)]  
  
    2. [!INCLUDE[proc_dont_have_correct_permissions](../../includes/proc-dont-have-correct-permissions.md)]  
  
2. [!INCLUDE[proc_settings_security](../../includes/proc-settings-security.md)]  
  
3.  Choose **Business Units**.  
  
4.  On the Actions bar, choose **New**.  
  
5.  In the **Business Unit** dialog box, type a name for the new business unit. [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] automatically fills in the **Parent Business** field with the name of the root business unit.  
  
 ![Business Unit dialog box in Dynamics 365](../media/business-unit-dialog-box.png "Business Unit dialog box in Dynamics 365")  
  
6.  If you want to change the parent business unit, choose the **Lookup** button ![Lookup button](../media/lookup-button-4.gif "Lookup button"), choose **Look Up More Records**, and then do one of the following:  
  
    -   Select an existing business unit from the list, and then choose **Add**.  
  
    -   To create a new parent business unit:  
  
        1.  Choose **New**, and then add the information for the new parent business unit in the **Business Unit** dialog box.  
  
        2.  When you’re done adding information, choose **Save and Close** in the **Business Unit** dialog box.  
  
        3.  In the **Look Up Record** dialog box, choose **Add**.  
  
7.  In the **Business Unit** dialog box, fill in any of the other optional fields, such as the division, contact information, website, bill to address, or ship to address.  
  
8.  Choose **Save** or **Save and Close**.  
  
<a name="bkmk2"></a>   
## Change the settings for a business unit  
  
1.  Make sure you have the System Administrator or System Customizer role.  
  
    Check your security role  
  
    1. [!INCLUDE[proc_follow_steps_in_link](../../includes/proc-follow-steps-in-link.md)]  
  
    2. [!INCLUDE[proc_dont_have_correct_permissions](../../includes/proc-dont-have-correct-permissions.md)]  
  
2. [!INCLUDE[proc_settings_security](../../includes/proc-settings-security.md)]  
  
3.  Choose **Business Units**.  
  
4.  Choose a business unit name to open the **Business Unit** dialog box.  
  
5.  In the **Business Unit** dialog box, do one or more of the following:  
  
    -   Modify the data in one or more fields.  
  
        > [!NOTE]
        >  You can’t change the name of a business unit or delete a business unit after it has been created. You can disable a business unit or change the parent, however. When you disable a business unit, all users and teams associated with the business unit are also disabled.  
  
    -   Choose **Actions** on the Actions bar, and then select a command. For example, to change the parent business unit, choose **Actions**, and then choose **Change Parent Business**.  
  
        > [!NOTE]
        >  When you change the parent business unit, [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] removes security roles for users and teams associated with the business unit. You must reassign them.  
  
    -   Under **Organization**, choose a record type to see a list of related records. For example, choose **Users** to view a list of users in the selected business unit or to add users to the business unit.  
  
6.  When you’re done making changes, choose **Save** or **Save and Close**.  
  
### See also  
 [Security concepts in Microsoft Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/admin/security-concepts)   
 [Manage users](https://docs.microsoft.com/dynamics365/customer-engagement/admin/create-users-assign-online-security-roles)   
 [Manage teams](manage-teams.md)   
 [Enable or disable security for a field](https://docs.microsoft.com/dynamics365/customer-engagement/admin/enable-disable-security-field)   
 [Print leads, quotes, and other records](https://docs.microsoft.com/dynamics365/customer-engagement/admin/create-edit-business-unit-control-access-records)
