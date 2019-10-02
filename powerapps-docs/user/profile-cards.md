---
title: "View the profile card for a contact or user | MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/03/2019
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

# View the profile card for a contact or user

Use the profile card to get quick information about a contact or user. When you select a contact or user field in Dynamics 365 for Customer Engagement apps, you can find information related to them on their profile card. For more information about profile cards, see [Profile cards in Office 365](https://support.office.com/en-us/article/Profile-cards-in-Office-365-e80f931f-5fc4-4a59-ba6e-c1e35a85b501).

> [!NOTE]
>  - The profile card experience is available in the Unified Interface of Dynamics 365 Customer Engagemnt apps.
>  - It is available for the  **Contact** and **User** entity. For information, see [Enable the profile card (for admins)](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/admin/enable-profile-card).

## View a contact's profile

1.	Navigate to **Sales Hub** > **Activities**.
2.	Select an existing activity or create a new one.
3.	Hover over the **Call To** field when it has a contact record. 

You can view details of the contact inline which includes the contact picture, name, title and account.

4. To view more details, select **Show more** to expand the contact's profile.
 
 ![Expand contact profile card detail](media/userprofilecard_1.gif "Expand contact profile card details")
   
 ## View a user's profile
 
1.	Navigate to **Sales Hub** > **Accounts**.
2.	Select an account record.
3.	Hover over the owner field when it has a user record. You can view the details of the user inline.
4.  To view more details like emails and shared files with the user, select **Show more** to expand the contact's profile.
 
![Expand User profile card detail](media/Userprofilecard_2.gif "Expand User profile card details")


 ## FAQs
 
### Where can I see profile cards in Dynamics 365?
Profile cards in Dynamics 365 can be seen in Unified Interface on contact and user records. You can only view them when they are in a lookup.

### Where is information shown in the profile card coming from?
The information shown on the contact profile card is fetched from Common Data Service (and not Microsoft Exchange). This means the contact details are coming from Dynamics 365.

The information shown on the user profile card is fetched from Office 365 (Azure Active Directory). For more information, see [Profile cards in Office 365 (admin section)](https://support.office.com/en-us/article/Profile-cards-in-Office-365-e80f931f-5fc4-4a59-ba6e-c1e35a85b501).

### How can I customize the fields shown on the profile card?
Currently, the list of fields displayed on the profile card are not open for customization.

### Why is the **Start chat** option on the profile card disabled (greyed out)?
The **Start chat** and the **Send Email** options on the profile card will open your default instant message and email apps. The **Start chat** option is enabled if the person you are trying to contact in the same Azure Active Directory environment as you or is a federated contact.

### Can I see profile cards in Dynamics 365 on the tablet app?
Profile cards in Dynamics 365 are only enabled for browsers on a desktop/PC currently, as they are activated on hover.

### What will happen to the Skype presence integration in Unified Interface?
When you have enabled both Skype presence and the profile card integration in Dynamics 365, you will see the profile card displayed in a lookup. All other areas referencing Skype card integration will not be affected.

> [!NOTE]
>  The profile card in Dynamics 365 is not displayed if multi-factor authentication is turned on for Office Delve service in Azure Active Directory.
  
