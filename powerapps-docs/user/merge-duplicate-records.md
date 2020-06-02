---
title: "Merge duplicate records| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/31/2019
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
# Merge duplicate records 

Duplicate records can creep into your data when you or others enter data manually or import data in bulk. Common Data Service helps you address potential duplicates by providing duplicate detection for active records such as, accounts and contacts. When you merge a record any related or child records will also be merged. Your administrator may also set up duplicate detection rules for other situations.  
  
For example, let's say you enter a contact record, Jim Glynn,  along with a mobile phone number.  The duplicate detection rule discovers that you already have a similar record, and displays this dialog box.  
  
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact record detectied](media/duplicates-detected.png "Duplicate contact record detectied")  
  
 You're not sure if this is a new record (one that happens to have the  same name as an existing contact) or a duplicate, so you select **Ignore And Save**.  
  
 Next, you go to the **All Contacts** list and see that now you have two records with the same name. After reviewing the records,  you  determine that they're duplicates that need to be merged.  
 
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact record detectied](media/duplicates-detected_1.png "Duplicate contact record detectied")  
 
Common Data Service includes duplicate detection rules for accounts and contacts. These rules are automatically turned on, so you don’t have to do anything to set up duplicate detection for these record types.  
  
> [!NOTE]
>  If available on your system, you may also be able to check for duplicates of other record types, in addition to contacts and accounts. Check with your system administrator. [Find your administrator or support person](find-admin.md)  
  
### How to merge duplicate records  
  
1. Select the duplicate records, and then select **Merge**.  
  
   > [!div class="mx-imgBorder"] 
   > ![Duplicate contact record detectied](media/duplicates-detected_2.png "Duplicate contact record detectied")  
  
2. In the **Merge Records** dialog box, select the master record (the one you want to keep), and then select any fields in the new record that you want to merge into the master record. Data in these fields may override the existing data in the master record. Select **OK**.  
  
     
   > [!div class="mx-imgBorder"] 
   > ![Dialog box for merging records](media/merge-records-dialog.png "Dialog box for merging records")  
  

There are a few situations when duplicates may be found:  

- When a record is created or updated.  
- When  you're using Dynamics 365 for Outlook and you go from offline to online.  
- When you import data using the Import Data wizard.  
- Duplicates aren't detected when you merge records, save an activity as completed, or change the status of a record, such as activating or reactivating a record.

> [!IMPORTANT]
>  If a field or control matches any of the following conditions, it will not show up in the merge dialog:  
>   - The containing section is invisible in form descriptor or form XML regardless whether the section shows up in runtime. It is possible to show it using the client API.
>   - The control does not have a class property.
>   - The attribute's metadata `ValidForUpdate` is False.
>   - The control is **Quick Form Collection Control** or **Reference Panel Quick Form Collection Control**.
>   - The attribute's metadata `ValidForUpdate` is False. 
>   - The attribute is `Picklist` or `MultiSelectPickList` and it has either a parent picklist or child picklist attribute.
>   - The attribute is ` parentaccountid` on the Account entity; this is a system setting and cannot be changed. 
>   - The attribute is ` parentcustomerid` on the  Contact Entity; this is a system setting and cannot be changed

