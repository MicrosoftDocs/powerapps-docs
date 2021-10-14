---
title: App navigation in model-driven apps | Microsoft Docs
description: Learn about app navigation in model-driven apps in Power Apps.
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.topic: conceptual
ms.component: model
ms.date: 19/07/2021
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# App navigation in model-driven apps

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

In a model-driven app, there are the three main app runtime navigation components.

1. *Areas* - For apps with more than one area, a switch control is displayed in the lower left navigation pane. In the screenshot below, the current area is named *Accounts*.
1. *Groups* - Group names appear as a navigation element in an app with the subarea names within the group listed beneath it. In the screenshot below, one group is named *Accounts* and one is named *New Group*.
1. *Subareas* - Subareas and pages appear under the group that they're configured within in the app designer. In the screenshot below, one subarea is named *All accounts revenue* and another subarea is named *Contacts*.

   :::image type="content" source="media/default-sitemap.png" alt-text="Default model-driven app site map":::

By default, a new model-driven app's navigation includes one area named **Area1**, one group named **Group1**, and one subarea named **Subarea1**. You can change the default area, group, and subarea names to something that is more meaningful to your users or configure a different site map.

## Create a group

To create a new group, complete the following steps:

1. On the left navigation pane, select **Navigation**.
1. Select **Add**, and then select **Group**.
   :::image type="content" source="media/add-navigation.png" alt-text="Add a group or subarea":::
1. Complete the properties pane for the group:

   - **Title**: Enter a title used to describe the group.
   - **ID**: The system generates an identifier for the group. Accept the system generated ID or enter a new one.

## Create a subarea

To create a new subarea, complete the following steps:

1. On the left navigation pane, select **Navigation**.
1. Select **Add**, and then select  **Subarea**.
  
1. Complete the **New subarea** dialog.
  
   - **Content type**: Select either **Table** or **Dashboard**.
   - **Table** or **Dashboard**: Depending on the content type you selected, select a table or dashboard from the list.
   - **Title**: Leave the default title or enter a title used to describe the subarea.

1. To save your app navigation changes select **Save**.
1. To publish the changes and make them available to other users, select **Publish**.

## Remove a group or subarea

1. On the left navigation pane, select **Navigation**.
1. Select the group or subarea you want, select the ellipses (**...**) and then select **Remove**.
