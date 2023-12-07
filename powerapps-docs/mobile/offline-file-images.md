---
title: "Configure mobile offline profiles for files and images| Microsoft Docs"
description: Configure mobile offline profiles for files and images.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 12/04/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Configure mobile offline profiles for files and images 

To work with file and image columns in offline mode, you need to add the corresponding columns to the offline profile.

Follow the steps in this topic, for a mobile offline profile that has a table with a column where **Data type** is set to **File** or **Image**.

## View column properties for a file or image 

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the left navigation, select **Tables**. [!include [left nav](../includes/left-navigation-pane.md)] 
  
1. Select the **Display name** of a column where **Data type** is set to **File** or **Image**.

1. The column properties show the **Data type**. Expand **Advanced options** to view the maximum size for a file or image.

   > [!div class="mx-imgBorder"]
   >![Maximum size for files and images.](media/offline-file-images-1.png "Maximum file and image size")

## Add file and image columns to mobile offline 

It is required to add the column where **Data Type** is set to **File** or **Image** to your mobile offline profile to make files and images available in offline mode.

1. In [Power Apps studio](../maker/canvas-apps/power-apps-studio.md), in the left side panel, select **Apps**.

1. Select your model-driven app, and then select **Edit**.

1. Select **Settings**.

1. Select **General**.

1. Make sure the **Can be used offline** toggle is **On**.

1. In the **Select offline mode and profile** section, select **Edit selected profile** from the "..."

1. Select the table that contains the file or image column to enable for offline, and then select **Edit** from the **More actions** button.
   
1. In the **Include these files and images** section, select the column where **Data Type** is set to **File** or **Image**  (Note that the columns are grouped by **Files** or **Images**)

1. Select **Save**.
   
1. Save and publish the app.    

