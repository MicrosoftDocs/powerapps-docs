---
title: "Understanding how data is organized (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 09/15/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 70c55a33-dd08-44bc-bb9c-0f3732aa30a9
caps.latest.revision: 5
author: "brycho"
ms.author: "brycho"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Understanding how data is organized

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

Whether you’re in sales, service, or marketing, [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] Customer Engagement helps you organize and get big returns on your customer data. Because sales and service are unified in one system, salespeople have visibility into any active service issues so that they aren’t blindsided as they’re trying to close a deal. Likewise, if a customer calls in for support, a service rep can see that a big sale is pending and handle the caller accordingly.

With Customer Engagement business apps, you’ll be able to spot and respond to issues that may be blocking deals, see how your service team is doing with meeting the terms of your service level agreements, monitor the success of your marketing campaigns, and so much more. 
  
Although you don’t need to know a lot about databases to start working with [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], it’s helpful to know a few things about how data is organized in the system. In particular, there are two definitions you should know because they are used many places in the system: **record** and **record type**.  

Every day, you’ll work with different customer records and record types as you move customers through your business processes, collecting the data you need to fill in the fields for their records—and ultimately to win their business.  

## What’s a record?  
 In [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], a **record** is a complete unit of information. Think of it like a single row in a table, with multiple columns, also known as fields, to store the pieces of info that make up the entire row.  
  
 For example, for an account you could have a column for **Company name**, **Address**, and **Contact name** for the person you call when you want to check in on the account. Each time you add a new account to the system, you’re creating a new record in the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] database.  
  
## What’s a record type?  
 Each record you add to the system belongs to a certain **record type**, such as account, contact, lead, opportunity, or case. [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] has quite a few other types of records besides these, but these are the ones you’ll probably work with most often for Sales and Customer Service.  
  
 Record types give you a way to group and organize similar data. For example, in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] you’ll find your contact records grouped by the icon for the contact record type.  
  
 Case records are grouped by the icon for the case record type, account records are grouped by the icon for the account record type, and so on.  
  
## What are accounts, contacts, leads, and opportunities for?  
 Account and contact records store much of the information that you and your team collect from your customers.  
  
 You store data about companies you do business with in **accounts**. Similar to [!INCLUDE[pn_MS_Outlook_Full](../includes/pn-ms-outlook-full.md)] or other email programs, you store data about the people you know and work with in **contacts**.  
  
 Usually, an account has more than one contact associated with it, especially when you’re working with a larger company with many departments or locations and you deal with several people to manage the account.  
  
 **Leads** are for potential sales, and most organizations get leads from many sources. For example, you can enter leads manually from business cards, generate them from marketing campaigns or inquiries from your website, buy them in mailing lists, create them automatically from posts on [!INCLUDE[tn_facebook](../includes/tn-facebook.md)] or [!INCLUDE[tn_twitter](../includes/tn-twitter.md)] – the possibilities are almost endless.  
  
 If all goes well, after you nurture a lead, you’ll be able to promote it to an **opportunity**, which is another name for a deal you’re getting ready to close.  
  
## What are cases?  
 You store all the data about customer issues or questions in a **case**. Cases can originate from phone calls, email, inquiries on your website, or even from posts on [!INCLUDE[tn_facebook](../includes/tn-facebook.md)] or [!INCLUDE[tn_twitter](../includes/tn-twitter.md)]. (Some organizations call cases “incidents” or “tickets.”)  
  
 Cases store the details that service reps need to know as they resolve an issue. When you look at a case record, you’ll see the case priority, where it originated, whether the customer has other recent cases, how much service the customer is entitled to, and how much time you have to resolve it.  
 
## What if you see different names for the different types of records in your system?
One of the beauties of [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] is that it’s so easy to customize to match your organization’s industry, business goals, or preferences. So you may see
different names for the types of records, because your organization calls that type of data something different. For example, your system administrator may have changed “account” to “company,” or “contact” to “individual.”

### See also  
 [Find your way around Dynamics 365](../basics/navigation-customer-engagement-enterprise.md)   
 [What are business processes?](../basics/what-are-business-processes.md)
