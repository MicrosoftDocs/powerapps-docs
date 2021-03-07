---
title: "FAQs: Transition to Unified Interface | MicrosoftDocs"
description: "FAQs related to the transition process for moving users from the legacy web client to Unified Interface."
ms.custom: ""
ms.date: 12/07/2020
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

### What is Unified Interface?

Unified Interface for model-driven apps provides a consistent and accessible user experience across devices. It is the latest look and feel of all model-driven apps and Dynamics 365 apps such as Dynamics 365 Sales and Dynamics 365 Customer Service. More information: [Enhanced user experience with the Unified Interface for model-driven apps](/powerapps/user/unified-interface).


### Why should I move to Unified Interface?

Microsoft's vision of a productive workplace requires a modern interface that includes the features and improvements contained in Unified Interface, which provides a more consistent user experience, improved performance and increased user efficiency. For more information, see [Unified Interface playbook.](https://docs.microsoft.com/powerapps/maker/model-driven-apps/unified-interface-playbook)

### Are my ISVs compatible?

ISVs (Independent Software Vendors) such as third-parties listed on [Microsoft AppSource](https://appsource.microsoft.com/en-us/?product=dynamics-365-business-central%3Bdynamics-365-customer-insights%3Bdynamics-365-for-customer-services%3Bdynamics-365-for-field-services%3Bdynamics-365-for-finance-and-operations%3Bdynamics-365-for-project-service-automation%3Bdynamics-365-for-sales) have been notified to take action on the transition to Unified Interface. Contact your ISV directly regarding their timeline for Unified Interface compatibility.

### What is the retraining effort?

From a technology standpoint, the retraining should be minimal as your business logic and schema remain unchanged. Retraining should focus on what's new within the navigation and the overall look and feel. Further training may be required if you have made a business decision to alter the design to optimize for the new capabilities and features.

### Will I need to re-create my solution customizations?

No, you should not have to recreate any customizations, provided you have followed the [Microsoft Dataverse Developer Guide](/powerapps/developer/data-platform/overview) and kept up to date with any changes. However, there may be new opportunities to take on our latest investments that could lead to customization alterations.

### How long will it take to transition/what is the work effort?

The work effort here will vary based upon the complexity of your environment. We recommend getting started with a pilot/POC model-driven app to begin testing. From there, you can work with the business to plan a full Unified Interface rollout. See the [Unified Interface Playbook](https://docs.microsoft.com/powerapps/maker/model-driven-apps/unified-interface-playbook) and [planning checklist](https://aka.ms/UIChecklist) for additional guidance on getting started and our [white paper](https://download.microsoft.com/download/A/F/3/AF3D45A7-4F38-41BE-8956-1DF7A4A5AFDB/approaching-unified-interface-transition.pdf).

### As an on-premises customer looking to move to the cloud, what is the best approach to adopt Unified Interface?

It is highly recommended to plan your move to Unified Interface at the same time as you migrate to the cloud. Begin testing of your legacy web client within Unified Interface and once migrated, confirmed Unified Interface compatibility before you release to your user community. This will reduce the training effort and allow users to adopt some of the new features and capabilities Unified Interface has to offer. For more information, please speak with your Microsoft representative.

### When will ISVs be notified of the need to move to Unified Interface?

ISVs (Independent Software Vendors) such as third-parties listed on [Microsoft AppSource](https://appsource.microsoft.com/en-us/?product=dynamics-365-business-central%3Bdynamics-365-customer-insights%3Bdynamics-365-for-customer-services%3Bdynamics-365-for-field-services%3Bdynamics-365-for-finance-and-operations%3Bdynamics-365-for-project-service-automation%3Bdynamics-365-for-sales) have been notified to take action on the transition to Unified Interface. Contact your ISV directly regarding their timeline for Unified Interface compatibility.

### How are language translations handled?

The process for language translation is primarily unchanged, with the exception of the sitemap. Sitemap areas, groups, and subareas are localized within the sitemap editor.

### I don't have budget or resources to do a project. Is the deadline a fixed date?

The official deprecation date is December 4, 2020 and this is a fixed date. After this date, we will start to automatically transition environments based upon geographic location. Depending on your location, you may have some extra time available before the legacy web client is removed. We recommend conducting some testing as soon as possible to understand the complexity of the project for your organization to get compatible. In most cases, extensive redesign should not be required to move forward quickly and start seeing user benefit. Contact Microsoft to provide any feedback that could stop your transition by creating a support case.

### We're working on transitioning to Unified Interface, but have hit some issues; how can we report to Microsoft?

Review our [resources](https://community.dynamics.com/365/unified-interface/) to help with guidance and log a support case following your standard procedure. You can also notify your partner, Microsoft representative, or FastTrack team (if applicable).

### When should I start moving to Unified Interface?

You can move right away; we already have many customers transitioned in production to Unified Interface. Complete your testing as soon as possible. Access our Community site: <https://community.dynamics.com/365/unified-interface/> for helpful content. Use the Standard Support procedure to log any issues.

### What happens to my environment after the December 4, 2020 deadline passes?

If you are still using the legacy web client on December 4, 2020, we will automatically transition your environment/organization to Unified Interface. This process will be applied by geographic location in alignment with a typical update cycle time frame. Customers should have already received communication on their final transition date but it is also available within the Unified Interface portal. To access, use the following steps:

1.	Visit <https://runone.powerappsportals.com>.
2.	Sign in with the admin credentials of the tenant you want to manage.
3.	Select **My Environments**, and review the final transition date associated to each environment.


We don't expect any downtime with the transition process, but you must ensure that your environment is compatible. For more information, see [Checklist: Unified Interface transition](/powerapps/maker/model-driven-apps/checklist-transition-unified-interface).

### I have a new feature idea for Unified Interface; where do I log it?

Visit our ideas portal (<https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas>), select **Suggest an idea**, and label the item with the 'Unified Interface' category.

### Is there any supporting content to help me plan and execute my transition to Unified Interface?

Yes, we have a new community group (<https://community.dynamics.com/365/unified-interface/>) that provides useful content, interactive forum, and blog to see all the latest updates and information about Unified Interface.

### How does the December 4 deprecation date impact on-premises customers?

This announcement is only in effect for online customers at present. We will update our [deprecation notification page](/power-platform/important-changes-coming) on any further updates.

### Is the timeline applicable for customers using Government Community Cloud (GCC) and other data centers such as China?

We plan to release Unified Interface updates to these data centers as part of the standard release program.

### What action should I take as a Unified Service Desk customer who is still on the web client?

The Unified Service Desk customers, who are still on the web client, need to migrate their configurations from web client to Unified Interface. This will necessitate upgrade to the latest versions of the [Unified Service Desk](https://docs.microsoft.com/dynamics365/unified-service-desk/download-unified-service-desk?view=dynamics-usd-4.1) (both client and server components). We have a [migration assistant](https://docs.microsoft.com/dynamics365/unified-service-desk/admin/migration-steps-web-client-unified-interface-configuration?view=dynamics-usd-4.1) to help with this effort.

### Are there any other deprecations that I should plan for?

Review our [deprecation notification page](https://docs.microsoft.com/power-platform/important-changes-coming) to identify if there are any other areas that also require planning.


## FAQs: Transitioning to Unified Interface

### Within the transition portal, I can see a final transition date that is after December 4, 2020. What does this mean?

If you are still using the legacy web client after December 4, 2020, we will automatically transition your environment to Unified Interface. This process will be applied by geographic location. The **Final Transition Date** column indicates when we expect this to happen. All the dates are shown in the MM/DD/YYYY format. Consider it the last date when the legacy web client will be available for your environment. We strongly discourage any customers delaying the transition until the last minute. The legacy web client will no longer be available to users after the final transition date. So, there won't be any opportunity to switch back and continue testing should you run into any issues after this date.

### Where can I go to see the final transition dates for my environment? 

Use the transition portal to review the final transition date for your environment.

1.	Visit <https://runone.powerappsportals.com>.
2.	Sign in with the admin credentials of the tenant you want to manage.
3.	Select **My Environments**, and review the final transition date associated to each environment.

### Do I need to wait until my final transition date to make the move to Unified Interface?

You don't need to wait. We recommend that you make the move prior to the final date. You can [switch manually](/powerapps/maker/model-driven-apps/transition-web-app) at any point prior to your environment final transition date.

### Is there a recommended checklist I should run through before transition?

Check out the supporting content available on the [community site](https://community.dynamics.com/365/unified-interface/). We also have a [transition checklist](https://aka.ms/UIChecklist) to help you plan effectively. Review it carefully to ensure that you are comfortable with the transition to Unified Interface.

### My environment is transitioned, but I am finding blocking issues for my users and want to move back to the legacy web client. Is this possible?

If you have manually transitioned, and it is prior to the final transition date for your environment, then it is possible to switch back to the legacy web client. You can make the [switch manually](https://docs.microsoft.com/power-platform/admin/enable-unified-interface-only) for the first 10 days or raise a [standard support request](https://admin.powerplatform.microsoft.com/support?referer=mbssupport) and set the problem type to be "Transition from legacy web client to Unified Interface" as the manual switch will be disabled. 

> [!NOTE]
> The ability to toggle back to the legacy web client is only possible until the final transition date. After that point it will no longer be available.

### I want to transition after December 4, 2020. Is that possible?

If you haven't transitioned before December 4, 2020, you will be automatically switched to Unified Interface. This will be applied dependent on your environment location over a multi-week schedule. To view the final transition date for your environment, use the portal (<https://runone.powerappsportals.com>). After the final transition date, the legacy web client won't be available. We don't have the ability to defer the date beyond the final date.

If you face any blocking items, log them using your standard support process as soon as possible. For more information, see this blog: [Unified Interface transition starts December 4 2020](https://powerapps.microsoft.com/en-us/blog/unified-interface-transition-starts-december-4th-2020/).


### What is the standard reminder procedure throughout this process?

As your environment approaches the final transition date, we will provide two reminder messages and a confirmation message post transition. Microsoft will send the following communication:

-    Initial message for each environment to remind the date is approaching.
-    There will be a further reminder two days before the date arrives. 
-    Post transition, there will be a closing message to confirm success (or if an issue occurred and what next steps we will take)

Messages can be seen using the following channels:
-    Message Center within the Microsoft 365 Tenant. This is typically visible to roles such as Global Admin, Service Admin, and Service Message Reader.
-    Direct e-mail.  Emails are sent only to the system administrator role for the specific environment in question, or email addresses that have been added to the **Notification** tab in the environment admin portal.

> [!NOTE]
> Administrators will receive this message for each production environment associated to their profile. This could result in multiple reminder messages.

### Is there a specific day and time when approved transitions will take place?

We don't anticipate any downtime when making this transition. However, we will only make a transition in alignment with our [maintenance timeline](/power-platform/admin/policies-communications#maintenance-timeline). We will send a communication about the transition (success or failure) the following Monday starting at 9:00 AM Pacific Time.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]