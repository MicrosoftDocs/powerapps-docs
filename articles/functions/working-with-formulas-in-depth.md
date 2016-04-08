<properties
	pageTitle="Understanding formulas | Microsoft PowerApps"
	description="Reference information for working with formulas"
	services=""
	suite="powerapps"
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
   ms.date="11/10/2015"
   ms.author="gregli"/>

# Understanding formulas in PowerApps #

## Behavior formulas ##

Most formulas calculate a value.  Like an Excel spreadsheet, recalculation happens automatically as values change.  For example, you might use this formula to color a label red if its value is less than zero:

- **Label.Color = If( Value(Label.Text) >= 0, Color.Black, Color.Red )**

In this world, what does it mean to press a button?  No value has changed so there is nothing new to calculate.  Excel has no equivalent to a button.  

By pressing the button, the user is initiating a sequence of actions, or behaviors, that will change the state of the app:

- Change the screen which is displayed: **[Back](function-navigate.md)** and **[Navigate](function-navigate.md)** functions.
- Control a [signal](signals.md): **[Enable](function-enable-disable.md)** and **[Disable](function-enable-disable.md)** functions.
- Refresh, update, or remove items in a [data source](working-with-data-sources.md): **[Refresh](function-refresh.md)**, **[Update](function-update-updateif.md)**, **[UpdateIf](function-update-updateif.md)**, **[Patch](function-patch.md)**, **[Remove](function-remove-removeif.md)**, **[RemoveIf](function-remove-removeif.md)** functions.
- Update a [context variable](working-with-variables.md#create-a-context-variable):  **[UpdateContext](function-updatecontext.md)** function.
- Create, update, or remove items in a [collection](working-with-data-sources.md#collections):  **[Collect](function-clear-collect-clearcollect.md)**, **[Clear](function-clear-collect-clearcollect.md)**, **[ClearCollect](function-clear-collect-clearcollect.md)** functions.

Since these functions change the state of the app, they cannot be automatically recalculated.  You can use these in the formulas for **OnSelect**, **OnVisible**, **OnHidden**, and other **On...** properties.  We call these *behavior formulas*.

### More than one action ###

You use semicolons to create a list of actions to perform.  For example, you might want to update a context variable and then return to the previous screen:

- **UpdateContext( { x: 1 } ); Back()**

Actions are performed in the order they appear in the formula.  The next function will not execute until the current function has completed.  If there is an error, subsequent functions may not execute.
