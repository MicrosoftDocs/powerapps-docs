---
title: "Multiple Dynamics 365 (online) instances or tenants | MicrosoftDocs"
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
ms.assetid: 2bdb7dc2-da26-4ab7-9e8f-65c04ae6df0d
caps.latest.revision: 4
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# About multiple online instances or tenants

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

[!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] gives you options for segregating your [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data and user access. For most companies, adding and using multiple instances in your subscription provides the right mix of functionality and ease of management. Enterprises with separate geographic locations might consider using multiple tenants to separate [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] licenses. Multiple instances can share users among instances; multiple tenants cannot.  
  
> [!NOTE]
>  The concept and operation of tenants and instances, though similar, differs between online and on-premises deployments of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. This topic is for those administering [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] deployments.  
  
<a name="BKMK_Terminology"></a>   
## Terminology  
  
|Term|Definition|  
|----------|----------------|  
|Tenant|For [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)], a tenant is the account you create in the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)] when you sign up for a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription. A tenant contains uniquely identified domains, users, security groups, and subscriptions and can contain multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances.<br /><br /> The tenant created for you has a domain name of \<account>.onmicrosoft.com. For example, contoso.onmicrosoft.com.|  
|Instance|When you sign up for a trial or purchase a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] subscription, a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] production instance is created. Each additional production or non-production (Sandbox) [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instance you add creates a separate and isolated [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] organization on the same tenant.<br /><br /> An instance has the URL format: https://\<URL name>.crm.dynamics.com. For example, https://contososales.crm.dynamics.com.|  
|Multiregional instance|An instance in a different region than where your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] tenant resides. Local instances can provide quicker data access for users in that region. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Add and edit multiregional instances](add-edit-multiregional-environments.md)|  
|Subscription|A subscription consists of the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] licenses and add-ons included with the trial or paid service you signed up for in your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] account. [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] subscriptions can vary in license type, price, and end date.<br /><br /> For example, a subscription might be 100 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Professional and 10 licenses of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Enterprise.|  
|Identity|The user account used to sign in to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. You can also use this identity to access other Microsoft Online services, such as [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] or [!INCLUDE[pn_sharepoint_online](../includes/pn-sharepoint-online.md)]. Administrators can decide if they want to federate user identity management between [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] and on-premises [!INCLUDE[pn_Active_Directory](../includes/pn-active-directory.md)].|  
|User account|A user account assigned by an organization (work, school, non-profit) to one of their constituents (an employee, student, customer) that provides sign-in access to one or more of the organization’s Microsoft cloud service subscriptions, such as [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. Access to an online service is controlled by the license assigned to the user account.<br /><br /> User accounts are stored in an organization’s cloud directory within [!INCLUDE[pn_azure_active_directory](../includes/pn-azure-active-directory.md)], and are typically deleted when the user leaves the organization. Organizational accounts differ from Microsoft accounts in that they are created and managed by admins in the organization, not by the user.|  
|Security group|If your company has multiple [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances, you can use instance security groups to control which licensed users can access a particular instance. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Control user access to instances: security groups and licenses](add-environment-subscription.md#BKMK_man_sec_group)|  
  
## Uses for multiple instances  
 [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances are similar in concept to a high-rise business complex with floors organized according to business functions. Consider each floor within the building as an application (Sales/Service/Marketing, Vendor management, Wealth management) and consider each unit within a floor as an instance for a specific purpose such as Production, Training, Testing, and Development.  
  
 ![Multiple Dynamics 365 instances as units in a building](media/multi-tenant-3.png "Multiple Dynamics 365 instances as units in a building")  
  
 Multiple instances are needed when segregation is required of plugins, workflows, or admin resources that cannot be easily isolated by using business units in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)].  
  
<a name="BKMK_Single"></a>   
## A multi-environment deployment  
 A typical [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] deployment includes one tenant only. A tenant can include one or more [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances; however, a [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instance is always associated with a single tenant.  
  
 ![Single tenant deployment in Dynamics 365 (online)](media/multi-tenant-1b.png "Single tenant deployment in Dynamics 365 (online)")  
  
 This example uses two instances for three teams: Sales, Marketing, and Services.  
  
 Sales and Marketing share an instance so lead information can be easily accessed by both. Services has its own instance so tickets and warranties can be managed separately from campaigns and other sales related events.  
  
 You can provide access to one or both instances easily.  Sales and Marketing users could be limited to their instance while Service users with extended access could update support escalations records related to accounts in both instances.  
  
 About single tenant with multiple instances:  
  
-   A tenant can include up to 50 [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] production instances and up to 75 non-production (Sandbox) instances.  
  
-   Each instance within the tenant receives its own SQL database.  
  
- [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data is not shared across instances.  
  
-   Storage is shared across the primary instance and any additional instances.  
  
-   All instances for a single customer tenant will be set up in the geography where they initially signed up for their account. Storage consumption is totaled and tracked across all the instances attached to a customer tenant.  
  
-   You can set up separate security groups for all instances.  
  
-   A licensed [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] user can potentially access all the [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances associated with the tenant. Access is controlled by instance security group membership.  
  
-   You can purchase additional instances through the Additional Instance Add-On. Additional instances can be added only to "paid" subscriptions - not trials or Internal Use Rights (IUR). If you purchased your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription through Volume Licensing, you must go through your Large Account Reseller (LAR) to purchase the additional instance. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Billing and subscription support](https://docs.microsoft.com/dynamics365/customer-engagement/admin/billing-support)  
  
-   You can’t merge existing trials or subscriptions onto an additional instance; instead, you will need to move your data and customizations.  
  
## Why use multiple instances?  
 The following are common use cases for multi-environment deployment. Consider these examples when you decide the deployment type that best fits your company’s requirements.  
  
 **Master data management**  
  
 In this scenario, a “master” data set provides for change management through a central master data source. This approach requires that the central master data be synchronized to all instances so that each instance has access to the latest version of the core information. Requested changes to the information can be made directly within the master system. Alternatively, users can explicitly access the master system or capture the changes in the local instance, with those changes subsequently passed on to the master instance.  
  
 Requiring that changes be made centrally can provide for centralized change control. For example, anti-fraud checks can be performed to ensure that changes are made only by a central team and not by local teams that might otherwise benefit from a change, such as a change in credit limits. This would provide a second level of change authorization and verification that avoids the ability for a single person or a group of people who work closely together to collaborate to affect a fraud. Pushing a request to a different, independent team can provide protection against potential fraud.  
  
 **Security and privacy**  
  
 Differences in regional, for example European Union (EU), or national legislation can result in variations in requirements for securing data or maintaining data privacy across the different regions or countries in a deployment. In some cases, legislative/regulatory restrictions make it illegal to host data outside the borders of a country or region, and addressing this challenge is particularly critical in specific business sectors.  
  
 For example, consider healthcare sector restrictions on sharing patient information. Some EU regulations require that any health information that is collected about people residing in the EU be maintained and shared only within EU boundaries, while similar data collected about people in the United States (US) is kept within US boundaries. Also consider banking sector restrictions on sharing customer information. In Switzerland, for example, regulations make it illegal to share customer information outside of their national boundaries.  
  
 **Scalability**  
  
 While a single instance of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] can scale up and out to support the growth of a customer’s business, with very high data volumes or levels of complexity, there are additional considerations. For example, in environments with extreme volumes and/or extensive use of Service Scheduling, scaling up [!INCLUDE[pn_SQL_Server_short](../includes/pn-sql-server-short.md)] can require complicated and expensive infrastructure that is prohibitively expensive or extremely difficult to manage.  
  
 There are many scenarios in which there is a natural functional split in capability requirements. In such cases, delegating workloads by creating scale-out scenarios that are based on these functional splits can provide for higher volumes by using commodity infrastructure.  
  
## Add an instance to your subscription  
 For information about how to add an instance to your [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] subscription, see [Add an instance to your subscription](add-environment-subscription.md).  
  
<a name="BKMK_Multi"></a>   
## A multi-tenant deployment  
 Global businesses with regional or country models that differ can use tenants to account for variations in approach, market size, or compliance with legal and regulatory constraints.  
  
 ![Multi-tenant deployment in Dynamics 365 (online)](media/multi-tenant-2.png "Multi-tenant deployment in Dynamics 365 (online)")  
  
 This example includes a second tenant for Contoso Japan.  
  
 User accounts, identities, security groups, subscriptions, licenses, and storage cannot be shared among tenants. All tenants can have multiple instances associated with each specific tenant. [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data is not shared across instances or tenants.  
  
 About multiple tenants:  
  
-   In a multi-tenant scenario, a licensed [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] user associated with a tenant can only access one or more [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] instances mapped to the same tenant. To access another tenant a user would need a separate license and a unique set of sign-in credentials for that tenant.  
  
     For example, if User A has an account to access Tenant A their license allows them to access any and all instances created within Tenant A - if they are allowed by their administrator.  If User A needs to access instances within Tenant B, they will need an additional [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] license.  
  
-   Each tenant will require a tenant administrator(s) with unique sign-in credentials, and each tenant affiliate will manage its tenant separately in the administrator console.  
  
-   Multiple instances within a tenant are visible from the [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] interface if the administrator has access.  
  
-   You cannot reassign licenses between tenant enrollments. An enrolled affiliate can use license reduction under one enrollment and add licenses to another enrollment to facilitate this.  
  
-   On-premises Active Directory federation cannot be established with more than one tenant unless you have top-level domains that you need to federate with different tenants (for example Contoso.com and Fabricam.com).  
  
## Why use multiple tenants?  
 **Functional localization**  
  
 This scenario typically arises in organizations with overlapping but separate functional needs. Some common examples include:  
  
-   Organizations with different business divisions, each with a different market or model of operation.  
  
-   Global businesses with regional or country models that differ to account for variations in approach, market size, or compliance with legal and regulatory constraints.  
  
 In these types of business environments, an organization often will have common sets of functionality that allow specific regions, countries, or business areas with a degree of localization regarding:  
  
-   Information capture. For example, capturing the ZIP Code in the United States would correlate to capturing the Post Code in the United Kingdom.  
  
-   Forms, workflows.  
  
**Physical distribution**  
  
 For business solutions that must support users that are physically distributed over large distances, particularly for global deployments, using a single instance may not be suitable because of the implications (such as WAN latency) associated with the infrastructure over which the users connect, which can significantly impact the user experience. Distributing instances to provide users with more local access can reduce or overcome WAN-related issues, as the access occurs over shorter network connections.  
  
<a name="BKMK_AddMulti"></a>   
## Add a multi-tenant deployment under volume licensing  
 For a multi-tenant deployment, you'll need a Multi-Tenant Amendment. A Multi-Tenant Amendment is an actual amendment to the Volume License agreement used to purchase licenses. Contact your Microsoft Sales Representative or Reseller to obtain the amendment.  
  
## Constraints of multi-tenants  
 Admins who want to deploy and manage multiple tenants should be aware of the following:  
  
-   User accounts, identities, security groups, subscriptions, licenses, and storage cannot be shared among tenants.  
  
-   A single domain can only be federated with one tenant.  
  
-   Each tenant must have its own namespace; UPN or SMTP namespaces cannot be shared across tenants.  
  
-   If an on-premises [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] organization exists, you cannot split this organization across multiple tenants.  
  
-   A consolidated Global Address List will not be available, except if explicitly managed downstream from the synchronization.  
  
-   Cross-tenant collaboration will be limited to [!INCLUDE[pn_Lync_Short](../includes/pn-lync-short.md)] Federation and [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] Federation features.  
  
- [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] access across tenants may not be possible. While this may be solved with Partner Access, the user experience is disrupted and licensing aspects apply.  
  
-   There can be no duplicate accounts across the tenants or partitions in the on-premises [!INCLUDE[pn_Active_Directory](../includes/pn-active-directory.md)].  
  
### See also  
 [Manage Microsoft Dynamics 365 (online) instances](manage-online-environments.md)   
 [Using multi-tenancy in Microsoft Dynamics CRM 2013 to address challenges in enterprise business environments (primarily on-premises)](http://www.microsoft.com/download/details.aspx?id=36056)   
 [Blog: Dynamics CRM and multi-tenancy (on-premises)](https://community.dynamics.com/crm/b/salimadamondynamicscrm/archive/2014/01/27/dynamics-crm-and-multi-tenancy.aspx)
