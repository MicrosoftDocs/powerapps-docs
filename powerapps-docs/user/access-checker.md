---
title: "Check your user access and permissions| MicrosoftDocs"
description: How to check user accesss and security role
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/21/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Check your user access and permissions

Common Data Service uses a role-based security model to help secure access to the database. When you're on a record select **Check Access** to check your security role and privileges.


1. To check your access, select a record and then select **Edit** on the command bar.

    > [!div class="mx-imgBorder"]
    > ![Select a record to edit it](media/edit_record.png "Select a record to edit it")
  
2. On the open record, select **Check Access** on the command bar.
    
### Record-level privileges  
Power Apps use eight different record-level privileges that determine the level of access a user has to a specific record or record type. 

Only your administrator can edit your security role and privileges. To find your administrator, see [Find your administrator or support person](https://docs.microsoft.com/powerapps/user/find-admin).
  
|Privilege|Description|  
|---------------|-----------------|  
|**Create**|Required to make a new record. Which records can be created depends on the access level of the permission defined in your security role.|  
|**Read**|Required to open a record to view the contents. Which records can be read depends on the access level of the permission defined in your security role.|  
|**Write**|Required to make changes to a record. Which records can be changed depends on the access level of the permission defined in your security role.|  
|**Delete**|Required to permanently remove a record. Which records can be deleted depends on the access level of the permission defined in your security role.|  
|**Append**|Required to associate the current record with another record. For example, a note can be attached to an opportunity if the user has Append rights on the note. The records that can be appended depend on the access level of the permission defined in your security role.<br /> In case of many-to-many relationships, you must have Append privilege for both entities being associated or disassociated.|  
|**Append To**|Required to associate a record with the current record. For example, if a user has Append To rights on an opportunity, the user can add a note to the opportunity. The records that can be appended to depend on the access level of the permission defined in your security role.|  
|**Assign**|Required to give ownership of a record to another user. Which records can be assigned depends on the access level of the permission defined in your security role.|  
|**Share**|Required to give access to a record to another user while keeping your own access. Which records can be shared depends on the access level of the permission defined in your security role.| 
    
 
For information on security roles, see [Security roles and privileges](https://docs.microsoft.com/power-platform/admin/security-roles-privileges). 

For information on how to configure security roles, see [Configure user security to resources in an environment](https://docs.microsoft.com/power-platform/admin/database-security).



    
  
  
