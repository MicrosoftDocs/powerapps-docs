<properties
	pageTitle="PowerApps: Navigate function"
	description="Reference information for the Navigate function in PowerApps, including syntax and examples"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/08/2015"
   ms.author="gregli"/>

# Navigate function in PowerApps #

Changes which [screen](file-name.md) appears.

## Overview ##

Most apps have multiple screens, and you use the **Navigate** function to change which screen appears at any given time. For example, set the [**OnSelect**](file-name.md) property of a button to a formula that's based on **Navigate** if you want to show a different screen when a user clicks that button. In that formula, you can specify a visual transition, such as Fade, to control how one screen changes to another.  

**Navigate** changes only which screen appears.

- You can set a property on one screen and refer to that property from another screen. For example, a user can change the value of a slider on one screen, navigate to a different screen, and see how that change affects what happens in the new screen.

- If you set the property of a control to a formula, it will continue to be calculated even when the screen that contains the control doesn't appear. For example, you can set the [**Text**](file-name.md) property of a label to a formula that calculates how many employees have responded to an HR survey. If the user navigates to a screen other than the one that contains the label, the new screen can update as more employees respond to the survey.

- If you set the value of a [context variable](file-name.md) on one screen, that value is preserved when the user navigates to a different screen unless you specify an argument to update the value. This is similar to passing parameters to procedures in other programming tools.

## Description ##

In the first argument, specify the name of the screen to display.  

 In the second argument, specify how the old screen changes to the new screen:

| Transition | Description |
|------------|-------------|
| **ScreenTransition!Cover** | The new screen slides into view, covering the current screen. |
| **ScreenTransition!Fade** | The old screen fades away to reveal the new screen. |
| **ScreenTransition!None** | The old screen is quickly replaced with the new screen. |
| **ScreenTransition!UnCover** | The old screen slides out of view, uncovering the new screen.|

TODO: What does it mean to pass "" for transition?

As an optional third argument, preserve one or more aspects of [app state](file-name.md) by specifying a [record](file-name.md) that contains the name of at least one column and a value for each column. This approach is similar to using the the **[UpdateContext](function-updatecontext.md)** function to manage the user experience in the new screen.  Note that context variables on the new screen are updated and not the old screen.

Set the **[OnHidden](file-name.md)** property of the old screen, the **[OnVisible](file-name.md)** property of the new screen, or both to make additional changes during the transition. The **[App!ActiveScreen](file-name.md)** property will be updated to reflect the change.

**Navigate** has no return value, and you can use it only within a [behavior formula](file-name.md).

## Syntax ##

**Navigate**( *Screen*, *Transition* [, *UpdateContextRecord* ] )

- *Screen* - Required.  The new screen to display.

- *Transition* - Required.  The visual transition to use between the current screen and the new screen. See the list of valid values for this argument earlier in this topic.

- *UpdateContextRecord* - Optional.  A record that contains the name of at least one column and a value for each column. This record updates the context variables of the new screen as if passed to the **[UpdateContext](function-update.md)** function.

## Examples ##

| Formula | Description | Result |
|---------|-------------|--------|
| **Navigate( Details, ScreenTransition!None )** | Displays the **Details** screen with no transition or change in value for a context variable. | The **Details** screen appears quickly. |
| **Navigate( Details, ScreenTransition!Fade )** | Displays the **Details** screen with a **Fade** transition.  No value of a context variable is changed. | The current screen fades away to show the **Details** screen. |
| **Navigate( Details, ScreenTransition!Fade, {&nbsp;ID:&nbsp;12&nbsp;} )** | Displays the **Details** screen with a **Fade** transition, and updates the value of the **ID** context variable to **12**.   | The current screen fades away to show the **Details** screen, and the context variable **ID** on that screen is set to **12**. |
| **Navigate( Details, ScreenTransition!Fade, {&nbsp;ID:&nbsp;12&nbsp;,&nbsp;Shade:&nbsp;Color!Red&nbsp;} )** | Displays the **Details** screen with a **Fade** transition. Updates the value of the **ID** context variable to **12**, and updates the value of the **Shade** context variable to **Color!Red**. | The current screen fades away to show the **Details** screen. The context variable **ID** on the **Details** screen is set to 12, and the context variable **Shade** is set to **Color!Red**. If you set the **Fill** property of a control on the **Details** screen to **Shade**, that control would display as red.  |


## Step-by-step example ##

1. Name the default screen **DefaultScreen**, add a label to it, and set the **Text** property of that label so that it shows **Default**.

1. Add a screen, and name it **AddlScreen**.

1. Add a label to **AddlScreen**, and set the **Text** property of the label so that it shows **Addl**.

1. Add a button to **AddlScreen**, and set its **OnSelect** property to this function:<br>**Navigate(DefaultScreen, ScreenTransition!Fade)**

1. From the **AddlScreen**, press F5, and then click the button.<br>**DefaultScreen** appears.

[Another example](add-screen-context-variables.md)
