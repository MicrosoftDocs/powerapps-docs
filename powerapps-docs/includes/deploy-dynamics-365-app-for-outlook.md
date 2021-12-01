---
title: "Deploy Dynamics 365 App for Outlook | MicrosoftDocs"
ms.custom: ""
ms.date: "2017-04-20"
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 09736e14-e744-48ca-a755-1b05bb55340e
caps.latest.revision: 39
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Deploy Dynamics 365 App for Outlook
People can use [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)] to tap the power of [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] while using  [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] on the desktop, web, or tablet. For example, view information about email or appointment recipients, or link an [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] email or appointment  to a [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] record such as an opportunity, account, or case. To learn more about what [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)] offers, see the [Dynamics 365 App for Outlook User's Guide](https://go.microsoft.com/fwlink/p/?LinkID=613099).  
  
> [!IMPORTANT]
>  [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] isn’t the same thing as [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)]. As of the [!INCLUDE[pn_crm_8_2_0_both](../includes/pn-crm-8-2-0-both.md)], [!INCLUDE[pn_ms_dyn_crm_app_for_outlook](../includes/pn-ms-dyn-crm-app-for-outlook.md)] paired with [!INCLUDE[cc_server_side_synch](../includes/cc-server-side-synch.md)] is the preferred way to integrate [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] with   [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)]. **Note that tracking activities is not supported when  [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] and [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] are used together by the same user.** For information on the  [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] add-in, see the [Dynamics 365 for Outlook User’s Guide](https://go.microsoft.com/fwlink/p/?LinkID=524751).  
>   
>  [Delegated users](https://support.office.com/article/Allow-someone-else-to-manage-your-mail-and-calendar-9684B670-7588-4EEA-8717-9E5799047540) can not use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] to track emails. We suggest using [folder-level tracking or automatic tracking](https://www.microsoft.com/dynamics/crm-customer-center/overview-of-tracking-records-in-dynamics-365-for-outlook.aspx) for delegated users.  
  
<a name="BKMK_Compare"></a>   
## Comparing Dynamics 365 App for Outlook with Dynamics 365 for Outlook  
 The following table compares [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] features with [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] (also known as the [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] client or add-in) as of the [!INCLUDE[pn_crm_8_2_0_both](../includes/pn-crm-8-2-0-both.md)].  
  
||||  
|-|-|-|  
|**Feature**|**[!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)]**|**[!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)]**|  
|Track and set regarding for email|Yes|Yes|  
|Track and set regarding for appointments|Yes|Yes|  
|Track and set regarding for contacts|Yes|Yes|  
|Track and set regarding for tasks|No|Yes|  
|One click set regarding|Yes|No|  
|Shows recipients' summary|Yes|No|  
|Shows the regarding record summary in the email/appointment|Yes|No|  
|Works with [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)]|Yes|No|  
|Works with [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] desktop|Yes|Yes|  
|Works with [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] for the Mac|Yes|No|  
|Works with phones|Yes|No|  
|Open and create [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] record directly|Yes|Yes|  
|Apply custom forms and business logic|Yes|Yes|  
|Work offline|No|Yes|  
|Apply email templates|Yes|Yes|  
|Apply sales literature|Yes|Yes|  
|Apply knowledge articles|Yes|Yes|  
|Ability to monitor emails after sending|Yes|No|  
|Sort, filter, format, group, and categorize views|No|Yes|  
|Create Word mail-merge documents|No|Yes|  
|Control field synchronization|No|Yes|  
  
<a name="BKMK_Requirements"></a>   
## Requirements  
 The following are required to use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)]:  
  
-   [!INCLUDE[pn_crm_online_2016_update](../includes/pn-crm-online-2016-update.md)], or [!INCLUDE[pn_crm_8_2_0_both](../includes/pn-crm-8-2-0-both.md)]  
  
-   Synchronization of incoming email through server-side synchronization. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)][Set up server-side synchronization of email, appointments, contacts, and tasks](../Topic/Set%20up%20server-side%20synchronization%20of%20email,%20appointments,%20contacts,%20and%20tasks.md)  
  
-   Required privileges as described below  
  
> [!NOTE]
>  Supported configurations and requirements for [!INCLUDE[pn_dyn_365](../includes/pn-dyn-365.md)] features are listed throughout our documentation. Specific configurations not documented should be  considered unsupported.  
  
### Required privileges  
 [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] provides access to [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] through the  **Use Dynamics 365 App for Outlook** privilege. If a user doesn’t have this privilege, they’ll receive the following error:  
  
> “You haven't been authorized to use this app. Check with your system administrator to update your settings.”  
  
 Users must also have read/write privileges for the following entities.  
  
 Business Management tab:  
  
-   **Mailbox**  
  
 Customization tab:  
  
-   **Entity**  
  
-   **Field**  
  
-   **Relationship**  
  
-   **System Application Metadata**  
  
-   **System Form**  
  
-   **User Application Metadata**  
  
-   **View**  
  
##### Set the privileges for a security role  
  
1.  [!INCLUDE[proc_settings_security](../includes/proc-settings-security.md)]  
  
2.  Click **Security Roles**.  
  
3.  Choose a security role, and then click the **Business Management** tab.  
  
4.  In the **Entity** section, review the **Mailbox** privileges settings. The security role should have User or higher settings.  
  
5.  In the **Privacy Related Privileges** section, verify that **Use Dynamics 365 App for Outlook** is set to **Organization**. If not, click **Use Dynamics 365 App for Outlook**.  
  
### Supported configurations with Microsoft Exchange  
 As of the [!INCLUDE[pn_crm_8_2_0_both](../includes/pn-crm-8-2-0-both.md)] you can use the app with any combination of [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] or [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-op-edition.md)] and [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)] or [!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises), including hybrid configurations. This means you can use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] in any of the following configurations:  
  
|||  
|-|-|  
|[!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]|[!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)]|  
|[!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)]|[!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises)|  
|[!INCLUDE[pn_crm_op_edition](../includes/pn-crm-op-edition.md)]|[!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] (on-premises)|  
|[!INCLUDE[pn_crm_op_edition](../includes/pn-crm-op-edition.md)]|[!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)]|  
  
> [!NOTE]
>  If you use [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-op-edition.md)], you'll need to authenticate with IFD authentication as described below.  
  
### Supported browsers for Outlook on the web  
 You can use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] with [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)] on the following browsers:  
  
-   [!INCLUDE[pn_IE_10](../includes/pn-ie-10.md)], [!INCLUDE[pn_ie_11](../includes/pn-ie-11.md)], or [!INCLUDE[pn_microsoft_edge](../includes/pn-microsoft-edge.md)]  
  
     The following configuration is supported:  
  
    -   Protected Mode is enabled for **Internet** security zone. To enable Protected Mode: in IE 10 or 11, go to **Tools** > **Internet options** > **Security tab** > **Internet**.  
  
    -   Protected Mode is enabled for **Local intranet**  security zone. To enable Protected Mode: in IE 10 or 11, go to **Tools** > **Internet options** > **Security tab** > **Local Internet**.  
  
    -   Your [!INCLUDE[pn_dyn_365](../includes/pn-dyn-365.md)] URL is in the **Local intranet** security zone list of trusted websites. In IE 10 or 11, go to **Tools** > **Internet options** > **Security tab** > **Local intranet** > **Sites** > **Advanced**.  
  
-   [!INCLUDE[tn_Google_Chrome](../includes/tn-google-chrome.md)] (latest version) on [!INCLUDE[pn_ms_Windows_short](../includes/pn-ms-windows-short.md)]  
  
-   [!INCLUDE[tn_Firefox](../includes/tn-firefox.md)] (latest version) on [!INCLUDE[pn_ms_Windows_short](../includes/pn-ms-windows-short.md)]  
  
-   [!INCLUDE[tn_apple](../includes/tn-apple.md)] [!INCLUDE[tn_Safari](../includes/tn-safari.md)] (version 9 or version 10) on Mac or on OSX  
  
### Supported operating systems for Outlook on the desktop  
 You can use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] on these versions of [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] for the desktop:  
  
-   [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] 2013 and [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] 2016.  
  
-   [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] for Mac*.  
  
     *[!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] version 15.0.847.32 or greater is required.  
  
### Supported mobile devices  
 You can use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] with [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)] in the mobile browser on any of the following phones and operating systems:  
  
-   [!INCLUDE[tn_apple](../includes/tn-apple.md)] [!INCLUDE[tn_iphone](../includes/tn-iphone.md)] devices running iOS version 8,  9, or 10.  
  
-   [!INCLUDE[tn_android](../includes/tn-android.md)] phones running [!INCLUDE[tn_android](../includes/tn-android.md)] 4.4 (KitKat) or 5.0 (Lollipop), 6 (Marshmallow), or 7 (Nougat).  
  
-   [!INCLUDE[pn_windows_phone](../includes/pn-windows-phone.md)] devices running [!INCLUDE[pn_windows_8_1](../includes/pn-windows-8-1.md)] or [!INCLUDE[pn_windows_10](../includes/pn-windows-10.md)].  
  
### Supported clients per feature  
 The [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] features supported depend on the client you're running. The following table summarizes which features are supported for each client/configuration of [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] and [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)].  
  
 ![Clients supported for each Dynamics 365 App for Outlook feature.](media/clients-supported-for-each-dynamics-365-app-for-outlook-feature.png "Clients supported for each Dynamics 365 App for Outlook feature")  
  
 (1)  [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)] supports [!INCLUDE[pn_IE_10](../includes/pn-ie-10.md)], [!INCLUDE[pn_ie_11](../includes/pn-ie-11.md)], [!INCLUDE[pn_microsoft_edge](../includes/pn-microsoft-edge.md)], [!INCLUDE[tn_Safari](../includes/tn-safari.md)] 9, [!INCLUDE[tn_Safari](../includes/tn-safari.md)] 10, [!INCLUDE[tn_Firefox](../includes/tn-firefox.md)], and [!INCLUDE[tn_chrome](../includes/tn-chrome.md)].  
  
 (2)  Mobile [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)] supports [!INCLUDE[pn_windows_8_1](../includes/pn-windows-8-1.md)], [!INCLUDE[pn_windows_10](../includes/pn-windows-10.md)], [!INCLUDE[tn_ios](../includes/tn-ios.md)] 8, [!INCLUDE[tn_ios](../includes/tn-ios.md)] 9, [!INCLUDE[tn_ios](../includes/tn-ios.md)] 10, [!INCLUDE[tn_android](../includes/tn-android.md)] KitKat (4.4), [!INCLUDE[tn_android](../includes/tn-android.md)] Lollipop, [!INCLUDE[tn_android](../includes/tn-android.md)] Marshmallow, and [!INCLUDE[tn_android](../includes/tn-android.md)] Nougat.  
  
 (3)  Tracking email in compose mode and tracking appointments requires [!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] 2013 CU14 or [!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)] 2016.  
  
 (4)  Tracking contacts is supported only on [!INCLUDE[pn_Exchange_Server_short](../includes/pn-exchange-server-short.md)]2016 CU3 and [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] 2016 16.0.6741.1000 and later.  
  
 (5)  Adding email templates, Knowledge Management articles, and sales literature is not supported in Mobile [!INCLUDE[pn_outlook_web_app](../includes/pn-outlook-web-app.md)].  
  
 (6)  Supported only on [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] 2016 16.0.7426.1049 and later.  
  
 (7)  Supported only on 16.0.6741.1000 and later.  
  
> [!NOTE]
>  Tablets are not supported at this time (coming CY2017).  
  
 [Read more details about supported clients in this blog: Dynamics 365 App for Outlook Support Matrix](https://blogs.msdn.microsoft.com/crm/2016/12/13/dynamics-365-app-for-outlook-support-matrix/)  
  
### Supported servers  
 The [server requirements for using Office Add-ins](https://dev.office.com/docs/add-ins/overview/requirements-for-running-office-add-ins) are [!INCLUDE[pn_Exchange_Server_2013_short](../includes/pn-exchange-server-2013-short.md)], [!INCLUDE[pn_exchange_server_2016_short](../includes/pn-exchange-server-2016-short.md)], or [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)].  
  
### Supported languages  
 [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] supports the following languages:  
  
||||  
|-|-|-|  
|Bulgarian (Bulgaria) - 1026|Hindi (India) - 1081|Portuguese (Portugal) - 2070|  
|Chinese (People's Republic of China) - 2052|Hungarian - 1038|Romanian - 1048|  
|Chinese (Taiwan) - 1028|Indonesian - 1057|Russian - 1049|  
|Croatian (Croatia) - 1050|Italian - 1040|Serbian - 2074|  
|Czech (Czech Republic) - 1029|Japanese - 1041|Slovak - 1051|  
|Danish - 1030|Kazakh - 1087|Slovenian - 1060|  
|Dutch - 1043|Korean - 1042|Spanish - 3082|  
|English - 1033|Latvian - 1062|Swedish - 1053|  
|Estonian - 1061|Lithuanian - 1063|Thai - 1054|  
|Finnish - 1035|Malaysian - 1086|Turkish - 1055|  
|French - 1036|Norwegian - 1044|Ukrainian - 1058|  
|German - 1031|Polish - 1045|Vietnamese - 1066|  
|Greek - 1032|Portuguese (Brazil) - 1046||  
  
<a name="BKMK_Deploy"></a>   
## Deploy Dynamics 365 App for Outlook  
 After setting up [!INCLUDE[cc_server_side_synch](../includes/cc-server-side-synch.md)] and setting the required privileges, you can push [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)] to some or all users, or you can have users install it themselves as needed.  
  
> [!NOTE]
>  If you're on [!INCLUDE[pn_dyn_365_op](../includes/pn-dyn-365-op.md)], see the section below:  [To deploy to Dynamics 365 on-premises users](#BKMK_DeployOnprem)  
  
#### To push the app to users  
  
1.  Go to **Settings** >  **Dynamics 365 App for Outlook**.  
  
2.  In the **Getting Started with Dynamics 365 App for Outlook** screen, under **Add for Eligible Users** (you may have to click **Settings** if you’re opening this screen for the second or subsequent time), select the **Automatically add the app to [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)]** check box if you want to have users get the app automatically. If a user has the required privileges and email is synchronized through [!INCLUDE[cc_server_side_synch](../includes/cc-server-side-synch.md)], you won’t have to do anything more to push the app to them. For example, if you add the required privileges to the Salesperson role, and then assign this role to a new user, they’ll automatically get the app.  
  
3.  Do one of the following:  
  
    -   To push the app to all eligible users, click **Add App for All Eligible Users**.  
  
    -   To push the app to certain users, select those users in the list, and then click **Add App to Outlook**.  
  
    > [!TIP]
    >  If the list shows that a user is pending or hasn’t been added, you can click the **Learn more** link next to the user to find more information about status.  
  
4.  When you’re done, click **Save**.  
  
#### To have users install the app themselves  
  
1.  Users click the **Settings** button ![Settings button.](media/mp-ua-r16-settings.png "Settings button"), and then click **Apps for Dynamics 365**.  
  
2.  In the **Apps for Dynamics 365** screen, under **[!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)]**, users click **Add app to [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)]**.  
  
> [!NOTE]
>  Users can also disable or remove the add-in themselves, if needed. For more information, see the [Dynamics 365 App for Outlook User’s Guide](https://go.microsoft.com/fwlink/p/?LinkID=613099).  
  
<a name="BKMK_DeployOnprem"></a>   
## To deploy to Dynamics 365 on-premises users  
 Follow these steps if you're using Dynamics 365 on-premises.  
  
-   Configure your Dynamics 365 server for Internet-facing deployment. See [Configure IFD for Microsoft Dynamics 365](https://technet.microsoft.com/library/dn609803.aspx).  
  
-   If you're connecting to Exchange on-premises, configure the OAuth provider and register client apps. See [Configure Windows Server 2012 R2 for Dynamics 365 applications that use OAuth](https://technet.microsoft.com/library/hh699726.aspx).  
  
<a name="BKMK_Troubleshoot"></a>   
## Troubleshooting installation problems  
 If you or your users have trouble installing [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)], it may be because their [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox is currently linked to another [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] organization. An [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox (email address) can only synchronize appointments, contacts, and tasks with one organization, and a user that belongs to that organization can only synchronize appointments, contacts, and tasks with one [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] mailbox.  You can overwrite the setting stored in [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] if you want to change the primary synchronizing organization. For more information, see [this KB article.](https://support.microsoft.com/en-gb/help/3211627/incomingemailrejected-error-when-attempting-to-install-dynamics-365-app-for-outlook)  
  
<a name="BKMK_Explore"></a>   
## Explore the User’s Guide and train your users  
 To learn how to use [!INCLUDE[pn_crm_app_for_outlook_short](../includes/pn-crm-app-for-outlook-short.md)], [see the Dynamics 365 App for Outlook User’s Guide](https://go.microsoft.com/fwlink/p/?LinkID=613099).  
  
 ![Dynamics 365 App for Outlook User's Guide page.](media/dynamics-365-app-for-outlook-user-s-guide-page.png "Dynamics 365 App for Outlook User's Guide page")  
  
## See Also  
 [Dynamics 365 App for Outlook User's Guide](https://go.microsoft.com/fwlink/p/?LinkID=613099)   
 [Read more details about supported clients in this blog: Dynamics 365 App for Outlook Support Matrix](https://blogs.msdn.microsoft.com/crm/2016/12/13/dynamics-365-app-for-outlook-support-matrix/)   
 [Set up server-side synchronization of email, appointments, contacts, and tasks](../Topic/Set%20up%20server-side%20synchronization%20of%20email,%20appointments,%20contacts,%20and%20tasks.md)   
 [Add users, licenses, and security roles](https://msdn.microsoft.com/23612155-f92d-4871-a109-186419d5c19d)   
 [Add interoperation features to Microsoft Dynamics 365 (online)](../DocSets/CRMIGv9_Admin/Toc/Add%20interoperation%20features%20to%20Microsoft%20Dynamics%20365%20\(online\).md)