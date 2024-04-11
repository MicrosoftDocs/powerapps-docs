---
title: Modern theming
description: Learn about modern themes and how to use them in Power Apps.
author: jasongre

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur-msft
ms.date: 08/01/2023
ms.subservice: canvas-maker
ms.author: jasongre


search.audienceType:
  - maker
contributors:
  - mduelae
---

# Use modern themes in canvas apps (preview)

[This article is pre-release document and is subject to change.]

Your app's appearance can be quickly changed by applying modern themes, which are predefined sets of styles that affect the user interface. Modern themes use Microsoft's Fluent design language. They modify various style elements, including color, typography, borders, and shadows, in a consistent and visually appealing manner. Modern theming simplifies the customization process, allowing makers to create a visually cohesive and consistent app with ease.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Prerequisites 

To use modern themes, you need to enable it. More information, see [Enable modern controls and themes for your app](overview-modern-controls.md#enable-modern-controls-and-themes-for-your-app).

> [!NOTE]
> When modern controls and themes is enabled, you won't be able to select classic themes from the command bar. To use classic themes, you'll need to turn off modern controls and themes.  

## Create a theme

While there are several out-of-the-box themes available to style your app, you can also create your own theme to customize the app's visual appearance to your liking. 

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, select **Add a theme**.
3. In the **Create a theme** dialog, enter the following information
    -  **Theme name**: The theme name you provide must be unique.
    -  **Font**: Choose the default font you want your controls to utilize when this theme is applied.
    -  **Seed color**: Select the color you want to base your theme on, or manually enter the Hex or RGB representation of the color. The system will then generate a 16-slot palette that is optimized for accessibility.
4. Select **Create**.

Your new theme will then be created and applied to your app. 

## Apply modern theme 

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, select one of the six default themes. 

When a modern theme is selected, the style of the theme is automatically applied to all the modern controls in your app. This action sets the **App.Theme** property.  

> [!NOTE]
> Modern themes don't make any automatic changes to classic controls; however, these controls can be manually styled to align to the theme through Power Fx.

## Edit a theme
If you need to change one or more parameters of your custom theme, you can accomplish this by editing the theme. 

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, find the tile corresponding to the theme you want to edit and select **Options** > **Edit**.
3. On the **Edit theme** pane, adjust the theme as desired.

> [!NOTE]
> Out-of-the-box themes cannot be edited. 

## Delete a theme
If you decide you no longer need a custom theme in your app, you can simply delete the theme from your app. 

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, find the tile corresponding to the theme you want to edit and select **Options** > **Delete**.
3. This will trigger a confirmation message. Select **Delete theme** to proceed with removing the theme.
4. [Optional] If you have any Power Fx formulas that reference this theme in your app, you will need to manually correct these.

> [!NOTE]
> Out-of-the-box themes cannot be deleted.  

## Use themes with Power Fx

Modern theme objects are available for makers to use through Power Fx. The currently active theme object can be referenced by **App.Theme**, and any theme loaded into the app can be referenced by its instance name such as **RedTheme**. It's recommended to reference the theme object using **App.Theme** to ensure that the color selections adapt to theme changes.  

Each theme object includes the following information: 
-  **Name**: The name of the theme.
-  **Colors**: A collection of the 16 colors comprising the brand ramp for the theme. Each color in this ramp is individually accessible by name.

The image below shows the slot variables inside the **Colors** collection and, as an example, the corresponding colors for the **Steel** theme.  
> [!div class="mx-imgBorder"]
> ![Turn on modern controls](media/modern-themes-color-ramp.png)

Using the theme brand ramp, you can manually style a classic control based on the current modern theme such as **Button.Fill = App.Theme.Colors.Primary**.


> [!NOTE]
> To provide feedback, see: [Provide your feedback to Microsoft](overview-modern-controls.md#provide-feedback-to-microsoft).

## See also

[Modern controls blog post](https://go.microsoft.com/fwlink/?linkid=2229189) 
