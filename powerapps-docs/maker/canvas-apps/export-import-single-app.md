---
title: Export and import a canvas app as a single app file 
description: Learn how to export and import a canvas app as a single app file.
author: caburk
ms.topic: how-to
ms.date: 5/16/2025
ms.subservice: canvas-maker
ms.author: caburk
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - caburk
---

# Export and import a canvas app as a single app file

In this article, you'll learn how to export and import a single canvas app. Before you begin, review the [overview](export-import-app.md) article to learn about the different export and import options available.

Using this option, you’re able to export a single canvas app in the format of a **.msapp** file extension. This allows you to export a single file that contains the canvas app that you’re currently editing and import it.

## Permissions 
Only the **Owner** or **Co-owner** of an app can export a canvas app package. To import an app, the [Environment Maker](/power-platform/admin/database-security#predefined-security-roles) security role is required on the destination environment, either directly or through a Dataverse team that is part of the **AAD Security Group** category. Custom security roles are not currently supported. 

## Export .msapp files in Power Apps

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Open the canvas app that you want to export in Power Apps Studio.  
1. In the Power Apps Studio, select **Save** drop-down menu and then select, **Download a copy**. 
 
The  **.msapp** file is downloaded to your device.  

## Import .msapp files in Power Apps
1. Sign in to [Power Apps](https://make.powerapps.com).
1. From the left navigation pane, select **Apps**.
1. Select **Import app** > **From file (.msapp)**. 

When Power Apps Studio opens, you can choose the appropriate  **.msapp** file to import. Power Apps Studio will reload with the  **.msapp** file opened. 

> [!Note]
> For more information on resources included in the single app file, see [Resources included](export-import-app.md#resources-included-in-canvas-apps-packages).

