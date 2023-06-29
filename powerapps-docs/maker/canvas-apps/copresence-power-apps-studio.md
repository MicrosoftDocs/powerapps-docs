---
title: Discover who's working on a canvas app in Power Apps Studio
description: The copresence feature in canvas apps lets you know who's working on the app.
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

Coauthoring is a new experimental feature that works similarly to copresence. The user who initiates the app has the editing privileges. When another user attempts to open the app, a notification is displayed, informing them that someone else is currently editing the app and they're limited to read-only access. In read-only mode, users have the option to download a copy of the app. The benefit of coauthoring is that you can see in real-time the changes that are being made by the maker editing the app without the need to refresh the app.

### Enable coauthoring

To use coauthoring, it must be tuned on for each individual app. Once coauthoring is enabled, it takes precedence over copresence.

1. To enable coauthoring, open your app for editing in Power Apps Studio.
2. Go to **Settings** > **Upcoming features** > **Experimental**.
3. Set the toggle for **Enable coauthoring** to **On**.


### Limitations of coauthoring

The maker editing the app and those accessing it in read-only mode are unable to perform or have disabled access to these options:

- Undo or redo changes
- Switch authoring version
- Open a new app from data or app from template
- Use **Save as** option
- [Monitor tool](../monitor-overview.md)
- Search pane
- Makers accessing the app in read-only mode can't make any changes


