<properties
	pageTitle="PowerApps: If function"
	description="Reference information for the If function in PowerApps, including syntax and examples"
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
   ms.date="11/07/2015"
   ms.author="gregli"/>

# If function in PowerApps #

Returns one value if a condition is true, and another value if not. 

## Description ##

The **If** function tests conditions until a **true** result is found.  The corresponding value is then returned as the result.  You can use **If** to return different results based on comparisons and other tests.  

You can use **If** in behavior formulas to branch between two actions.  At most one branch will be executed.  Conditions are evaluated in order, and once a **true** result is found, no further conditions are checked.

If no conditions are satisfied and an odd number of arguments are provided, the value of the last argument is returned.  This is the case with the common **If( *condition*, *value*, *else* )**.  For an even number of arguments, *Blank* is returned.

## Syntax ##

**If**( *Condition*, *Result* [, *ElseResult* ] )<br>**If**( *Condition1*, *Result1* [, *Condition2*, *Result2*, ... [ , *ElseResult* ] ] )

- *Condition(s)* - Required.  Formulas to test for **true**.  These formulas commonly contain comparison operators such as **<**, **>**, and **=**, and test functions such as **IsBlank** and **IsEmpty**.
- *Result(s)* - Required.  The corresponding value to return for a condition that evaluates to **true**.
- *ElseResult* - Optional.  The value to return if no conditions are satisfied.  If not specified, *blank* is returned.

## Examples ##

### Values in formulas ###

| Formula | Description | Result |
|---------|-------------|--------|
| **If( true, "Result1" )** | The condition is **true** and the corresponding result is returned. | "Result1" |
| **If( false, "Result1" )** | The condition is **false** and there is no *ElseResult* provided.  | *blank* |
| **If( true, "Result1", "Result2" )** | The condition is **true** and the corresponding result is returned. | "Result1" |
| **If( false, "Result1", "Result2" )** | The condition is **false** and the *ElseResult* has been provided and is returned.   | "Result2" |
| **If( true, "Result1", true, "Result2" )** | The first condition is **true** and the corresponding result is returned. | "Result1" |
| **If( false, "Result1", true, "Result2" )** | The first condition is **false**, but the second condition is **true** and the corresponding result is returned. | "Result2" |
| **If( false, "Result1", false, "Result2" )** | Both the first and second conditions are **false** and there is no *ElseResult* provided.    | *blank* |
| **If( false, "Result1", false, "Result2", "Result3")** | Both the first and second conditions are **false** and the *ElseResult* has been provided and is returned. | "Result3" |

### Branching in behavior formulas ###

| Formula | Description | Result |
|---------|-------------|--------|
| **If( true, Navigate( Screen1, ScreenTranstion!None ) )** | The condition is **true** and the **Navigate** function is executed. **Navigate** returns **true**. | **true**<br><br>The display is changed to **Screen1**. |
| **If( false, Navigate( Screen1 ) )** | The condition is **false** and no *ElseResult* was provided. | *blank*<br><br>No action is taken. |
| **If( false, Navigate( Screen1, ScreenTransition!None ), Back() )** | The condition is **false** and **Back** has been provided for the *ElseResult* | **true**<br><br>The display is changed to the previous screen. |

### Step by step ###

1. Place an input text box **Text1** on a new screen.  Its default name is **Text1**.
  
2. Type the number 15 into the input text box.
 
3. Place a label control on the screen.  Place the following formulas in its **Text** property:

| Formula | Description | Result |
|---------|-------------|--------|
| **Text1!Text** | With no condition, the return value is the value of the input text control. | "15" |
| **If( Value(Text1!Text) < 40, "Order more!", Text1!Text )** | The condition is **true** and the corresponding value is returned. | "Order more!" |
| **If( Value(Text1!Text) < 20, "Order MANY more!", Value(Text1!Text) < 40, "Order more!", Text1!Text )** |  The first condition is **true** and the corresponding value is returned. | "Order MANY more!" |


