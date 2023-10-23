---
title: Coauthoring in model-driven apps with Power Apps
description: The model-driven app designer lets multiple makers make changes to an app at the same time.
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: how-to 
ms.date: 06/23/2023
ms.custom: template-how-to
---
# Coauthoring in model-driven apps

Coauthoring allows multiple makers—whether pro or citizen developers—to make changes to the app at the same time and see those changes in real time. As a result, teams can innovate together and build stronger connections between professional developers and business domain experts, a critical ingredient to maximizing low-code development. 

> [!IMPORTANT]
> - This feature is being gradually rolled out across regions and might not be available yet in your region.
> - This feature isn't currently available in Germany, China, and Government Cloud regions. Regions where coauthoring isn't available have copresence. More information: [Discover who's working on an app](copresence.md)

## What you can coauthor in an app

Here's what multiple makers can do at the same time in the app while seeing each other's others changes in real-time.

- Add and remove components, such as tables, dashboards, and custom pages, to and from the model-driven app.
- Add and remove subcomponents, such as views, forms, and charts, to and from the tables in the model-driven app.
- Add and remove areas, groups, and subareas to and from the navigation bar in the model-driven app.
- Change properties of the model-driven app.
- Change properties of the navigation pane.
- Change properties of areas, groups, and subareas in the navigation pane, including **Display Options** and **Advanced Settings**.
- Change order of the areas, groups, and subareas in the navigation pane.
- Change **General**, **Features** and **Upcoming** tabs in the **Settings** dialog.  

## How to know you're coauthoring

First, once there are other makers editing the app together with you, you see their presence in the top navigation bar and the left menu. You can see what components other makers are working on or what pages they have open. You'll also see them move through the components on the left navigation bar in real-time.

:::image type="content" source="media/coauthoring1.png" alt-text="App makers working in the app are displayed":::
When someone is adding or removing a page, all other makers will see it appearing on the left navigation bar with a sparkle graphic indicator. The sparkle remains displayed until you select that page. You won’t see a sparkle for the components and pages that you’ve added.

:::image type="content" source="media/coauthoring2.png" alt-text="Sparkle graphic indicator appears when changes are made by other makers":::

Once someone removes the page, it disappears for other makers in real-time.

## Limitations

- Currently, there's no auto-save functionality, so you need to select the **Save** button to save changes. However, any maker that has access to the app can save the changes for others, as their changes are synced. Unsaved changes will be removed from the app in eight hours.
- Under **Settings**, changes to the **Features** and **Upcoming** sections must be saved from the settings dialog in order to be set. Users that don't see the changes immediately can close and open the settings dialog to see the most up-to-date settings.
- Changes made in other designers, such as the view and form designers, won't be synchronized in real-time in the modern app designer.

## See also

[Add comments](comments.md)
