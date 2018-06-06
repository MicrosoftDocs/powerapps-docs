---
title: "Set up Dynamics 365 for phones and Dynamics 365 for tablets | MicrosoftDocs"
ms.custom: ""
ms.date: 01/22/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
author: "jimholtz"
ms.assetid: 7a28ff46-558b-47c5-9c99-073fd6f66844
caps.latest.revision: 141
ms.author: "jimholtz"
manager: "brycho"
---
# Setup overview for mobile apps

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]

Your users can access their [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] data while they're out in the field by using either of the following apps:  
  
- **[!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)]**: With [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)], you can design your information architecture once and the customizations will automatically flow to all form factors. Much is shared with [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
 ![Video symbol](../media/video-thumbnail-4.png "Video symbol") [Video: Customize the Dynamics 365 mobile app (1:51)](http://go.microsoft.com/fwlink/p/?LinkID=836829)  
  
- **[!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]**: With the same basic features as [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)], tablet users will appreciate the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] experience optimized for a larger screen.  
    
<a name="BKMK_GetStartedTablets"></a>   
## Get started with [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
  
### Requirements  
 For hardware and software requirements for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)], see [Support for Dynamics 365 for phones and Dynamics 365 for tablets](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/support-phones-tablets).  
  
### Required privileges  
 [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] uses a security privilege, **Dynamics 365 for mobile**, to provide access to [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]. The privilege is pre-configured for Sales roles, but not other security roles, so you may want to add to other roles for your teams.  
  
 Follow these steps to check and assign the security privilege for a security role:  
  
1. [!INCLUDE[proc_settings_security](../../includes/proc-settings-security.md)]  
  
2.  Click **Security Roles**.  
  
3.  Choose a security role > **Business Management** tab.  
  
4.  In the **Privacy Related Privileges** section, verify that **Dynamics 365 for mobile** is set to **Organization**. If not, click **Dynamics 365 for mobile**.  
  
5.  Click **Save and Close** to save the changes to the security role.  
  
6.  Send an email to tablet-enabled users to let them know they can download the mobile app from the app store. Include the organization URL and sign-in information in the email.  
  
 This applies to new installations of [!INCLUDE[pn_CRM_Online](../../includes/pn-crm-online.md)], [!INCLUDE[pn_crmv6](../../includes/pn-crmv6.md)] or later. You can add or remove this privilege from custom or default security roles to meet your business needs. Users who do not have this privilege will see the following error:  
  
> You haven't been authorized to use this app. Check with your system administrator to update your settings.  
  
> [!NOTE]
> [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] includes the ability to audit user access. Audit events are logged if a user accesses your Dynamics 365 organization through [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]. However, there is not a new event type that indicates the access was through [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]. The audit login events would appear as **User Access via Web Services**.  
  
 In addition, particularly if you have created a custom security role, validate that these entities have **Read** permission.  
  
1. [!INCLUDE[proc_settings_security](../../includes/proc-settings-security.md)]  
  
2.  Click **Security Roles**.  
  
3.  Choose a security role > **Customization** tab. Verify that the **Read** permission is set for the following entities:  
  
    -   Custom Control  
  
    -   Custom Control Default Config  
  
    -   Custom Control Resource  
  
    -   System Application Metadata  
  
    -   System Form  
  
    -   User Application Metadata  
 
    -   View  
 
    -   App
  
4.  Choose a security role > **Business Management** tab. Verify that the **Read** permission is set for the following entity:  
  
    -   User Settings  
  
5.  Click **Save and Close** to save the changes to the security role.  
  
<a name="BKMK_UsersToDo"></a>   
## What users need to do  
 See this topic: [Dynamics 365 for phones and tablets User's Guide](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)  
  
### Install [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 [Install Dynamics 365 for tablets and phones](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)  
  
> [!TIP]
>  Be sure to provide users the URL and credentials they need to sign in.  
  
<a name="BKMK_AdminToDo"></a>   

## What admins need to do  
  
### Security privileges  
 [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] uses a security privilege, **Dynamics 365 for mobile**, to provide access to [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]. This privilege is pre-configured for Sales roles, but not other security roles, so you may want to add to other roles for your teams.  
  
### Enable dashboards for Dynamics 365 for phone and Dynamics 365 for tablet users  
 Multiple dashboards are available for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] users. After you set up standard or custom dashboards for mobile access, users can easily modify which dashboards appear and how they appear on their phones or tablets.  
  
1. [!INCLUDE[proc_settings_customization](../../includes/proc-settings-customization.md)]  
  
2.  Click **Customize the System**.  
  
3.  Under Components, click **Dashboards**.  
  
4.  Double-click or press and hold the dashboard you want to enable for phone or tablet access.  
  
5.  Click **Properties** > **Enable for mobile** > **OK**.  
  
6.  Click **Save**.  
  
 Show your users how to set and view the enabled dashboards on their phones or tablets. More information: [Get around in Dynamics 365 for phones and tablets](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)  
  
 You can assign security roles to a dashboard so the dashboard appears only to users with certain security roles. For example, to set who has access to the Sales Dashboard, click **Settings** > **Customizations** > **Customize the System** > **Components** > **Dashboards**, and then select   the **Sales Dashboard**. Then, click **Enable Security Roles**.  
  
### Update the registry on managed mobile devices  
 If your mobile devices are managed under the control of group policy, the following steps describe what you need to do.  
  
> [!CAUTION]
>  This task contains steps that tell you how to modify the registry. However, because serious problems may occur if you modify the registry incorrectly, it’s important that you follow these steps carefully. For added protection, back up the registry before you modify it. Then, you can restore the registry if a problem occurs. For more information about how to back up and restore the registry, open the following link to view the article in the Microsoft Knowledge Base: [How to back up and restore the registry in Windows](http://support.microsoft.com/kb/322756).  
  
1.  If you plan on using group policy to do a domain wide deployment of the registry change and your server is not running [!INCLUDE[pn_windows_server_2012_r2](../../includes/pn-windows-server-2012-r2.md)] or later, download and install the [Windows Server Administrative Templates](http://go.microsoft.com/fwlink/p/?LinkId=392790).  
  
2.  Open the Group Policy Management Editor.  
  
3.  Select an existing policy or create a new policy.  
  
4.  Go to **Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **App runtime** and set **Turn on dynamic Content URI Rules for Windows store apps** to **Enabled**.  
  
5.  Click **Show**, and then add the URL for your organization. For example, https://orgname.contoso.com.  
  
6.  Close the group policy editor and save your changes.  
  
 [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [How to update links to external web pages for an enterprise environment](http://go.microsoft.com/fwlink/p/?LinkId=392788) and [Group Policy](https://technet.microsoft.com/windowsserver/bb310732.aspx)  
  
### Update the registry on unmanaged mobile devices using a script  
 If your mobile devices are unmanaged, see the following sample [!INCLUDE[pn_PowerShell_short](../../includes/pn-powershell-short.md)] script that shows how to change the registry on each [!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)] or later device.  
  
```powershell  
  
# *********************************************************  
#   
#    Copyright (c) Microsoft. All rights reserved.  
#    This code is licensed under the Microsoft Limited Public License.  
#    THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF  
#    ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY  
#    IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR  
#    PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.  
#   
# *********************************************************  
param([string]$admin)  
  
#Force PowerShell to relaunch in Admin mode  
if($admin -ne 'LaunchingAsAdminNow')   
{  
    $Args = '-ExecutionPolicy Unrestricted -file "' + ((Get-Variable MyInvocation).Value.MyCommand.Path) + '" LaunchingAsAdminNow'  
    $AdminProcess = Start-Process "$PsHome\PowerShell.exe" -Verb RunAs -ArgumentList $Args -PassThru  
}  
else  
{  
    # Create Packages key if it does not exist  
    $packages=Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages -ErrorAction SilentlyContinue  
    if($packages -eq $null)  
    { New-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies -Name Packages}  
  
    # Create Applications key if it does not exist  
    $apps=Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications -ErrorAction SilentlyContinue  
    if($apps -eq $null)  
    { New-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages -Name Applications}  
  
    # Add or overwrite EnableDynamicContentUriRules value to 1  
    New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications -Name EnableDynamicContentUriRules -PropertyType DWord -Value 1 -force  
  
    # Create ContentUriRules key if it does not exist  
    $rules=Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications\ContentUriRules -ErrorAction SilentlyContinue  
    if($rules -eq $null)  
    {New-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications -Name ContentUriRules}  
  
    # Prompt user for the domain uri  
    $domainname = Read-Host 'Please provide the domain uri that you want to add to the allow list(such as https://*.contoso.com:444)'  
  
    # Add uri to the allow list under ContentUriRules  
    $urls=Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications\ContentUriRules -ErrorAction SilentlyContinue  
    New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Packages\Applications\ContentUriRules -Name ($urls.ValueCount+1) -PropertyType String -Value $domainname -force  
}  
  
```  
  
### Update the registry on unmanaged mobile devices using the Registry Editor  
 If your mobile devices are unmanaged, you can also change the registry on each [!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)] or later device like this:  
  
1.  Start Registry Editor.  
  
2.  Before making changes to your registry, make a backup. Click **File** > **Export**, and then enter your settings.  
  
3.  Locate the following registry subkey: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\policies  
  
4.  Right-click or tap **policies**, point to **New**, and then click **Key**.  
  
5.  Type **Packages**, and then press **ENTER**.  
  
6.  Right-click or tap **Packages**, point to **New**, and then click **Key**.  
  
7.  Type **Applications**, and then save the text.  
  
8.  Right-click or tap **Applications**, point to **New**, and then click **DWORD (32-bit) Value**.  
  
9. Type `EnableDynamicContentUriRules` and then save the text.  
  
10. Right-click or tap **EnableDynamicContentUriRules**, and then click **Modify**.  
  
11. Type **1** in the **Value Data** box, and then click **OK**.  
  
12. Right-click or tap **Applications**, point to **New**, and then click **Key**.  
  
13. Type **ContentUriRules**, and then save the text.  
  
14. Right-click or tap **ContentUriRules**, point to **New**, and then click **String Value**.  
  
15. Type **1**, and then save the text.  
  
16. Right-click or tap **1**, and then click **Modify**.  
  
17. Type your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] organization’s URL in the **Value Data** box (for example, https://contoso.com), and then click **OK**.  
  
18. Exit Registry Editor.  
  
     Now you can point your users to the [!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)] app, so they can get the added functionality of the offline experience. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Install the Dynamics 365 for tablets app](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)  
  
<a name="BKMK_Configure"></a>   
## Configure [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
  
### Navigation bar  
 If an entity is enabled for **Dynamics 365 for mobile** and appears in the nav bar (sitemap) for the web application, it will also appear on the nav bar in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
 The [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] apps show the entities as a flat list in the same order as the sitemap in the web application. They ignore any groupings within web application areas. You can add an entity to multiple groups on the web application, but [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] display a flattened list and do not show any repeats. [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] apply your [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] security role, so you will not see an entity unless you have at least read access to that entity.  
  
 Custom entities use a fixed custom entity symbol.  
  
 ![Dynamics 365 for tablets nav bar](../media/dynamics-365-tablets-navigation-menu.png "Dynamics 365 for tablets nav bar")  
  
### Simple lists  
 The lists of records that appear on the Sales Dashboard and within a form appear as simple lists. These lists have a different appearance than the typical view of records. There are a few frequently used actions you can perform on a simple list.  
  
> [!NOTE]
>  Simple lists are not available in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)]. Instead use the command bar **…** and click **Select View** to change your view.  
  
-   Tap the list header to see the full list for the current view.  
  
-   Tap a list item to open the form for that item.  
  
-   Tap and hold an item to display the command bar.  
  
-   Tap the **New Item** button + to the right of the view name to create a new record of that type.  
  
 Some more things to note:  
  
-   You’ll see the **New Item** button +  to the right of the view name for any entity type that is read/write enabled for [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
-   Simple lists retrieve ten records at a time regardless of the **Records Per Page** setting in your **Personal Options** area of the web application. As you scroll to the bottom of the list, [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] displays additional records.  
  
 **Fields Displayed**  
  
 A typical view of records displays all columns in the view definition. A simple list displays the first few columns from the selected view. Simple lists are also capable of displaying images for each record if the entity is enabled to display images.  
  
 ![Dynamics 365 for tablets simple list](../media/x-microsoft-crm.png "Dynamics 365 for tablets simple list")  
  
 The number of fields you’ll see in the list is different depending on whether or not the entity is enabled for images. If it is, the image is the first thing to appear. Next to the image the primary field for the entity is displayed first and wraps up to two lines. The primary field is followed by the first two columns in the view that are not the primary field. Those fields will each appear on one line.  
  
 If the entity is not enabled for images, the primary field for the entity is displayed first. The primary field is followed by the first three columns in the view that are not the primary field.  
  
 There are a few special list types: Activity, Stakeholders, and Sales Team. These are discussed in the next sections.  
  
 **Activity Lists**  
  
 The simple list for activities includes some special functionality that isn’t available on other lists. Each standard activity type (such as Phone call and Task) includes a symbol to differentiate it from the other activity types. Next to the symbol, the primary field for the activity is displayed and will wrap up to three lines. The next field to display is the first field from the view (excluding the primary field), **Due Date**, and **Activity Type**. Activities that can be marked as complete have a check box next to them. Tap the check box to mark the activity as complete.  
  
 The activities list shows activities that are due today and past due activities in a darker color. Activities that are not due today or past due appear in a lighter color. Activities with a due date include the date and time of when they are due.  
  
> [!IMPORTANT]
> [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] uses a composite Activity entity to store and retrieve data common between different activity types (like Task, Appointment, or Phone Call). The due date for activities is stored in the Actual End field for the composite Activity entity.  Appointment activities have a Start Date and End Date.  Because the due date for the activities list is retrieved from the Actual End field, the time that an appointment ends is displayed in the Activities list. This means an appointment that starts at 1pm and ends at 2pm will show a time of 2pm on the tile for the appointment in the activities simple list.  
  
 ![Dynamics 365 for tablets simple activity list](../media/y-microsoft-crm.png "Dynamics 365 for tablets simple activity list")  
  
 Some more things to note:  
  
-   The Description field for emails will not appear in lists.  
  
-   For Activities, the **New Item** button + opens a flyout so you can select the type of activity to create. This flyout contains a list of all the read/write enabled activities.  
  
 **Stakeholders and Sales Team Lists**  
  
 The Stakeholders and Sales Team lists that appear in an Opportunity display the primary field and role. These two entity lists have inline create and editing. When you tap the **New Item** button + on these lists, the existing list items move down, and a lookup and a drop-down list appear. Now you can select (or create) an entity to add to the list through the lookup, and assign a role through the drop-down list.  
  
 ![Stakeholders and sales team lists](../media/crm-ua-31463.gif "Stakeholders and sales team lists")  
  
 Editing is an inline experience as well.  If you tap the down arrow next to the role name, the drop-down list appears in edit mode and you can change roles.  
  
 **Select View**  
  
 To change the view used to display a list of records, tap and hold the name of the list. The command bar appears, which includes the **Select View** button.  Tap the **Select View** button to select a different view.  
  
 Personal views are listed before system views.  You can’t create new views within [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)].  
  
### Charts  
 All the charts you can create in the Chart Designer, such as Bar, Line, Pie, and Funnel charts, are viewable in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
 Some more things to note:  
  
-   Open a chart from the Sales Dashboard to get a page with a chart and the records used to generate the chart.  
  
-   Choose the chart sections to see the records filtered for that part of the chart.  
  
-   Charts are not available offline with [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
-   You can add charts to dashboards and chart pages only.  
  
### Forms  
 Forms in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] are based on the development principle of “Design once and deploy across clients.” Entity behavior and business processes in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] forms function similarly to forms in the web application, but with a flow tailored for a tablet. In Microsoft Dynamics 365 online,  you can preview how forms look on tablets and phones when you customize them in the web app.  
  
> [!NOTE]
>  Forms work a bit differently for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)]. See the section below [Things to know about Dynamics 365 for phones](set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets.md#BKMK_PhonesThingsToKnow).  
  
||||  
|-|-|-|  
|![Sales form in Dynamics 365](../media/e-microsoft-crm.png "Sales form in Dynamics 365")<br /><br /> Sales Lead form in web application|>|![Sales form in Dynamics 365 for tablets](../media/g-microsoft-crm.png "Sales form in Dynamics 365 for tablets")<br /><br /> Sales Lead form in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]|  
  
 This diagram shows common parts of the updated entity forms in the web application.  
  
 ![Diagram shows Updated entity form structure in Dynamics 365](../media/updated-form-diagram.png "Diagram shows Updated entity form structure in Dynamics 365")  
  
 [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] takes many of the Main form elements and presents them in a way that is optimized for tablets, as shown in the following diagram.  
  
 ![Diagram of a form in Dynamics Dynamics 365 for tablets](../media/crm-itpro-cust-mocaformdiagram.png "Diagram of a form in Dynamics Dynamics 365 for tablets")  
  
 **Relationships**  
  
 The Relationships area of the form displays entity relationships that are configured in the Navigation area of a form.  If an entity relationship is configured to appear in the Navigation area within the form customization, and the entity is enabled for [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)], the entity relationship will appear in the Relationships section. The Connections relationship tile is not displayed in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
 The relationships section also has a tile that represents the owner of the record, which is a Lookup field.  In addition to the Owner tile, there are some other examples of hardcoded tiles that represent Lookup fields. For example, the Contact form has a tile for the parent account.  You cannot choose additional Lookup fields as tiles in this section.  
  
 ![Form customization with navigation items](../media/crm-ua-arrow-down-blue.gif "Form customization with navigation items")  
  
 Form customization that shows navigation items on the left side of the screen  
  
 ![Relationships section within a form](../media/crm-ua-arrow-down-gray.gif "Relationships section within a form")  
  
 Relationships section within a form  
  
 Some more things to note:  
  
-   Forms in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] are limited to 5 tabs (or 75 fields and 10 lists). This limit includes hidden fields.  
  
-   Activity Feeds and [!INCLUDE[pn_yammer](../../includes/pn-yammer.md)] are not supported in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
<a name="BKMK_PhonesThingsToKnow"></a>   
## Things to know about [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)]  
  
### Forms  
 Forms in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] use the Main form type. Entity behavior and business processes in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] forms function similarly to forms in the web application, but with a flow tailored for a phone.  
  
 To further simplify forms, you can hide components from appearing in the phone app. You can hide tabs, sections, subgrids, fields, and charts. For example, to hide the Details tab in the Contact form, click **Settings** > **Customizations** > **Customize the System** > **Components** > expand **Entities** > expand the **Contact** entity > **Forms**. Select the **Contact** form, then scroll down and click **Details**. Click **Change Properties** and clear the **Available on phone** check box to hide the Detail tab from appearing on the Contact form for phone users.  
  
 ![Hide the Detail tab on Dynamics  Dynamics 365 for phones](../media/crm-itpro-phonehidedetailtab.png "Hide the Detail tab on Dynamics  Dynamics 365 for phones")  
  
### Other differences with [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 There are a few differences between [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]:  
  
-   Simple lists are not available in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)]. Instead use the command bar **…** and click **Select View** to change your view.  
  
-   Duplicate detection is not available.  
  
-   The **Open in browser** feature is not available.  
  
<a name="BKMK_PhoneLanguages"></a>   
## Supported languages for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] support the following languages:  
  
-   Basque (Basque) - 1069  
  
-   Bulgarian (Bulgaria) - 1026  
  
-   Catalan (Catalan) - 1027  
  
-   Chinese (Hong Kong S.A.R.) - 3076  
  
-   Chinese (People's Republic of China) - 2052  
  
-   Chinese (Simplified) - 2052  
  
-   Chinese (Taiwan) - 1028  
  
-   Chinese (Traditional) - 1028  
  
-   Croatian (Croatia) - 1050  
  
-   Czech (Czech Republic) - 1029  
  
-   Danish - 1030  
  
-   Dutch - 1043  
  
-   English - 1033  
  
-   Estonian - 1061  
  
-   Finnish - 1035  
  
-   French - 1036  
  
-   Galician  
  
-   German - 1031  
  
-   Greek - 30  
  
-   Hindi (India) - 91  
  
-   Hungarian - 36  
  
-   Indonesian - 62  
  
-   Italian - 1040  
  
-   Japanese - 1041  
  
-   Kazakh - 705  
  
-   Korean - 82  
  
-   Latvian - 371  
  
-   Lithuanian - 370  
  
-   Norwegian - 47  
  
-   Polish - 48  
  
-   Portuguese (Brazil) - 55  
  
-   Portuguese (Portugal) - 2070  
  
-   Romanian - 40  
  
-   Russian - 7  
  
-   Serbian  
  
-   Slovak - 421  
  
-   Slovenian - 386  
  
-   Spanish - 3082  
  
-   Swedish - 46  
  
-   Thai - 66  
  
-   Turkish - 90  
  
-   Ukrainian - 380  
  
 When the application first loads after installation, it will determine the device language and load the user interface in that language. If the device language is not one of the supported languages, the application will load in English. When the application has been configured in a [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] organization, the application will load in the language specified in the user’s personal options. If the user language is not one of the supported languages, the application will fall back to the base language of the Dynamics 365 organization, if it is in the supported language list. If the organization’s base language isn’t supported, English will be the final fallback if it is enabled on the server.  
  
<a name="BKMK_PhoneEntities"></a>   
## Entities and [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 You can enable a limited set of entities for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]. To see if an entity is enabled or to enable an entity, click **Settings** > **Customizations** > **Customize the System** > **Entities**. Select an entity and review the **Outlook & Mobile** settings.  
  
 Some more things to note:  
  
-   All custom entities can be enabled for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
-   You can use the Lookup for entities that are not enabled for [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] from a record that is enabled and see the data. However, you won’t be able to edit the entity.  
  
 **Entities that are visible and read/write in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]**  
  
|Entity Name| Visibility Property| Read-only Property|  
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
|Account|Modifiable|Modifiable|  
|Activity|Not modifiable|Not modifiable|  
|Appointment|Modifiable|Modifiable|  
|Case|Modifiable|Modifiable|  
|Competitor|Modifiable|Modifiable|  
|Connection|Not modifiable|Modifiable|  
|Contact|Modifiable|Modifiable|  
|Invoice|Modifiable|Modifiable|  
|Lead|Modifiable|Modifiable|  
|Note|Not modifiable|Not modifiable|  
|Opportunity|Modifiable|Modifiable|  
|Order|Modifiable|Modifiable|  
|Phone Call|Modifiable|Modifiable|  
|Quote|Modifiable|Modifiable|  
|Social Activity|Modifiable|Modifiable|  
|Social Profile|Modifiable|Modifiable|  
|Task|Modifiable|Modifiable|  
  
 **Entities that are visible and read-only in [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]**  
  
|Entity Name| Visibility Property| Read-only Property|  
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
|Attachment|Not modifiable|Not modifiable|  
|Email|Modifiable|Not modifiable|  
|Entitlement|Not modifiable|Not modifiable|  
|Knowledge Article|Modifiable|Not modifiable|  
|Price List|Not modifiable|Not modifiable|  
|Product|Modifiable|Not modifiable|  
|Queue|Modifiable|Not modifiable|  
|Sharepoint Document|Not modifiable|Not modifiable|  
|SLA KPI Instance|Not modifiable|Modifiable|  
|Team|Not modifiable|Not modifiable|  
|User|Not modifiable|Not modifiable|  
|Web Resource|Not modifiable|Not modifiable|  
  
<a name="BKMK_PhoneAuth"></a>   
## Authentication and [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] authenticate users with browser-based authentication, which means no credentials are stored on the phone.  
    
<a name="BKMK_SecuringData"></a>   
## Considerations and best practices for securing Dynamics 365 data on [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]  
 Consider the following when planning security for [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)]:  
  
- **Data transmission**. [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] requires an [!INCLUDE[pn_Internet_facing_deployment](../../includes/pn-internet-facing-deployment.md)], so when your organization’s mobile devices synchronize [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] data with your online [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)], the data is encrypted with [!INCLUDE[pn_Secure_Sockets_Layer](../../includes/pn-secure-sockets-layer.md)].  
  
- **Cached data**. [!INCLUDE[pn_Mobile_Express_short](../../includes/pn-mobile-express-short.md)] and [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] only cache records and lists that you’ve recently accessed in the app. To clear cached data, users can either sign out or reconfigure.
  
- **Encrypting cached data**. Cached data is not encrypted. You can use [BitLocker](https://technet.microsoft.com/library/hh831713.aspx) to encrypt the entire hard drive on a [!INCLUDE[pn_windows8](../../includes/pn-windows8.md)] or later device. For Apple and Android devices, consider [Windows Intune](http://go.microsoft.com/fwlink/p/?LinkID=394174) or a product from another company to encrypt the hard drive on the mobile device.  
  
<a name="BKMK_OtherFeatures"></a>   
## Other features  
  
### Save  
 Records are saved in [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)] based on how you configured autosave in your organization settings. To view your save settings, click **Settings** > **Administration** > **System Settings** > **General** tab. View the settings under **Select the default save option for forms**.  
  
 If autosave is:  
  
-   Enabled for the organization, changes to forms are saved when users leave forms.  
  
-   Disabled for the organization, users must use the command bar and click **Save** to save form changes.  
  
### Images  
 Images, such as contact photos, are not stored in the browser cache. Images may not be displayed when users work offline with [!INCLUDE[pn_moca_short](../../includes/pn-moca-short.md)].  
  
<a name="BKMK_Privacy"></a>   
## Privacy notice  
 [!INCLUDE[cc_privacy_crm_for_tablets](../../includes/cc-privacy-crm-for-tablets.md)]  
  
### See Also  
 [Secure and manage Dynamics 365 for phones and tablets](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/secure-manage-phones-tablets)   
 [What's supported](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/support-phones-tablets) </br>
 [Troubleshooting](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/mobile-app/troubleshooting-things-know-about-phones-tablets)   
 [Install Dynamics 365 for tablets and phones](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)   
 
 
