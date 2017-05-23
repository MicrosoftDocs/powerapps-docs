<properties
	pageTitle="If and Switch functions | Microsoft PowerApps"
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
   ms.date="04/24/2017"
   ms.author="gregli"/>

# If and Switch functions in PowerApps #

After finding a true condition or match, evaluates a corresponding formula and returns the result.

## Description ##

The **If** function tests a series of conditions until a **true** result is found.  When found, a corresponding formula is evaluated and returned as the result of the function.  If no condition evaluates to **true**, a final default result can be returned. 

The **Switch** function evaluates a formula and compares the result with a series of possible matches. When a match is found, a corresponding formula is evaluated and returned as the result of the function.  If no match is found, a final default result can be returned. 

**If** and **Switch** are very similar.  Here are some of the reasons to use one versus the other:

- Use **If** if you have a single condition to be evaluated.  **If( *Condition*, *ThenResult*, *ElseResult* )** is the most common form of **If**.
- Use **If** if you have multiple unrelated conditions. Supporting multiple conditions extends the Microsoft Excel **If** function and avoids the need for nested **If**s.
- Use **Switch** if you have a single formula with multiple possible matches.  You can also use **If** for this but it would require repeating the formula for each match.

You can use both of these functions in [behavior formulas](../working-with-formulas-in-depth.md#behavior-formulas) to branch between two or more actions.  Only one branch will be executed.  Conditions and matches are evaluated in order and stops after a **true** condition or match is found.

If no conditions/matches are satisfied and a default result has not been provided, *Blank* is returned.

## Syntax ##

**If**( *Condition*, *Result* [, *DefaultResult* ] )<br>**If**( *Condition1*, *Result1* [, *Condition2*, *Result2*, ... [ , *DefaultResult* ] ] )

- *Condition(s)* - Required.  Formulas to test for **true**.  These formulas commonly contain comparison [operators](operators.md) (such as **<**, **>**, and **=**) and test functions such as **[IsBlank](function-isblank-isempty.md)** and **[IsEmpty](function-isblank-isempty.md)**.
- *Result(s)* - Required.  The corresponding value to return for a condition that evaluates to **true**.
- *DefaultResult* - Optional.  The value to return if no conditions are satisfied.  If you don't specify this argument, *blank* is returned.

**Switch**( *Formula*, *Match1*, *Result1* [, *Match2*, *Result2*, ... [, *DefaultResult* ] ] )

- *Formula* - Required.  Formula to evaluate for matches.  This formula is evaluated only once.
- *Match(s)* - Required.  Values to compare with the result from *Formula*.  If a match is found, the corresponding *Result* is returned.  The match must be exact.
- *Result(s)* - Required. The corresponding value to return for when a match is found.
- *DefaultResult* - Optional.  If no match is found, this value is returned.  If you don't specify this argument, *blank* is returned.

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
| **Switch( Slider1.Value, 25, "Result1" )** | The value of the formula matches the value for the first match of **25**, and the corresponding result is returned. | "Result1" |
| **Switch( Slider1.Value, 20, "Result1", 25, "Result2", 30, "Result3" )** | The value of the formula matches the value for the second match of **25**, and the corresponding result is returned. | "Result2" |
| **Switch( Slider1.Value, 20, "Result1", 10, "Result2", 0, "Result3", "ElseResult" )** | The value of the formula does not match any of the match values.  Since an additional result argument has been supplied, it is returned.  | "ElseResult" |

### Branching in behavior formulas ###

In the following examples, a **[Text input](../controls/control-text-input.md)** control named **FirstName** has the value "John" typed into it.

| Formula | Description | Result |
|---------|-------------|--------|
| **If( ! IsBlank( FirstName.Text ), Navigate(&nbsp;Screen1, ScreenTransition.None ) )** | The condition is **true**, and the **[Navigate](function-navigate.md)** function is executed. You can use the **[IsBlank](function-isblank-isempty.md)** function to test whether a required form field has been filled in.  If the text-input box was [blank](function-isblank-isempty.md), this formula would have no effect.  | **true**<br><br>The display is changed to **Screen1**. |
| **If( IsBlank( FirstName.Text ), Navigate(&nbsp;Screen1, ScreenTransition.None ), Back() )** | Without the **.** operator, the condition is **false**, and the **[Navigate](function-navigate.md)** function isn't executed.  Because the *ElseResult* has been provided, the **[Back](function-navigate.md)** function is executed. | **true**<br><br>The display goes back to the screen that was previously shown. |
| **Switch( FirstName.Text, "Jim", Navigate(&nbsp;Screen1, ScreenTransition.None ), "Paul", Navigate( Screen2, ScreenTransition.None ), "John", Navigate( Screen3, ScreenTransition.None ) )** | Compares the value of **FirstName.Text** against "Jim", "Paul", and "John" in that order.  When a match is found with "John", the app will navigate to Screen3. | **true**<br><br>The display is changed to **Screen3**. |


### Step by step ###

1. On an empty screen, add a **[Text input](../controls/control-text-input.md)** control, and name it **Text1** if it doesn't have that name by default.

2. In **Text1**, type **15**.

3. Add a label, and set its **[Text](../controls/properties-core.md)** property to the following formulas:

| Formula | Description | Result |
|---------|-------------|--------|
| **Text1.Text** | With no condition, the return value is the value of the input-,text control. | "15" |
| **If( Value(Text1.Text) < 40, "Order more!", Text1.Text )** | The condition is **true**, and the corresponding value is returned. | "Order more!" |
| **If( Value(Text1.Text) < 20, "Order MANY more!", Value(Text1.Text) < 40, "Order more!", Text1.Text )** |  The first condition is **true**, and the corresponding value is returned. | "Order MANY more!" |
