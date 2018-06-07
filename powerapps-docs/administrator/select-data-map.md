---
title: "Select a data map (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 09/15/2017
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 31cc6338-3d1a-4b76-b1cb-e835803a3595
caps.latest.revision: 41
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Select a data map

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

1.  Select a data map to tell the Import Data wizard how to organize your imported data into the right columns and fields in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)].  
  
     Select the default data map to let the wizard automatically map your data, or select a data map to match the type of information you’re importing.  
  
     The following tables help you decide which data map to use.  
  
2.  Click **Next**.  
   
|||  
|-|-|  
|**System Data Maps**|**When to Use**|  
|Default (Automatic Mapping)|Recommended. Use when you want the wizard to map the imported data to the columns and fields in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] automatically.<br /><br /> If the wizard can’t determine how to map your data, you’ll have an opportunity to map it manually later. **Important:**  Import files can only contain one type of data, such as contacts, leads, accounts, or cases. Also, the column headings in the source file must match exactly with the field names in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)].|  
|For Generic Contact and Account Data|Use when the import file contains contacts or accounts.|  
  
|||  
|-|-|  
|**Data Maps for [!INCLUDE[tn_salesforce](../includes/tn-salesforce.md)]**|**When to Use**|  
|For Contact and Account Report Export|Use this map when your import file contains contacts or accounts from [!INCLUDE[tn_salesforce](../includes/tn-salesforce.md)].|  
|For Full Data Export|Use this map when your import file is exported from [!INCLUDE[tn_salesforce](../includes/tn-salesforce.md)] using Full Data Export.|  
|||  
|For Report Export|Use this map when your import file is exported from [!INCLUDE[tn_salesforce](../includes/tn-salesforce.md)] using Report Export.|  
  
|||  
|-|-|  
|**Data Maps for Microsoft Outlook Business Contact Manager**|**When to Use**|  
|For [!INCLUDE[pn_ms_Outlook_2010_BCM](../includes/pn-ms-outlook-2010-bcm.md)]|Use this map when your import file contains data from [!INCLUDE[pn_ms_Outlook_2010_BCM](../includes/pn-ms-outlook-2010-bcm.md)].|  
  
|||  
|-|-|  
|**Custom Maps**(optional)|**When to Use**|  
|Custom maps|If available, custom data maps created for your organization are listed here.|  
  
### See also  
 [Import contacts](https://docs.microsoft.com/dynamics365/customer-engagement/basics/import-contacts)   
 [Import accounts, leads, or other data](https://docs.microsoft.com/dynamics365/customer-engagement/basics/import-accounts-leads-other-data)   
