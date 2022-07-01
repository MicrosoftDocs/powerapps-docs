---
title: "App ratings for Model-driven-apps | MicrosoftDocs"
description: Understand ratings for model-driven apps. 
ms.custom: ""
ms.date: 07/04/2022
ms.reviewer: "matp"

ms.topic: overview
author: "yogupt"
ms.subservice: common
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker, admin
search.app: 
  - PowerApps
---
# What are app ratings? (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

End users of Power Apps provide feedback for apps they use. With app ratings feature, we enable our makers and administrators to view the app’s satisfaction score and comments provided by end users. The collection of feedback is compliant with all international privacy laws. The feature also provides action to improve your app by navigating to solution checker, performance insights, live monitoring, and usability recommendations.

:::image type="content" source="media/app-ratings-overview.png" alt-text="Ratings feature image":::

>[!NOTE]
>This feature is currently only available for model-driven Power Apps.

This feature provides a view of [app satisfaction score](#what-is-an-app-satisfaction-score) on scale of 0 to 200, provides a [score trend](#how-does-score-trend-work) over last 90 days, displays different score [based on web or mobile device](#app-satisfaction-by-device) and [based on different browsers](#app-satisfaction-by-browser) as well.

The report for current score and comments can be exported per app in the app ratings dashboard to share with more stakeholders.

## How to access? 

1. Sign in to [Power Apps](https://make.powerapps.com). 

1. On the left navigation pane, select **Apps**, and then select a model-driven app.

1. Use the **...** context menu or command bar to select **Ratings (Preview)**.

:::image type="content" source="media/ratings-option.png" alt-text="Ratings option image":::

## How does Power Apps capture end user satisfaction?

Based on user’s activity inside the app, Microsoft Power Apps asks users to score the app with following question below:

1. How satisfied are you with (name of the app)?
-	Very satisfied
-	Satisfied
-	Dissatisfied
-	Very Dissatisfied

2. What can we do to improve?

:::image type="content" source="media/app-satisfaction-dialog.png" alt-text="App satisfaction dialog image":::

Based on the feedback above, we display [app satisfaction score](#what-is-an-app-satisfaction-score) and comments in ratings dashboard.

We follow the guidelines below while prompting feedback dialog:
-	If a user has at least 3 active days during the first 14 days since sign-up, the user will be prompted.
-	If the user has 6 active days in the last (recent) 90 days, the user will be prompted.
-	No users can be prompted more than once in 90 days for the same app/product.

## What is an app satisfaction score?
App satisfaction score is calculated by taking the responses with an answer "Very Satisfied" and subtracting out the percentage of the responses with an answer "Dissatisfied" or "Very Dissatisfied". The total NSAT score is then calculated like this:

>100 + (%Very Satisfied) - (%Dissatisfied) - (%Very Dissatisfied)

We report App Satisfaction on a scale of 0 to 200, where:
- 1 to 100 is poor score
- 100 to 140 is fair score
- 140 to 160 is good score
- 160 to 200 is world class score

## How does score trend work? 
App satisfaction score for each day is calculated based on total responses received in the previous 28 days. We display trends from 1 to maximum 90 days depending on the app’s first publish and first response date. This score provides a visualization on how the satisfaction score is trending over a period. We recommend this to analyze with the app updates if updates have helped in improving the score.

## App satisfaction by device
Currently, we provide distribution of score by device types – web, mobile or others. For tablets, the score will be calculated as mobile. “Others” option categorizes score for unknown devices.

## App satisfaction by browser
The feature also displays comparison across different browsers. The feature can identify different types of browsers including Edge, IE, Chrome, Mozilla, Opera etc. For those browsers which feature is not able to identify, the score will get attributed towards “others” category.

## Improve your application
With public preview release, the feature provides following direct links to take actions to improve your app:
1. **[Solution Checker](../data-platform/use-powerapps-checker)** – This link will take you to a list of solutions to run checker if applicable. We don’t have the ability yet to precisely identify the solution which app was part of during environment migration. Makers or admins will need to manually identify the solution and run checker tool to identify issues. Know more(link).
2. **[Performance Insights](performance-insights-overview.md)** – This tool provides direct insights on respective app’s performance and what can makers do to improve the app performance issues. Know more(link).
3. **[Monitor](../model-driven-apps/monitor-page-checker)** – This tool helps makers to troubleshoot and diagnose issues with live monitoring of a user’s session. Know more(link).
4. **Usability** – This action redirects to documentation of best Power Apps provided recommendations on design and patterns.

## How is the feedback data stored in Dataverse?
Microsoft added a new default entity in dataverse called “User Rating” to all Power Apps and Dynamics 365 organizations based on dataverse. This entity stores rating score and comments from each user feedback. This is an organization owned entity with default create, read, and delete rights provided to system administrators and customizers. Environment Makers role has only read privilege available.

>[!Note]
>1.	Only users with read privileges can view ratings of the apps.
>2.	Update on user rating entity records is blocked for all roles and users.

Administrators can also share the app score and comments to external stakeholders by creating [PowerBI dashboards on User Rating entity](../data-platform/use-powerbi-dataverse). This will help them to convey feedback to makers outside organizations and lacking access to production environments.

