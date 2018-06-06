---
title: "Connect Customer Engagement to Yammer | MicrosoftDocs"
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
ms.assetid: 7e180f88-c913-4b46-a923-c7162cf44566
caps.latest.revision: 25
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Connect to Yammer 

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

[!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] gives colleagues at your organization a central place to have conversations, create and edit documents, and share information without sending a single email or attending any meetings.  
  
 After you set up your organization to work with [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)], employees will see posts in a newsfeed on their [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] dashboard whenever people update customer info, and they’ll be able to join in the conversation with their own posts.  
  
## Connect your organization to Yammer  
  
### Prerequisites  
  
-   Before your organization can use [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] in [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)], your organization needs to buy [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] enterprise licenses.  

- [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] integration is only available for [!INCLUDE[pn_CRM_Online](../../includes/pn-crm-online.md)].
  
- [!INCLUDE[proc_permissions_system_admin](../../includes/proc-permissions-system-admin.md)]  
  
-   You’ll also need to have verified system administrator privileges for your organization’s [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] account, plus both the Write Organization and Configure Yammer privileges. If you’re not an administrator, by default these privileges aren’t available, and must be added.  
  
-   Install the most recent product updates for [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)].  
  
-   Meet [browser and system requirements](https://support.office.com/en-us/article/Yammer-admin-guide-a9c206d4-fb18-4250-bec6-e783b926e4f6).  
  
### Connect Dynamics 365 to Yammer  
  
1.  Sign up for a [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] Enterprise account, and note the name of the network you receive. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Visit the Yammer website](http://go.microsoft.com/fwlink/p/?LinkID=272440)  
  
2. [!INCLUDE[proc_settings_system](../../includes/proc-settings-system.md)]  
  
3.  Choose **Administration** > **Yammer Configuration**  
  
4.  Read the disclaimer, and then choose **Continue**.  
  
5.  Choose **Authorize [!INCLUDE[pn_CRM_Online](../../includes/pn-crm-online.md)] (or [!INCLUDE[pn_crm_2016_shortest](../../includes/pn-crm-2016-shortest.md)]) to connect to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)]**.  
  
6.  Sign in to your enterprise [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] account using your administrator credentials.  
  
7.  Follow the on-screen instructions to accept the [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] terms of service, note which [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] network has been set up for you, and connect your organization to it. After your organization is connected, you’ll see a confirmation message at the bottom of the screen.  
  
    > [!NOTE]
    > [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] only supports connecting to the primary [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] network. Connecting to External Networks in [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] is not supported.  
  
8.  If desired, stay signed in to your [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] account and set your organization’s preferences for [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] posts.  
  
### Set your organization’s preferences for Yammer posts (optional)  
  
1.  Make sure you’re signed in to your enterprise [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] account using your administrator credentials.  
  
2.  If desired, select whether [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] posts are **public** (everyone sees [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] posts in the newsfeed, or **private** (people must “follow” a record to see posts about that record in the newsfeed).  
  
3.  If desired, select the default group where you would like [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] posts to appear.  
  
4.  If desired, select which record types trigger automatic posts to the [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] newsfeed.  
  
## Enable Dynamics 365 entities for Yammer  
 Once you’ve connected [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)], you need to specify which [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] entities are enabled for use with [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)]. Enabled entities can be followed by users  
  
1. [!INCLUDE[proc_settings_system](../../includes/proc-settings-system.md)]  
  
2.  Choose **Activity Feeds Configuration** > **Post Configurations**  
  
3.  Choose the entity, and then choose **Activate**.  
  
4.  Confirm the activation, and then choose **More Commands (…)** > **Publish All Customizations**  
  
## What triggers automatic posts to the Yammer newsfeed?  
 The record types and rules in the following list can be enabled to trigger a [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] post automatically. Record types that are enabled by default are marked “Yes.” If you want to enable an entity or rule type, make sure that the entity or rule is activated and that the types of auto-posts you want are enabled.  
  
|Post Entity Id|Name|Enabled to Post Automatically|  
|--------------------|----------|-----------------------------------|  
|Case|New Case for an Account|Yes|  
|Case|New Case for a Contact|Yes|  
|Case|Case Closed for an Account||  
|Case|Case closed for a Contact||  
|Case|Case Assigned to User/Team||  
|Case|Case Routed to Queue||  
|Lead|New Lead created||  
|Lead|A Lead has been qualified||  
|Opportunity|New opportunity for an Account|Yes|  
|Opportunity|New opportunity for a Contact|Yes|  
|Opportunity|Probability for an Opportunity Updated for an account||  
|Opportunity|Probability for an Opportunity Updated for a contact||  
|Opportunity|Opportunity Won for an Account|Yes|  
|Opportunity|Opportunity Won for a Contact|Yes|  
|Opportunity|Opportunity Lost for an Account||  
|Opportunity|Opportunity Lost for a Contact||  
|Account|New Account Created|Yes|  
|Contact|New Contact Created||  
|Competitor|New Competitor Created|Yes|  
  
 When you have [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] set up, keep these things in mind:  
  
-   All user posts (conversations) are stored in [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)], not in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)].  
  
-   All system posts are stored in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)].  
  
-   If the Post to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] Activity Stream rule (or posttoyammer attribute) is set to True in Post Rules Configuration, that activity will post to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)].  
  
## Additional considerations  
  
### When connecting Dynamics 365 with a federated Yammer  
 If you have configured [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] to use single sign-on, you’ll need to generate and use a temporary password to connect [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)].  
  
1.  Sign in to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] with the single sign-on credentials.  
  
2.  Choose **More commands (…)** > **Apps**  
  
3.  Scroll to the bottom of the page to the **All Apps** section.  
  
4.  Choose the **[!INCLUDE[pn_yammer](../../includes/pn-yammer.md)]** tab, and then choose an app like [!INCLUDE[pn_windows_phone](../../includes/pn-windows-phone.md)]. The app must support generating a temporary password.  
  
5.  Complete the process to obtain a temporary user name and password.  
  
6.  Use the temporary user name and password to complete the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] connection configuration.  
  
### Add Yammer sites to the browser as trusted  
 Add your Yammer sites to your browser as trusted. For example, for Dynamics 365 (online), add the following:  
  
-   https://*.crm.dynamics.com  
  
-   https://*.yammer.com  
  
-   https://*.assets-yammer.com  
  
## Privacy notice  
[!INCLUDE[cc_privacy_crm_gcc_yammer_configuration](../../includes/cc-privacy-crm-gcc-yammer-configuration.md)]
  
### See also  
 [Collaborate and communicate with Yammer](https://docs.microsoft.com/dynamics365/customer-engagement/basics/collaborate-communicate-with-yammer)   
 [Visit the Yammer website](http://go.microsoft.com/fwlink/p/?LinkID=272440)
