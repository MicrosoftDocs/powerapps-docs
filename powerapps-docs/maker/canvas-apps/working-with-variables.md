---
title: Understand variables in canvas apps | Microsoft Docs
description: Reference information about working with state, context variables, and collections in canvas apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 02/28/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Understand canvas-app variables in PowerApps

If you've used another programming tool, such as Visual Basic or JavaScript, you may be asking: **Where are the variables?** PowerApps is a little different and requires a different approach. Instead of reaching for a variable when you build a canvas app, ask yourself: **What would I do in Excel?**

In other tools, you may have explicitly performed a calculation and stored the result in a variable. However, PowerApps and Excel both automatically recalculate formulas as the input data changes, so you usually don't need to create and update variables. By taking this approach whenever possible, you can  more easily create, understand, and maintain your app.

In some cases, you'll need to use variables in PowerApps, which extends Excel's model by adding [behavior formulas](working-with-formulas-in-depth.md). These formulas run when, for example, a user selects a button. Within a behavior formula, it's often helpful to set a variable to be used in other formulas.

In general, avoid using variables. But sometimes only a variable can enable the experience you want. Key point to remember: variables in PowerApps are implicitly created and typed.

## Translate Excel into PowerApps

### Excel
Let's review how Excel works. A cell can contain a value, such as a number or a string, or a formula that's based on the values of other cells. After the user enters a different value into a cell, Excel automatically recalculates any formulas that depend on the new value. You don't have to do any programming to enable this behavior.

![](media/working-with-variables/excel-recalc.png)

Excel doesn't have variables. The value of a cell that contains a formula changes based on its input, but there's no way to remember the result of a formula and store it in a cell or anywhere else. If you change a cell's value, the entire spreadsheet may change, and any previously calculated values are lost.  An Excel user can copy and paste cells, but that's under the user's manual control and isn't possible with formulas.

### PowerApps
Apps that you create in PowerApps behave very much like Excel. Instead of updating cells, you can add controls wherever you want on a screen and name them for use in formulas.

For example, you can replicate the Excel behavior in an app by adding a **[Label](controls/control-text-box.md)** control, named **TextBox1**, and two **[Text input](controls/control-text-input.md)** controls, named **TextInput1** and **TextInput2**. If you then set the **[Text](controls/properties-core.md)** property of **TextBox1** to **TextInput1 + TextInput2**,  it will always shows the sum of whatever numbers are in **TextInput1** and **TextInput2** automatically.

![](media/working-with-variables/recalc1.png)

Notice that the **TextBox1** control is selected, showing its **[Text](controls/properties-core.md)** formula in the formula bar at the top of the screen.  Here we find the formula **TextInput1 + TextInput2**.  This formula creates a dependency between these controls, just as dependencies are created between cells in an Excel workbook.  Let's change the value of the **TextInput1**:

![](media/working-with-variables/recalc2.png)

The formula for **TextBox1** has been automatically recalculated, showing the new value.

In PowerApps, you can use formulas to determine not only the primary value of a control but also properties such as formatting. In the next example, a formula for the **[Color](controls/properties-color-border.md)** property of the label will automatically show negative values in red. The **[If](functions/function-if.md)** function should look very familiar from Excel:
<br>**If( Value(TextBox1.Text) < 0, Red, Black )**

![](media/working-with-variables/recalc-color1.png)

Now, if the result of our calculation in **TextBox1.Text** is negative, the number will be shown in red:

![](media/working-with-variables/recalc-color2.png)

You can use formulas for a wide variety of scenarios:

* By using your device's GPS, a map control can display your current location with a formula that uses **Location.Latitude** and **Location.Longitude**.  As you move, the map will automatically track your location.
* Other users can update [data sources](working-with-data-sources.md).  For example, others on your team might update items in a SharePoint list.  When you refresh a data source, any dependent formulas are automatically recalculated to reflect the updated data. Furthering the example, you might set a gallery's **[Items](controls/properties-core.md)** property to the formula **Filter( SharePointList )**, which will automatically display the newly filtered set of [records](working-with-tables.md#records).

### Benefits
Using formulas to build apps has many advantages:

* If you know Excel, you know PowerApps. The model and formula language are the same.
* If you've used other programming tools, think about how much code would be required to accomplish these examples.  In Visual Basic, you'd need to write an event handler for the change event on each text-input control.  The code to perform the calculation in each of these is redundant and could get out of sync, or you'd need to write a common subroutine.  In PowerApps, you accomplished all of that with a single, one-line formula.
* To understand where **TextBox1**'s text is coming from, you know exactly where to look: the formula in the **[Text](controls/properties-core.md)** property.  There's no other way to affect the text of this control.  In a traditional programming tool, any event handler or subroutine could change the value of the label, from anywhere in the program.  This can make it hard to track down when and where a variable was changed.
* If the user changes a slider control and then changes their mind, they can change the slider back to its original value.  And it's as if nothing had ever changed: the app shows the same control values as it did before.  There are no ramifications for experimenting and asking "what if," just as there are none in Excel.  

In general, if you can achieve an effect by using a formula, you'll be better off. Let the formula engine in PowerApps work for you.  

## Know when to use variables
Let's change our simple adder to act like an old-fashioned adding machine, with a running total. If you select an **Add** button, you'll add a number to the running total. If you select a **Clear** button, you'll reset the running total to zero.

![](media/working-with-variables/button-changes-state.png)

Our adding machine uses something that doesn't exist in Excel: a button. In this app, you can't use only formulas to calculate the running total because its value depends on a series of actions that the user takes. Instead, our running total must be recorded and updated manually. Most programming tools store this information in a *variable*.    

You'll sometimes need a variable for your app to behave the way you want.  But the approach comes with caveats:

* You must manually update the running total. Automatic recalculation won't do it for you.
* The running total can no longer be calculated based on the values of other controls. It depends on how many times the user selected the **Add** button and what value was in the text-input control each time. Did the user enter 77 and select **Add** twice, or did they specify 24 and 130 for each of the additions? You can't tell the difference after the total has reached 154.
* Changes to the total can come from different paths. In this example, both the **Add** and **Clear** buttons can update the total. If the app doesn't behave the way you expect, which button is causing the problem?

## Use a global variable
To create our adding machine, we require a variable to hold the running total. The simplest variables to work with in PowerApps are *global variables*.  

How global variables work:

* You set the value of the global variable with the **[Set](functions/function-set.md)** function.  **Set( MyVar, 1 )** sets the global variable **MyVar** to a value of **1**.
* You use the global variable by referencing the name used with the **Set** function.  In this case, **MyVar** will return **1**.
* Global variables can hold any value, including strings, numbers, records, and [tables](working-with-tables.md).

Let's rebuild our adding machine by using a global variable:

1. Add a text-input control, named **TextInput1**, and two buttons, named **Button1** and **Button2**.

2. Set the **[Text](controls/properties-core.md)** property of **Button1** to **"Add"**, and set the **Text** property of **Button2** to  **"Clear"**.

3. To update the running total whenever a user selects the **Add** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **Set( RunningTotal, RunningTotal + TextInput1 )**
   
    The mere existance of this formula establishes **RunningTotal** as a global variable that holds a number because of the **+** operator.  **RunningTotal** can now be referenced anywhere in the app.  Whenever this app is loaded and begins execution, **RunningTotal** will have an initial value of *blank*.    

    The first time a user selects the **Add** button and **[Set](functions/function-set.md)** is executed, **RunningTotal** will be set to the value **RunningTotal + TextInput1**
   
    ![](media/working-with-variables/global-variable-1.png)
4. To set the running total to **0** whenever the user selects the **Clear** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **Set( RunningTotal, 0 )**
   
    ![](media/working-with-variables/global-variable-2.png)
5. Add a **[Label](controls/control-text-box.md)** control, and set its **[Text](controls/properties-core.md)** property to **RunningTotal**.
   
    This formula will automatically be recalculated and show the user the value of **RunningTotal** as it changes based on the buttons that the user selects.
   
    ![](media/working-with-variables/global-variable-3.png)
6. Preview the app, and we have our adding machine as described above.  Enter a number in the text box and press the **Add** button a few times.  When ready, return to the authoring experience using the Esc key.  
   
    ![](media/working-with-variables/global-variable-4.png)
7. To see our global variable's value, select the **File** menu and select **Variables** in the left hand pane.
   
    ![](media/working-with-variables/global-variable-file-1.png)
8. To see all the places where our variable is defined and used, select it.
   
    ![](media/working-with-variables/global-variable-file-2.png)

## Types of variables
There are three types of variables in PowerApps:

| Variables type | Scope | Description | Functions that Establish |
| --- | --- | --- | --- |
| Global variables |App |Simplest to use.  Holds a number, text string, Boolean, record, table, etc. that can be references from anywhere in the app. |[**Set**](functions/function-set.md) |
| Context variables |Screen |Great for passing values to a screen, much like parameters to a procedure in other languages.  Can only be referenced from one screen. |[**UpdateContext**](functions/function-updatecontext.md)<br>[**Navigate**](functions/function-navigate.md) |
| Collections |App |Holds a table that can be references from anywhere in the app.  Allows the contents of the table to be modified rather than being set as a whole. Can be saved to the local device for later use. |[**Collect**](functions/function-clear-collect-clearcollect.md)<br>[**ClearCollect**](functions/function-clear-collect-clearcollect.md) |

## Creating and removing variables
All variables are created implicitly when they appear in a **Set**, **UpdateContext**, **Navigate**, **Collect**, or **ClearCollect** function.  Appearance in these functions, anywhere in your app, is all that is needed to declare a variable and its type.  Executing these functions does not create a variable; these function only fill a variable with a value.  There is no explicit declaration of variables as is done in other programming tools and all typing is implicit from usage.

For example, imagine you have a button control with an **OnSelect** formula equal to **Set( X, 1 )**.  That this formula exists in your app establishes **X** as a variable with a type of number.  You can now use **X** in formulas as a number and it will default to its initial value of *blank*.  **All this happened without pressing the button!**  Press the button and **X** will now have a value of **1**.

What would happen if you add another button with an **OnSelect** formula equal to **Set( X, "Hello" )**?  This will produce an error because the type (text string) does not match the type in the previous **Set** (number).  All implicit definitions of the variable must agree on type.  Again, all this happened because **X** was mentioned in formulas, not because any of those formulas had actually executed.

How do you remove a variable?  Simply remove all the **Set**, **UpdateContext**, **Navigate**, **Collect**, or **ClearCollect** function calls that had implicitly established the variable.  Without these the variable does not exist.  Remember to remove any references to the variable too as those will now be in error.

## Variable lifetime and initial value
All variables are held in memory while the app is running.  After the app closes, the values held in the variables are lost.  

You can store the contents of a variable in a Data Source using **Patch** or **Collect** functions, or in the case of collections you can store to the local device with the [**SaveData**](functions/function-savedata-loaddata.md) function.  

When the app is first loaded all variables will have the *blank* value.

## Reading variables
You use the variable's name to read its value. For example, you can define a variable with this formula:

`Set( MyColor, Red )`

Then you can simply use **MyColor** anywhere a color value can be used, and it will be replaced with **Red**. If you give a context variable the same name as a global variable or a collection, the context variable will take precedence. However, you can still reference the global variable or collection if you use the [disambiguation operator](functions/operators.md#disambiguation-operator) **@[MyColor]**.

## Use a context variable
Let's look at how our adding machine would be created using a context variable instead of a global variable.    

How context variables work:

* You implicitly establish and set context variables by using the **[UpdateContext](functions/function-updatecontext.md)** or **[Navigate](functions/function-navigate.md)** function.  When the app starts its initial value will be *blank*.
* You update context variables with records. In other programming tools, you commonly use "=" for assignment, as in "x = 1".  For context variables, use **{ x: 1 }** instead. When you use a context variable, use its name directly without the record syntax.  
* You can also set a context variable when a screen is displayed, by using the **[Navigate](functions/function-navigate.md)** function. If you think of a screen as a kind of procedure or subroutine, this is similar to parameter passing in other programming tools.
* Except for **[Navigate](functions/function-navigate.md)**, context variables are limited to the context of a single screen, which is where they get their name.  You can't use or set them outside of this context.
* Context variables can hold any value, including strings, numbers, records, and [tables](working-with-tables.md).

Let's rebuild our adding machine by using a context variable:

1. Add a text-input control, named **TextInput1**, and two buttons, named **Button1** and **Button2**.

2. Set the **[Text](controls/properties-core.md)** property of **Button1** to **"Add"**, and set the **Text** property of **Button2** to  **"Clear"**.

3. To update the running total whenever a user selects the **Add** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **UpdateContext( { RunningTotal: RunningTotal + TextInput1 } )**
   
    The mere existance of this formula establishes **RunningTotal** as a context variable that holds a number because of the **+** operator.  **RunningTotal** can now be referenced anywhere in this screen.  Whenever this app is loaded and begins execution, **RunningTotal** will have an initial value of *blank*.    

    The first time a user selects the **Add** button and **[UpdateContext](functions/function-updatecontext.md)** is executed, **RunningTotal** will be set to the value **RunningTotal + TextInput1**.
   
    ![](media/working-with-variables/context-variable-1.png)
4. To set the running total to **0** whenever the user selects the **Clear** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **UpdateContext( { RunningTotal: 0 } )**
   
    Again, **[UpdateContext](functions/function-updatecontext.md)** is used with the formula **UpdateContext( { RunningTotal: 0 } )**.
   
    ![](media/working-with-variables/context-variable-2.png)
5. Add a **[Label](controls/control-text-box.md)** control, and set its **[Text](controls/properties-core.md)** property to **RunningTotal**.
   
    This formula will automatically be recalculated and show the user the value of **RunningTotal** as it changes based on the buttons that the user selects.
   
    ![](media/working-with-variables/context-variable-3.png)
6. Preview the app and we have our adding machine as described above.  Enter a number in the text box and press the **Add** button a few times.  When ready, return to the authoring experience using the Esc key.  
   
    ![](media/working-with-variables/context-variable-4.png)
7. You can set the value of a context variable while navigating to a screen.  This is useful for passing "context" or "parameters" from one screen to another.  To see this, insert a new screen, and insert a button with the **OnSelect** property set to:
   
    **Navigate( Screen1, None, { RunningTotal: -1000 } )**
   
    ![](media/working-with-variables/context-variable-5.png)
   
    Selecting this button on **Screen2** (which you can do while authoring if you select the button toward the ends) will show **Screen1** and also set the context variable **RunningTotal** to -1000.
   
    ![](media/working-with-variables/context-variable-6.png)
8. To see our context variable's value, select the **File** menu and select **Variables** in the left hand pane.
   
    ![](media/working-with-variables/context-variable-file-1.png)
9. To see where your context variable is defined and used, select it.
   
    ![](media/working-with-variables/context-variable-file-2.png)

## Use a collection
Finally, let's look at creating our adding machine with a collection.  Since a collection holds a table that is easy to modify, we will make this adding machine keep a "paper tape" of each value as they are entered.

How collections work:

* Create and set collections by using the **[ClearCollect](functions/function-clear-collect-clearcollect.md)** function.  You can use the **[Collect](functions/function-clear-collect-clearcollect.md)** function instead, but it will effectively require another variable instead of replacing the old one.  
* A collection is a kind of data source and, therefore, a table. To access a single value in a collection, use the **[First](functions/function-first-last.md)** function, and extract one field from the resulting record. If you used a single value with **[ClearCollect](functions/function-clear-collect-clearcollect.md)**, this will be the **Value** field, as in this example:<br>**First(** *VariableName* **).Value**

Let's recreate our adding machine by using a collection:

1. Add a **[Text input](controls/control-text-input.md)** control, named **TextInput1**, and two buttons, named **Button1** and **Button2**.

2. Set the **[Text](controls/properties-core.md)** property of **Button1** to **"Add"**, and set the **Text** property of **Button2** to **"Clear"**.

3. To update the running total whenever a user selects the **Add** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **Collect( PaperTape, TextInput1.Text )**

    The mere existance of this formula establishes **PaperTape** as a collection that holds a single column table of text strings.  **PaperTape** can now be referenced anywhere in this app.  Whenever this app is loaded and begins execution, **PaperTape** will be an empty table.  
   
    When executed, this formula will add the new value to the end of the collection.  Since we are adding a single value, **Collect** will automatically place it in a single column table with the column name **Value** which we will use later.
   
    ![](media/working-with-variables/papertape-1.png)
4. To clear our paper tape when the user selects the **Clear** button, set its **[OnSelect](controls/properties-core.md)** property to this formula:
   
    **Clear( PaperTape )**
   
    ![](media/working-with-variables/papertape-2.png)
5. To display the running total, add a label, and set its **[Text](controls/properties-core.md)** property to this formula:
   
    **Sum( PaperTape, Value )**
   
    ![](media/working-with-variables/papertape-3.png)
6. To run the adding machine, press F5 to open Preview, enter numbers in the text-input control, and select buttons.
   
    ![](media/working-with-variables/papertape-run-1.png)
7. To return to the default workspace, press the Esc key.
8. To display the paper tape, insert a **Data table** control, and set its **[Items](controls/properties-core.md)** property to this formula:
   
    **PaperTape**
   
    You will also need to select the columns to show in the right hand pane, in our case show the **Value** column:
   
    ![](media/working-with-variables/papertape-4.png)
9. To see the values in your collection, select **Collections** on the **File** menu.
   
    ![](media/working-with-variables/papertape-file.png)
10. To store and retrieve your collection, add two additional button controls and set their text to **Load** and **Save**.  For **Load**, set the **OnSelect** property to:
    
     **Clear( PaperTape ); LoadData( PaperTape, "StoredPaperTape", true )**
    
     We need to clear the collection first as **LoadData** will append the stored values to the end of the collection.
    
     ![](media/working-with-variables/papertape-5.png)
11. For **Save**, set the **OnSelect** property to:
    
     **SaveData( PaperTape, "StoredPaperTape" )**
    
     ![](media/working-with-variables/papertape-6.png)
12. Preview again by pressing the F5 key, enter numbers in the text-input control, and select buttons.  Select the **Save** button.  Close and reload your app, and select the **Load** button to reload your collection.  
    
    > [!NOTE]
    > **SaveData** and **LoadData** don't function in PowerApps Studio or the web player for PowerApps, but they do in PowerApps Mobile.

