---
title: "Set up security permissions for a field for Dynamics 365 Customer Engagement | MicrosoftDocs"
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
ms.assetid: 578abf62-e903-452e-90e0-7fb43343fcaf
caps.latest.revision: 26
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Set up security permissions for a field 

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

You can restrict access to a field by creating a field security profile. After you create the profile, you assign users and or teams to that profile, and set up specific read, create, or write permissions for the field.  
  
 [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Security concepts for Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/admin/security-concepts)  
  
1. [!INCLUDE[proc_permissions_system_admin](../includes/proc-permissions-system-admin.md)]  
  
    Check your security role  
  
    - [!INCLUDE[proc_follow_steps_in_link](../includes/proc-follow-steps-in-link.md)]  
  
    - [!INCLUDE[proc_dont_have_correct_permissions](../includes/proc-dont-have-correct-permissions.md)]  
  
2. [!INCLUDE[proc_settings_security](../includes/proc-settings-security.md)]  
  
3.  Click **Field Security Profiles**, and then on the command bar, click **New**.  
  
4.  Enter a name and a description (optional) and click **Save**.  
  
5.  Under **Common**, click **Field permissions**.  
  
6.  Select a field, and then click **Edit**.  
  
7.  Select the permissions that you want to assign to users or teams, and then click **OK**.  
  
8.  To add users or teams:  
  
    1.  Under **Members**, click **Teams** or **Users**.  
  
    2.  On the command bar, click **Add**.  
  
    3.  In the **Look Up Records** dialog box, select a team or user from the list (or search for a team or user), and then click **Select**.  
  
    4.  Repeat the preceding steps to add multiple teams or users, and then click **Add**.  
  
### See also  
 [Enable or disable security for a field](https://docs.microsoft.com/dynamics365/customer-engagement/admin/enable-disable-security-field)
