---
title: UpdateContext function in Power Apps
description: Reference information including syntax and examples for the UpdateContext function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/08/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# UpdateContext function in Power Apps
Creates or updates [context variables](../working-with-variables.md#use-a-context-variable) of the current screen.

## Overview
Use the **UpdateContext** function to create a context variable, which temporarily holds a piece of information, such as the number of times the user has selected a button or the result of a data operation.

Context variables are scoped to a screen, which means that you can't build a formula that refers to a context variable on another screen. If you've used another programming tool, you can think of a context variable as similar to a local variable.  Use the [**Set** function](function-set.md) to work with global variables that are available throughout your app.  

Power Apps are based on formulas that automatically recalculate as the user interacts with an app.  Context variables don't offer this benefit and can make your app harder to create and understand.  Before you use a context variable, review [working with variables](../working-with-variables.md).

## Description
To create or update a context variable, pass a single [record](../working-with-tables.md#records) to the **UpdateContext** function. In each record, specify the name of a [column](../working-with-tables.md#columns), which defines or matches the name of the variable, and the value to which you want to set that variable.

* If you specify the name of a variable that you've previously defined, **UpdateContext** sets the value of the variable to the value that you specify.
* If you specify the name of a variable that doesn't yet exist, **UpdateContext** creates a variable with that name and sets the value of that variable to the value that you specify.
* If you've previously defined a variable but don't specify it in this particular **UpdateContext** formula, its value remains the same.

Context variables are implicitly created by using the **UpdateContext** or [**Navigate** function](function-navigate.md).  There is no explicit declaration required.  If you remove all the **UpdateContext** and **Navigate** references to a context variable, then that context variable will cease to exist.  To clear a variable set its value to the result of the [**Blank** function](function-isblank-isempty.md).

You can see your variables' values, definitions, and uses with the Variables view under the File menu in the authoring environment.

You reference a context variable in a formula by using the variable's column name. For example, **UpdateContext( { ShowLogo: true } )** creates a context variable named **ShowLogo** and sets its value to **true**. You can then use the value of this context variable by using the name **ShowLogo** in a formula.  You can write **ShowLogo** as the formula for the **Visible** property of an image control and show or hide that control based on whether the value of the context variable is **true** or **false**.

As the examples later in this topic show, context variables can hold several kinds of information, including these:

* a single value
* a record
* a table
* an object reference
* any result from a formula

A context variable holds its value until the app is closed.  If you define a context variable and set its value on a particular screen, that information remains intact even if the user switches to a different screen.  Once the app is closed, the context variable's value will be lost and must be recreated when the app is loaded again.  

Every context variable is scoped to a screen. If you want to define a context variable on one screen and modify that variable from another screen, you must build a formula that's based on the **[Navigate](function-navigate.md)** function.  Or use a global variable.

**UpdateContext** has no return value, and you can use it only within a [behavior formula](../working-with-formulas-in-depth.md).

## Syntax
**UpdateContext**( *UpdateRecord* )

* *UpdateRecord* – Required. A record that contains the name of at least one column and a value for that column. A context variable is created or updated for each column and value that you specify.

**UpdateContext**( { *ContextVariable1*: *Value1* [, *ContextVariable2*: *Value2* [, ... ] ] } )

* *ContextVariable1* - Required.  The name of a context variable to create or update.
* *Value1* - Required.  The value to assign to the context variable.
* *ContextVariable2*: *Value2*, ... - Optional. Additional context variables to create or update and their values.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **UpdateContext( {&nbsp;Counter:&nbsp;1&nbsp;} )** |Creates or modifies the context variable **Counter**, setting its value to **1**. |**Counter** has the value **1**. You can reference that variable by using the name **Counter** in a formula. |
| **UpdateContext( {&nbsp;Counter:&nbsp;2&nbsp;} )** |Sets the value of the **Counter** context variable from the previous example to **2**. |**Counter** has the value **2**. |
| **UpdateContext( {&nbsp;Name:&nbsp;"Lily",&nbsp;Score:&nbsp;10&nbsp;} )** |Creates or modifies the context variables **Name** and **Score**, setting their values to **Lily** and **10** respectively. |**Name** has the value **Lily**, and **Score** has the value **10**. |
| **UpdateContext( {&nbsp;Person:&nbsp;{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;}&nbsp;} )** |Creates or modifies the context variable **Person**, setting its value to a record. The record contains two columns, named **Name** and **Address**. The value of the **Name** column is **Milton**, and the value of the **Address** column is **1 Main St**. |**Person** has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;}&nbsp;}**.<br><br>Reference this record as a whole with the name **Person**, or reference an individual column of this record with **Person.Name** or **Person.Address**. |
| **UpdateContext( {&nbsp;Person: Patch(&nbsp;Person,&nbsp;{Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}&nbsp;) }&nbsp;)** |Works with the **[Patch](function-patch.md)** function to update the **Person** context variable by setting the value of the **Address** column to **2 Main St**. |**Person** now has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}&nbsp;}**. |

### Step-by-step example 1
1. Name the default screen **Source**, add another screen, and name it **Target**.
2. On the **Source** screen, add two buttons, and set their **[Text](../controls/properties-core.md)** properties so that one says **English** and the other says **Spanish**.
3. Set the **[OnSelect](../controls/properties-core.md)** property of the **English** button to this expression:<br>**Navigate(Target, ScreenTransition.Fade, {Language:"English"})**
4. Set the **[OnSelect](../controls/properties-core.md)** property of the **Spanish** button to this expression:<br>**Navigate(Target, ScreenTransition.Fade, {Language:"Spanish"})**
5. On the **Target** screen, add a label, and set its **[Text](../controls/properties-core.md)** property to this expression:<br>**If(Language="English", "Hello!", "Hola!")**
6. On the **Target** screen, select **Shapes** on the **Insert** tab, and then select the Back arrow.
7. Set the Back arrow's **[OnSelect](../controls/properties-core.md)** property to this formula:<br>**Navigate(Source, ScreenTransition.Fade)**
8. From the **Source** screen, press F5, and then select the button for either language.

    On the **Target** screen, the label appears in the language that corresponds to the button that you selected.
9. Select the Back arrow to return to the **Source** screen, and then select the button for the other language.

    On the **Target** screen, the label appears in the language that corresponds to the button that you selected.
10. Press Esc to return to the default workspace.

### Step-by-step example 2

1. Open the canvas app where you want to use this formula. 
1. Add a new blank screen by selecting **New screen** from the command bar.
1. Add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula: <br> **UpdateContext( { Name: "Lily", Score: 10 } )**
   
[Another example](../add-screen-context-variables.md)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]