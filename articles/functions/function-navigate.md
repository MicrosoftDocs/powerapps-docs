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
   ms.date="10/21/2015"
   ms.author="gregli"/>

# Navigate function in PowerApps #

Displays a [screen](file-name.md).

## Overview ##

Users experience PowerApps through visual screens.  The Navigate function changes the currently display screen, optionally through a visual transition.  

Screens and their controls remain alive and active even if they are not currently displayed.  Property values are still available throughout the app, formulas continue to be calculated, and context variables are preserved.  All that changes is which screen is displayed.

Through the transition, you can also provide new values for [context variables](file-name.md) of the new screen.  This is similar to passing parameters to procedures in other programming tools.

## Description ##

The first argument to the Navigate function is the new screen to display.  

The second argument controls the transition from the old screen to the new screen:

| Transition | Description |
|------------|-------------|
| **ScreenTransition!Cover** | The new screen slides into view, covering the current screen. |
| **ScreenTransition!Fade** | The old screen fades away to reveal the new screen. |
| **ScreenTransition!None** | The old screen is quickly replaced with the new screen. |
| **ScreenTransition!UnCover** | The old screen slides out of view, uncovering the new screen.|

TODO: What does it mean to pass "" for transition?

Optionally with the third argument, you can provide a [record](file-name.md) of column name and value pairs to be applied through the equivalent of the **[UpdateContext](function-updatecontext.md)** function on the new screen.  Note that context variables on the new screen are updated and not the old screen.

The **[OnHidden](file-name.md)** formula will execute for the old screen, while the **[OnVisible](file-name.md)** formula will execute for the new screen.  The **[App!ActiveScreen](file-name.md)** property will be updated to reflect the change.

The Navigate function has no return value.  

This function can only be used within a [behavior formula](file-name.md).

## Syntax ##

**Navigate**( *Screen*, *Transition* [, *UpdateContextRecord* ] )

- *Screen* - Required.  The new screen to display.

- *Transition* - Required.  The visual transition to use between the current screen and the new screen.  See the **ScreenTransition** enumeration above.

- *UpdateContextRecord* - Optional.  A record containing column name and value pairs to be applied to the context variables of the new screen as if passed to **[UpdateContext](function-update.md)**.

## Examples ##

| Formula | Description | Result |
|---------|-------------|--------|
| **Navigate( Details, ScreenTransition!None )** | Displays the Details screen with no transition or change in context variables. | The **Details** screen is quickly displayed. |
| **Navigate( Details, ScreenTransition!Fade )** | Displays the Details screen with a fade transition.  No context variables are changed. | The current screen fades away to show the **Details** screen. |
| **Navigate( Details, ScreenTransition!Fade, {&nbsp;ID:&nbsp;12&nbsp;} )** | Displays the Details screen with a fade transition.  A change record for one context variable on the new screen has also been provided.   | The current screen fades away to show the **Details** screen. The context variable **ID** on the **Details** screen is set to 12.   |
| **Navigate( Details, ScreenTransition!Fade, {&nbsp;ID:&nbsp;12&nbsp;,&nbsp;Shade:&nbsp;Color!Red&nbsp;} )** | Displays the Details screen with a fade transition.  A change record for two context variables on the new screen has also been provided.   | The current screen fades away to show the **Details** screen. The context variable **ID** on the **Details** screen is set to 12, and the context varialbe **Shade** is set to Color!Red.  A control on the **Details** screen could use **Shade** in a formula for the **Fill** property - the control would display as red.  |


## Step-by-Step Example ##

<ol><li>Name the default screen **DefaultScreen**, add a label to it, and set the **Text** property of that label so that it shows **Default**.</li><br><li>Add a screen, and name it **AddlScreen**.</li><br><li>Add a label to **AddlScreen**, and set the **Text** property of the label so that it shows **Addl**.</li><br><li>Add a button to **AddlScreen**, and set its **OnSelect** property to this function:<br>**Navigate(DefaultScreen, ScreenTransition!Fade)**</li><br><li>From the **AddlScreen**, press F5, and then click the button.<br>**DefaultScreen** appears.</li></ol>[Another example](add-screen-context-variable.md)
