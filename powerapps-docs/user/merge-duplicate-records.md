---
title: "Merge duplicate records| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/25/2019
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

Duplicate records can creep into your data when you or others enter data manually or import data in bulk. Common Data Service helps you address potential duplicates by providing duplicate detection for accounts and contacts. Your administrator may also set up duplicate detection rules for other situations.  
  
For example, let's say you enter a contact record, Jim Glynn,  along with a mobile phone number.  The duplicate detection rule discovers that you already have a similar record, and displays this dialog box.  
  
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact record detectied](/media/duplicates-detected.png "Duplicate contact record detectied")  
  
 You're not sure if this is a new record (one that happens to have the  same name as an existing contact) or a duplicate, so you select **Ignore And Save**.  
  
 Next, you go to the **All Contacts** list and see that now you have two records with the same name. After reviewing the records,  you  determine that they're duplicates that need to be merged.  
 
 > [!div class="mx-imgBorder"] 
 > ![Duplicate contact record detectied](media/duplicates-detected_1.png "Duplicate contact record detectied")  
 
Dynamics 365 Customer Engagement (on-premises) includes duplicate detection rules for accounts, contacts, and leads. These rules are automatically turned on, so you don’t have to do anything to set up duplicate detection for these record types.  
  
> [!NOTE]
>  If available on your system, you may also be able to check for duplicates of other record types, in addition to contacts and accounts. Check with your system administrator. [Find your administrator or support person](find-admin.md)  
  
## Merge duplicate records  
  
1. Select the duplicate records, and then select **Merge**.  
  
  > [!div class="mx-imgBorder"] 
  > ![Duplicate contact record detectied](media/duplicates-detected_1.png "Duplicate contact record detectied")  
  
2. In the **Merge Records** dialog box, select the master record (the one you want to keep), and then select any fields in the new record that you want to merge into the master record. Data in these fields may override the existing data in the master record. Select **OK**.  
  
     
  > [!div class="mx-imgBorder"] 
  > ![Dialog box for merging records](media/merge-records-dialog.png "Dialog box for merging records")  
  
> [!NOTE]
>  There are three situations when duplicates may be found:  
> 
> - When a record is created or updated.  
>   - When  you're using [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] and you go from offline to online.  
>   - When you import data using the Import Data wizard.  
> 
>   Duplicates aren't detected when you merge records, convert a lead, save an activity as completed, or change the status of a record, such as activating or reactivating a record.  
