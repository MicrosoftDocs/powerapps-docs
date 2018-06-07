---
title: "Grant users access to Dynamics 365 (online) | MicrosoftDocs"
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
ms.assetid: a67a5f58-6d75-46bd-a14e-3e77331df206
caps.latest.revision: 4
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# Grant users access

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

To have users up and running in [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)], you complete some administrative tasks in the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)]—which you generally do only once—followed by administrative tasks in [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)].  
  
 [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] is an online service subscription. When you signed up for this service, you received a set of licenses with your subscription, one license for each user. You can purchase additional licenses if you need them.  
  
 As described in step one that follows, in the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)], register your users so that they are recognized in the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)], assign a license to each user, and then assign administrative roles to the users you choose to fill those roles. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Assigning admin roles](https://support.office.com/article/Assign-admin-roles-in-Office-365-eac4d046-1afd-4f1a-85fc-8219c79e1504)  
  
 In [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], populate the service with your organization’s data, including users and their security roles, business units, and any existing [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data that you want to import from other applications or services. If your organization uses business units, assign users to the appropriate business unit, and then assign a security role to each user. [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] includes predefined security roles that aggregate a set of user permissions to simplify user security management. An organization can define additional roles or edit predefined security roles to meet its unique security needs. For more information about security roles in [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], see [Security roles and privileges](security-roles-privileges.md).  
  
> [!IMPORTANT]
>  Users can’t access [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] until they’ve been assigned at least one security role. See [Step Two: Assign security roles in Dynamics 365 (online)](grant-users-access.md#BKMK_StepTwo).  
  
<a name="BKMK_O365CRMroles"></a>   

## Differences between the Microsoft Online services environment administrative roles and Dynamics 365 (online) security roles  
 *Administrative roles* are available to assign to users in the [!INCLUDE[pn_MS_Online_Services_Portal](../includes/pn-ms-online-services-portal.md)]. The administrative roles cover a set of rights and permissions related to managing the service subscription, such as adding users and assigning licenses. The global administrator role has rights to control every aspect of the subscription and to add subscriptions to other online services. The password administrator role has rights to reset a user’s password, create service requests, and monitor the service.  
  
 *Security roles* are assigned within [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] and cover rights and permissions-related aspects, for example, permission to update records or to publish customizations.  
  
 The roles are similar in that both types contain aggregated sets of permissions that allow access to some items and not to others, and that allow some actions to be taken but not others. The roles are different in that the first one applies to the management of the subscription but not to the service itself, and the second applies only within the service.  
  
 Using roles is a powerful way to group a set of rights that are common to a job title or business unit. This way, the administrator can grant a whole set of permissions to users simply by assigning a user or group of users to a given role.  
  
## Step One: Provision users, and assign licenses and administrative roles in the Office 365 admin center  
 Your organization’s subscription to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] provides access to the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)] through a global administrator account. The global administrator manages every aspect of the subscription and may add subscriptions to other [!INCLUDE[pn_MS_Online_Services](../includes/pn-ms-online-services.md)].  
  
 As the global administrator for your organization, one of your first tasks is to create users in the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)]. This registers users in the system and enables users to be licensed to use services available within the online service environment. You decide which service you want your users to have by assigning a license for that service to a user. For instructions about creating users in the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)], see [Create or edit users in Office 365](http://go.microsoft.com/fwlink/p/?LinkId=251998). For instructions about assigning a license to a user, see [Assign or remove licenses, or view a list of unlicensed users](http://go.microsoft.com/fwlink/p/?LinkId=255449).  
  
 During your planning phase, you might have identified a set of key administrative roles that you want to fill. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Plan for Microsoft Dynamics 365 (online) deployment and administration](plan-for-deployment-and-administration.md). Because the administrative roles provide coverage for administrative tasks when the global administrator is not available, it’s a best practice to assign these roles to users, including assigning the global administrator role to a second user. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Assigning admin roles](http://go.microsoft.com/fwlink/p/?LinkId=255444) and [Permissions in Office 365](http://go.microsoft.com/fwlink/p/?LinkId=255464).  
  
### The online service sends an invitation to each user  
 After you set up a user in the [!INCLUDE[pn_office_365_admin_center](../includes/pn-office-365-admin-center.md)], that user receives an email invitation with a link and a password for the [!INCLUDE[pn_ms_online_services_environment](../includes/pn-ms-online-services-environment.md)]. The credentials in the invitation provide access to the portal and to documentation. However, the users who receive these invitations can’t access [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] until you complete step two in this process.  
  
<a name="BKMK_StepTwo"></a>   

## Step Two: Assign security roles in Dynamics 365 (online)  
 Sign in to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] and add business units (if your organization needs more than one business unit), and assign security roles and business units to users. The users you registered with the online service in step one are automatically added to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. After you assign at least one security role to a user, that user can click the link in the email invitation, enter credentials, and begin using [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Assign a security role to a user](create-users-assign-online-security-roles.md#assign-a-security-role-to-a-user).  
  
> [!IMPORTANT]
> Before you start adding information to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], we recommend that you turn off or disable your browser’s pop-up blocker. Pop-up blockers can block data-entry dialog boxes in [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]. For more information about browser and other settings for improved product performance, see [Key preparation and configuration tasks](https://docs.microsoft.com/dynamics365/customer-engagement/admin/key-preparation-and-configuration-tasks).  
  
 You might have [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data located in other systems. In your planning phase, you considered how you’ll import this data. Before you invite users into [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], ensure that you have completed the data migration process. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Import data (all record types)](import-data-all-record-types.md).  
  
### See also  
 [Get started administering Microsoft Dynamics 365 (online)](getting-started.md)   
 [Plan for Microsoft Dynamics 365 (online) deployment and administration](plan-for-deployment-and-administration.md)   
 [Manage subscriptions, licenses, and user accounts](manage-subscriptions-licenses-user-accounts.md)   
 [Import data (all record types)](import-data-all-record-types.md)   
