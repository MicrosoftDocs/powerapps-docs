---
title: "What is Office 365 and how does it relate to Dynamics 365 (online)? | MicrosoftDocs"
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
ms.assetid: 1d489839-9400-4d74-b270-468e33719d80
caps.latest.revision: 4
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# What is Office 365 and how does it relate to Dynamics 365 (online)? 

> [!NOTE]
> ![This page is under construction. Check back soon!](media/under_construction.png "Coming soon")  [!INCLUDE[cc-under-construction](../includes/cc-under-construction.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

[Office 365](https://products.office.com/business/enterprise-productivity-tools) is a collection of online services designed to work together to provide enterprise-grade, anywhere access to email, file sharing, and online meetings. [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] includes features that allow administrators to add users, manage passwords and licenses, and much more. [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] takes advantage of the [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] administration features to simplify user management. [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] users are created and managed in the [Office 365 admin center](https://support.office.com/article/About-the-Office-365-admin-center-758befc4-0888-4009-9f14-0d147402fd23).  
  
 A [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription doesn’t include [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] applications such as [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)]. You can significantly enhance your company’s online, collaborative experience by integrating [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] applications with your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription. However, that requires a separate purchase. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Add Office 365 Online services](add-office-365-online-services.md).  
  
> [!TIP]
>  You should also take a look at the data compilation and visualization possibilities with [Power BI for Office 365](http://go.microsoft.com/fwlink/p/?LinkID=389739). In addition, see the blog post [Dynamics CRM Online in Power Query](http://blogs.msdn.com/b/powerbi/archive/2013/12/19/dynamics-crm-online-in-power-query.aspx) for a presentation on [!INCLUDE[pn_power_bi_for_office_365_short](../includes/pn-power-bi-for-office-365-short.md)] and [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] integration.  
  
<a name="BKMK_Terminology"></a>   
## Terminology  
  
|Term|Definition|  
|----------|----------------|  
|Tenant|For [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)], a tenant is the account you create in the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)] when you sign up for a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription. A tenant contains uniquely identified domains, users, security groups, and subscriptions and can contain multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances.<br /><br /> The tenant created for you has a domain name of \<account>.onmicrosoft.com. For example, contoso.onmicrosoft.com.|  
|Instance|When you sign up for a trial or purchase a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] subscription, a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] production instance is created. Each additional production or non-production (Sandbox) [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instance you add creates a separate and isolated [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] organization on the same tenant.<br /><br /> An instance has the URL format: https://\<URL name>.crm.dynamics.com. For example, https://contososales.crm.dynamics.com.|  
|Subscription|A subscription consists of the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] licenses and add-ons included with the trial or paid service you signed up for in your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] account. [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] subscriptions can vary in license type, price, and end date.<br /><br /> For example, a subscription might be 100 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Professional and 10 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Enterprise.|  
|Identity|The user account used to sign in to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. You can also use this identity to access other Microsoft Online services, such as [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] or [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)]. Administrators can decide if they want to federate user identity management between [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] and on-premises [!INCLUDE[pn_Active_Directory](../includes/pn-active-directory.md)].|  
|User account|A user account assigned by an organization (work, school, non-profit) to one of their constituents (an employee, student, customer) that provides sign-in access to one or more of the organization’s Microsoft cloud service subscriptions, such as [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. Access to an online service is controlled by the license assigned to the user account.<br /><br /> User accounts are stored in an organization’s cloud directory within [!INCLUDE[pn_azure_active_directory](../includes/pn-azure-active-directory.md)], and are typically deleted when the user leaves the organization. Organizational accounts differ from Microsoft accounts in that they are created and managed by admins in the organization, not by the user.|  
|Security group|If your company has multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances, you can use instance security groups to control which licensed users can access a particular instance. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Control user access to instances: security groups and licenses](add-environment-subscription.md#BKMK_man_sec_group)|  
  
### See also  
 [Office 365 Service Descriptions](https://technet.microsoft.com/library/office-365-service-descriptions.aspx)   
 [Compare all Office 365 for business plans](https://products.office.com/business/compare-more-office-365-for-business-plans?legRedir=true&CorrelationId=56bfcc21-5017-4cde-982d-bfe9de7c9a14)   
 [Add Office 365 Online services](add-office-365-online-services.md)
