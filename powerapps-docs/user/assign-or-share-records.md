---
title: "Assign or share records| MicrosoftDocs"
description: How to assign or share records
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 1/20/2020
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
# Assign or share rows

If you would like another person in your organization to handle a customer row, you can assign the row to that person. You can also assign a row to a team, or to yourself.  

Use the **Share** option if you want to keep ownership of the row but let someone else work on it with you. 

1. From the left navigation pane, select a row type. For example, **Contacts**.

2. From the list of rows, select the row that you want to reassign.  
  
3. On the command bar, select **Assign**.

   > [!div class="mx-imgBorder"]
   > ![Reassign a row](media/assign1.png "Reassign a row")

   > [!NOTE]
   > If you want to keep ownership of the row but let someone else work with it, select **Share**. Then use the tooltips to guide you through the **Share** option. 
   
4. In the assign dialog box, in the **Assign to** area, choose **Me** or **User or Team**.

   > [!div class="mx-imgBorder"]
   > ![Reassign a row to me or team](media/assign2.png "Reassign a row me team")
  
   If you select **User or Team**, in the **Look for Rows** box, enter the name of the user or team. If you need to create a new row, select **+ New**.
  
5. When you're done, select **Assign**.

## Use advanced find to reassign rows

Use advanced find to search for rows and then reassign them to someone else. For more information on advanced find, see [Create, edit, or save an Advanced Find search](advanced-find.md).


1. On the command bar, select **Advanced Find**.

   > [!div class="mx-imgBorder"]
   > ![Advanced find](media/assign3.png "advacned find")
   
2. From the list of rows, select the rows that you want to reassign and then select the assign option.

   > [!div class="mx-imgBorder"]
   > ![Reassign a row using advanced find](media/assign4.png "Reassign a row using advacned find")
   
 
 ## Reassign all rows (for admins)
 
 A admin can reassign all row for a user from the admin Setting area.
 
 1. Go to **Settings** > **Security**.
 2. Select **Users** and select a user name to open the user's profile.
 3. On the command bar, select **REASSIGN RECORDS**.
 
   > [!div class="mx-imgBorder"]
   > ![Reassign all rows](media/assign5.png "Reassign all rows")
   
 4. On the **Reassign Rows** dialog box choose how to want to reassign all the rows and then select **OK**.
 
  > [!NOTE]
   > - The **Reassign Rows** option will reassign all rows regardless of their status. Inactive and active rows will be reassigned to the other user or team. This will also deactivate all activated processes including business rules and workflows when the row is reassigned to another user or team. The new owner must activate the processes that was deactivated when the row is reassigned.  
   > - When there is a large amount rows to reassign, the system may take a while to process. 
   > - If there is an issue during the reassignment process such as the user that the rows are being reassigned to doesn't have the required privileges then the **Reassign Rows** process will stop. The rows that are processed before the issue will be updated and saved. For the rows that were not saved, you will need reassign the rows again using the **Reassign Rows** option.
   
 
   > [!div class="mx-imgBorder"]
   > ![Reassign all rows to user or team](media/assign6.png "Reassign all rows to user or team")
 

