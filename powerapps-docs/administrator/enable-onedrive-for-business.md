---
title: "Enable OneDrive for Business (online) with Dynamics 365 Customer Engagement| MicrosoftDocs"
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
ms.assetid: c3742b70-863a-488e-beb3-fb9d63c2e6e5
caps.latest.revision: 5
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# Enable OneDrive for Business (online)

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

This feature was introduced in [!INCLUDE[pn_crm_online_2016_update_shortest](../includes/pn-crm-online-2016-update-shortest.md)].  
  
 Users can create and manage private documents with [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)]. Those documents can be accessed in [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] after the system administrator has enabled [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)].  
  
## Requirements  

> [!NOTE]
>  This topic applies to organizations deploying online versions of [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] and [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. For information on integrating [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] on-premises with Dynamics 365, or an online/on-premises mix of these products, see: [Enable OneDrive for Business (on-premises)](connect-onedrive-business.md).  

 The following are required to use [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] with [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]:  
  
-   [Configure server-based authentication with Dynamics 365 (online) and SharePoint Online](https://docs.microsoft.com/dynamics365/customer-engagement/admin/configure-server-based-authentication-sharepoint-online).  
  
-   A [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] license for each user. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [What is OneDrive for Business?](https://support.office.com/article/What-is-OneDrive-for-Business-187f90af-056f-47c0-9656-cc0ddca7fdc2)  
  
-   A [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] license for each user. Users with a [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] license can use [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)]. For [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)], [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] subscriptions come with [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)] licenses.  
  
- [!INCLUDE[cc_Office365PlanRequirement](../includes/cc-office365planrequirement.md)]  
  
-   Before using [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)], the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] administrator and end users should access [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] through the web interface. For example, if you’re using [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)], go to **https://portal.office.com** > **app launcher**![Office 365 app launcher](media/crm-itpro-officeapplauncher.png "Office 365 app launcher") > **OneDrive**. The site and other information required by [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] to enable [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] integration gets created only when the site is accessed.  
  
## Enable OneDrive for Business  
 You can enable [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] as follows.  
  
1.  Click **Settings** > **Document Management** > **Enable OneDrive for Business**.  
  
2.  Click **Enable OneDrive for Business** to enable it, and then choose **OK**.  
  
## Controlling access to OneDrive for Business in Dynamics 365  
 You can toggle availability of [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] for end users through the **OneDrive for Business** privilege.  
  
1.  Click **Settings** > **Security** > **Security Roles**.  
  
2.  Select a security role, and then click the **Core Records** tab.  
  
3.  Under **Miscellaneous Privileges**, toggle the **OneDrive for Business** privilege to the desired availability.  
  
 ![Toggle availability of OneDrive for Business](media/crm-itpro-onedriveforbusn-priv.png "Toggle availability of OneDrive for Business")  
  
### See also  
 [Enable OneDrive for Business (on-premises)](connect-onedrive-business.md)   
 [What is OneDrive for Business?](https://support.office.com/en-US/article/What-is-OneDrive-for-Business-187f90af-056f-47c0-9656-cc0ddca7fdc2)
