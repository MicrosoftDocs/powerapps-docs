---
title: "Global and Service administrators can administer Dynamics 365 (Online) without a license | MicrosoftDocs"
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
ms.assetid: 9707d6fd-f289-4e46-895e-6b871ca3a9ea
caps.latest.revision: 4
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# Global and Service administrators can administer without a license 

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

By default, all [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Global administrators and [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Service administrators who do not have a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] license are granted the following two levels of permission in [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)].  
  
-   System administrator security role  
  
-   Administrative access mode  
  
The system administrator security role is typically granted to [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] administrators giving them unrestricted access to the administrative (Settings) areas, which are used for managing and configuring features of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)].  
  
Administrative access mode limits access to those areas of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] used to configure or customize the system.  
  
To give these administrators access to additional areas, such as the Sales, Marketing, and Service areas, a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] license must be added to the [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Global administrator or [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Service administrator user account, by using the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)]. Note that Administrative access mode cannot be changed on the user form in the [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] application.  
  
## Create a Dynamics 365 administrator account  
  
1.  Sign in to the [Office 365 admin center](https://portal.office.com), and then choose **Users** > **Active Users**.  
  
2.  Select an existing user in the list. If you want to create a new administrative user, see [Create or edit users](https://support.office.com/article/Create-or-edit-users-435ccec3-09dd-4587-9ebd-2f3cad6bc2bc) and [Assigning admin roles](https://support.office.com/article/Assign-admin-roles-in-Office-365-eac4d046-1afd-4f1a-85fc-8219c79e1504).  
  
3.  Next to **Product licenses**, click **Edit**.  
  
4.  Make sure a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] license is **not** assigned to this user, and then click **Save**.  
  
    > [!IMPORTANT]
    > Unlicensed [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Global and Service administrators have access to the *administrative* areas of [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. However, if the administrator also needs access to additional areas of [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] you must select a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] license for the user.  
  
5.  Next to **Roles**, click **Edit** and then click either **Global administrator** or **Customized administrator** > **Service administrator**. For more information about these roles, see [Assigning admin roles](https://support.office.com/article/Assign-admin-roles-in-Office-365-eac4d046-1afd-4f1a-85fc-8219c79e1504).  
  
6.  Enter an alternate email address, and then click **Save**.  
  
### See also  
 [Manage subscriptions, licenses, and user accounts](manage-subscriptions-licenses-user-accounts.md)
