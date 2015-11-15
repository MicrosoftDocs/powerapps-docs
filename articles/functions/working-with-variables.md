<properties
	pageTitle="PowerApps: Working with State"
	description="Reference information for working with state, context variables, and collections"
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
   ms.date="11/10/2015"
   ms.author="gregli"/>

# Working with Variables in PowerApps #

You may be asking: **where are the variables?**

If you are asking this question, you have probably used another programming tool in the past, such as VBA (Visual Basic for Applications) or JavaScript.  PowerApps is a little different, requiring a different approach.

When reaching for a variable, instead ask yourself: **what would I do in Excel?**  

PowerApps is modeled after Excel and what works well there often works in PowerApps too.  The equivalent of Excel's cells are PowerApps controls.  In other tools you may have explicitly performed a calculation and placed the result in a variable.  In PowerApps you create a formula that connects controls together and is automatically recalculated, just like Excel.  With this approach, your app will be easier to create, understand, and maintain. 

There is a place for variables in PowerApps.  PowerApps extends Excel's model with [behavior formulas]() that execute when, for example, a button is clicked.  Within a behavior formula, it is often helpful to set a variable to be used in other formulas.

## Working without variables ##

### Excel ###

Let's review how Excel works.  A cell can contain a value, such as a number or a string, or it can contain a formula that is based on and floats with the values of other cells.  After a user enters a new value into a cell, Excel dutifully recalculates all the dependent formulas based on the new value.  This behavior is automatic and does not require any programming.
![](media/working-with-variables/excel-recalc.png)
Excel does not have variables.  While a cell's value can float with a formula, there is no way to remember the result of a formula and store it in a cell (or anywhere else).  If you change a cell's value, the entire spreadsheet may change, and any previously calculated values will be lost.  Of course an Excel user can copy and paste cells, but that is under the user's manual control and is not possible with formulas.

### PowerApps ###

PowerApps behaves like Excel, with controls for cells.  For the above example in PowerApps, we make the following substitutions:
- Cell **A1** becomes an Input Text control, named **Text1**.  This allows the user to type in a value.
- Cell **A2** becomes an Input Text control, named **Text2**.  Again, the user can type into this text box.
- Cell **A3** becomes a Label control, named **Label1**.  This is where the result of our calculation will appear.
- The formula for **A3** becomes a formula for the label control: **Label1!Text = Text1 + Text2**.

This app has the same recalculation behavior as Excel.  Change the value of either of the text boxes, and the formula is recalculated automatically and the new result displayed.

You can use formulas for more than the primary value of a control, for example formatting properties can also be based on formulas.  For example, we can display negative values in red with the formula **Label1!Color = if( value( Label1!Text ) >= 0, Color!Black, Color!Red )**.  This formula is recalculated automatically as **Label1!Text** changes, which is recalculated automatically as **Text1** changes.

Data sources are an interesting case.  

Consider the advantages of this approach for building apps:
- A single formula connects three controls.  User changes automatically flow through.   

TODO: Data Sources, auto refresh

TODO: Data source,s updating

TODO: Map control with GPS

If possible, it is better to build your app without variables.
   
## The need for variables ##

Let's return to our simple adder.  What if we wanted to change our app to instead act like an old fashioned adding machine, with a running total.  Adding machines utilize a feature that Excel lacks: a button.

This app remembers the running total, and adds to it with each successive press of the "Add" button.  The "Clear" button resets the total to zero.

Remembering the result of a formula is sometimes needed for an app to do what we want.  But it also comes with downsides:
- We must manually update the running total with each button click.  No longer will automatic recalculation do this for us.   
- The running total can no longer be calculated based on the values of other controls, it is dependent on how many times the button was pressed and the value that was in the text box for each button press.  The steps that were taken to reach the total have been lost and only the total remains.  Backtracking to see where an error may have been introduced is impossible.
- Changes to the total can come from different paths.  In this app both the "Add" and "Clear" buttons can update the total.  

## Context Variables ##

To create our adding machine, we require a variable to hold the running total.  The simplest variables in PowerApps are called *context variables*.  The word "context" since they are limited to the context of a particular screen.

The basics of context variables:
- Context variables are used like any other named value in a formula.
- Context variables are created and set with the **UpdateContext** function.
- Context variables can also be set when a screen is displayed, with the **Navigate** function.  This is similar to parameter passing other languages, with the screen being a procedure or subroutine.
- Context variables are limited to the context of the current screen.   They cannot be used or set outside of this context (except with **Navigate** as described above).

## Collections ##

There are times when being limited to the context of a screen is inadequate.  You may need a variable that can be used and set from any formula, on any screen.  In these cases, you can use a [collection](working-with-data-sources#collections) to hold a global variable.

The basics of collections:
- Collections are a data source, and therefore a table.  To access a single variable stored in a collection, you will need to use the **First** or **Lookup** functions.
- Collections are created and set with the **Collect** and **ClearCollect** functions.
- Collections can be accessed from anywhere in the app.

Let's move our adding machine app's running total from a context variable to a collection:

TODO: Uses table record notation
  




PowerApps is similar.

| State | Recalcs? | Settable?  |
|-------|----------|------------|
| User input | No | Yes, user input to the app |
| Control Properties | Yes | No, driven by an author written formula and user input |
| Ambient | Yes | No, defined by the system |
| Data Sources | Yes | Yes, by external users and with Patch and other data functions |
| Context Variables | No | Yes, with UpdateContext and Navigate |
| Collections | No | Yes, with Collect |


    








