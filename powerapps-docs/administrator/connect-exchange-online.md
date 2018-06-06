---
title: "Connect Dynamics 365 (online) to Exchange Online | MicrosoftDocs"
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
ms.assetid: 1b2b7846-5a69-4af7-849d-0c0acc300a7e
caps.latest.revision: 22
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
---
# Connect Dynamics 365 (online) to Exchange Online 

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

With both [!INCLUDE[pn_CRM_Online](../../includes/pn-crm-online.md)] and [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)] hosted as online services, connecting the two is a simpler, more straightforward configuration.  
  
> [!TIP]
> ![Video symbol](../media/video-thumbnail-4.png "Video symbol") Check out the following video: [Connect Dynamics 365 (online) to Exchange Online using server-side sync](https://go.microsoft.com/fwlink/p/?linkid=836831).  
  
> [!IMPORTANT]
> [!INCLUDE[cc_feature_requires_office_365](../../includes/cc-feature-requires-office-365.md)]  
  
<a name="BKMK_GetExchangeReady"></a>   
## Get Exchange ready  
 To use [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)] with [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)], you must have an [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)] subscription that comes as part of an [!INCLUDE[pn_Office_365](../../includes/pn-office-365.md)] subscription or that can be subscribed to separately. For information on [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)], see:  
  
-   [Exchange Online](https://technet.microsoft.com/library/jj200580\(v=exchg.150\).aspx)  
  
-   [Exchange Online Service Description](https://technet.microsoft.com/library/jj819276.aspx)  
  
-   [Office 365 service comparison](https://technet.microsoft.com/office/dn788955)  
  
> [!TIP]
>  To make sure you’ve got a good connection to [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)], run the [Microsoft Remote Connectivity Analyzer](https://testconnectivity.microsoft.com/). For information on what tests to run, see [Test mail flow with the Remote Connectivity Analyzer](https://technet.microsoft.com/library/dn305950\(v=exchg.150\).aspx).  
  
<a name="BKMK_VerifyProfile"></a>   
## Verify you have the profile: Microsoft Exchange Online  
 If you have an [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)] subscription in the same tenant as your [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)] subscription, [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)] creates a default profile for the email connection: **Microsoft Exchange Online**. To verify this profile:  
  
1.  Go to **Settings** > **Email Configuration** > **Email Server Profiles**.  
  
2.  Click **Active Email Server Profiles** and check that the **Microsoft Exchange Online** profile is in the list.  
  
 ![Verify the Microsoft Exchange Online profile](../media/exchange-online-profile.png "Verify the Microsoft Exchange Online profile")  
  
     If the [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)] profile is missing, verify you have an [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)] subscription and that it exists in the same tenant as your [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)] subscription.  
  
3.  If there are multiple profiles, click the **Microsoft Exchange Online** profile and set it as default.  
  
<a name="BKMK_ConfigureDefault"></a>   
## Configure default email processing and synchronization  
 Set server-side synchronization to be the default configuration method for newly created users.  
  
1.  Go to **Settings** > **Email Configuration** > **Email Configuration Settings**.  
  
2.  Set the processing and synchronization fields as follows:  
  
    - **Server Profile**: [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)]  
  
    - **Incoming Email**: Server-Side Synchronization or Email Router  
  
    - **Outgoing Email**: Server-Side Synchronization or Email Router  
  
    - **Appointments, Contacts, and Tasks**: Server-Side Synchronization or Email Router  
  
 ![System Settings for server-side synchronization](../media/exchange-online-sss-settings.png "System Settings for server-side synchronization")  
  
3.  Click **OK**.  
  
All new users will have these settings applied to their mailbox.  
  
<a name="BKMK_ConfigureMailboxes"></a>   
## Configure mailboxes  
 New users will have their mailboxes configured automatically with the settings you made in the prior section. For existing users added prior to the above settings, you must set the Server Profile and the delivery method for email, appointments, contacts, and tasks.  
  
 In addition to administrator permissions, you must have Read and Write privileges on the Mailbox entity to set the delivery method for the mailbox.  
  
 Choose **one** of the following methods:  
  
### Set mailboxes to the default profile  
  
1.  Go to **Settings** > **Email Configuration** > **Mailboxes**.  
  
2.  Choose **Active Mailboxes**.  
  
3.  Select all the mailboxes that you want to associate with the [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)] profile, click **Apply Default Email Settings**, verify the settings, and then click **OK**.  
  
 ![Apply default email settings](../media/apply-default-email-settings.png "Apply default email settings")  
  
     By default, the mailbox configuration is tested and the mailboxes are enabled when you click **OK**.  
  
### Edit mailboxes to set the profile and delivery methods  
  
1.  Go to **Settings** > **Email Configuration** > **Mailboxes**.  
  
2.  Click **Active Mailboxes**.  
  
3.  Select the mailboxes that you want to configure, and then click **Edit**.  
  
4.  In the **Change Multiple Records** form, under **Synchronization Method**, set **Server Profile** to **Microsoft Exchange Online**.  
  
5.  Set **Incoming** and **Outgoing** **Email** to **Server-Side Synchronization or Email Router**.  
  
6.  Set **Appointments, Contacts, and Tasks** to **Server-Side Synchronization**.  
  
7.  Click **Change**.  
  
<a name="BKMK_ApproveEmail"></a>   
## Approve email  
 You need to approve each user mailbox or queue before that mailbox can process email.  
  
> [!NOTE]
>  You must be an Office 365 Global administrator to approve mailboxes.  
  
1.  Go to **Settings** > **Email Configuration** > **Mailboxes**.  
  
2.  Click **Active Mailboxes**.  
  
3.  Select the mailboxes that you want to approve, and then click **More Commands** (**…**) > **Approve Email**.  
  
4.  Click **OK**.  
  
<a name="BKMK_TestConfiguration"></a>   
## Test configuration of mailboxes  
  
1.  Go to **Settings** > **Email Configuration** > **Mailboxes**.  
  
2.  Click **Active Mailboxes**.  
  
3.  Select the mailboxes you want to test, and then click **Test & Enable Mailboxes**.  
  
     This tests the incoming and outgoing email configuration of the selected mailboxes and enables them for email processing. If an error occurs in a mailbox, an alert is shown on the Alerts wall of the mailbox and the profile owner. Depending on the nature of the error, [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] tries to process the email again after some time or disables the mailbox for email processing.  
  
     To see alerts for an individual mailbox, open the mailbox and then under **Common**, click **Alerts**.  
  
     The result of the email configuration test is displayed in the **Incoming Email Status**, **Outgoing Email Status**, and **Appointments, Contacts, and Tasks Status** fields of a mailbox record. An alert is also generated when the configuration is successfully completed for a mailbox. This alert is shown to the mailbox owner.  
  
     You can find information on recurring issues and other troubleshooting information in [Blog: Test and Enable Mailboxes in Microsoft Dynamics CRM 2015](http://blogs.msdn.com/b/crm/archive/2015/08/31/test-and-enable-mailboxes-in-microsoft-dynamics-crm-2015.aspx) and [Troubleshooting and monitoring server-side synchronization](https://docs.microsoft.com/dynamics365/customer-engagement/admin/troubleshooting-monitoring-server-side-synchronization).  
  
     Make sure you’ve got a good connection to [!INCLUDE[pn_Exchange_Online](../../includes/pn-exchange-online.md)] by running the [Microsoft Remote Connectivity Analyzer](https://testconnectivity.microsoft.com/). For information on what tests to run, see [Test mail flow with the Remote Connectivity Analyzer](https://technet.microsoft.com/library/dn305950\(v=exchg.150\).aspx).  
  
> [!TIP]
>  If you’re unable to synchronize contacts, appointments, and tasks for a mailbox, you may want to select the **Sync items with Exchange from this Dynamics 365 org only, even if Exchange was set to sync with a different org** check box. [Read more about this check box](https://docs.microsoft.com/dynamics365/customer-engagement/admin/when-would-want-use-check-box).  
  
<a name="BKMK_TestEmailConfig"></a>   
## Test email configuration for all mailboxes associated with an email server profile  
  
1.  Go to **Settings** > **Email Configuration** > **Email Server Profiles**.  
  
2.  Select the [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)] profile, and then click **Test & Enable Mailboxes**.  
  
     When you test the email configuration, an asynchronous job runs in the background. It may take a few minutes for the test to be completed. [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] tests the email configuration of all the mailboxes associated with the [!INCLUDE[pn_Microsoft_Exchange_Online](../../includes/pn-microsoft-exchange-online.md)] profile. For the mailboxes configured with server-side synchronization for synchronizing appointments, tasks, and contacts, it also checks to make sure they’re configured properly.  
  
> [!TIP]
>  If you’re unable to synchronize contacts, appointments, and tasks for a mailbox, you may want to select the **Sync items with Exchange from this Dynamics 365 org only, even if Exchange was set to sync with a different org** check box. [Read more about this check box](https://docs.microsoft.com/dynamics365/customer-engagement/admin/when-would-want-use-check-box).  
  
### See also  
 [Troubleshooting and monitoring server-side synchronization](https://docs.microsoft.com/dynamics365/customer-engagement/admin/troubleshooting-monitoring-server-side-synchronization)   
 [Test mail flow with the Remote Connectivity Analyzer](https://technet.microsoft.com/library/dn305950\(v=exchg.150\).aspx)   
