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

To perform an action on a record, a user needs to have the required privilege assigned through a security role or the user is a member of a team that has a security role with assigned privileges.

To perform actions on a record the systerm checks your privileges and if the privilege check passes then the system preforms an access check. The access check verifies that you have the required rights to perform actions on a record such as, read, write, create, delete, append, append to, share, and assign.
 

You can have access rights to a perform an action on a record through ownership, role access, shared access, or hierarchy access.

|Access type|Description|  
|---------------|-----------------|  
|**Ownership**| User owns the record or belongs to a team that owns the record.|  
|**Role access**|User has access to perform an action on a record because of their security role.|  
|**Shared access**| The record is shared with a user, team, or organization by a user that has appropriate share rights.|  
|**Hierarchy access**|Hierarchy access only takes place if hierarchy security management is turned on for the organization and the entity. The user also needs to be a manager.

## Check your access for a record


1. Select a record and then select **Edit** on the command bar.

    > [!div class="mx-imgBorder"]
    > ![Select a record to edit it](media/edit_record.png "Select a record to edit it")
  
2. On the open record, select **Check Access** on the command bar.
3. The **Check Access** dialog box will appear and display acccess information.


    > [!div class="mx-imgBorder"]
    > ![Acess checker showing your accesss leve](media/check_access_page.png "Acess checker showing your accesss level")
    
Contact your administrator if you don't have the reqired access. Only an administrator can edit your security role and privileges. To find your administrator, see [Find your administrator or support person](https://docs.microsoft.com/powerapps/user/find-admin).




    
  
  
