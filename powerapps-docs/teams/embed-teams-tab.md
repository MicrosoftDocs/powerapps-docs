---
title: Embed a canvas app as tab app | Microsoft Docs
description: Learn how to add an app to a Microsoft Teams channel using the PowerApps tab so that people you've shared the app with can open it in that channel.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 09/15/2020
ms.author: mkaur
ms.custom: intro-internal
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Embed a canvas app as tab app in Teams

You can customize the Teams experience by adding Power Apps canvas apps to your channels in Teams using the **PowerApps** tab. In this topic, you learn how to add the Product Showcase sample app to a Teams channel, and then open the app from that channel. 

![App embedded in Microsoft Teams.](media/open-app-embedded-in-teams/embedded-app.png "App embedded in Microsoft Teams")

If you're not signed up for Power Apps, [sign up for free](https://make.powerapps.com/signup?redirect=marketing&email=) before you begin.

## Prerequisites

To follow this procedure, you need an [Office 365 subscription](https://signup.microsoft.com/Signup?OfferId=467eab54-127b-42d3-b046-3844b860bebf&dl=O365_BUSINESS_PREMIUM&ali=1) and a [channel in Teams](https://www.youtube.com/watch?v=he2f1quaR7M).

## Sign in to Power Apps

Sign into Power Apps at [https://make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## Add an app

1. In Microsoft Teams, select a team, and a channel under that team. In this example, it's the **General** channel under the **Business Development** team.

    ![Select General channel.](media/open-app-embedded-in-teams/teams-select-channel.png "Select General channel")

2. Choose **+** to add a tab.

    ![Select +.](media/open-app-embedded-in-teams/teams-add-tab.png "Select +")

3. In the **Add a tab** dialog box, choose **Power Apps**.

    ![Select Add a tab.](media/open-app-embedded-in-teams/add-a-tab.png "Select Add a tab")

4. Choose **Sample apps** > **Product Showcase** > **Save**.

    ![Select Product Showcase and Save.](media/open-app-embedded-in-teams/select-an-app.png "Select Product Showcase and Save")

    The app is now available to use in the channel.

    ![App shows up in channel.](media/open-app-embedded-in-teams/app-in-channel.png "App shows up in channel")

> [!NOTE]
> You must [share](../maker/canvas-apps/share-app.md) your own apps before you add them to Teams (sample apps are shared by default).

## Open an app

1. In Microsoft Teams, choose the team and the channel that contains the app.

    ![Select General in Teams under your team.](media/open-app-embedded-in-teams/teams-select-channel.png "Select General in Teams under your team")

2. Choose the **Product Showcase** tab.

    ![Select Product Showcase tab.](media/open-app-embedded-in-teams/open-tab.png "Select Product Showcase tab")

    The app opens in the channel.

    ![App opens.](media/open-app-embedded-in-teams/app-in-channel.png "App opens")

## Known issues

In the desktop app for Microsoft Teams:

* Apps must load content such as images and .pdf files over a secure (https) connection.
* Not all sensors, such as **Acceleration**, **Compass**, and **Location**, are supported.
* Only these audio formats are supported: AAC, H264, OGG Vorbis, and WAV.

## Clean up resources

To remove the app from the channel, choose the **Product Showcase** tab > **Remove**.


[!INCLUDE[footer-include](../includes/footer-banner.md)]