---
title: Understand behavior formulas for canvas apps
description: Reference information about working with behavior formulas, which change the state of a canvas app.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/10/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - gregli-msft
---
# Understand behavior formulas for canvas apps

Most formulas calculate a value.  Like an Excel spreadsheet, recalculation happens automatically as values change.  For example, you might want to show the value in a **[Label](controls/control-text-box.md)** control in red if the value is less than zero or in black otherwise. So you can set the **[Color](controls/properties-color-border.md)** property of that control to this formula:

```powerapps-dot
If( Value(TextBox1.Text) >= 0, Color.Black, Color.Red )
```

In this context, what does it mean when the user selects a **[Button](controls/control-button.md)** control?  No value has changed, so there is nothing new to calculate. Excel has no equivalent to a **[Button](controls/control-button.md)** control.  

By selecting a **[Button](controls/control-button.md)** control, the user initiates a sequence of actions, or behaviors, that will change the state of the app:

* Change the screen that's displayed: **[Back](functions/function-navigate.md)** and **[Navigate](functions/function-navigate.md)** functions.
* Control a [signal](functions/signals.md): **[Enable](functions/function-enable-disable.md)** and **[Disable](functions/function-enable-disable.md)** functions.
* Refresh, update, or remove items in a [data source](working-with-data-sources.md): **[Refresh](functions/function-refresh.md)**, **[Update](functions/function-update-updateif.md)**, **[UpdateIf](functions/function-update-updateif.md)**, **[Patch](functions/function-patch.md)**, **[Remove](functions/function-remove-removeif.md)**, **[RemoveIf](functions/function-remove-removeif.md)** functions.
* Update a [context variable](working-with-variables.md#use-a-context-variable):  **[UpdateContext](functions/function-updatecontext.md)** function.
* Create, update, or remove items in a [collection](working-with-data-sources.md#collections):  **[Collect](functions/function-clear-collect-clearcollect.md)**, **[Clear](functions/function-clear-collect-clearcollect.md)**, **[ClearCollect](functions/function-clear-collect-clearcollect.md)** functions.

Because these functions change the state of the app, they can't be automatically recalculated. You can use them in the formulas for the **[OnSelect](controls/properties-core.md)**, **[OnVisible](controls/control-screen.md)**, **[OnHidden](controls/control-screen.md)**, and other **On...** properties, which are called behavior formulas.

### More than one action
Use semicolons to create a list of actions to perform. For example, you might want to update a context variable and then return to the previous screen:

```powerapps-dot
UpdateContext( { x: 1 } ); Back()
```

Actions are performed in the order in which they appear in the formula.  The next function won't start until the current function has completed. If an error occurs, subsequent functions might not start.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]