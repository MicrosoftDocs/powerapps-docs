---
title: "Security roles and privileges for Dynamics 365 Customer Engagement | MicrosoftDocs"
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
ms.assetid: 460766f2-4b19-4406-8fd0-fff46d4cbb5e
caps.latest.revision: 21
author: "Mattp123"
ms.author: "matp"
manager: "brycho"
---
# Security roles and privileges

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

To control data access, you must set up an organizational structure that both protects sensitive data and enables collaboration. You do this by setting up business units, security roles, and field security profiles.  
  
## Security roles  
 A security role defines how different users, such as salespeople, access different types of records. To control access to data, you can modify existing security roles, create new security roles, or change which security roles are assigned to each user. Each user can have multiple security roles.  
  
 Security role privileges are cumulative: having more than one security role gives a user every privilege available in every role.  
  
 Each security role consists of record-level privileges and task-based privileges.  
  
 *Record-level privileges* define which tasks a user with access to the record can do, such as Read, Create, Delete, Write, Assign, Share, Append, and Append To. *Append* means to attach another record, such as an activity or note, to a record. *Append to* means to be attached to a record. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Record-level privileges](security-roles-privileges.md#BKMK_privileges)  
  
 *Task-based privileges*, at the bottom of the form, give a user privileges to perform specific tasks, such as publish articles.  
  
 The colored circles on the security role settings page define the access level for that privilege. Access levels determine how deep or high in the organizational business unit hierarchy the user can perform the specified privilege. The following table lists the levels of access in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)], starting with the level that gives users the most access.  
  
|||  
|-|-|  
|![Access level global](../media/access-level-global.gif "Access level global")|**Global**. This access level gives a user access to all records in the organization, regardless of the business unit hierarchical level that the instance or the user belongs to. Users who have Global access automatically have Deep, Local, and Basic access, also.<br /><br /> Because this access level gives access to information throughout the organization, it should be restricted to match the organization's data security plan. This level of access is usually reserved for managers with authority over the organization.<br /><br /> The application refers to this access level as **Organization**.|  
|![Access level deep](../media/access-deep.gif "Access level deep")|**Deep**. This access level gives a user access to records in the user's business unit and all business units subordinate to the user's business unit.<br /><br /> Users who have Deep access automatically have Local and Basic access, also.<br /><br /> Because this access level gives access to information throughout the business unit and subordinate business units, it should be restricted to match the organization's data security plan. This level of access is usually reserved for managers with authority over the business units.<br /><br /> The application refers to this access level as **Parent: Child Business Units**.|  
|![Access level local](../media/access-local.gif "Access level local")|**Local**. This access level gives a user access to records in the user's business unit.<br /><br /> Users who have Local access automatically have Basic access, also.<br /><br /> Because this access level gives access to information throughout the business unit, it should be restricted to match the organization's data security plan. This level of access is usually reserved for managers with authority over the business unit.<br /><br /> The application refers to this access level as **Business Unit**.|  
|![Access level basic](../media/access-level-basic.gif "Access level basic")|**Basic**.<br /><br /> This access level gives a user access to records that the user owns, objects that are shared with the user, and objects that are shared with a team that the user is a member of.<br /><br /> This is the typical level of access for sales and service representatives.<br /><br /> The application refers to this access level as **User**.|  
|![Access level none](../media/access-level-none.gif "Access level none")|**None**. No access is allowed.|  
  
> [!IMPORTANT]
>  To ensure that users can view and access all areas of the web application, such as entity forms, the nav bar, or the command bar, all security roles in the organization must include the Read privilege on the `Web Resource` entity. For example, without read permissions, a user won’t be able to open a form that contains a web resource and will see an error message similar to this: “Missing `prvReadWebResource` privilege.” [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Create or edit a security role](https://docs.microsoft.com/dynamics365/customer-engagement/admin/create-edit-security-role)  
  
<a name="BKMK_privileges"></a>   
### Record-level privileges  
 [!INCLUDE[pn_dynamics_crm](../../includes/pn-dynamics-crm.md)] has eight different record-level privileges that determine the level of access a user has to a specific record or record type.  
  
|Privilege|Description|  
|---------------|-----------------|  
|**Create**|Required to make a new record. The records that can be created depends on the access level of the permission defined in your security role.|  
|**Read**|Required to open a record to view the contents. The records that can be read depends on the access level of the permission defined in your security role.|  
|**Write**|Required to make changes to a record. The records that can be changed depends on the access level of the permission defined in your security role.|  
|**Delete**|Required to permanently remove a record. The records that can be deleted depends on the access level of the permission defined in your security role.|  
|**Append**|Required to associate a record with the current record. For example, if a user has Append rights on an opportunity, the user can add a note to an opportunity. The records that can be appended depends on the access level of the permission defined in your security role.|  
|**Append To**|Required to associate the current record with another record. For example, a note can be attached to an opportunity if the user has Append To rights on the note. The records that can be appended to depends on the access level of the permission defined in your security role.|  
|**Assign**|Required to give ownership of a record to another user. The records that can be assigned depends on the access level of the permission defined in your security role.|  
|**Share**|Required to give access to a record to another user while keeping your own access. The records that can be shared depends on the access level of the permission defined in your security role.|  
  
## Overriding security roles  
 The owner of a record or a person who has the Share privilege on a record can share a record with other users or teams. Sharing can add Read, Write, Delete, Append, Assign, and Share privileges for specific records.  
  
 Teams are used primarily for sharing records that team members ordinarily couldn't access. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Manage security, users and teams](manage-teams.md)  
  
 It’s not possible to remove access for a particular record. Any change to a security role privilege applies to all records of that record type.  
  
### See also  
 [Security concepts for Microsoft Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/admin/security-concepts)   
 [Manage security, users and teams](https://docs.microsoft.com/dynamics365/customer-engagement/admin/manage-security-users-and-teams)   
 [Create or edit a security role](https://docs.microsoft.com/dynamics365/customer-engagement/admin/create-edit-security-role)
