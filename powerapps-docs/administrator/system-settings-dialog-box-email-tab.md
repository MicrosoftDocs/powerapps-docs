---
title: "System Settings dialog box - Email tab for Dynamics 365 Customer Engagement | MicrosoftDocs"
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
ms.assetid: 7ffc3f15-6624-4718-ab77-5bcb5360943a
caps.latest.revision: 63
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# System Settings dialog box - Email tab

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

Use the settings on this page to set up email processing in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)].  
  
## Open the System Settings dialog box (if it isn’t already open)  
  
1. [!INCLUDE[proc_permissions_system_admin_and_customizer](../includes/proc-permissions-system-admin-and-customizer.md)]  
  
    Check your security role  
  
    - [!INCLUDE[proc_follow_steps_in_link](../includes/proc-follow-steps-in-link.md)]  
  
    - [!INCLUDE[proc_dont_have_correct_permissions](../includes/proc-dont-have-correct-permissions.md)]  
  
2. [!INCLUDE[proc_settings_email_config](../includes/proc-settings-email-config.md)]  
  
3.  Choose **Email Configuration Settings**.  
  
|Settings|Description|  
|--------------|-----------------|  
|**Configure email processing**||  
|Process Email Using|Select whether you want to process email by using server-side synchronization or the Email Router. server-side synchronization is the preferred synchronization method.<br /><br /> [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Integrate your email system with Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/admin/integrate-synchronize-your-email-system)|  
|**Configure default synchronization method**|For any mailbox that is automatically created in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] when a user or queue is created, the default email settings as defined in this section will be applied.|  
|Server Profile|For server-side synchronization, select the email server profile that you want to use. The email server profile holds the configuration data that enables [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] to connect to [!INCLUDE[pn_Microsoft_Exchange](../includes/pn-microsoft-exchange.md)]. If you’re connecting [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)] with [!INCLUDE[pn_Exchange_Online](../includes/pn-exchange-online.md)], the email server profile is automatically created for you.|  
|Incoming Email|Select whether you want to use [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)], the Email Router, server-side synchronization, or a forward mailbox for processing incoming email. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Create forward mailboxes or edit mailboxes](https://docs.microsoft.com/dynamics365/customer-engagement/admin/create-forward-mailboxes-edit-mailboxes)|  
|Outgoing Email|Select whether you want to use [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)], the Email Router, or server-side synchronization for processing outgoing email.|  
|Appointments, Contacts, and Tasks|Select whether you want to use [!INCLUDE[pn_crm_for_outlook_short](../includes/pn-crm-for-outlook-short.md)] or server-side synchronization to synchronize appointments, contacts, and tasks between [!INCLUDE[pn_Outlook_short](../includes/pn-outlook-short.md)] and [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. **Note:**  You can’t synchronize appointments, contacts, and tasks if you’re synchronizing with a [!INCLUDE[pn_POP3_short](../includes/pn-pop3-short.md)] email server.|  
|**Email processing for unapproved users and queues**|Select these check boxes if you want to allow email processing only for users and queues whose email addresses have been approved by the system administrator.<br /><br /> -   Process email only for approved users<br />-   Process email only for approved queues|  
|**Configure folder-level tracking and email correlation**||  
|Use folder-level tracking for [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] folders (server-side synchronization must be enabled)|Users can set up [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] tracking folders, and then move messages to those folders to track them automatically on virtually any device. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Track Outlook email by moving it to a tracked Exchange folder](https://docs.microsoft.com/dynamics365/customer-engagement/admin/track-outlook-email-by-moving-it-tracked-exchange-folder)<br /><br /> Folder-level tracking provides 100% tracking accuracy. To use folder-level tracking:<br /><br /> -   You must select this check box.<br />-   Your organization must synchronize email through server-side synchronization. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Set up server-side synchronization](set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks.md)|  
|Use correlation to track email conversations|Select this check box if you want to link email activities with other related records using the information in the email headers. This method uses email properties for correlation and is more accurate than smart matching, but less accurate than folder-level tracking or tracking tokens. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Email message filtering and correlation](https://docs.microsoft.com/dynamics365/customer-engagement/admin/email-message-filtering-correlation) **Note:**  Email correlation using email headers works best when email is processed using server-side synchronization. If you’re using the Email Router to process email, you can use tracking tokens or smart matching to correlate email activities with related records.|  
|Use tracking tokens|Select this check box to use tracking tokens and to configure how [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] displays them in the Subject line of the email messages.<br /><br /> Tracking tokens provide 100% tracking accuracy. If you don’t want to see tokens in Subject lines, however, consider folder-level tracking, which also provides 100% tracking accuracy.<br /><br /> You can configure prefixes and other sections of tracking tokens. Long prefixes or too many prefix changes may cause lost data in history, however. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Email message filtering and correlation](https://docs.microsoft.com/dynamics365/customer-engagement/admin/email-message-filtering-correlation)|  
|Use smart matching|Select this check box to use smart matching to correlate email based on the similarity between email messages. Smart matching isn’t as accurate as tracking tokens or folder-level tracking. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Email message filtering and correlation](https://docs.microsoft.com/dynamics365/customer-engagement/admin/email-message-filtering-correlation)|  
|**Set tracking options for emails between Dynamics 365 users**||  
|Track email sent between two Dynamics 365 users as two activities|Select this option to create two email activities between [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] users, one for the sender and one for the recipient.|  
|**Set email form options**||  
|Use secure frames to restrict email message content|If this is set to **Yes**, you may see the following error message when you’re reading email: “This content cannot be displayed in a frame”. Although this can make sending sensitive content in email less secure, changing the setting to **No** typically eliminates this error.|  
|Allow messages with unresolved recipients to be sent|Set this to **Yes** if you want to send email messages that have unresolved recipients.|  
|Set To, cc, bcc, fields as unresolved values if multiple matches are found in Incoming Emails.|Use this setting to choose which record an email address resolves to when there are multiple possible matches in **to**, **cc**, or **bcc** fields of an email. When you select **Yes**, if the **to**, **cc**, or **bcc** fields of an email have an email address that can be resolved to multiple contacts (or other records), the email address will be resolved in the unresolved mode instead of resolving to all possible records. Unresolved email addresses can then be resolved individually as you encounter them. The default value is **No**.|  
|Apply same email address to all unresolved matches when you manually resolve it for one.|When set to **Yes**, the same email address is applied to all similar unresolved email addresses when resolved in one email activity.  When set to **No**, the email address is applied only to the specific email activity and does not resolve similar addresses present in other email activities. The default value is **Yes**. <br /><br />This setting appears when **Set To, cc, bcc, fields as unresolved values is multiple matches are found in Incoming Emails** is set to **Yes**.|
|**Set file size limit for attachments**||  
|Maximum file size (in Kilobytes)|Increase or decrease the maximum file size for attached files. The default size is 5 MB (5,120 KB). The maximum size is 128 MB (131,072 KB).| 
|**Configure alerts**|Select check boxes for the type of alerts that must be sent to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] users:<br /><br /> -   Error (default)<br />-   Warning<br />-   Information (default) **Tip:**  Select **Warning** if you’re troubleshooting or testing or want to get more detailed messages on the alert wall.|  
|Notify mailbox owner|By default, the system administrator is notified of any error that occurs for an email server profile.<br /><br /> Select this check box if you also want to notify the mailbox owner.|  
  
### See also  
 [Track Outlook email by moving it to a tracked Exchange folder](https://docs.microsoft.com/dynamics365/customer-engagement/admin/track-outlook-email-by-moving-it-tracked-exchange-folder)   
 [Frequently asked questions about synchronizing records between Microsoft Dynamics 365 and Outlook](https://docs.microsoft.com/dynamics365/customer-engagement/admin/frequently-asked-questions-synchronizing-records-dynamics-365-and-outlook)   
 [Set up email through server-side synchronization](set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks.md)   
