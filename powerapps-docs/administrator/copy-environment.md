---
title:  Copy an instance to a Sandbox instance | Microsoft Docs
description: In this quickstart, you learn how to download a list of apps created in your environments
services: 'powerapps'
suite: powerapps
documentationcenter: na
author: jimholtz
manager: kfile
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
# Copy an instance to a Sandbox instance

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

You can use Copy instance in the [!INCLUDE[pn_dyn_365_admin_center](../includes/pn-dyn-365-admin-center.md)] to copy the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] application and all data from any instance to a Sandbox instance. You can do either a full or minimal copy.  
  
> [!TIP]
> ![Video symbol](media/video-thumbnail-4.png "Video symbol") Check out the following video on copying an instance to a Sandbox instance: [Microsoft Dynamics CRM 2013 Spring '14 Online New Features -Copy](http://youtu.be/y6duFi8nZaE).  ![video-thumbnail-4.png](media/video-thumbnail-4.png)
>   
>  This video also applies to [!INCLUDE[pn_crm_online_2015_update_1_shortest](../includes/pn-crm-online-2015-update-1-shortest.md)] and [!INCLUDE[pn_crm_online_2016_update](../includes/pn-crm-online-2016-update.md)].  
  
> [!NOTE]
>  To copy instances larger than 100 GB, please contact [technical support](contact-technical-support.md).  
  
## Full copy instance  
 A full copy includes all application data, users, and customizations from the source instance and is suitable for:  
  
-   User acceptance testing  
  
-   Upgrade testing  
  
-   Preview in production (TAP/EA)  
  
-   Training  
  
**An example scenario**  
  
Isaac, a business application developer, has received a request from the sales department to configure and deploy a social media integration solution from another company vendor.  Isaac has never installed a solution from this vendor and is unsure what impact this would have on the production application.  He’d like to import the solution into an environment that is nearly identical to, but isolated from, production to learn about the solution and make the appropriate configuration changes. Isaac submits a request to Thomas, the IT Manager for Contoso, to create a full copy Sandbox instance for him.  
  
After the full copy is complete, Isaac receives a mail from Thomas telling him the Sandbox instance is ready.  Isaac logs into the Sandbox instance and makes the necessary changes to make sure that production external services will not be impacted by the Sandbox instance.  Once changes are complete, Isaac turns off administration mode and enables background services.  Isaac is able to use the full copy Sandbox instance to do his testing and later manually import the solution into production.  
  
## Minimal copy instance  
 A Minimal copy only includes users, customizations, and schema from the source instance and is suitable for:  
  
-   Iterative team development  
  
-   Partner/ISV solutions  
  
-   Proof of concept  
  
**An example scenario**  
  
Isaac has a large development project starting next week for the sales department.  He has a team of developers ready to start on the project, some of whom are internal to Contoso and some are external vendors. The Contoso sales application contains Personally Identifiable Information (PII) that the sales manager has explicitly stated must not be made available to any external parties for privacy and legal liability reasons.  Isaac requests a minimal copy Sandbox instance that does not contain any production data or users. In addition, Isaac creates an Office 365 security group to give the development team access to the Sandbox instance.  
  
After modifying and enabling some of the plug-ins, the developer Sandbox instance functions the same and is completely isolated from the production application.  The development team works on their modifications in this instance for several weeks.  They package their changes into a solution and export/import to deploy to the full copy Sandbox instance.  After a successful round of testing and signoffs, the changes are manually deployed to production.  
  
### Entities copied in a Minimal copy  
 The following entities are copied when you do a Minimal copy:  

| Entities |  
|-----------|  
|BusinessUnit|  
|ConnectionRole|  
|Currency|  
|DuplicateRule|  
|DuplicateRuleCondition|  
|EmailServerProfile|  
|FieldPermission|  
|FieldSecurityProfile|  
|ImportMap|  
|InternalAddress|  
|Mailbox|  
|Organization|  
|Position|  
|Report|  
|Resource|  
|ResourceGroup|  
|Role|  
|RollupField|  
|SavedQuery|  
|SLAKPIInstance|  
|Solution|  
|Subject|  
|Team|  
|TeamTemplate|  
|Template|  
|SystemUser|  
  
<a name="BKMK_ToCopy"></a>   

## To copy an instance  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
    > [!NOTE]
    >  Global administrators can copy all available instances. [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] System administrators can copy instances for which they have the System administrator role.  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select an instance, and then click **Copy**.  
  
5.  On the **copy instance** page, select a target instance, a copy type, adjust the instance settings as needed, and then click **Copy**.  
  
     A target instance can be a Sandbox or Preview instance; not a Production instance.  
  
    > [!WARNING]
    >  The target instance will be deleted and replaced with a copy of the data and customizations from the source instance. You won’t be able to recover any deleted data.  
  
6.  Click **yes** in the confirmation dialog box.  
  
Once the copy process is complete, the target instance is placed in [Administration mode](manage-sandbox-environments.md#BKMK_AdminMode) and background operations are disabled. The next section describes recommended Administrator actions for the newly created copy (target) instance.  
  
<a name="BKMK_NextSteps"></a>   

## Next steps after copying an instance  
 To ensure the newly created copy (target) instance does not impact your production instance, once the copy operation is complete, two things happen:  
  
1.  The newly created copy instance is placed in administration mode. Only those with [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] System Administrator or System Customizer security roles can sign in and manage the copy instance. Regular [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] users cannot sign in and use the copy instance.  
  
2.  Background operations are disabled in the copy instance. Disabled operations include workflows and synchronization with [!INCLUDE[pn_Microsoft_Exchange](../includes/pn-microsoft-exchange.md)].  
  
**Review components**  
  
 You should review the status of application components in the copy instance with external connections such as [!INCLUDE[pn_yammer](../includes/pn-yammer.md)], email, plug-ins, custom workflow activities, etc. Review these and consider what action to take:  
  
1.  Disable the component.  
  
2.  Redirect the component to another service instance such as one running [!INCLUDE[pn_Exchange](../includes/pn-exchange.md)] or [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)].  
  
3.  Do nothing – leave the component as is in the copy instance. For example, you might decide to allow Yammer posting to both the copy and production instances.  
  
 Here are some possible application components in the copy instance that could have external connections and therefore could impact services with the same connections in your production instance.  
  
- **Email**. A mailbox cannot be synced with two different instances. For a full copy instance, the user mailboxes in the copy instance must be disabled so the mailboxes do not attempt to send or receive email, or track appointments, contacts, or tasks. Set synchronization for the following to None.  
  
    -   Incoming Email  
  
    -   Outgoing Email  
  
    -   Appointments, Contacts, Tasks  
  
 [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Set the delivery method for incoming and outgoing email](set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks.md)  
  
- **SharePoint**. Deactivate or redirect [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] to a sandbox [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] environment to prevent impacting documents in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] managed by [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)]. In [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)], go to **Settings** > **Documentation Management** > **SharePoint Sites**. Select your site, and then click **Deactivate**.  
  
- **Yammer**. Disable [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] or redirect to a separate [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] service to prevent posts made in the copy instance conflicting with posts made in the production instance. In [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)], go to **Settings** > **Administration** > **Yammer Configuration**.  
  
     After creating a new Sandbox instance, workflows and system jobs might be pending execution. Apart from these jobs, if you have connected [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] there will be [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] activity streams posted from [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] asynchronously. These activity streams are not visible through the system jobs. If there were any pending [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] activity streams before the Disable Background Process is turned on, these activity steams will be posted to the current [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] configuration once the Disable Background Process is turned back off. In the Sandbox instance, if you have your current [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] configuration connected to the same [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] network as your production environment, you might see duplicate activity streams. To avoid duplicate [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] activity streams, redirect your Sandbox instance to another [!INCLUDE[pn_yammer](../includes/pn-yammer.md)] network (possibly a test network) before turning background processes back on.  
  
- **Platform extensibility**. Consider disabling the following that could be running in the copy instance and impacting external service components.  
  
    - **Server-side plug-ins**.  
  
    - **Workflow custom activity**.  
  
- **Client extensibility**. Review the following.  
  
    - **Client-side JavaScript**. Take a look at your JavaScript and HTML web resources for read/write operations that could impact external services.  
  
    - **IFRAMES**. Determine if the target of an IFRAME is a production instance.  
  
### See also  
 [Introducing Sandbox Instances in CRM Online](http://blogs.msdn.com/b/crm/archive/2014/03/20/introducing-sandbox-environments-in-crm-online.aspx)   
 [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md)   
 [Manage Microsoft Dynamics 365 (online) instances](manage-online-environments.md)
