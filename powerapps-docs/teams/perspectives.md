---
title: Perspectives (preview) sample app
description: Learn how to use the Perspectives app.
author: Joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/24/2021
ms.subservice: teams
ms.author: jshum
ms.reviewer: tapanm-msft
contributors:
  - joel-lindstrom
  - josephshum
  - tapanm-msft
---

# Perspectives (preview) sample app

[This article is pre-release documentation and is subject to change.]

In this tutorial, you'll learn about configuring and using the **Perspectives** sample app.

## Overview

The Perspectives sample app template for Microsoft Teams provides a simple way to add topics and extend the topics with Q&A where anyone in the organization can have a perspective about the topics, and have a discussion about them in Teams.

Benefits of using the Perspectives app:

-   Create discussions. 
-   Interact with colleagues.
-   Find interesting discussions.
-   Flag recommended discussions.

> [!NOTE]
> - Before you can use this app, you may be asked for your permissions to use the connection. More information: [Allow connections in sample apps](use-sample-apps-from-teams-store.md#step-1---allow-connections)
> - This app is available in three different Teams themes: Default, Dark and High contrast. When you [change the theme in Teams](https://support.microsoft.com/en-us/office/change-settings-in-teams-b506e8f1-1a96-4cf1-8c6b-b6ed4f424bc7), the app automatically updates to match the selected theme. More information: [Get the Teams theme using the Teams integration object](use-teams-integration-object.md#get-the-teams-theme)

> [!IMPORTANT]
>-   This is a preview feature.
>-   Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

Before using this app:

1. Install the app by side-loading the app manifest into Teams. You can get the app manifest at https://aka.ms/TeamsPerspectives. For more information and help with installing this app, read the documentation available with the app manifest.

2. Set up the app for the first use.


## Using Perspectives app

In this section, you'll learn about the following capabilities in the Perspectives app:

- [Open the Perspectives app](#open-the-perspectives-app)
- [Understanding the Perspectives app interface](#understanding-the-perspectives-app-interface)
- [Add a topic](#add-a-topic)
- [Find a topic](#find-a-topic)
- [View discussions](#view-discussions)
- [Add a discussion](#add-a-discussion)
- [Add a response](#add-a-response)
- [Edit a response](#edit-a-response)
- [Edit the Perspectives app in Power Apps](#edit-the-perspectives-app-in-power-apps)



## Open the Perspectives app

To open the Perspectives app:

1. Sign in to Teams.

2. Select the Team in which the app is installed.

3. Select the channel where you installed the **Perspectives** app.

4. Select the **Perspectives** tab.

5. Select **Allow** if the app asks for your permissions to use the connectors.

## Understanding the Perspectives app interface

The Perspectives app is a place to listen and be heard in your organization. A simple search-and-browse experience makes it easy to find interesting discussions, whether you're looking to share your perspective or tap into the collective knowledge of your team.

The most relevant content rises to the top when team members up-vote a response or the discussion's creator flags one as Recommended.  The app can be used for employee engagement, diversity and inclusion efforts, support systems, process Q&As, and more. 

![Perspectives main screen.](media/perspectives/perspectives-main-screen.png "Perspectives main screen")

 Let's explore the primary functions of the Perspectives app.

## Add a Topic

Do you have a topic that you would like to discuss? Add a topic to get started.

1. In Teams, navigate to the team in which Perspectives is installed.

2. Select the Perspectives tab.

3. Select **Add a Topic**. 

4. Enter the title. 

5. Add description.

6. Select an image or an icon. 

   ![Enter topic information.](media/perspectives/add-topic-screen.png "Add topic screen")

7. Select **Save**.

 



## Find a topic

If you want to find topics that interest you, you can search for them using the following steps:

1. In the Perspectives app, select the **Find a Topic** search field.

2. Enter the name of the discussion you want to find.

3. Topics that match the search words will be displayed. Select the Topic you want.



## Edit a topic

If you want to change the name of a topic, you can rename it with the following steps:

1. Select a Topic.

2. Select Edit. 

3. Change the title and description.

4. Select the Image.

5.  Select **Save**.

## View discussions

You can view the discussions in a topic using the following steps:

1. From the Perspectives app, select a topic.
2.  View the discussions in the topic.




## Add a discussion

Within a topic, you can have multiple discussions. A discussion is a question or conversation starter. Other users respond to the discussion by adding perspectives.

![Topic screen displaying discussions.](media/perspectives/discussion-screen.png "Discussion Screen")

 You can add new discussions using the following steps:

1. Select a Topic.

2. Select **New Discussion**.

3. Enter Title.

4. Enter Context. 

5. Select **Save**.

    ![Screen to add a new discussion.](media/perspectives/begin-a-new-discussion.png "Begin a new discussion")

  

 

## Add a response

Responses to discussions are displayed in a familiar conversation thread. You can add responses to a discussion using the following steps:

3. In the Boards app, select a topic.

4. Select a discussion.

5. Select **Add a response.**

   ![The add a response button on the discussion screen.](media/perspectives/add-response-button.png "Add response button")

6. Add relevant text to put your perspective for the discussion.

7. Select **Add**. 
   



## Edit a response

You can Edit your response using the following steps:

1. In the Perspectives app, select a topic.

2. Select a discussion.

3. Select a response that you've added.

4. Select Edit.

5. Select **Update**.  

​             

## Edit the Perspectives app in Power Apps

1. In Teams, add the Power Apps app from the Teams store by selecting the ellipses in the app menu, searching for Power Apps, and then selecting **Install.**

2. Right-click on Power Apps icon and select **Pop out app** to open the app in a new window. This pop-out action will ensure that you don't lose your changes if you navigate somewhere else in Teams.

   ![Power Apps main screen in Teams.](media/perspectives/power-apps-first-screen.png "Power Apps first screen")

3. Select **Build** tab.

4. Select the team in which the Perspectives app is installed, then select **Installed apps.**

5. In the Boards tile, select the **Perspectives** app to open it in Power Apps in Team.

   ![The Perspectives app in Power Apps.](media/perspectives/perspectives-tile.PNG)

6. You may get prompted to authorize the app's connectors to connect. Select **Allow**.

7. From here, you can customize the app. ![Perspectives app open in Power Apps studio.](media/perspectives/power-apps-screen.png "Power Apps Screen")

### See also

- [Understand Perspectives (preview) sample app architecture](perspectives-architecture.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]