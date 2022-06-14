---
title: "Create and join a Teams meeting from an appointment| MicrosoftDocs"
description: Create and join a Teams meeting from an appointment
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 6/10/2022
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Create and join a Teams meeting from an appointment 

Now you can create and join a Teams meeting from an appointment in your model-driven app.


> [!div class="mx-imgBorder"] 
> ![The diagram shows how to add a Teams meeting to an appointment and then join the meeting.](media/teams-meeting-in-appt.gif)


## Prerequisites

Your system administrator will need to enable the following items: 

- Turn on the **Collaboration (preview)** feature called **End users can add and join Teams meeting from appointments in model-driven apps** for your environment. More information: [Manage feature settings](/power-platform/admin/settings-features).
- Set up server side-sync for appointments. More information: [Set up server-side synchronization of email, appointments, contacts, and tasks](/power-platform/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks). Note, once server side-sync is setup it takes a few minutes for your meetings to sync between your app and Teams.

> [!NOTE]
> When this feature is enabled, the **Description** field in appointments also supports editing and viewing in rich text.

## Add a Teams meeting to an appointment 

1. From the left navigation pane, select **Activities**.
2. From the list of activities, select an existing appointment or select **Appointment** on the command bar to create a new one.
   > [!div class="mx-imgBorder"] 
   > ![Open or create a new appointment.](media/teams-meeting-appt.png)   
4. Enter the required information and in the **Details** section, set the **Teams meeting** toggle to, **Yes**.
   > [!div class="mx-imgBorder"] 
   > ![Add a Teams meeting to an appointment.](media/teams-meeting-appt-1.png)  
6. When you're done, select **Save**.
> [!NOTE]
> It may take a couple of minutes for the meeting to sync with Outlook and for the meeting link to appear in the appoitnment.

## Join a Teams meeting from an appointment

1. Open an appointment activity. 
2. Choose one of the following ways to join the meeting:
     - On the command bar select, **Join Teams Meeting**.
     - From the **Details** section, select the **Join Teams Meeting** link. 
     - Scroll down the **Description** section of the appointment and select, **Click here to join the meeting**.
     
       > [!div class="mx-imgBorder"] 
       > ![Join a Teams meeting from an appointment.](media/teams-meeting-appt-2.png)  

3. Follow the instructions on your screen and choose how you want to join the Teams meeting. 
   > [!div class="mx-imgBorder"] 
   > ![Choose how you want to join the Teams meeting.](media/teams-meeting-appt-3.png)  

