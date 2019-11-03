---
title: "FAQs: Unified Interface transition | MicrosoftDocs"
description: "FAQs related to the auto-transition process for moving users from the legacy web client to Unified Interface."
ms.custom: ""
ms.date: 11/04/2019
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

# FAQs: Unified Interface transition

This topic provides answers to the most common questions about the transition process for moving users from the legacy web client to Unified Interface.

### Where can I go to see the transition dates that have been assigned to my environments? 

Use the auto-transition portal to manage your environment transition date: <https://runone.powerappsportals.com>.

### How do I gain access to the portal?

Do the following:
1. Visit <https://runone.powerappsportals.com>.
2. Sign in with the admin credentials of the tenant you want to manage.
3. Select **My Environements**, and review all environments that have a target date assigned.

### I see my environment has a date for auto transition. Can I change this date?

Yes, this is possible if you have the **Global admin** or **Service admin** role for the tenant. To change the date, select the drop-down icon next to the environment and view the record. Tenant admin roles will then be able to submit an exception request for an earlier or later transition date.

- For an earlier transition date, update the existing date to your preferred option in the list. This doesn’t require approval. You can also switch manually if our dates are not suitable.

- For a later transition date, you can submit an exception request. Suggested dates will be available in the drop down. Once approved, the date will update in the portal accordingly.

You can request a total of two exceptions per environment. Exceptions are granted based on the business justification alongside the proposed date selected. The date will be updated within the portal once confirmed.

> [!NOTE]
> If the scheduled transition is within 48 hours, you’ll not be able to change the date. Likewise, you can’t request a date after October 1, 2020 as the legacy web client will no longer be available.

### My auto transition date is within 48 hours and I can’t change the date within the portal. How can I stop transition taking place?

The ability to change the transition date for an environment is available only until 48 hours prior to transition. To stop the process after this period, raise a support case. 

> [!NOTE]
> We can't guarantee the transition can be stopped if the request is made after the date has been locked on the portal (48 hrs or less).

### I have environments without a target auto-transition date. Can I update these to include a date?

Yes, if you have a **Global admin** or **Service admin** for the tenant, select the environment, submit an exception request, and update with your proposed time frame using the target date list. 

We will update the portal with the date to confirm. Notification e-mails will also be sent to the global tenant admins as you get close to the transition date. This will follow the standard reminder procedure detailed within this document.

### Is there a recommended checklist I should run through before transition?

Check out the supporting content available on the [community site](https://community.dynamics.com/365/unified-interface/). We also have a [transition checklist](https://aka.ms/UIChecklist) to help you plan effectively. Review it carefully to ensure that you are comfortable with the transition to Unified Interface.

### My environment has been transitioned, but I am finding blocking issues for my users and wish to move back to the legacy web client. Is this possible?

Yes, you will still be able to switch back to the legacy web client for up to 10 days post transition. You can make the [switch manually](https://docs.microsoft.com/power-platform/admin/enable-unified-interface-only) for the first 4 days or after that point, raise a support request from your usual channel as the manual switch will be disabled. 

> [!NOTE]
> The 10 days need to be prior to October 1, 2020 as the legacy web client will no longer be available after that date.

### I want to transition after October 1, 2020. Is that possible?

The legacy web client available won't be available post October 1, 2020. We don't have the ability to defer the transition beyond that date.

If you encounter any blocking items, log them using your standard support process as soon as possible.

### What is the standard reminder procedure throughout this process?

Microsoft will send the following communication:

-	Initial message for each environment that has a transition date assigned
-	Reminder message 2 days before the dates are locked within the portal
-	Final reminder to state the transition date is locked and will go ahead.
-	Closing message to confirm success (or if an issue occurred)

Messages can be seen using the following channels:
-	Message Center within the Microsoft 365 Tenant. This is typically visible to roles such as Global Admin, Service Admin, Service Message Reader.
-	Direct e-mail.  Emails are sent only to the system administrator role for the specific environment in question, or email addresses that have been added to the "Notification" tab in the environment admin portal.

> [!NOTE]
> You will receive an e-mail for each environment where your user account has the system administrator role.

### I have requested a date to postpone but still receiving e-mails and Message Center posts that my environment is set to transition. Should I be concerned?

Our first recommendation is to check the transition portal (<https://runone.powerappsportals.com/>) as this will be the single source of truth for all of your environments. If the date is updated, then it is highly likely that our communication system sent the message before we updated the communications list. 

If the date in the portal isn’t updated to your new date, raise a support request following your standard procedure.

### If I already have an environment transitioned to Unified Interface, will I still be able to switch back to the legacy web client manually?

If your environment has been transitioned for at least 4 days, we will look to disable the manual switch back to the legacy web client. 

If you find this has been disabled and have a requirement to switch back, raise a support request from your usual channel for evaluation.



