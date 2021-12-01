---
title: "Check your user access and permissions| MicrosoftDocs"
description: How to check user access and security role.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 1/15/2021
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Check your user access to a row


To perform an action on a row, a user needs to have the required privilege assigned through a security role or the user must be a member of a team that has a security role with assigned privileges.

To perform actions on a row, the system checks your privileges and if the privilege check passes, then the system performs an access check. The access check verifies that you have the required rights to perform actions on a row such as read, write, create, delete, append, append to, share, and assign.

You can have access rights to a perform an action on a row through ownership, role access, shared access, or hierarchy access.

|Access type|Description|  
|---------------|-----------------|  
|**Ownership**| User owns the row or belongs to a team that owns the row.|  
|[**Role access**](/power-platform/admin/how-record-access-determined#role-access)|User has access to perform an action on a row because of their security role.|  
|[**Shared access**](/power-platform/admin/how-record-access-determined#shared-access)| The row is shared with a user, team, or organization by a user that has appropriate share rights.|  
|[**Hierarchy access**](/power-platform/admin/how-record-access-determined#hierarchy-access)|Hierarchy access only takes place if hierarchy security management is turned on for the organization and the table. The user also needs to be a manager.

For more information on how privileges and access checks work, go to [How access to a row is determined](/power-platform/admin/how-record-access-determined).


## Check your access to a row


1. Select a row and then select **Edit** on the command bar.

    > [!div class="mx-imgBorder"]
    > ![Select a row to edit it.](media/edit_record.png "Select a row to edit it")
  
2. On the open row, select **Check Access** on the command bar.
3. The **Check Access** dialog box will appear and display your access information.


    > [!div class="mx-imgBorder"]
    > ![Access checker showing your access level.](media/check_access_page.png "Access checker showing your access level")
    
Contact your administrator if you don't have the required access. Only an administrator can edit your security role and privileges. To find your administrator, go to [Find your administrator or support person](./find-admin.md).


## Check another user's access to a row

If you're an administrator, you can check the access another user has to a row.

1. Open a row, select **Check Access** on the command bar.
2. In the **User Lookup** field select or enter a user name to search for the user.

   > [!div class="mx-imgBorder"]
   > ![Access checker showing your access level for an admin.](media/check_access_page_admin-1.png "Access checker showing your access level for an admin")
  
3.   The **Check Access** dialog box will appear and display the user's access information.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
