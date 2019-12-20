---
title: "FAQs: Transition to Unified Interface | MicrosoftDocs"
description: "FAQs related to the transition process for moving users from the legacy web client to Unified Interface."
ms.custom: ""
ms.date: 12/20/2019
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

This topic provides answers to the most common questions about the transition options for moving users from the legacy web client to Unified Interface.

### Where can I go to see the transition dates that have been suggested for my environments? 

Use the transition portal to manage your environment transition date: <https://runone.powerappsportals.com>.

### How do I gain access to the portal?

Do the following:
1. Visit <https://runone.powerappsportals.com>.
2. Sign in with the admin credentials of the tenant you want to manage.
3. Select **My Environments**, and review all environments that have a suggested date applied.

### I see my environment has a date suggested for transition. Can I change this date?

Yes, this is possible if you have the **global admin**, **Dynamics 365 service administrator**, or **Power Platform administrator** role for the tenant. 

The dates associated to your environment is a suggestion that requires approval to go ahead. Please approve if the date works for your organization.  

To change the date, select the drop-down icon next to the environment and view the record. Tenant admin roles will then be able to reschedule the transition date to an earlier or later date.

To reschedule to an earlier date, update the existing date to your preferred option in the list. You can also [switch manually](transition-web-app.md) if our dates are not suitable. 
 
To schedule to a later date, select the reschedule transition date button. Suggested dates will be available in the drop down. Once approved, the date will be updated in the portal accordingly. Please then accept the updated date if you would like your environment to be transitioned. 
 
Date changes will be reviewed and granted if the date is prior to October 1, 2020. The date will be updated within the portal once confirmed. 

> [!NOTE]
> If you have an approved transition and the scheduled date is within 48 hours, you’ll not be able to change the date. Likewise, you can’t request a date after October 1, 2020 as the legacy web client will no longer be available then.

### What will happen if I don't opt in and approve a suggested transition date for my environment?

There won't be any change to your environment if you haven't approved the suggested date within the portal. When the suggested date passes, we'll look to provide another date in the future for you to consider.  
 
> [!NOTE]
> After October 1, 2020, all environments will be updated to Unified Interface as per the October 2020 release wave.

### My transition date is within 48 hours and I can’t change the date within the portal. How can I stop the transition from taking place?

The ability to change the transition date for an environment is available only until 48 hours prior to transition. To stop the process after this period, raise a support case. 

> [!NOTE]
> We can't guarantee the transition can be stopped if the request is made after the date has been locked on the portal (48 hrs or less).

### I have environments without a scheduled date. Can I update these to include a date?

Yes, if you have a **global admin**, **Dynamics 365 service administrator**, or **Power Platform administrator** role for the tenant, select the environment, and select a date by clicking on the reschedule transition date button.

We will update the portal with the date to confirm. Notification e-mails will also be sent to the global tenant admins as you get close to the transition date. This will follow the standard reminder procedure detailed within this document.

### Is there a recommended checklist I should run through before transition?

Check out the supporting content available on the [community site](https://community.dynamics.com/365/unified-interface/). We also have a [transition checklist](https://aka.ms/UIChecklist) to help you plan effectively. Review it carefully to ensure that you are comfortable with the transition to Unified Interface.

### My environment has been transitioned, but I am finding blocking issues for my users and want to move back to the legacy web client. Is this possible?

Yes, you will still be able to switch back to the legacy web client for up to 10 days post transition. You can make the [switch manually](https://docs.microsoft.com/power-platform/admin/enable-unified-interface-only) for the first 4 days or after that point, raise a support request from your usual channel as the manual switch will be disabled. 

> [!NOTE]
> The 10 days need to be prior to October 1, 2020 as the legacy web client will no longer be available after that date.

### I want to transition after October 1, 2020. Is that possible?

The legacy web client won't be available post the October 2020 release wave for end users. We don't have the ability to defer the date beyond that period.

If you encounter any blocking items, log them using your standard support process as soon as possible.

### What is the standard reminder procedure throughout this process?

Communication will be in waves, at least 30 days prior to the suggested timeframe, but you can sign in to the portal (<https://runone.powerappsportals.com>) at any time to view the status. Microsoft will send the following communication:

-	Initial message for each environment that has a suggested transition date.
-	If you have approved the date, you will receive a reminder message 2 days before the dates are locked within the portal. 
-	Final reminder will be sent 2 days before the transition. This will state the transition date is locked and will go ahead with the transition.
-	Post transition, there will be a closing message to confirm success (or if an issue occurred)

Messages can be seen using the following channels:
-	Message Center within the Microsoft 365 Tenant. This is typically visible to roles such as Global Admin, Service Admin, Service Message Reader.
-	Direct e-mail.  Emails are sent only to the system administrator role for the specific environment in question, or email addresses that have been added to the "Notification" tab in the environment admin portal.

> [!NOTE]
> You will receive an e-mail for each environment where your user account has the system administrator role.

### I have requested a date to postpone but still receiving e-mails and Message Center posts that my environment is set to transition. Should I be concerned?

Our first recommendation is to check the transition portal (<https://runone.powerappsportals.com/>) as this will be the single source of truth for all of your environments. If the date is updated, then it is highly likely that our communication system sent the message before we updated the communications list. 

If the date in the portal isn’t updated to your new date, raise a support request following your standard procedure.

Only admin-approved dates will be transitioned. 

### If I already have an environment transitioned to Unified Interface, will I still be able to switch back to the legacy web client manually?

If your environment has been transitioned for at least 4 days, we will look to disable the manual switch back to the legacy web client. 

If you find this has been disabled and have a requirement to switch back, raise a support request from your usual channel for evaluation.

### Is there a specific day and time when approved transitions will take place? 

We don't anticipate any downtime when making this transition. However, we will only make a transition on a Friday, following the same maintenance timelines outlined within our standard policies and communications. More information: [Maintenance timeline
](https://docs.microsoft.com/power-platform/admin/policies-communications#maintenance-timeline)

### Are environments from all data centers included within this transition service?

At present, environments from specific data centers, such as Government Community Cloud (GCC), have not been included within the portal. We are looking to provide some suggested transition dates for these by June, 2020. Customers who want to make the move to Unified Interface can always [switch manually](/power-platform/admin/enable-unified-interface-only#how-to-enable-unified-interface-only-mode) at any time before October 1, 2020.


