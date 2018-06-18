---
title:  Terminology used in the product and documentation  | Microsoft Docs
description: In this quickstart, you learn how to download a list of apps created in your environments
services: 'powerapps'
suite: powerapps
documentationcenter: na
author: jimholtz
manager: kvivek
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 06/30/2018
ms.author: jimholtz

---
# Terminology used in the product and documentation

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

The following are terms used throughout the [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] product and documentation.  
  
<a name="BKMK_Terminology"></a>  
  
|Term|Definition|  
|----------|----------------|  
|Tenant|For [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)], a tenant is the account you create in the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)] when you sign up for a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription. A tenant contains uniquely identified domains, users, security groups, and subscriptions and can contain multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] environments.<br /><br /> The tenant created for you has a domain name of \<account>.onmicrosoft.com. For example, contoso.onmicrosoft.com.|  
|Environment <br />(previously called instances)|When you sign up for a trial or purchase a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] subscription, a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] production environment is created. Each additional production or non-production (Sandbox) [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] environment you add creates a separate and isolated [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] organization on the same tenant.<br /><br /> An environment has the URL format: https://\<URL name>.crm.dynamics.com. For example, https://contososales.crm.dynamics.com.|  
|Multiregional environment|An environment in a different region than where your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] tenant resides. Local environments can provide quicker data access for users in that region. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Add and edit multiregional environments](add-edit-multiregional-environments.md)|  
|Subscription|A subscription consists of the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] licenses and add-ons included with the trial or paid service you signed up for in your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] account. [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] subscriptions can vary in license type, price, and end date.<br /><br /> For example, a subscription might be 100 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Professional and 10 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Enterprise.|  
|Identity|The user account used to sign in to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. You can also use this identity to access other Microsoft Online services, such as [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] or [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)]. Administrators can decide if they want to federate user identity management between [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] and on-premises [!INCLUDE[pn_Active_Directory](../includes/pn-active-directory.md)].|  
|User account|A user account assigned by an organization (work, school, non-profit) to one of their constituents (an employee, student, customer) that provides sign-in access to one or more of the organization’s Microsoft cloud service subscriptions, such as [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. Access to an online service is controlled by the license assigned to the user account.<br /><br /> User accounts are stored in an organization’s cloud directory within [!INCLUDE[pn_azure_active_directory](../includes/pn-azure-active-directory.md)], and are typically deleted when the user leaves the organization. Organizational accounts differ from Microsoft accounts in that they are created and managed by admins in the organization, not by the user.|  
|Security group|If your company has multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] environments, you can use environment security groups to control which licensed users can access a particular environment. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Control user access to environments: security groups and licenses](add-environment-subscription.md#BKMK_man_sec_group)|  
|Common Data Services  |[Common Data Service ](../maker/common-data-service/data-platform-intro.md) is the data platform that comes with PowerApps and allows you to store and model business data. It's the platform on which Dynamics 365 applications are built; if you’re a Dynamics customer, your data is already in the Common Data Service.   |
|Data loss prevention policy (DLP) |A policy designed to protect an organization's data by defining which consumer connectors and what data can be shared. For example, an organization that uses PowerApps can create a DLP to prevent business data that's stored in SharePoint to not be automatically published to its Twitter feed. See [Create a data loss prevention (DLP) policy](create-dlp-policy.md)  |
|Data groups  |Data groups are a simple way to categorize services within a data loss prevention (DLP) policy. See [Data groups](introduction-to-data-groups.md).   |
  
### See also  
 [Manage Microsoft Dynamics 365 (online) environments](manage-online-environments.md)
