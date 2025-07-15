---
title: "Merge duplicate records| MicrosoftDocs"
description: How to merge duplicate records
author: smurkute

ms.component: pa-user
ms.topic: how-to
ms.date: 07/15/2025
ms.subservice: end-user
ms.author: smurkute
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
- fafuxa-ms
---
# Merge duplicate rows 

Duplicate rows can creep into your data when you or others enter data manually or import data in bulk. Microsoft Dataverse helps you address potential duplicates by providing duplicate detection for active rows such as accounts and contacts. When you merge a row any related or child rows will also be merged. Your administrator can also set up duplicate detection rules for other situations.  

There are a few situations when duplicates might be found:  

- When a row is created or updated.  
- When  you're using Dynamics 365 for Outlook and you go from offline to online.  
- When you import data using the Import Data wizard.  
- Duplicates aren't detected when you merge rows, save an activity as completed, or change the status of a row, such as activating or reactivating a row.
  
For example, let's say you enter a contact row, Jim Glynn,  along with a mobile phone number.  The duplicate detection rule discovers that you already have a similar row, and displays this dialog box.  
  
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact row detected.](media/duplicates-detected.png "Duplicate contact row detected")  
  
 You're not sure if this is a new row (one that happens to have the  same name as an existing contact) or a duplicate, so you select **Ignore And Save**.  
  
 Next, you go to the **My Active Contacts** list and see that now you have two rows with the same name. After reviewing the rows,  you  determine that they're duplicates that need to be merged.  
 
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact row is detected.](media/duplicates-detected-1.png "Duplicate contact row is detected")  
 
Dataverse includes duplicate detection rules for accounts and contacts. These rules are automatically turned on, so you don’t have to do anything to set up duplicate detection for these row types.  
  
> [!NOTE]
>  If available on your system, you may also be able to check for duplicates of other row types, in addition to contacts and accounts. Check with your system administrator. [Find your administrator or support person](find-admin.md)  

> [!NOTE]
>  To modify the columns that are visible for the current record in the duplicate detection dialog, administrators can modify the **Advanced Find View** for that entity. 
  
### How to merge duplicate rows
> [!NOTE]
>  Merging rows is only supported for account, contact, and lead tables, it doesn't support any other Dataverse out of box tables or custom tables. You can only merge two records at a time.
  
1. Select the duplicate rows from the view page in your model-driven app, and then select **Merge** in the command bar at the top of the page.  
  
   > [!div class="mx-imgBorder"] 
   > ![Duplicate row detected.](media/duplicates-detected-2.png "Duplicate row detected")  
  
2. In the **Merge Contacts** dialog box, select the primary row (the one you want to keep) and then select any columns in the new row that you want to merge into the primary row. Data in these columns may override the existing data in the primary row. Select **OK**.  

   > [!NOTE]
   > If you run into issues during the merge process, uncheck **Enable parent check**. If files are deleted during the merge process, you can skip the parent check. This allows your merge to continue even if someone deletes a row from the set while the job is running in the background. For more information, see [Asynchronous processing of cascading transactions](/power-platform/admin/async-cascading#troubleshooting-file-deletion-issues-during-cascade-merge).
  
     
   > [!div class="mx-imgBorder"] 
   > ![Dialog box for merging rows.](media/merge-dups.gif "Dialog box for merging rows")  
  


> [!IMPORTANT]
>  If a column or control matches any of the following conditions, it will not show up in the merge dialog:  
>   - The field or containing section is invisible in form descriptor or form XML regardless whether the section shows up in runtime. It's possible to show it using the client API.
>   - The control doesn't have a class property.
>   - The column's metadata `ValidForUpdate` is False.
>   - The control is **Quick Form Collection Control** or **Reference Panel Quick Form Collection Control**.
>   - The column is `Choice` or `MultiSelectPickList` and it has either a parent choice or child choice column.
>   - The column is `parentaccountid` on the Account table; this is a system setting and can't be changed. 
>   - The column is `parentcustomerid` on the  Contact Table; this is a system setting and can't be changed.
>   - The column is of type `Owner` (example: `ownerid`).

> [!IMPORTANT]
> Merging records with a SharePoint documents library only merges the records and not the documents libraries. Learn more in [Collaborate using SharePoint](collaborate-using-sharepoint.md).

[!INCLUDE[footer-include](../includes/footer-banner.md)]
