---
title: Configure files and images in offline model-driven apps
description: Configure mobile offline profiles for files and images.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/29/2024
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Configure files and images in offline model-driven apps

To work with file and image columns in offline mode, you need to add them to your mobile offline profile.

This article helps you configure a mobile offline profile that has a table with a column where **Data type** is set to **File** or **Image**.

## View column properties for a file or image

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the navigation menu, select **Tables**. [!INCLUDE [left-navigation-pane](../includes/left-navigation-pane.md)] 

1. Select the table that has the columns you want to view.

1. Under **Schema**, select **Columns**.
  
1. Select the **Display name** of a column where **Data type** is set to **File** or **Image**.

1. The column properties show the **Data type**. Expand **Advanced options** to view the maximum size for a file or image. For more information about columns, see [Columns overview](../maker/data-platform/fields-overview.md).

## Add file and image columns to mobile offline

Add the column where **Data Type** is set to **File** or **Image** to your mobile offline profile to make files and images available in offline mode.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the left navigation pane, select **Apps**.

1. Select a model-driven app and on the command bar select **Edit**. This opens your app in editing mode in [model-driven app designer](../maker/model-driven-apps/app-designer-overview.md). 

1. Select **Settings** > **General**.

1. Set the **Can be used offline** toggle to **On**.

1. Under **Select offline mode and profile**, select **Edit selected profile** from the "...".

1. Find the table that contains the file or image column to enable for offline, and then select **Edit** from the **More actions** button.

1. In the **Include these files and images** section, select the column where **Data Type** is set to **File** or **Image**  (the columns are grouped by **Files** or **Images**).

1. Select **Save**.

1. Save and publish the app.
