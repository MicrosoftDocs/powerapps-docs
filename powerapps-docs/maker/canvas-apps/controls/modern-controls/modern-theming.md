---
title: Modern theming
description: Learn about modern themes and how to use them in Power Apps.
author: jasongre

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur-msft
ms.date: 04/11/2024
ms.subservice: canvas-maker
ms.author: jasongre


search.audienceType:
  - maker
contributors:
  - mduelae
---

# Use modern themes in canvas apps (preview)

[This article is pre-release document and is subject to change.]

Modern themes, which are pre-established style sets, can transform the look of your app. These themes, based on Microsoft's Fluent design language, modify various style aspects such as color, typography, borders, and shadows, ensuring a visually pleasing and consistent interface. Modern theming streamlines the customization process, enabling creators to effortlessly design an app with a unified and consistent visual appeal.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Prerequisites 

To use modern themes, you need to enable it. More information, see [Enable modern controls and themes for your app](overview-modern-controls.md#enable-modern-controls-and-themes-for-your-app).

> [!NOTE]
> When modern controls and themes is enabled, you won't be able to select classic themes from the command bar. To use **retired** classic themes, you'll need to enable the **Keep classic themes** retired app setting.  

## Create a theme

There's several out-of-the-box themes available to style your app. You can also design your own theme for a more personalized visual aesthetic.

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, select **Add a theme**.
3. In the **Create a theme** dialog, enter the following information:
    -  **Theme name**: The theme name must be unique.
    -  **Font**: Choose the default font that the controls in the app use will use when the theme is applied.
    -  **Seed color**: Select the color you want to base your theme on, or manually enter the Hex or RGB representation of the color. The system generates a 16-slot palette that is optimized for accessibility.
    -  **Hue/Vibrancy**: Adjust the generation palette, especially the lighter colors, with the **Hue** and **Vibrancy** sliders. The **Hue** impacts the color shade, and **vibrancy** impacts the muteness or brightness of the palette.  
4. Optionally, look at the static preview of your new theme. You can interact with the sample controls to see how your theme is applied to the rest state and various interaction states.    
5. Select **Create**.

Your new theme is created and applied to your app.

## Apply modern theme 

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, select one of the default themes. 

When a modern theme is selected, the style of the theme is automatically applied to the controls in your app. This action sets the **App.Theme** property.  

> [!NOTE]
> Modern themes do now impact classic controls by setting properties on the classic controls with Power Fx formulas that reference variables from the modern theme. 

## Edit a theme
You can edit the theme and change one or more parameters of the custom theme.

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, find the tile corresponding to the theme you want to edit and select **Options** > **Edit**.
3. On the **Edit theme** pane, adjust the theme as needed.

> [!NOTE]
> You can't edit out-of-the-box themes.

## Delete a theme
If you decide you no longer need a custom theme in your app, you can delete it.

1. On the app authoring menu, select > ![Themes icon](media/theme-icon.png) **Themes**.
2. On the **Themes** pane, find theme that you want to edit and then, select (...) **Options** > **Delete**.
3. On the confirmation dialog box, select **Delete theme**.

If you have any Power Fx formulas that reference this theme in your app, you need to manually update the formula.

> [!NOTE]
> You can't delete out-of-the-box themes.

## Use themes with Power Fx

Modern theme objects are available for makers to use through Power Fx. The currently active theme object can be referenced by **App.Theme**, and any theme loaded into the app can be referenced by its instance name such as **RedTheme**. We recommend that you reference the theme object using **App.Theme** to ensure that the color selections adapt to theme changes.  

Each theme object includes the following information: 
-  **Name**: The name of the theme.
-  **Colors**: A collection of the 16 colors comprising the brand ramp for the theme. Each color in this ramp is individually accessible by name.

The image shows the slot variables inside the **Colors** collection and, as an example, the corresponding colors for the **Steel** theme.  
> [!div class="mx-imgBorder"]
> ![Turn on modern controls](media/modern-themes-color-ramp.png)

Using the theme brand ramp, you can manually style a classic control based on the current modern theme such as **Button.Fill = App.Theme.Colors.Primary**.


> [!NOTE]
> To provide feedback, see: [Provide your feedback to Microsoft](overview-modern-controls.md#provide-feedback-to-microsoft).

## See also

[Modern controls blog post](https://go.microsoft.com/fwlink/?linkid=2229189) 
