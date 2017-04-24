<properties
	pageTitle="If function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the If function in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# If function in PowerApps #

Returns one value if a condition is true, and returns another value if the same condition is false.

## Description ##

The **If** function tests conditions until a **true** result is found.  The corresponding value is then returned as the result.  You can use **If** to return different results based on comparisons and other tests.  

You can use **If** in [behavior formulas](../working-with-formulas-in-depth.md#behavior-formulas) to branch between two actions.  At most, one branch will be executed.  Conditions are evaluated in order, and after a **true** result is found, no further conditions are checked.

If no conditions are satisfied and an odd number of arguments are provided, the value of the last argument is returned.  This is the case with the common **If( *Condition*, *Value*, *Else* )**.  If an even number of arguments are provided, *Blank* is returned.

## Syntax ##

**If**( *Condition*, *Result* [, *ElseResult* ] )<br>**If**( *Condition1*, *Result1* [, *Condition2*, *Result2*, ... [ , *ElseResult* ] ] )

- *Condition(s)* - Required.  Formulas to test for **true**.  These formulas commonly contain comparison [operators](operators.md) (such as **<**, **>**, and **=**) and test functions such as **[IsBlank](function-isblank-isempty.md)** and **[IsEmpty](function-isblank-isempty.md)**.
- *Result(s)* - Required.  The corresponding value to return for a condition that evaluates to **true**.
- *ElseResult* - Optional.  The value to return if no conditions are satisfied.  If you don't specify this argument, *blank* is returned.

## Examples ##

### Values in formulas ###

In the following examples, a slider control named **Slider1** has a value of **25**.

| Formula | Description | Result |
|---------|-------------|--------|
| **If( Slider1.Value&nbsp;=&nbsp;25, "Result1" )** | The condition is **true**, and the corresponding result is returned. | "Result1" |
| **If( Slider1.Value&nbsp;>&nbsp;1000, "Result1" )** | The condition is **false**, and no *ElseResult* is provided.  | *blank* |
| **If( Slider1.Value&nbsp;=&nbsp;25, "Result1", "Result2" )** | The condition is **true**, and the corresponding result is returned. | "Result1" |
| **If( Slider1.Value&nbsp;>&nbsp;1000, "Result1", "Result2" )** | The condition is **false**, and the *ElseResult* has been provided and is returned.   | "Result2" |
| **If( Slider1.Value&nbsp;=&nbsp;25, "Result1", Slider1.Value&nbsp;>&nbsp;0, "Result2" )** | The first condition is **true**, and the corresponding result is returned. The second condition is also **true**, but its corresponding value isn't returned because it appears on the argument list after the first condition.  | "Result1" |
| **If( IsBlank(&nbsp;Slider1.Value&nbsp;), "Result1", IsNumeric(&nbsp;Slider1.Value&nbsp;), "Result2" )** | The first condition is **false** because the slider has a value of 25 and isn't *blank*. The second condition is **true** because the slider's value is a number, and the corresponding result is returned. | "Result2" |
| **If( Slider1.Value&nbsp;>&nbsp;1000, "Result1", Slider1.Value&nbsp;>&nbsp;50, "Result2", "Result3")** | Both the first and second conditions are **false**, and the *ElseResult* has been provided and is returned. | "Result3" |

### Branching in behavior formulas ###

In the following examples, a **[Text input](../controls/control-text-input.md)** control named **FirstName** has the value "John" typed into it.

| Formula | Description | Result |
|---------|-------------|--------|
| **If( ! IsBlank( FirstName.Text ), Navigate(&nbsp;Screen1, ScreenTransition.None ) )** | The condition is **true**, and the **[Navigate](function-navigate.md)** function is executed. You can use the **[IsBlank](function-isblank-isempty.md)** function to test whether a required form field has been filled in.  If the input text box was [blank](function-isblank-isempty.md), this formula would have no effect.  | **true**<br><br>The display is changed to **Screen1**. |
| **If( IsBlank( FirstName.Text ), Navigate(&nbsp;Screen1, ScreenTransition.None ), Back() )** | Without the **.** operator, the condition is **false**, and the **[Navigate](function-navigate.md)** function isn't executed.  Because the *ElseResult* has been provided, the **[Back](function-navigate.md)** function is executed. | **true**<br><br>The display goes back to the screen that was previously shown. |

### Step by step ###

1. On an empty screen, add a **[Text input](../controls/control-text-input.md)** control, and name it **Text1** if it doesn't have that name by default.

2. In **Text1**, type **15**.

3. Add a label, and set its **[Text](../controls/properties-core.md)** property to the following formulas:

| Formula | Description | Result |
|---------|-------------|--------|
| **Text1.Text** | With no condition, the return value is the value of the input-,text control. | "15" |
| **If( Value(Text1.Text) < 40, "Order more!", Text1.Text )** | The condition is **true**, and the corresponding value is returned. | "Order more!" |
| **If( Value(Text1.Text) < 20, "Order MANY more!", Value(Text1.Text) < 40, "Order more!", Text1.Text )** |  The first condition is **true**, and the corresponding value is returned. | "Order MANY more!" |
