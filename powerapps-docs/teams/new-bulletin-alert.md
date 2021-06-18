---
title: Send an alert when a new bulletin is posted
description: Learn about how to send an alert when a new bulletin is posted
author: sbahl10
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/18/2021
ms.author: v-shrutibahl
ms.reviewer: tapanm
contributors:
    - v-ljoel
---

# Bulletins App – Send an alert when a new bulletin is posted

The Bulletins Power App Template for Microsoft Teams provides a central location for all company communication such as broadcasts, memos, announcements, and company news. The app allows you to create, categorize, bookmark, search and read bulletin posts.

The Bulletins app solution consists of two apps:

[**Manage bulletins app**](https://docs.microsoft.com/en-us/powerapps/teams/bulletins#manage-bulletins-app)

-   Manager experience for managing **Bulletins** app.

-   Allows managers to create, edit, and categorize posts read through the Bulletins app.

[**Bulletins app**](https://docs.microsoft.com/en-us/powerapps/teams/bulletins#bulletins-app)

-   Central location for all company communication such as memos, broadcasts, and news.
    
-   Shows bulletins, FAQs, links, and contacts created using the **Manage bulletins** app.

In this topic we will learn how to send an email notification using Power Automate flow, when a new bulletin is created.

> NOTE: before starting this topic, please review **How to customize Bulletins** (insert link).

## Prerequisites

To complete this lesson, we would need the ability to login into Microsoft Teams which will be available as part of select Microsoft 365 subscriptions and will also need to have the Bulletins Power Apps template for Microsoft Teams installed. This app can be installed from aka.ms/TeamsBulletins (confirm link).

## Create Power Automate Flow to send email notification

We will create a flow to send the email notification. Power Automate makes sending emails easy, and since a flow can be triggered automatically when
records are created, the email will be sent whenever a bulletin is added.

1.  Login into flow.microsoft.com.

2.  On the top right, select the environment with the same name as the team where the Bulletins app is installed.
    
3.  Select +Create from the left navigation menu.

4.  Select Automated cloud flow under the Start from blank options.

5.  Enter Flow name – Send email notification when a new bulletin is added.

6.  Look for the trigger and select – When a new row is added, modified or deleted (Microsoft Dataverse).
    
7.  Hit the Create button.

8.  The flow screen opens.

9. In the trigger box, select

   - Change type = Create

   - Table name = Bulletins

   - Scope = Organization

![](media/new-bulletin-alert/bulletin-alert-flow-trigger.png)

10. Select +New step.

11. Look for and select the Action – Send an email (V2) (Office 365 Outlook).

12. In the To field enter the email address you would like to send notifications to. For example, if you want all people in a team to be notified, you could create an email with the address for the team channel. To find this email address, select the three dots by the team channel and select **Get email
    address.** 

![Get Team Channel's email address](media/new-bulletin-alert/get-email-address.png "Get Team Channel's email address")

13. In the Subject field enter – New Bulletin created

14. In the Body, we can display any details we would like to. To keep it simple, you could enter –

```
A new Bulletin board {select Title from dynamic content} ({select Subtitle from dynamic content}) was added.
```

![Send email flow step](media/new-bulletin-alert/send-email-flow-step.png "Send email flow step")

>   NOTE: you can also add a hyperlink to the Bulletin app. To do this go to the team in which Bulletins is installed, open the app tab, then select the pop
>   out button to open the app in a new window. The URL of the app is in URL field for this window, and you can use this as a hyperlink in your email.

## Test the app

1.  Log in Microsoft Teams and navigate to Team where the Bulletins app is installed.
    
2.  Select the Manage Bulletins tab on the top.

3.  Navigate to the Bulletins tab.

4.  Select the New Bulletin button on the top right.

5.  The New bulletin screen appears.

6.  Select the Category for which you want the bulletin created.

7.  Enter a title in the Add title text box – Upcoming Offers.

8.  Enter a subtitle in the Add subtitle text box – Summer offers for customers.

9.  Enter a description in the big text box – This Bulletin will list all the upcoming summer offers for customers.
    
10. Hit the Save button on top.

11. Then hit the Publish button.

12.  In a few minutes, an email as shown in the image below should appear in the inbox of the email address provided in the Power Automate flow.

![New Bulletin Email alert screenshot](media/new-bulletin-alert/new-bulletin-email-screenshot.png "New Bulletin Email alert screenshot")
