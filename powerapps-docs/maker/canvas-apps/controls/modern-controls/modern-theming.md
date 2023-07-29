---
title: Modern theming
description: Learn about modern themes and how to use them in Power Apps.
author: jasongre

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur-msft
ms.date: 07/28/2023
ms.subservice: canvas-maker
ms.author: jasongre


search.audienceType:
  - maker
contributors:
  - mduelae
---

# Modern themes in canvas apps (preview)

[This article is pre-release document and is subject to change.]

Themes allow you to easily change the look and feel of your entire app from a single selection. 

## Description
Themes refer to predefined sets of styles that can be applied to the user interface of the entire app. The modern theming system is rooted in Microsoft's Fluent design language, with modern themes impacting all aspects of styling including color, typography, borders, shadows, etc. These themes are designed to simplify the process of customizing an app's appearance and help makers more easily create visually appealing and consistent user interfaces, which can help makers concentrate more on building functionality that meets their users' needs.   


## Enable modern themes for your app
To enable modern theming for you app, follow [these instructions](overview-modern-controls.md#enable-modern-controls-for-your-app).

> [!NOTE]
> When this setting is enabled, you will no longer have the ability to select classic themes from the command bar. If the classic themes are needed, you will need to disable this setting.  

## Apply a modern theme to your app
1. On the app authoring menu, select **Themes**.
2. On the Themes pane, select one of the 6 out-of-the-box themes. 

When a modern theme is selected, the theme styling will be automatically applied to all the modern controls in your app. This action will also set the **App.Theme** property.  

> [!NOTE]
> Modern themes do not make any automatic changes to classic controls; however, these controls can be manually styled to align to the theme through Power Fx. 

## Using theme information with Power Fx
Modern theme objects are available for makers to use through Power Fx. The currently active theme object can be referenced by **App.Theme**, and any theme loaded into the app can be referenced by its instance name (e.g. RedTheme). The majority of the time you will want to reference the theme object using **App.Theme** to ensure that the color selections adapt to theme changes.  

Each theme object includes the following information: 
-  *Name* - The name of the theme.
-  *Colors* - A collection of the 16 colors comprising the brand ramp for the theme. Each color in this ramp is individually accessible by name.

Below is an image showing the slot variables inside the Colors collection and, as an example, the corresponding colors for the Steel theme.  
> [!div class="mx-imgBorder"]
> ![Turn on modern controls](media/modern-themes-color-ramp.png)

Using the theme brand ramp, you can manually style a classic control based on the current modern theme (e.g. Button.Fill = App.Theme.Colors.Primary).  

## What's next
We're not done with modern theming! We'll be continuing to improve this experience and add new theming capabilities. For more information, see our blog for [what's new](https://go.microsoft.com/fwlink/?linkid=2229189) or [provide your feedback to Microsoft](overview-modern-controls.md#provide-feedback-to-microsoft).
