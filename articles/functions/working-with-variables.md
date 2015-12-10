<properties
	pageTitle="Working with variables | Microsoft PowerApps"
	description="Reference information for working with state, context variables, and collections"
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

# Working with variables in PowerApps #

You may be asking: **Where are the variables?**

If you're asking this question, you've probably used another programming tool in the past, such as Visual Basic or JavaScript.  PowerApps is a little different, requiring a different approach.

When reaching for a variable, instead ask yourself: **What would I do in Excel?**

PowerApps is modeled after Microsoft Excel and what works there often works in PowerApps too. The equivalent of Excel's cells are PowerApps controls. In other tools, you may have explicitly performed a calculation and placed the result in a variable. In PowerApps, you create a formula that connects controls together and is automatically recalculated, just like Excel. With this approach, your app will be easier to create, understand, and maintain.

There is a place for variables in PowerApps, which extends Excel's model with [behavior formulas](working-with-formulas-in-depth.md#behavior-formulas) that execute when, for example, a user clicks a button.  Within a behavior formula, it's often helpful to set a variable to be used in other formulas.

## Working without variables ##

### Excel ###

Let's review how Excel works.  A cell can contain a value, such as a number or a string, or it can contain a formula that's based on and floats with the values of other cells.  After a user enters a new value into a cell, Excel dutifully recalculates all the dependent formulas based on the new value.  This behavior is automatic and doesn't require you to do any programming.

![](media/working-with-variables/excel-recalc.png)

Excel doesn't have variables.  A cell's value can float with a formula, but there's no way to remember the result of a formula and store it in a cell or anywhere else.  If you change a cell's value, the entire spreadsheet may change, and any previously calculated values will be lost.  An Excel user can copy and paste cells, but that's under the user's manual control and isn't possible with formulas.

### PowerApps ###

PowerApps behaves very much like Excel. Instead of cells, you can name and place controls wherever you want on a screen.  The Excel example looks like the following in an app:

- An input-text control, named **Text1**, which takes the place of cell **A1**.  In this control, the user types the first value to add.
- Another input-text control, named **Text2**, which takes the place of cell **A2**.  In this control, the user types in the second value to add.
- A label, named **Label1**, which takes the place of cell **A3** and shows the result of the addition.
- A formula for the **Text** property of **Label1**, which performs the addition:<br>**Label1!Text = Text1 + Text2**

This app has the same recalculation behavior as Excel. If you change the value of either of the text boxes, the label's formula is recalculated automatically, and the new result is displayed.

![](media/working-with-variables/recalc.png)

In PowerApps, formulas can determine more than the primary value of a control.  For example, you can use formulas to control formatting.  In this next example, a formula for the Color property of the label will automatically show negative values in red.  The **[If](function-if.md)** function should look very familiar from Excel.

![](media/working-with-variables/recalc-color.png)

Formulas can be used for a wide variety of scenarios:

- By using your device's GPS, a map control can display your current location with a formula that uses **Location!Lattitude** and **Location!Longitude**.  As you move, the map will automatically track your location.
- Other users can update [data sources](working-with-data-sources.md).  For example, others on your team might update items in a SharePoint list.  When you refresh a data source, any dependent formulas are automatically recalculated and displayed on the updated data.  Furthering the example, you might set a gallery's **Items** property to the formula **Filter( SharePointList )**, which will automatically display the newly filtered set of [records](working-with-tables.md#records).

### Benefits ###

Using formulas to build apps has many advantages:

- If you know Excel, you know PowerApps.  The model and formula language are the same.
- If you've used other programming tools, think about how much code would be required to accomplish these examples.  In Visual Basic, you'd need to write an event handler for the change event on each text box.  The code to perform the calculation in each of these is redundant and could get out of sync, or you'd need to write a common subroutine.  In PowerApps, all of that was accomplished with a single one-line formula.
- To understand where **Label1**'s text is coming from, you know exactly where to look: the formula in the **Text** property.  There's no other way to affect the text of this control.  In a traditional programming tool, any event handler or subroutine could change the value of the label, from anywhere in the program.  This can make it hard to track down when and where a variable was changed.
- If a user changes a slider control and then changes their mind, they can change the slider back to its original value.  And it's as if nothing had ever changed: the app shows the same control values as it did before.  There are no ramifications for experimenting and asking "what if," just as there are none in Excel.  

In general, if your desired behavior can be accomplished through a formula, you'll be better off. Let PowerApps' formula engine work for you.  

## The need for variables ##

Let's change our simpler adder to act like an old-fashioned adding machine, with a running total. If you select an **Add** button, you'll add a number to the running total. If you select a **[Clear](function-clear-collect-clearcollect.md)** button, you'll reset the running total to zero.

![](media/working-with-variables/button-changes-state.png)

Our adding machine uses something that doesn't exist in Excel: a button.  In this app, the running total can't be calculated because its value depends on a series of actions that the user takes.  Instead, our running total must be recorded and updated manually.  It's what most programming tools call a *variable*.    

You'll sometimes need a variable for your app to behave the way you want.  But it comes with some caveats:

- You must manually update the running total. Automatic recalculation won't do it for you.   
- The running total can no longer be calculated based on the values of other controls. It depends on how many times the user selected the button and what value was in the text box each time.  Did the user enter 77 and select **Add** twice, or did they specify 24 and 130 for each of the additions?  You can't tell the difference after the total has reached 154.
- Changes to the total can come from different paths.  In this example, both the **Add** and **[Clear](function-clear-collect-clearcollect.md)** buttons can update the total.  Which one is causing an undesired behavior?

In general, avoid using variables.  But sometimes only a variable can enable the experience you want.

## Context variables ##

To create our adding machine, we require a variable to hold the running total.  The simplest variables in PowerApps are *context variables*.  

How context variables work:

- You create and set context variables by using the **[UpdateContext](function-updatecontext.md)** function.  If a context variable doesn't already exist when first updated, it will be created with a default value of *blank*.
- You create and update context variables with records.  In other programming tools, you  commonly use "=" for assignment, as in "x = 1".  For context variables, use **{ x: 1 }** instead.  When you use a context variable, use its name directly.  
- You can also set a context variable when a screen is displayed, by using the **[Navigate](function-navigate.md)** function.  If you think of a screen as a kind of procedure or subroutine, this is similar to parameter passing in other programming tools.
- Except for **[Navigate](function-navigate.md)**, context variables are limited to the context of a single screen (which is where they get their name).  You can't use or set them outside of this context.
- Context variables can hold any value, including strings, numbers, records, and [tables](working-with-tables.md).
- When an app ends, all of its context variables are lost.   

Let's build our adding machine by using context variables:

1. We start with an input-text control, named **Text1**, and two buttons, named **Button1** and **Button2**.

	When a user selects **Button1**, its **OnSelect** property will add to the running total based on this formula:<br> **UpdateContext( { RunningTotal: RunningTotal + Text1 } )**.

	The first time a user selects **Button1** and **[UpdateContext](function-updatecontext.md)** is called, **RunningTotal** is created with a default value of *blank*.  In the addition, it will be treated as a zero.

	![](media/working-with-variables/context-variable-1.png)

2. **Button2** will clear the running total by setting it to 0.  Again, **[UpdateContext](function-updatecontext.md)** is used with the formula **UpdateContext( { RunningTotal: 0 } )**.

	![](media/working-with-variables/context-variable-2.png)

3. Finally, we insert a label, named **Label1**, which will display the value of **RunningTotal**.  This formula will automatically be recalculated and show the user the value of **RunningTotal** as it changes based on the buttons the user selects.

	![](media/working-with-variables/context-variable-3.png)

4. Preview the app, and we have our adding machine as described above.

## Collections ##

Being limited to the context of a screen is sometime inadequate.  You may need a variable that can be used and set from any screen.  In these cases, use a [collection](working-with-data-sources.md#collections) to hold a global variable.

How collections work:

- You create and set collections by using the **[ClearCollect](function-clear-collect-clearcollect.md)** function.  You can use the **[Collect](function-clear-collect-clearcollect.md)** function instead, but it will effectively require another variable instead of replacing the old one.  
- A collection is a data source and, therefore, a table.  To access a single value stored in a collection, use the **[First](function-first-last.md)** function, and extract one property from the resulting record.  If you used a single value with **[ClearCollect](function-clear-collect-clearcollect.md)**, this will be the **Value** property, as in this example:<br>**First( VariableName )!Value**
- Collections can be accessed from any formula in the app, on any screen.
- When an app ends, all of its collections are emptied.

Let's recreate our adding machine using a collection:

1. Again, start with an input-text control, named **Text1**, and two buttons, named **Button1** and **Button2**.

	When the user selects **Button1**, its **OnSelect** property will update the running total by using this formula:<br> **ClearCollect( RunningTotal, First( RunningTotal )!Value + Text1 )**

	By using **[ClearCollect](function-clear-collect-clearcollect.md)** with a single value, a record will be created in the collection with a single **Value** property.

	The first time that the user selects **Button1** and **[ClearCollect](function-clear-collect-clearcollect.md)** is called, **RunningTotal** will be [empty](function-isblank-isempty.md).  In the addition, **[First](function-first-last.md)** will return *blank* and will be treated as a zero.

	![](media/working-with-variables/collection-1.png)

2. **Button2** will clear the running total by setting it to 0.  Again, **[ClearCollect](function-clear-collect-clearcollect.md)** is used with the formula **ClearCollect( RunningTotal, 0 )**.

	![](media/working-with-variables/collection-2.png)

3. Finally, we insert a label, named **Label1**, which will display the value of **RunningTotal**.  This formula will automatically be recalculated and show the user the value of **RunningTotal** as it changes based on the buttons that the user selects.  We need to extract the **Value** property of the first record of the **RunningTotal** collection.

	![](media/working-with-variables/collection-3.png)

4. Preview the app, and we have our adding machine as described above.

5. Return to the default workspace. On the **File** menu, select **Collections** to see your collection's value.

	![](media/working-with-variables/view-collections.png)
