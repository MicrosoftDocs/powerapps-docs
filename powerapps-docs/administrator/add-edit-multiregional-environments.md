---
title:  Add and edit multiregional instances | Microsoft Docs
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
ms.date: 03/21/2018
ms.author: jimholtz

---
# Add and edit multiregional instances

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

For multinational companies with employees and customers distributed around the world, you can create and manage [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instances specific to your global regions. You can create an instance in a different region than where your [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] tenant resides. Local instances can provide quicker data access for users in that region. Be sure to read [A multi-environment deployment](multiple-online-environments-tenants.md#BKMK_Single) to understand the features of multiple instances.  
  
 Purchase the [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] instance on the [Purchase subscriptions](https://portal.office.com/Commerce/Catalog.aspx) page. You must have an active [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] account to complete the purchase. Additional storage and instances can be purchased by customers who have a paid [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Professional or [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Enterprise subscription.  
  
 You must have an [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Global administrator or [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] System administrator role to do these tasks. For more information, see [Assigning admin roles](https://support.office.com/article/Assign-admin-roles-eac4d046-1afd-4f1a-85fc-8219c79e1504).  
  
> [!NOTE]
>  To request the ability to create [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instances (production and non-production) in more than one geographical region, please contact your account manager or [Technical Support](contact-technical-support.md).  
  
<a name="BKMK_info_instance"></a>   
## What information do I need to create an instance?  
 During the initial configuration an instance, you can accept the default values, or enter different values to create a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instance.  
  
- **Region**. Choose from the following: Asia Pacific (APAC); Canada (CAN); Europe, Middle-East, Africa (EMEA); India (IND); Japan (JPN); North America (NA); Oceania (OCE); South America (LATAM/SAM).  
  
    > [!TIP]
    >  To view the current data centers for your region, see [Where is my data?](http://go.microsoft.com/fwlink/p/?LinkID=401277)  
  
- **Name**. This is typically the name of your organization and is displayed in the [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] application.  
  
- **URL**. The URL name is used to construct the URL for users to sign-in to the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] application. Therefore, we recommend that you limit the length of URL name to reduce the overall length of the URL.  
  
- **Purpose**. This value is used to associate the instance with a specific intent and is only displayed in the instance picker. For example, if this instance is for exclusive use by your sales and marketing departments you can enter *Contoso Sales and Marketing* or if the instance is for development and for testing purposes enter a relevant name such as *Contoso Development*.  
  
- **Instance Security Group**. This value is used to determine the [!INCLUDE[pn_MS_Online_Services](../includes/pn-ms-online-services.md)] security group that includes the users who will have access to this instance of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)]. For more information, see [Control user access to instances: security groups and licenses](add-environment-subscription.md#BKMK_man_sec_group).  
  
    > [!IMPORTANT]
    >  If you do not specify a security group, all users associated with the subscription who have a [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] license will be added to the new instance.  
  
- **Organizational language**. This language will be used for the [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] application.  
  
- **Base currency**. When you add an instance, you must select a base currency before the instance is provisioned. Although you can add currencies in the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] application, only the base currency will be used for reporting.  
  
    > [!WARNING]
    >  Once set, the base currency cannot be changed.  
  
<a name="BKMK_add_instance"></a>   
## Create a regional instance  
 The following steps apply to customers who do not purchase using volume licensing. Volume license customers should see: [Purchase Microsoft Dynamics 365 Through Volume Licensing](http://www.microsoft.com/licensing/online-services/how-to-buy.aspx).  
  
### Step 1: Purchase the additional instance  
  
1.  Global administrators sign in to the [Office 365 admin center](https://portal.office.com), and then, in the navigation pane, click **Billing** > **Purchase services**.  
  
2.  Scroll down to the **Add-on subscriptions** section, and then hover over **Microsoft Dynamics 365 (online) Additional Non-production Instance** or **Microsoft Dynamics 365 (online) Additional Production Instance**, and then click **Buy now**.  
  
3.  Proceed through the screens to purchase additional instances.  
  
     You can choose to add production or non-production (Sandbox) instances. For more information, see [Microsoft Dynamics 365 pricing and licensing](http://go.microsoft.com/fwlink/p/?LinkID=324564).  
  
### Step 2: Configure the additional instance for a region  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select the instance that you want to configure, and then click **Configure**.  
  
    > [!IMPORTANT]
    >  If the instance does not appear in the list or is in a state other than **ready to configure**, wait a few minutes and then try again.  
    >   
    >  You cannot start a new [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] instance until you click **Configure** and complete the configuration process.  
    >   
    > [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instances will not come prepared with sample data when configured by a Global administrator who does not have a [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] license. Sample data may be added later, after the instance is configured and ready to use, by a [!INCLUDE[pn_crm_online_subsequent](../includes/pn-crm-online-subsequent.md)] licensed user who has the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] system administrator security role. For more information, see [Add or remove sample data](https://docs.microsoft.com/dynamics365/customer-engagement/admin/add-remove-sample-data).  
  
5.  On the **configure new instance** page, select a region for the instance.  
  
6.  Enter the rest of your settings, including choosing a currency, and then click **Next**.  
  
    > [!IMPORTANT]
    >  After a base currency is selected it cannot be changed.  
    >   
    >  Although you can add currencies in the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] application, only the base currency will be used for reporting. To select a different currency, click **Change currency** and select a different one or specify a custom currency.  
  
7.  On the confirmation page, verify that the settings are correct and then click **Configure**.  
  
8.  On the **Your Microsoft Dynamics 365 organization is ready** page, click **Launch Dynamics 365 (online)** to start [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] to prepare the instance for users such as assign security roles, create teams, customize, and import data. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Getting started](getting-started.md).  
  
    > [!TIP]
    >  Note the [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instance URL that is displayed on the page. You can use this URL to directly access the [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] instance.  
  
<a name="BKMK_ConfigureManage"></a>   
## Configure and manage a regional instance  
 To configure and manage a regional instance, you must first select your active region to be the same as the regional instance.  
  
### Select a regional instance to configure and manage  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  From the drop-down list, select the region of the regional instance to configure. For example, to edit an instance in Japan, select the APAC region.  
  
    > [!NOTE]
    >  If you don’t see the **Your current region is:** drop-down list, you don’t have any instances outside of your current region.  
  
5.  Select the instance that you want to configure, and then click **Configure**.  
  
     The **Edit**, **Copy**, and **Reset** buttons appear when you’ve selected a regional instance matching your active region.  
  
    > [!NOTE]
    > - Copied instances are copied to the same region as the source instance.  
    > - Instances that are reset are reset to the current region.  
  
### See also  
 [Edit properties of an instance](edit-properties-environment.md)   
 [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md)   
 [Manage Microsoft Dynamics 365 (online) instances](manage-online-environments.md)   
 [Differences between the Microsoft Online services environment administrative roles and Dynamics 365 (online) security roles](grant-users-access.md) <br />
 [Grant users access to Microsoft Dynamics 365 (online) as a Microsoft Online service](grant-users-access.md)   
 [Manage subscriptions, licenses, and user accounts](manage-subscriptions-licenses-user-accounts.md)
