---
title: "Deploy Dynamics 365 App for Outlook (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 03/22/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 09736e14-e744-48ca-a755-1b05bb55340e
caps.latest.revision: 39
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
tags:
 - "MigrationHO"
---
# Deploy Dynamics 365 App for Outlook  

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

> [!IMPORTANT]
> The latest release of [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)], works with [!INCLUDE [pn-crm-9-0-0-online](../includes/pn-crm-9-0-0-online.md)] or later only. 
>
> [Delegated users](https://support.office.com/article/Allow-someone-else-to-manage-your-mail-and-calendar-9684B670-7588-4EEA-8717-9E5799047540) can not use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] to track emails. 

People can use [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)] to tap the power of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] while using [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] on the desktop, web, or tablet. For example, view information about email or appointment recipients, or link an [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] email or appointment  to a [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] record such as an opportunity, account, or case. To learn more about what [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)] offers, see the [Dynamics 365 App for Outlook User Guide](https://docs.microsoft.com/dynamics365/customer-engagement//outlook-app/dynamics-365-app-outlook-user-s-guide).  

## Known issues

For known issues with this version of [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)], see the [Dynamics 365 Customer Engagement Readme](https://docs.microsoft.com/dynamics365/customer-engagement/admin/readme-9).

There are two ways to install [!INCLUDE [pn-ms-office](../includes/pn-ms-office.md)]: using a Windows Installer (MSI) version or a Click-to-Run (C2R) version of [!INCLUDE [pn-office-shortest](../includes/pn-office-shortest.md)]. You might have issues accessing [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] in the Add-ins area of [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] if you don't have the necessary updates for your installation version. For more information, see [Issue when trying to access Dynamics 365 within the Add-ins area of Outlook](https://support.microsoft.com/help/3211586/error-message-0x8006ffff-occurs-when-you-access-dynamics-365-within-th).

## Requirements  
 The following are required to use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)]:  
  
- [!INCLUDE [pn-crm-9-0-0-online](../includes/pn-crm-9-0-0-online.md)] or later
  
- Synchronization of incoming email through server-side synchronization. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Set up server-side synchronization of email, appointments, contacts, and tasks](https://docs.microsoft.com/dynamics365/customer-engagement/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks)  
  
- [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] is an [!INCLUDE [pn-outlook](../includes/pn-outlook.md)] add-in that uses [!INCLUDE [pn-exchange-web-services-ews](../includes/pn-exchange-web-services-ews.md)] to interact with [!INCLUDE [pn-microsoft-exchange](../includes/pn-microsoft-exchange.md)]. This requires OAuth be enabled on [!INCLUDE [pn-microsoft-exchange](../includes/pn-microsoft-exchange.md)]. For more information regarding this dependency, see [Authentication and permission considerations for the makeEwsRequestAsync method](https://docs.microsoft.com/outlook/add-ins/web-services#authentication-and-permission-considerations-for-the-makeewsrequestasync-method).

- Required privileges as described below  
  
> [!NOTE]
>  Supported configurations and requirements for [!INCLUDE[pn_dyn_365](../includes/pn-dyn-365.md)] features are listed throughout our documentation. Specific configurations not documented should be  considered unsupported.  
  
### Required privileges 
[!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] provides access to [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] through the **Use Dynamics 365 App for Outlook** privilege. If a user doesn’t have this privilege, they’ll receive the following error:  
  
“You haven't been authorized to use this app. Check with your system administrator to update your settings.”  
  
Users must also have read/write privileges for the following entities:  
  
 Business Management tab:  
  
- **Mailbox**  
  
Customization tab:  
  
- **Entity**  
  
- **Field**  
  
- **Relationship**  
  
- **System Application Metadata**  
  
- **System Form**  
  
- **User Application Metadata**  
  
- **View**  
  
#### Set the privileges for a security role  

For example, to set privileges for the Mailbox entity:
  
1. [!INCLUDE[proc_settings_security](../includes/proc-settings-security.md)]  
  
2.  Click **Security Roles**.  
  
3.  Choose a security role, and then click the **Business Management** tab.  
  
4.  In the **Entity** section, review the **Mailbox** privileges settings. The security role should have User or higher settings.  
  
5.  In the **Privacy Related Privileges** section, verify that **Use Dynamics 365 App for Outlook** is set to **Organization**. If not, click **Use Dynamics 365 App for Outlook**.  
  
### Supported configurations with Microsoft Exchange  
 As of the [!INCLUDE[pn_crm_8_2_0_both](../includes/pn-crm-8-2-0-both.md)] you can use the app with any combination of [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] or [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)] and [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises), including hybrid configurations. This means you can use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] in any of the following configurations:  
  
|||  
|-|-|  
|[!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]|[!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)]|  
|[!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]|[!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises), version 15.0.1236.3.32 (Cumulative Update 14 for Exchange Server 2013) or greater|  
|[!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)]|[!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises), version 15.0.1236.3.32 (Cumulative Update 14 for Exchange Server 2013) or greater|  
|[!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)]|[!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)]|  
  
<!--
> [!NOTE]
>  If you use [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)], you'll need to authenticate with IFD authentication as described below.  
-->
  
### Support summary

#### Windows desktop
- Outlook 2013 (desktop client)*
- Outlook 2016 (desktop client)
- Outlook on the web on Internet Explorer 11, Microsoft Edge, and Chrome

*[Support for 2013 versions of Office 365 ProPlus ended February 28, 2017.](https://support.microsoft.com/help/3199744/support-for-the-2013-versions-of-office-365-proplus-ends-february-28)

#### Macintosh
- Outlook 2016 for Mac

#### iPhone
- Apple iPhone 6S or higher, running iOS version 8 or higher.

#### Android phones
- Outlook for Android, on Android phones running Android 4.4 (KitKat), 5.0 (Lollipop), 6.0 (Marshmallow), or 7.0 (Nougat).

#### Android tablets
- Not supported

#### Windows phones and tablets
- Not supported

Check back later for updates on supported platforms.

### Feature support per client

||||||
|-|-|-|-|-|
| |Received email<br />(view information and track)|Compose email<br />(view information, track, <br />and add templates, <br />knowledge base articles, <br />and sales literature)|Appointments and meetings <br />(view information and track)|Contacts<br />(view information and track)|
|[!INCLUDE [pn-outlook-2016](../includes/pn-outlook-2016.md)] (desktop client)|O and M|O and M<sup>1</sup> |O and M<sup>1</sup> |O<sup>3</sup>  and M<sup>2</sup> |
|[!INCLUDE [pn-ms-outlook-2013-short](../includes/pn-ms-outlook-2013-short.md)]  (desktop client)|O and M|O and M<sup>1</sup> |O and M<sup>1</sup> ||
|Outlook for Mac (desktop client)|O and M||||
|[!INCLUDE [pn-outlook-web-app](../includes/pn-outlook-web-app.md)] (OWA)|O and M|O and M<sup>1</sup> |O and M<sup>1</sup> ||
|Mobile Outlook app<sup>4</sup>|O||||

(O)nline: [!INCLUDE [pn-crm-online](../includes/pn-crm-online.md)], [!INCLUDE [pn-exchange-online](../includes/pn-exchange-online.md)] <br />
(M)ixed: [!INCLUDE [pn-crm-online](../includes/pn-crm-online.md)], Exchange Server 2013/2016

Note: Dynamics 365, version 9 is not available on-premises.

(1) Tracking email in compose mode and tracking appointments requires Exchange Server 2013 CU14 or [!INCLUDE [pn-exchange-server-2016-short](../includes/pn-exchange-server-2016-short.md)]. <br />
(2) Tracking contacts is supported only on Exchange Server 2016 CU3 and Outlook 2016 16.0.6741.1000 or later. <br />
(3) Supported only on Outlook 2016 16.0.7426.1049 or later.<br />
(4) Supported on iPhones 6S or higher, with iOS 8 or higher.


 
### Supported servers  
 The [server requirements for using Office Add-ins](https://dev.office.com/docs/add-ins/overview/requirements-for-running-office-add-ins) are [!INCLUDE[pn_Exchange_Server_2013_short](../includes/pn-exchange-server-2013-short.md)], [!INCLUDE[pn_exchange_server_2016_short](../includes/pn-exchange-server-2016-short.md)], or [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)].  
  
### Supported languages  
[!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] supports the following languages:  

||||  
|-|-|-|  
|Bulgarian (Bulgaria) - 1026|Hebrew - 1037|Portuguese (Brazil) - 1046|  
|Chinese (People's Republic of China) - 2052|Hindi (India) - 1081|Portuguese (Portugal) - 2070|  
|Chinese (Taiwan) - 1028|Hungarian - 1038|Romanian - 1048|  
|Croatian (Croatia) - 1050|Indonesian - 1057|Russian - 1049|  
|Czech (Czech Republic) - 1029|Italian - 1040|Serbian - 2074|  
|Danish - 1030|Japanese - 1041|Slovak - 1051|  
|Dutch - 1043|Kazakh - 1087|Slovenian - 1060|  
|English - 1033|Korean - 1042|Spanish - 3082|  
|Estonian - 1061|Latvian - 1062|Swedish - 1053|  
|Finnish - 1035|Lithuanian - 1063|Thai - 1054|  
|French - 1036|Malaysian - 1086|Turkish - 1055|  
|German - 1031|Norwegian - 1044|Ukrainian - 1058|  
|Greek - 1032|Polish - 1045|Vietnamese - 1066|  

<a name="BKMK_Deploy"></a>   

## Deploy Dynamics 365 App for Outlook  
 After setting up [!INCLUDE[cc_server_side_synch](../includes/cc-server-side-synch.md)] and setting the required privileges, you can push [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] to some or all users, or you can have users install it themselves as needed.  
  
<!--
> [!NOTE]
>  If you're on [!INCLUDE[pn_dyn_365_op](../includes/pn-dyn-365-op.md)], see the section below:  [To deploy to Dynamics 365 on-premises users](#BKMK_DeployOnprem)  
--> 

### Enable

1. [!INCLUDE[proc_permissions_system_admin_and_customizer](../includes/proc-permissions-system-admin-and-customizer.md)]  
  
    Check your security role  
  
    - [!INCLUDE[proc_follow_steps_in_link](../includes/proc-follow-steps-in-link.md)]  
  
    - [!INCLUDE[proc_dont_have_correct_permissions](../includes/proc-dont-have-correct-permissions.md)]  
  
2. [!INCLUDE[proc_settings_administration](../includes/proc-settings-administration.md)]  
  
3. Choose **System Settings** > **Previews** tab.  

4. For **I have read and agree to the license terms**, select **Yes**.

5. For **Enable Dynamics 365 App for Outlook**, select **Yes**.

#### To push the app to users  
  
1.  Go to **Settings** > **Dynamics 365 App for Outlook**.  
  
2.  In the **Getting Started with Dynamics 365 App for Outlook** screen, under **Add for Eligible Users** (you may have to click **Settings** if you’re opening this screen for the second or subsequent time), select the **Automatically add the app to [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)]** check box if you want to have users get the app automatically. If a user has the required privileges and email is synchronized through [!INCLUDE[cc_server_side_synch](../includes/cc-server-side-synch.md)], you won’t have to do anything more to push the app to them. For example, if you add the required privileges to the Salesperson role, and then assign this role to a new user, they’ll automatically get the app.  
  
3.  Do one of the following:  
  
    -   To push the app to all eligible users, click **Add App for All Eligible Users**.  
  
    -   To push the app to certain users, select those users in the list, and then click **Add App to Outlook**.  
  
    > [!TIP]
    >  If the list shows that a user is pending or hasn’t been added, you can click the **Learn more** link next to the user to find more information about status.  
  
4.  When you’re done, click **Save**.  
  
#### To have users install the app themselves  
  
1.  Users click the **Settings** button ![Settings button](media/mp-ua-r16-settings.png "Settings button"), and then click **Apps for Dynamics 365**.  
  
2.  In the **Apps for Dynamics 365** screen, under **[!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)]**, users click **Add app to [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)]**.  
  
> [!NOTE]
>  Users can also disable or remove the add-in themselves, if needed. For more information, see the [Dynamics 365 App for Outlook User’s Guide](https://docs.microsoft.com/dynamics365/customer-engagement//outlook-app/dynamics-365-app-outlook-user-s-guide).  

<!--    
<a name="BKMK_DeployOnprem"></a>   

## To deploy to Dynamics 365 on-premises users  
 Follow these steps if you're using Dynamics 365 on-premises.  
  
-   Configure your Dynamics 365 server for Internet-facing deployment. See [Configure IFD for Microsoft Dynamics 365](https://technet.microsoft.com/library/dn609803.aspx).  


-   If you're connecting to Exchange on-premises, configure the OAuth provider and register client apps. See [Configure Windows Server 2012 R2 for Dynamics 365 applications that use OAuth](https://technet.microsoft.com/library/hh699726.aspx).  
-->
  
<a name="BKMK_Troubleshoot"></a>   

## Troubleshooting installation problems  

1. If you don't see [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] when you click the **Settings** button ![Settings button](media/mp-ua-r16-settings.png "Settings button"), check that you've enabled the feature. See [Enable](#enable).

2. If you or your users have trouble installing [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)], it may be because their [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox is currently linked to another [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] organization. An [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox (email address) can only synchronize appointments, contacts, and tasks with one organization, and a user that belongs to that organization can only synchronize appointments, contacts, and tasks with one [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox.  You can overwrite the setting stored in [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] if you want to change the primary synchronizing organization. For more information, see [this KB article.](https://support.microsoft.com/en-gb/help/3211627/incomingemailrejected-error-when-attempting-to-install-dynamics-365-app-for-outlook)
  
<a name="BKMK_Explore"></a>   

## Explore the User’s Guide and train your users  
 To learn how to use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)], see the [Dynamics 365 App for Outlook User’s Guide](https://docs.microsoft.com/dynamics365/customer-engagement//outlook-app/dynamics-365-app-outlook-user-s-guide).  
  
### See also  
 [Dynamics 365 App for Outlook User Guide](https://docs.microsoft.com/dynamics365/customer-engagement//outlook-app/dynamics-365-app-outlook-user-s-guide)   
 [Read more details about supported clients in this blog: Dynamics 365 App for Outlook Support Matrix](https://blogs.msdn.microsoft.com/crm/2016/12/13/dynamics-365-app-for-outlook-support-matrix/)   
 [Set up server-side synchronization of email, appointments, contacts, and tasks](https://docs.microsoft.com/dynamics365/customer-engagement/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks)   


<!-- 2. If you see the message "Your account's email settings aren't configured to use this app", you need to [Set up server-side synchronization of email, appointments, contacts, and tasks](../admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks.md).

   ![App for Outlook settings not configured](media/app-outlook-settings-not-configured.png)
-->
