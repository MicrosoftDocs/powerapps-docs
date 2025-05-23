---
title: "App ratings for Model-driven-apps | MicrosoftDocs"
description: Understand ratings for model-driven apps. 
ms.custom: ""
ms.date: 07/04/2022
ms.reviewer: "matp"
ms.topic: overview
author: "yogeshgupta698"
ms.subservice: common
ms.author: "matp"
search.audienceType: 
  - maker, admin
---
# What are app ratings? (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Power Apps takes feedback from app users on how satisfied they are with their app experience. With the app ratings feature, makers and administrators view the app's satisfaction score and comments provided by users. The collection of feedback is compliant with all international privacy laws. The feature also seamlessly integrates with solution checker, performance insights, and live monitoring, which can help makers improve their app.

:::image type="content" source="media/app-ratings-overview.png" alt-text="Ratings feature image":::

>[!NOTE]
> - This feature is currently only available for model-driven Power Apps.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)] More information: [Power Apps preview program](../powerapps-preview-program.md)

This feature has the following benefits: 
- Provides a view of the [app satisfaction score](#app-satisfaction-score) on a scale of 0 to 200. 
- Provides a [score trend](#score-trend) over the last 90 days.
- Displays different satisfaction scores based on [web or mobile device](#app-satisfaction-by-device) and [browser](#app-satisfaction-by-browser).

The report for current score and comments can be exported for each app in the app ratings dashboard to share with others.

## Access the ratings dashboard

1. Sign in to [Power Apps](https://make.powerapps.com). 

1. On the left navigation pane, select **Apps**, and then select a model-driven app.

1. Select the **...** context menu, and then select **Ratings (preview)**.

   :::image type="content" source="media/ratings-option.png" alt-text="Ratings option image":::

## How app user satisfaction is collected

Based on the user’s activity inside the app, Power Apps occasionally prompts users to score the app with the following questions:

1. How satisfied are you with (name of the app)?

   - Very satisfied
   - Satisfied
   - Dissatisfied
   - Very Dissatisfied

1. What can we do to improve?

:::image type="content" source="media/app-satisfaction-dialog.png" alt-text="App satisfaction dialog image":::

Based on the feedback, an [app satisfaction score](#app-satisfaction-score) and comments are displayed in the ratings dashboard.

The following guidelines are used to prompt an app user with the feedback dialog:
-	If a user has at least three active days during the first 14 days since sign-up, the user is prompted.
-	If the user has six active days in the last (recent) 90 days, the user is prompted.
-	No users are prompted more than once in 90 days for the same app.

## App satisfaction score

The app satisfaction score is calculated by taking the responses with an answer "Very Satisfied" and subtracting the percentage of the responses with an answer "Dissatisfied" or "Very Dissatisfied". The total NSAT score is then calculated like this:

>100 + (%Very Satisfied) - (%Dissatisfied) - (%Very Dissatisfied)

 App satisfaction is reported on a scale of 0 to 200, where:

- 1 to 100 is a poor score.
- 100 to 140 is a fair score.
- 140 to 160 is a good score.
- 160 to 200 is a world class score.

### Score trend

The app satisfaction score for each day is calculated based on total responses received in the previous 28 days. Trends from 1 to maximum 90 days are displayed depending on the app’s first publish and first response date. This score provides a visualization on how the satisfaction score is trending over a period. We recommend you use this feature to analyze subsequent updates to the app and follow how those updates have helped in improving the general experience with users.

### App satisfaction by device

The app score is separated by device types – web, mobile, or others. For tablets, the score is calculated as mobile. The Others option categorizes the score for unknown devices.

### App satisfaction by browser

App ratings also display a comparison across different browsers. The feature can identify different types of browsers including Microsoft Edge, IE, Chrome, Mozilla, and Opera. For browsers that can't be identified, the score is attributed under the Others category.

## Improve your application

With the public preview release, the app ratings provides the following direct links to take actions to improve your app:
1. **[Solution Checker](../data-platform/use-powerapps-checker.md)** – This link takes you to a list of solutions to run solution checker if applicable. Notice that makers or admins must manually identify the solution and run solution checker to identify issues.
2. **[Performance Insights](performance-insights-overview.md)** – This tool provides direct insights on the respective app’s performance and what makers can do to improve the app performance issues.
3. **[Monitor](../model-driven-apps/monitor-page-checker.md)** – This tool helps makers troubleshoot and diagnose issues with live monitoring of a user’s session.
4. **Usability** – This action redirects to documentation of best Power Apps provided recommendations on design and patterns.

## How the feedback data is stored

A new system table in Microsoft Dataverse called **User Rating** was added to all Power Apps environments that include Dataverse. This table stores the rating score and comments from each user feedback. This is an organization owned table with default create, read, and delete rights provided to system administrators and customizers. The environment maker role has only read privilege on the table.

> [!Note]
> 1.	Only users with at least read privileges on the User Rating table can view app ratings data.
> 1.	By default update on User Rating table records is unavailable for all other security roles.

Administrators can also share the app score and comments to external stakeholders by creating [Power BI dashboards on the User Rating table](../data-platform/use-powerbi-dataverse.md). This can help convey app ratings data to makers outside organizations who don't have access to production environments.
