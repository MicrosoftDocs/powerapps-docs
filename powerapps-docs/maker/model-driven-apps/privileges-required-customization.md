---
title: "Privileges required for customizing apps build on Dataverse | MicrosoftDocs"
description: Understand the privileges required to apps built on Dataverse
ms.custom: ""
ms.date: 08/19/2025
ms.reviewer: "matp"
ms.topic: article
ms.subservice: mda-maker
ms.author: "matp"
author: "Mattp123"
search.audienceType: 
  - maker
---
# Privileges required for Dataverse customization

App users can personalize the system and even share some of their customizations with others, but only users with the correct privileges can apply changes for everyone.  
  
> [!NOTE]
>
> - This section assumes you know how to work with security roles. For more information about working with security roles, see [Security roles and privileges](/power-platform/admin/security-roles-privileges).  
> - For some feature and data access, a system customizer security role might be required. More information: [A copied system customizer security role might not provide the same access](/power-platform/admin/copy-security-role#a-copied-system-customizer-security-role-might-not-provide-the-same-access).

## System administrator and system customizer security roles

Anyone who customizes have at least the system customizer security role associated with their account. This security role gives you the permission you need to customize in Microsoft Dataverse.  
  
|System administrator|System customizer|  
|--------------------------|-----------------------|  
|Has full permission to customize the system and manage the environment. |Has permission to customize the system.|  
|Can view all data in the system. |Can view all custom tables in the system but only view rows (records) in the account, contact, and activity tables that they create. |  
  
The difference between the system administrator and system customizer security roles is that a system administrator has read privileges on most records in the system and can see everything. Assign the system customizer role to someone who needs to perform customization tasks and has access to all the custom tables but only has access to the account, contact, and activity rows (records) they create. However, testing is an important part of customizing the system. If system customizers can’t see any data, they need to create rows (records) to test their customizations. By default, system customizers have full access to custom tables. If you want to have the same limitations that exist for system tables, you need to adjust the system customizer security role so that the access level is **User** rather than **Organization** for custom tables. 

### Add a security role to a user

For information about how a Power Platform admin can add a security role to a user, go to [Add users to a security role](/power-platform/admin/security-roles-privileges?tabs=new#add-users-to-a-security-role)
  
## Delegate customization tasks  

You might want to delegate some tasks to trusted people so that they can apply changes they need. Keep in mind that anyone can have multiple security roles associated with their user account and that privileges and access rights granted by security roles is based on the *least restrictive* level of permissions.  
  
 This means that you can give the system customizer security role to someone who already has another security role, perhaps a sales manager. This access lets them customize the system in addition to other privileges they already have. You don’t need to edit the security role they already have, and you can remove the system customizer security role from the person’s user account when you want.  
  
## Test customizations without customization privileges

You should always test any customizations you make with a user account that doesn’t have customization privileges. This way you can make sure that people without the system administrator or system customizer security roles are able to use your customizations. To do this effectively, you need access to two user accounts: One account with the system administrator security role and another that has the security roles that represent the people who will be using the customizations.  
  
> [!IMPORTANT]
> Don’t attempt to remove your system administrator security role if you have only one user account. The system warns you if you try, but if you proceed you could find that you aren’t be able to get it back. Most security roles don’t allow editing of a user’s security roles.  
  
## Next steps

[Understand model-driven app components](model-driven-app-components.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
