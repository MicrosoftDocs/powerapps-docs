---
title: "Privileges required for customizing apps build on Dataverse | MicrosoftDocs"
description: Understand the privileges required to apps built on Dataverse
ms.custom: ""
ms.date: 06/18/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 43cf7f3a-7e26-4990-8b5a-c817ac6d51bb
caps.latest.revision: 13
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Privileges required for Dataverse customization

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

App users can personalize the system and even share some of their customizations with others, but only users with the correct privileges can apply changes for everyone.  
  
> [!NOTE]
>  This section assumes you know how to work with security roles. For more information about working with security roles, see [Create users and assign security roles](/dynamics365/customer-engagement/admin/create-users-assign-online-security-roles).  
  
<a name="BKMK_SysAdminAndSysCustomizer"></a>   
## System Administrator and System Customizer security roles  
 Anyone who customizes will have the System Administrator or System Customizer security role associated with their account. These security roles give you the permissions you need to customize in Microsoft Dataverse.  
  
|System Administrator|System Customizer|  
|--------------------------|-----------------------|  
|Has full permission to customize the system|Has full permission to customize the system|  
|Can view all data in the system|Can only view rows for system tables that they create|  
  
 The difference between the System Administrator and System Customizer security roles is that a system administrator has read privileges on most rows in the system and can see everything. Assign the System Customizer role to someone who needs to perform customization tasks but shouldn’t see any data in the system tables. However, testing is an important part of customizing the system. If system customizers can’t see any data, they will need to create rows to test their customizations. By default, system customizers have full access to custom tables. If you want to have the same limitations that exist for system tables, you’ll need to adjust the system customizer security role so that the access level is **User** rather than **Organization** for custom tables.  
  
<a name="BKMK_DelegatingCustomizationTasks"></a>   
## Delegate customization tasks  
 You might want to delegate some tasks to trusted people so that they can apply changes they need. Keep in mind that anyone can have multiple security roles associated with their user account and that privileges and access rights granted by security roles is based on the *least restrictive* level of permissions.  
  
 This means that you can give the System Customizer security role to someone who already has another security role, perhaps a sales manager. This lets them customize the system in addition to other privileges they already have. You don’t need to edit the security role they already have, and you can remove the System Customizer security role from the person’s user account when you want.  
  
<a name="BKMK_UsingTwoUserAccounts"></a>   
## Test customizations without customization privileges  
 You should always test any customizations you make with a user account that doesn’t have customization privileges. This way you can make sure that people without the System Administrator or System Customizer security roles will be able to use your customizations. To do this effectively, you need access to two user accounts: One account with the System Administrator security role and another that has the security roles that represent the people who will be using the customizations.  
  
> [!IMPORTANT]
>  Don’t attempt to remove your System Administrator security role if you have only one user account. The system will warn you if you try, but if you proceed you could find that you won’t be able to get it back. Most security roles don’t allow editing of a user’s security roles.  
  
## Next steps  
[Understand model-driven app components](model-driven-app-components.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]