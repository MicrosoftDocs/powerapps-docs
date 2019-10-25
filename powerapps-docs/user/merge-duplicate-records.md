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
# Merge duplicate records for accounts, contacts, or leads

Duplicate records can creep into your data when you or others enter data manually or import data in bulk. Dynamics 365 Customer Engagement (on-premises) helps you address potential duplicates by providing duplicate detection for accounts, contacts, and leads. Your administrator may also set up duplicate detection rules for other situations.  
  
 For example, let's say you enter a contact record, Jim Glynn,  along with a mobile phone number.  The duplicate detection rule discovers that you already have a similar record, and displays this dialog box.  
  
 ![Duplicate contact record detectied in Dynamics 365 Customer Engagement (on-premises)](../basics/media/duplicates-detected.png "Duplicate contact record detectied in Dynamics 365 Customer Engagement (on-premises)")  
  
 You're not sure if this is a new record (one that happens to have the  same name as an existing contact) or a duplicate, so you click **Save**.  
  
 Next, you go to the **My Active Contacts** list and see that now you have two records with the same name. After reviewing the records,  you  determine that they're duplicates that need to be merged.  
  
   > [!div class="mx-imgBorder"] 
   > ![Duplicate contacts listed in the My Active Contacts list in Dynamics 365 Customer Engagement (on-premises)](../basics/media/duplicates-list.png "Duplicate contacts listed in the My Active Contacts list in Dynamics 365 Customer Engagement (on-premises)")  
 
Dynamics 365 Customer Engagement (on-premises) includes duplicate detection rules for accounts, contacts, and leads. These rules are automatically turned on, so you don’t have to do anything to set up duplicate detection for these record types.  
  
> [!NOTE]
>  If available on your system, you may also be able to check for duplicates of other record types, in addition to contacts, accounts, and leads. Check with your system administrator. [Find your Dynamics 365 Customer Engagement (on-premises) administrator or support person](../basics/find-administrator-support.md)  
  
## Merge duplicate records  
  
1. Select the duplicate records, and then click **Merge**.  
  
   > [!div class="mx-imgBorder"] 
   > ![Merge records button in Dynamics 365 Customer Engagement (on-premises)](../basics/media/merge-contact-sbutton.png "Merge records button in Dynamics 365 Customer Engagement (on-premises)")  
  
2. In the **Merge Records** dialog box, select the master record (the one you want to keep), and then select any fields in the new record that you want to merge into the master record. Data in these fields may override the existing data in the master record. Click **OK**.  
  
   ![Dialog box for merging records in Dynamics 365 Customer Engagement (on-premises)](../basics/media/merge-records-dialog.png "Dialog box for merging records in Dynamics 365 Customer Engagement (on-premises)")  
  
> [!NOTE]
>  There are three situations when duplicates may be found:  
> 
> - When a record is created or updated.  
>   - When  you're using [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] and you go from offline to online.  
>   - When you import data using the Import Data wizard.  
> 
>   Duplicates aren't detected when you merge records, convert a lead, save an activity as completed, or change the status of a record, such as activating or reactivating a record.  
