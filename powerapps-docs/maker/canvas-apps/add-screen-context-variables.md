---
title: Add a screen to a canvas app and navigate between screens
description: Add a screen to a canvas app and use next and back arrows to go between screens.
author: emcoope-msft

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 02/03/2019
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
contributors:
  - mduelae
  - emcoope-msft
---
# Add a screen using screen layouts

When you add a new screen, you can choose from a variety of screen layouts. Each screen layout automatically adjusts to fit the screen size of the device being used to run the app. 

> [!div class="mx-imgBorder"]
> ![Screen layouts.](./media/add-screen-context-variables/screen-layouts.png)


## Add a new screen

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. Create a canvas app in tablet format. 
3. In Power Apps Studio, on the command bar, select **New screen** and then select a screen layout.

When you're done, you can preview the app and see how the app displays on different devices. More information: [Preview an app](preview-app.md)


## Reorder screens

When you have more then one screen you can reorder them.

In the left pane, hover over a screen that you want to move up or down, and then select **Move up** or **Move down**.

> [!NOTE]
> When the app is opened, the screen at the top of the hierarchical list of controls usually appears first. But you can specify a different screen by setting the **[OnStart](controls/control-screen.md)** property to a formula that includes the **[Navigate](functions/function-navigate.md)** function.

## Add navigation

When you create a canvas app with multiple screens, you can add navigatation so you're users can navigate between screens.


1. With the screen selected, select **Insert** and in the search box type **Next arrow** and then select it.

2. (optional) Move the arrow so that it appears in the lower-right corner of the screen.

3. With the arrow still selected, set t he **[OnSelect](controls/properties-core.md)** property for the arrow is automatically set to a **Navigate** function.

    ![OnSelect property set to Navigate function.](./media/add-screen-context-variables/onselect-default.png)

    When a user selects the arrow, the **Target** screen fades in.

4. On the **Target** screen, add a **Back arrow**, and set its **[OnSelect](controls/properties-core.md)** property to this formula:

    `Navigate(screen name, ScreenTransition.Fade)`

   > [!NOTE]
   > In the formula above where it says **screen name** enter the name of the screen that you are navigating to. 


## More information

[Screen-control reference](controls/control-screen.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]


