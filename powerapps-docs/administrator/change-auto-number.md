---
title: "Change auto-numbering prefixes in Dynamics 365 Customer Engagement | MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 13aa0eb0-537f-432e-ac26-706ebd511dbd
caps.latest.revision: 39
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Change auto-numbering prefixes for contracts, cases, articles, quotes, orders, invoices, campaigns, categories, and knowledge articles

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

Contracts, cases, articles, quotes, orders, invoices, marketing campaigns, categories, and knowledge articles (the new Knowledge Article entity introduced in [!INCLUDE[pn_crm_online_2016_update](../includes/pn-crm-online-2016-update.md)] and [!INCLUDE[pn_crm_2016](../includes/pn-crm-2016.md)]) are automatically numbered by [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. If your organization has standard numbering formats, you can change the default three-character prefixes and number format to match your organization.  
  
1.  Go to **Settings** > **Administration** > **Auto-Numbering**.  
  
2.  In the **Set Auto-Numbering** dialog box, select the record type that you want to change.  
  
3.  In the **Prefix** box, enter up to three characters, symbols, or numbers.  
  
     Prefixes are system-wide and are used for all system-generated numbers for the selected record type. If you change the prefix for a record type, it won’t change the prefix of numbers that are already assigned.  
  
     The prefix of the tracking token for email messages is set in the System Settings area. More information: [System Settings dialog box - Email tab](system-settings-dialog-box-email-tab.md)  
  
4.  In the **Number** box, enter the starting number.  
  
     If you haven’t set a numbering format before, the **Number** box displays 1000. After you set the numbering format and save your settings, this field is set to read-only and you can’t modify it. If a custom auto-numbering solution was used, you won’t be able to change the number.  
  
5.  Select a suffix length.  
  
     Articles and knowledge articles don’t have suffixes. The suffix is used for records that were created while you were offline and for which the number can’t be guaranteed to be unique.  
  
6.  Click **OK** to save your settings.  
  
### See also  
 [Use the default solution to customize](../../maker/common-data-service/use-solutions-for-your-customizations.md)