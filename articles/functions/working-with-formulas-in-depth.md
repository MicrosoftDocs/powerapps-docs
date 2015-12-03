<properties
	pageTitle="Working with formulas in depth | Microsoft PowerApps"
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

# Working with formulas in PowerApps #

## Behavior formulas ##

Most formulas calculate a value.  For example, you might use:

- **Label!Color = If( Value(Label!Text) >= 0, Color!Black, Color!Red )** 
 
to color a label red if it's value is less than zero.  Like an Excel spreadsheet, recalculation happens automatically as values change.

In this world, what does it mean to press a button?  No value has changed so there is nothing new to calculate.  Excel has no equivalent.  By pressing the button, the user is initiating a sequence of actions that will change the state of the app:

- Change which screen is displayed: **Back** and **Navigate** functions.
- Refresh, update, or remove items in a data source: **Refresh**, **Update**, **UpdateIf**, **Patch**, **Remove**, **RemoveIf** functions.
- Update a context variable:  **UpdateContext** function.
- Create, update, or remove items in a collection:  **Collect**, **Clear**, **ClearCollect** functions.

Since these functions change the state of the app, they cannot be automatically recalculated.  You can use these in the formulas for **OnSelect**, **OnVisible**, **OnHidden**, and other **On...** properties.  We call these *behavior formulas*.

### More than one action ###

You use semicolons to create a list of actions to perform.  For example, you might want to update a context variable and then return to the previous screen:

- **UpdateContext( { x: 1 } ); Back()**

Actions are performed in the order they appear in the formula.  The next function will not execute until the current function has completed.  If there is an error, subsequent functions may not execute. 
    