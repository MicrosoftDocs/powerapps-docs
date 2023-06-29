---
title: Discover who's working on a canvas app in Power Apps Studio
description: The copresence feature in canvas lets you know who's working on the app.
author: mkaur
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 06/09/2023
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  
---

# Find out who's working on the same app

Use copresence to identify individuals working on the same app as you in Power Apps Studio. 

> [!div class="mx-imgBorder"] 
> ![Copresence in Power Apps Studio.](media/copresence/canvas-copresence.png)

Legend

1. The command bar displays the names and icons of other makers who are working on the app and may be making changes. 
2. The left-hand navigation pane in Power Apps Studio displays the app's structure, indicating which part of the app is being worked on. You receive a notification to refresh the app when the maker that's editing the app makes changes and saves that app.

> [!NOTE]
> This feature is in the process of rolling out, and might not be available in your region yet.

## How copresence works

The first time someone opens your app in Power Apps Studio while you're working on it, copresence indicators appear that shows other people are also working on the app. 

The maker that opens the app first has editing control. If a second user tries to open the app, a notification appears letting them know that someone else is editing the app so they're in read-only mode. If you're in read-only mode, you can save a copy of the app.

Icons of copresent makers appear in both the command bar and the left navigation pane showing where other makers are working in the app.

You may be working on the app, or you may be idle, but once someone else saves a change to the app, you receive a notification letting you know that another maker made changes. When you see this notification, consider refreshing the app to get the latest version.

## Coauthor (experimental)

[This section is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Coauthoring is a new experimental feature that works similar to copresence. The user who initiates the app has the editing privileges. When another user attempts to open the app, a notification is displayed, informing them that someone else is currently editing the app and they are limited to read-only access. In read-only mode, users have the option to save a copy of the app. The benefit of coauthoring is that you can see in real-time the changes that are being made by the person editing the app without the need to refresh to see the changes.

### Enable coauthoring

Coauthoring needs to be tuned on per app.

1. To enable coauthoring, open your app for editing in Power Apps Studio.
2. Go to **Settings** > **Upcoming features** > **Experimental**.
3. Set the toggle for **Enable coauthoring** to **On**.


#### Limitations of coauthoring

The following options cannot be performed or are disabled for the maker editing the app and the makers wtih read only access:
- undo/redo
- switch authoring version
- open, new, app from data, or app from template
- Save as
- Monitor tool
- Search pane 

The following 
All the limitations of the writers
All the limitations of copresence (e.g. no save)
Making changes to the app is disabled


