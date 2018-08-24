---
title: Back and Navigate functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Navigate and Back functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/08/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Back and Navigate functions in PowerApps
Changes which screen is displayed.

## Overview
Most apps contain multiple screens.  Use the **Back** and **Navigate** function to change which screen is displayed. For example, set the **[OnSelect](../controls/properties-core.md)** property of a button to a formula that includes a **Navigate** function if you want to show a different screen when a user selects that button. In that formula, you can specify a visual transition, such as **Fade**, to control how one screen changes to another.  

**Back** and **Navigate** change only which screen is displayed. Screens that aren't currently displayed continue to operate behind the scenes. You can build formulas that refer to properties of controls on another screen. For example, a user can change the value of a slider on one screen, navigate to a different screen that uses that value in a formula, and see how it affects what happens in the new screen.  The user can then navigate back to the original screen and see that the slider has retained its value.

[Context variables](../working-with-variables.md#create-a-context-variable) are also preserved when a user navigates between screens. You can use **Navigate** to set one or more context variables for the screen that the formula will display, which is the only way to set a context variable from outside the screen. You can use this approach to pass parameters to a screen. If you've used another programming tool, this approach is similar to passing parameters to procedures.

## Description
### Back
The **Back** function displays the screen that was most recently displayed. You don't specify any arguments for this function.

### Navigate
In the first argument, specify the name of the screen to display.  

 In the second argument, specify how the old screen changes to the new screen:

| Transition Argument | Description |
| --- | --- |
| **ScreenTransition.Cover** |The new screen slides into view, covering the current screen. |
| **ScreenTransition.Fade** |The old screen fades away to reveal the new screen. |
| **ScreenTransition.None** |The old screen is quickly replaced with the new screen. |
| **ScreenTransition.UnCover** |The old screen slides out of view, uncovering the new screen. |

You can use **Navigate** to create or update context variables of the new screen. As an optional third argument, pass a [record](../working-with-tables.md#records) that contains the context-variable name as a [column](../working-with-tables.md#columns) name and the new value for the context variable.  This record is the same as the record that you use with the **[UpdateContext](function-updatecontext.md)** function.

Set the **[OnHidden](../controls/control-screen.md)** property of the old screen, the **[OnVisible](../controls/control-screen.md)** property of the new screen, or both to make additional changes during the transition. The **App.ActiveScreen** property will be updated to reflect the change.

**Back** normally returns **true** but returns **false** if the user is on the first screen shown and there is no previous screen.  **Navigate** normally returns **true** but returns **false** if there is a problem with one of its arguments.

You can use these functions only within a [behavior formula](../working-with-formulas-in-depth.md).

## Syntax
**Back**()

**Navigate**( *Screen*, *Transition* [, *UpdateContextRecord* ] )

* *Screen* - Required. The screen to display.
* *Transition* - Required.  The visual transition to use between the current screen and the next screen. See the list of valid values for this argument earlier in this topic.
* *UpdateContextRecord* - Optional.  A record that contains the name of at least one column and a value for each column. This record updates the context variables of the new screen as if passed to the **[UpdateContext](function-updatecontext.md)** function.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Navigate( Details, ScreenTransition.None )** |Displays the **Details** screen with no transition or change in value for a context variable. |The **Details** screen appears quickly. |
| **Navigate( Details, ScreenTransition.Fade )** |Displays the **Details** screen with a **Fade** transition.  No value of a context variable is changed. |The current screen fades away to show the **Details** screen. |
| **Navigate( Details, ScreenTransition.Fade, {&nbsp;ID:&nbsp;12&nbsp;} )** |Displays the **Details** screen with a **Fade** transition, and updates the value of the **ID** context variable to **12**. |The current screen fades away to show the **Details** screen, and the context variable **ID** on that screen is set to **12**. |
| **Navigate( Details, ScreenTransition.Fade, {&nbsp;ID:&nbsp;12&nbsp;,&nbsp;Shade:&nbsp;Color.Red&nbsp;} )** |Displays the **Details** screen with a **Fade** transition. Updates the value of the **ID** context variable to **12**, and updates the value of the **Shade** context variable to **Color.Red**. |The current screen fades away to show the **Details** screen. The context variable **ID** on the **Details** screen is set to **12**, and the context variable **Shade** is set to **Color.Red**. If you set the **Fill** property of a control on the **Details** screen to **Shade**, that control would display as red. |

### Step-by-step
1. Name the default screen **DefaultScreen**, add a label to it, and set the **[Text](../controls/properties-core.md)** property of that label so that it shows **Default**.
2. Add a screen, and name it **AddlScreen**.
3. Add a label to **AddlScreen**, and set the **[Text](../controls/properties-core.md)** property of the label so that it shows **Addl**.
4. Add a button to **AddlScreen**, and set its **[OnSelect](../controls/properties-core.md)** property to this function:<br>**Navigate(DefaultScreen, ScreenTransition.Fade)**
5. From the **AddlScreen**, press F5, and then select the button.<br>**DefaultScreen** appears.

[Another example](../add-screen-context-variables.md)

