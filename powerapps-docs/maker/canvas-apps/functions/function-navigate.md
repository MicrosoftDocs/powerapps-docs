---
title: Back and Navigate functions in Power Apps
description: Reference information including syntax and examples for the Back and Navigate functions in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/19/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - tapanm-msft
---
# Back and Navigate functions in Power Apps

Changes which screen is displayed.

## Overview

Most apps contain multiple screens.  Use the **Back** and **Navigate** function to change which screen is displayed. For example, set the **[OnSelect](../controls/properties-core.md)** property of a button to a formula that includes a **Navigate** function if you want to show a different screen when a user selects that button. In that formula, you can specify a visual transition, such as **Fade**, to control how one screen changes to another.  

**Back** and **Navigate** change only which screen is displayed. Screens that aren't currently displayed continue to operate behind the scenes. You can build formulas that refer to properties of controls on other screens. For example, a user can change the value of a slider on one screen, navigate to a different screen that uses that value in a formula, and determine how it affects what happens in the new screen. The user can then navigate back to the original screen and confirm that the slider has kept its value.

[Context variables](../working-with-variables.md#use-a-context-variable) are also preserved when a user navigates between screens. You can use **Navigate** to set one or more context variables for the screen that the formula will display, which is the only way to set a context variable from outside the screen. You can use this approach to pass parameters to a screen. If you've used another programming tool, this approach is similar to passing parameters to procedures.

Use the **App** object's [**StartScreen**](object-app.md#startscreen-property) property to control the first screen to be displayed.

You can use either function only within a [behavior formula](../working-with-formulas-in-depth.md).

## Navigate

In the first argument, specify the name of the screen to display.  

 In the second argument, specify how the old screen changes to the new screen:

| Transition Argument | Description | Demonstration |
| --- | --- | --- |
| **ScreenTransition.Cover** |The new screen slides into view, moving right to left, to cover the current screen. | ![screen transition cover animation.](media/function-navigate/cover.gif) |
| **ScreenTransition.CoverRight** |The new screen slides into view, moving left to right, to cover the current screen. | ![screen transition cover right animation.](media/function-navigate/coverright.gif) |
| **ScreenTransition.Fade** |The current screen fades away to reveal the new screen. | ![screen transition fade animation.](media/function-navigate/fade.gif) |
| **ScreenTransition.None** (Default) |The new screen quickly replaces the current screen. | ![screen transition none animation.](media/function-navigate/none.gif) |
| **ScreenTransition.UnCover** | The current screen slides out of view, moving right to left, to uncover the new screen. | ![screen transition uncover animation.](media/function-navigate/uncover.gif) |
| **ScreenTransition.UnCoverRight** | The current screen slides out of view, moving left to right, to uncover the new screen. | ![screen transition uncover right animation.](media/function-navigate/uncoverright.gif) |

You can use **Navigate** to create or update [context variables](../working-with-variables.md#use-a-context-variable) of the new screen. As an optional third argument, pass a [record](../working-with-tables.md#records) that contains the context-variable name as a [column](../working-with-tables.md#columns) name and the new value for the context variable.  This record is the same as the record that you use with the **[UpdateContext](function-updatecontext.md)** function.

Set the **[OnHidden](../controls/control-screen.md)** property of the old screen, the **[OnVisible](../controls/control-screen.md)** property of the new screen, or both to make additional changes during the transition. The **App.ActiveScreen** property will be updated to reflect the change.

**Navigate** normally returns **true** but will return **false** if an error is encountered.

Context variables for navigation are explained in the article [navigate between screens](../add-screen-context-variables.md#add-navigation).

## Back

The **Back** function returns to the screen that was most recently displayed.

For each **Navigate** call, the app tracks the screen that appeared and the transition. You can use successive **Back** calls to return all the way to the screen that appeared when the user started the app.

When the **Back** function runs, the inverse transition is used by default. For example, if a screen appeared through the **CoverRight** transition, **Back** uses **UnCover** (which is to the left) to return.  **Fade** and **None** are their own inverses. Pass an optional argument to **Back** to force a specific transition.

**Back** normally returns **true** but returns **false** if the user hasn't navigated to another screen since starting the app.

## Syntax

**Back**( [ *Transition* ] )

* *Transition* - Optional. The visual transition to use between the current screen and the previous screen. Refer to the list of valid values for this argument earlier in this article. By default, the transition through which a screen returns is the inverse of the transition through which it appeared.

**Navigate**( *Screen* [, *Transition* [, *UpdateContextRecord* ] ] )

* *Screen* - Required. The screen to display.
* *Transition* - Optional.  The visual transition to use between the current screen and the next screen. See the list of valid values for this argument earlier in this article. The default value is **None**.
* *UpdateContextRecord* - Optional.  A record that contains the name of at least one column and a value for each column. This record updates the [context variables](../working-with-variables.md#use-a-context-variable) of the new screen as if passed to the **[UpdateContext](function-updatecontext.md)** function.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Navigate( Details )** |Displays the **Details** screen with no transition or change in value for a context variable. |The **Details** screen appears quickly. |
| **Navigate( Details, ScreenTransition.Fade )** |Displays the **Details** screen with a **Fade** transition.  No value of a context variable is changed. |The current screen fades away to show the **Details** screen. |
| **Navigate( Details, ScreenTransition.Fade, {&nbsp;ID:&nbsp;12&nbsp;} )** |Displays the **Details** screen with a **Fade** transition, and updates the value of the **ID** context variable to **12**. |The current screen fades away to show the **Details** screen, and the context variable **ID** on that screen is set to **12**. |
| **Navigate( Details, ScreenTransition.Fade, {&nbsp;ID:&nbsp;12&nbsp;,&nbsp;Shade:&nbsp;Color.Red&nbsp;} )** |Displays the **Details** screen with a **Fade** transition. Updates the value of the **ID** context variable to **12**, and updates the value of the **Shade** context variable to **Color.Red**. |The current screen fades away to show the **Details** screen. The context variable **ID** on the **Details** screen is set to **12**, and the context variable **Shade** is set to **Color.Red**. If you set the **Fill** property of a control on the **Details** screen to **Shade**, that control would display as red. |
| **Back()** | Displays the previous screen with the default return transition. | Displays the previous screen through the inverse transition of the transition through which the current screen appeared. |
| **Back( ScreenTransition.Cover )** |  Displays the previous screen with the **Cover** transition. | Displays the previous screen through the **Cover** transition, regardless of the transition through which the current screen appeared. |

### Step-by-step

1. Create a blank app.

1. Add a second screen to it.

    The app contains two blank screens: **Screen1** and **Screen2**.

1. Set the **Fill** property of **Screen2** to the value `Gray`.

1. On **Screen2**, add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:

    ```powerapps-dot
    Navigate( Screen1, ScreenTransition.Cover )
    ```

1. While holding down the **Alt** key, select the button.

    **Screen1** appears with a white background through a transition that covers to the left.

1. On **Screen1**, add a button, and set its **OnSelect** property to this formula:

    ```powerapps-dot
    Back()
    ```

1. While holding down the **Alt** key, select the button.

    The second screen appears with a gray background through a transition that uncovers to the right (the inverse of **Cover**).

1. Select the button on each screen repeatedly to bounce back and forth.

### See also

[Using context variables](../working-with-variables.md#use-a-context-variable)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]