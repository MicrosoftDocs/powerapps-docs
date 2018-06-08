---
title:  Manage Sandbox instances  | Microsoft Docs
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
# Manage Sandbox instances

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

A Sandbox instance is any non-production instance of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)]. Isolated from production, a Sandbox instance is the place to safely develop and test application changes with low risk.  
  
> [!NOTE]
>  With [!INCLUDE[pn_crm_8_2_0_online](../includes/pn-crm-8-2-0-online.md)], we no longer require a minimum purchase amount to receive a free Sandbox instance. If you've purchased a subscription and have not received a free Sandbox instance, you will be provided one when you purchase full Dynamics 365 Enterprise licenses. There is a limit of one free Sandbox instance per tenant. You can also purchase additional Sandbox instances. For more information, see [Dynamics 365 pricing and licensing](http://go.microsoft.com/fwlink/p/?LinkID=321102).  
  
> [!TIP]
> ![Video symbol](media/video-thumbnail-4.png "Video symbol") Check out the following video: [Sandbox instances for Dynamics 365 (3:18)](https://go.microsoft.com/fwlink/p/?linkid=838057).  
  
<a name="BKMK_View"></a>   

## View your Sandbox instances  
 You manage your Sandbox instances from the [!INCLUDE[pn_dyn_365_admin_center](../includes/pn-dyn-365-admin-center.md)].  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
 On the **Manage your Dynamics 365 instances** page, you’ll see a list of all your instances.  
  
<a name="BKMK_Reset"></a>   
## Reset a Sandbox instance  
 You can reset a Sandbox instance to delete and re-provision it. Consider a reset when you want to:  
  
-   Change to a different version of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)].  
  
-   Create a new project  
  
-   Free up storage space  
  
-   Remove an instance containing Personally Identifiable Information (PII) data  
  
> [!NOTE]
> -  You can only reset Sandbox instances.  
> -  ![Video symbol](media/video-thumbnail-4.png "Video symbol") Check out the following video: [Dynamics CRM 2013 Spring '14 Online New Features -Reset](http://youtu.be/nJDyuFdh0Nk).  
>   
>      This video also applies to [!INCLUDE[pn_crm_online_2015_update_1_shortest](../includes/pn-crm-online-2015-update-1-shortest.md)] and [!INCLUDE[pn_crm_online_2016_update](../includes/pn-crm-online-2016-update.md)].  
  
 **An example scenario**  
  
 Thomas is looking at the storage consumed by the various Contoso instances and is getting concerned that they’ll run out of space in one of their production instances.  He’d like to free up some space so he can give the production instance some additional storage.  He’s also been notified that the Legal department has set a retention policy on the use of production data in the test environment.  
  
 After contacting Isaac, Thomas resets the Sales department’s complete Sandbox instance. The instance is re-provisioned to factory settings and ready for future use as a Sandbox instance for a future project.  
  
### To reset an instance  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select a Sandbox instance, and then click **Reset**.  
  
5.  On the **reset instance** page, adjust the instance settings as needed and then click **Reset**.  
  
    > [!WARNING]
    >  The Sandbox instance will be deleted and reset to factory settings. You will not be able to recover any deleted data.  
  
6.  Click **yes** in the confirmation dialog box.  
  
<a name="BKMK_AdminMode"></a>   
## Administration mode  
 When you place a Sandbox instance in administration mode only users with [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] System Administrator or System Customizer security roles will be able to sign in to that instance. Administration mode is useful when you want to make operational changes and not have regular users affect your work, and not have your work affect regular users.  
  
> [!NOTE]
> - You can only place Sandbox instances in administration mode.  
> - Processes that use code, such as plug-ins or custom workflow assemblies, continue to be processed by the [!INCLUDE [pn-crm-2016-shortest](../includes/pn-crm-2016-shortest.md)] platform when administration mode is enabled and background operations are disabled.
> - ![Video symbol](media/video-thumbnail-4.png "Video symbol") Check out the following video: [Dynamics CRM 2013 Spring '14 Online New Features -Admin Mode](http://youtu.be/aUgwT-GuKO8).  
>   
>      This video also applies to [!INCLUDE[pn_crm_online_2015_update_1_shortest](../includes/pn-crm-online-2015-update-1-shortest.md)] and [!INCLUDE[pn_crm_online_2016_update](../includes/pn-crm-online-2016-update.md)].  
  
 On the **admin settings** page, you can set the following.  
  
|Setting|Description|  
|-------------|-----------------|  
|Enable administration mode|Select to enable administration mode for the selected Sandbox instance. Only System Administrators or System Customizers will be able to sign in to the selected Sandbox instance.|  
|Disable background operations|Select to disable all asynchronous operations (see [Asynchronous service architecture](https://docs.microsoft.com/dynamics365/customer-engagement/developer/asynchronous-service-architecture)) such as workflows and synchronization with Exchange. Emails will not be sent and server-side synchronization for appointments, contacts, and tasks are disabled. **Note:**  Administration mode must be enabled to disable background operations.|  
|Custom message for end users|Enter a message that will be displayed to all users when they attempt to sign in.|  
  
### Set administration mode  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select a Sandbox instance, and then click **Admin**.  
  
5.  Select **Enable administration mode** to enable it, and then click **Save**.  
  
### See also  
 [Blog: Introducing Sandbox Instances in CRM Online](http://blogs.msdn.com/b/crm/archive/2014/03/20/introducing-sandbox-environments-in-crm-online.aspx)   
 [Switch an instance](switch-environment.md)   
 [Delete an instance](delete-environment.md)   
 [Copy an instance](copy-environment.md)   
