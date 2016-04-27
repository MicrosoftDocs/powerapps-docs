<properties
	pageTitle="Understanding behavior formulas | Microsoft PowerApps"
	description="Reference information for working with behavior formulas"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="erikre"
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

# Understanding behavior formulas in PowerApps #

## Behavior formulas ##

Most formulas calculate a value.  Like an Excel spreadsheet, recalculation happens automatically as values change.  For example, you might want to show the value in a **Text box** control in red if the value is less than zero or in black otherwise. So you can set the **Color** property of that control to this formula:
<br>**If( Value(TextBox1.Text) >= 0, Color.Black, Color.Red )**

In this context, what does it mean when the user selects a **Button** control?  No value has changed, so there is nothing new to calculate. Excel has no equivalent to a **Button** control.  

By selecting a **Button** control, the user initiates a sequence of actions, or behaviors, that will change the state of the app:

- Change the screen that's displayed: **[Back](function-navigate.md)** and **[Navigate](function-navigate.md)** functions.
- Control a [signal](signals.md): **[Enable](function-enable-disable.md)** and **[Disable](function-enable-disable.md)** functions.
- Refresh, update, or remove items in a [data source](working-with-data-sources.md): **[Refresh](function-refresh.md)**, **[Update](function-update-updateif.md)**, **[UpdateIf](function-update-updateif.md)**, **[Patch](function-patch.md)**, **[Remove](function-remove-removeif.md)**, **[RemoveIf](function-remove-removeif.md)** functions.
- Update a [context variable](working-with-variables.md#create-a-context-variable):  **[UpdateContext](function-updatecontext.md)** function.
- Create, update, or remove items in a [collection](working-with-data-sources.md#collections):  **[Collect](function-clear-collect-clearcollect.md)**, **[Clear](function-clear-collect-clearcollect.md)**, **[ClearCollect](function-clear-collect-clearcollect.md)** functions.

Because these functions change the state of the app, they can't be automatically recalculated. You can use them in the formulas for the **OnSelect**, **OnVisible**, **OnHidden**, and other **On...** properties, which are called behavior formulas.

### More than one action ###
Use semicolons to create a list of actions to perform. For example, you might want to update a context variable and then return to the previous screen:

- **UpdateContext( { x: 1 } ); Back()**

Actions are performed in the order in which they appear in the formula.  The next function won't start until the current function has completed. If an error occurs, subsequent functions might not start.
