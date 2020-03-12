---
title: "FAQs: Transition to Unified Interface | MicrosoftDocs"
description: "FAQs related to the transition process for moving users from the legacy web client to Unified Interface."
ms.custom: ""
ms.date: 03/04/2020
ms.reviewer: "kvivek"
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.author: "haybass"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# FAQs: Transition to Unified Interface

This topic provides answers to the most common questions about Unified Interface and about transitioning from the legacy web client to Unified Interface.

## FAQs: Unified Interface and legacy web client

### Why should I move to Unified Interface?

Microsoft's vision of a productive workplace requires a modern interface that includes the features and improvements contained in Unified Interface, which provides a more consistent user experience, improved performance and increased user efficiency. For more information, see [Unified Interface playbook.](https://docs.microsoft.com/powerapps/maker/model-driven-apps/unified-interface-playbook)

### Are my ISVs compatible?

ISVs have been notified to take action on the transition to Unified Interface. Contact your ISV directly regarding their timeline for Unified Interface compatibility.

### What is the retraining effort?

From a technology standpoint the retraining should be minimal as your business logic and schema remain unchanged. Retraining should focus on what's new within the navigation and the overall look and feel. Further training may be required if you have made a business decision to alter the design to optimize for the new capabilities and features.

### Will I need to re-create my solution customizations?

No, you should not have to recreate any customizations, provided you have followed the [Common Data Service Developer Guide](/powerapps/developer/common-data-service/overview) and kept up to date with any changes. However, there may be new opportunities to take on our latest investments that could lead to customization alterations.

### How long will it take to transition/what is the work effort?

The work effort here will vary based upon the complexity of your environment. We recommend getting started with a pilot/POC model-driven app to begin testing. From there, you can work with the business to plan a full Unified Interface rollout. See the [Unified Interface Playbook](https://docs.microsoft.com/powerapps/maker/model-driven-apps/unified-interface-playbook) and [planning checklist](https://aka.ms/UIChecklist) for additional guidance on getting started and our [white paper](https://download.microsoft.com/download/A/F/3/AF3D45A7-4F38-41BE-8956-1DF7A4A5AFDB/approaching-unified-interface-transition.pdf).

### Where can I find public information about the Unified Interface direction?

The strategic direction of Unified Interface is already in the public domain through events such as:
- [MBAS: BRK2073 Microsoft Power Apps: Run one UI – the future of canvas, model-driven, and Unified Interface in Power Apps](https://powerusers.microsoft.com/t5/MBAS-Gallery/Microsoft-PowerApps-Run-one-UI-the-future-of-canvas-model-driven/td-p/301580)
- [BRK3031 Implementation Best Practices for Dynamics 365: Making the move to modern Unified Interface](https://powerusers.microsoft.com/t5/Microsoft-Business-Applications/Implementation-Best-Practices-for-Dynamics-365-Making-the-move/m-p/299928)


### As an on-premises customer looking to move to the cloud, what is the best approach to adopt Unified Interface?

It is highly recommended to plan your move to Unified Interface at the same time as you migrate to the cloud. Begin testing of your legacy web client within Unified Interface and once migrated, confirmed Unified Interface compatibility before you release to your user community. This will reduce the training effort and allow users to adopt some of the new features and capabilities Unified Interface has to offer. For more information, please speak with your Microsoft representative.

### When will ISVs be notified of the need to move to Unified Interface?

ISVs have been notified to take action on the transition to Unified Interface. Contact your ISV directly regarding their timeline for Unified Interface compatibility.

### How are language translations handled?

The process for language translation is primarily unchanged, with the exception of the sitemap. Sitemap areas, groups, and subareas are localized within the sitemap editor.

### I don't have budget or resources to do a project. Is the deadline a fixed date?

We're locked to move away from the legacy web client by October 1, 2020. We recommend conducting some testing as soon as possible to understand the complexity of the project for your organization to get compatible. In most cases, extensive redesign should not be required to move forward quickly and start seeing user benefit. Contact Microsoft to provide any feedback that could stop your transition by creating a support case.

### We're working on transitioning to Unified Interface, but have hit some issues; how can we report to Microsoft?

Review our [resources](https://community.dynamics.com/365/unified-interface/) to help with guidance and log a support case following your standard procedure. You can also notify your partner, Microsoft representative, or FastTrack team (if applicable).

### When should I start moving to Unified Interface?

You can move right away; we already have many customers transitioned in production to Unified Interface. Start your testing as soon as possible. Access our Community site: <https://community.dynamics.com/365/unified-interface/> for helpful content. Use the Standard Support procedure to log any issues.

### What are the risks associated with moving to Unified Interface?

We see a risk in staying on legacy web client because our investment and strategic direction is on Unified Interface. If you are now planning to start the transition, review our [community site](https://community.dynamics.com/365/unified-interface/) and [quick start guides](https://docs.microsoft.com/powerapps/maker/model-driven-apps/transition-web-app-existing). This will help you identify gaps (if any) and have a plan to fix those before you do a full deployment.

### I have a new feature idea for Unified Interface; where do I log it?

Visit our ideas portal (<https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas>), select **Suggest an idea**, and label the item with the 'Unified Interface' category.

### Is there any supporting content to help me plan and execute my transition to Unified Interface?

Yes, we have a new community group (<https://community.dynamics.com/365/unified-interface/>) that provides useful content, interactive forum, and blog to see all the latest updates and information about Unified Interface.

### How does this move impact on-premises customer and what will happen when the web client is deprecated (do web client forms become unsupported)?

This announcement is only in effect for online customers at present. We will continue to support the legacy web client for on-premises deployments.

### Is the timeline applicable for customers using Government Community Cloud (GCC) and other data centers such as China?

We plan to release Unified Interface updates to these data centers as part of the standard release program.

### What action should I take as a Unified Service Desk customer who is still on the web client?

The Unified Service Desk customers, who are still on the web client, need to migrate their configurations from web client to unified interface. This will necessitate upgrade to the latest versions of the [Unified Service Desk](https://docs.microsoft.com/dynamics365/unified-service-desk/download-unified-service-desk?view=dynamics-usd-4.1) (both client and server components). We have a [migration assistant](https://docs.microsoft.com/dynamics365/unified-service-desk/admin/migration-steps-web-client-unified-interface-configuration?view=dynamics-usd-4.1) to help with this effort.

### Are there any other deprecations that I should plan for?

Review our [deprecation notification page](https://docs.microsoft.com/power-platform/important-changes-coming) to identify if there are any other areas that also require planning.

### Where can I find further information on the transition service?

To help accelerate momentum for transition, we are providing a suggested target date for environments to be switched from the legacy web client to Unified Interface via our transition service. Customers will need to approve the date prior to any action and then will receive a series of communication reminder messages as the date draws closer. Dates can also be rescheduled if they are not suitable for the business up until the October 1, 2020 deadline. For more information, see **FAQs: Transitioning to Unified Interface** later in this topic.


## FAQs: Transitioning to Unified Interface

### Where can I go to see the transition dates that have been suggested for my environments? 

Use the transition portal to manage your environment transition date: <https://runone.powerappsportals.com>.

### How do I gain access to the portal?

Do the following:
1. Visit <https://runone.powerappsportals.com>.
2. Sign in with the admin credentials of the tenant you want to manage.
3. Select **My Environments**, and review all environments that have a suggested date applied.

### I see my environment has a date suggested for transition. Can I change this date?

Yes, this is possible if you have the **global admin**, **Dynamics 365 service administrator**, or **Power Platform administrator** role for the tenant. 

The dates associated to your environment is a suggestion that requires approval to go ahead. Approve if the date works for your organization.  

To change the date, select the drop-down icon next to the environment and view the record. Tenant admin roles will then be able to reschedule the transition date to an earlier or later date.

To reschedule to an earlier date, update the existing date to your preferred option in the list. You can also [switch manually](transition-web-app.md) if our dates are not suitable. 
 
To schedule to a later date, select the reschedule transition date button. Suggested dates will be available in the drop-down. Once approved, the date will be updated in the portal accordingly. Accept the updated date if you would like your environment to be transitioned. 
 
Date changes will be reviewed and granted if the date is before October 1, 2020. The date will be updated within the portal once confirmed. 

> [!NOTE]
> If you have an approved transition and the scheduled date is within 48 hours, you'll not be able to change the date. Likewise, you can't request a date after October 1, 2020 as the legacy web client will no longer be available then.

### What will happen if I don't opt in and approve a suggested transition date for my environment?

There won't be any change to your environment if you haven't approved the suggested date within the portal. When the suggested date passes, we'll look to provide another date in the future for you to consider.  
 
> [!NOTE]
> After October 1, 2020, all environments will be updated to Unified Interface as per the October 2020 release wave.

### My transition date is within 48 hours and I can't change the date within the portal. How can I stop the transition from taking place?

The ability to change the transition date for an environment is available only until 48 hours prior to transition. To stop the process after this period, raise a support case. 

> [!NOTE]
> We can't guarantee the transition can be stopped if the request is made after the date has been locked on the portal (48 hrs or less).

### I have environments without a scheduled date. Can I update these to include a date?

Yes, if you have a **global admin**, **Dynamics 365 service administrator**, or **Power Platform administrator** role for the tenant, select the environment, and select a date by clicking on the reschedule transition date button.

We will update the portal with the date to confirm. Notification e-mails will also be sent to the global tenant admins as you get close to the transition date. This will follow the standard reminder procedure detailed within this document.

### Is there a recommended checklist I should run through before transition?

Check out the supporting content available on the [community site](https://community.dynamics.com/365/unified-interface/). We also have a [transition checklist](https://aka.ms/UIChecklist) to help you plan effectively. Review it carefully to ensure that you are comfortable with the transition to Unified Interface.

### My environment has been transitioned, but I am finding blocking issues for my users and want to move back to the legacy web client. Is this possible?

Yes, you will still be able to switch back to the legacy web client for up to 10 days post transition. You can make the [switch manually](https://docs.microsoft.com/power-platform/admin/enable-unified-interface-only) for the first 10 days or raise a [standard support request](https://admin.powerplatform.microsoft.com/support?referer=mbssupport) and set the problem type to be "Transition from legacy web client to Unified Interface" as the manual switch will be disabled. 

> [!NOTE]
> The 10 days need to be prior to October 1, 2020 as the legacy web client will no longer be available after that date.

### I want to transition after October 1, 2020. Is that possible?

The legacy web client won't be available post the October 2020 release wave for end users. We don't have the ability to defer the date beyond that period.

If you encounter any blocking items, log them using your standard support process as soon as possible.

### What is the standard reminder procedure throughout this process?

Communication will be in waves, at least 30 days prior to the suggested time frame, but you can sign in to the portal (<https://runone.powerappsportals.com>) at any time to view the status. Microsoft will send the following communication:

-    Initial message for each environment that has a suggested transition date.
-    If you have approved the date, you will receive a reminder message two days before the dates are locked within the portal. 
-    Final reminder will be sent two days before the transition. This will state the transition date is locked and will go ahead with the transition.
-    Post transition, there will be a closing message to confirm success (or if an issue occurred)

Messages can be seen using the following channels:
-    Message Center within the Microsoft 365 Tenant. This is typically visible to roles such as Global Admin, Service Admin, Service Message Reader.
-    Direct e-mail.  Emails are sent only to the system administrator role for the specific environment in question, or email addresses that have been added to the "Notification" tab in the environment admin portal.

> [!NOTE]
> You will receive an e-mail for each environment where your user account has the system administrator role.

### I have requested a date to postpone but still receiving e-mails and Message Center posts that my environment is set to transition. Should I be concerned?

Our first recommendation is to check the transition portal (<https://runone.powerappsportals.com/>) as it will be the single source of truth for all of your environments. If the date is updated, then it is highly likely that our communication system sent the message before we updated the communications list. 

If the date in the portal isn't updated to your new date, raise a support request following your standard procedure.

Only admin-approved dates will be transitioned. 

### If I already have an environment transitioned to Unified Interface, will I still be able to switch back to the legacy web client manually?

If your environment has been transitioned for at least 10 days, we will look to disable the manual switch back to the legacy web client. 

If you find this has been disabled and have a requirement to switch  back, raise a [standard support request](https://admin.powerplatform.microsoft.com/support?referer=mbssupport) and set the problem type to be "Transition from legacy web client to Unified Interface."

### Is there a specific day and time when approved transitions will take place?

We don't anticipate any downtime when making this transition. However, we will only make a transition on a Friday, following the same maintenance timelines outlined within our standard policies and communications. More information: [Maintenance timeline
](https://docs.microsoft.com/power-platform/admin/policies-communications#maintenance-timeline)

### Are environments from all data centers included within this transition service?

At present, environments from specific data centers, such as Government Community Cloud (GCC), have not been included within the portal. We'll provide suggested transition dates for these environments by June 2020. Customers who want to make the move to Unified Interface can always [switch manually](/power-platform/admin/enable-unified-interface-only#how-to-enable-unified-interface-only-mode) at any time before October 1, 2020.


