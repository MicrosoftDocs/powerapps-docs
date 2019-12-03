---
title: IfError function | Microsoft Docs
description: Reference information, including syntax and examples, for the IfError function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/21/2018
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# IfError function in Power Apps

Detects errors and provides an alternative value or takes action.

## Description

> [!NOTE]
> This function is part of an experimental feature and is subject to change. The behavior that this topic describes is available only when the *Formula-level error management* feature is turned on. This app-level setting is off by default. To turn this feature on, open the *File* tab, select *App settings* in the left hand menu, and then select *Experimental features*. Your feedback is very valuable to us - please let us know what you think in the [Power Apps community forums](https://powerusers.microsoft.com/t5/Expressions-and-Formulas/bd-p/How-To).

The **IfError** function tests one or more values until it finds an error result . If the function finds an error, the function returns a corresponding value. Otherwise, the function returns a default value. In either case, the function might return a string to show, a formula to evaluate, or another form of result. The **IfError** function resembles the **If** function: **IfError** tests for errors, while **If** tests for **true**.

Use **IfError** to replace error values with valid values. For example, use this function if user input might result in a division by zero. Build a formula to replace the result with a 0 or another value that's appropriate for your app so that downstream calculations can proceed. Your formula can be as simple as this example:

```powerapps-dot
IfError( 1/x, 0 )
```

If the value of **x** isn't zero, the formula returns **1/x**. Otherwise, **1/x** produces an error, and the formula returns 0 instead.

Use **IfError** in [behavior formulas](../working-with-formulas-in-depth.md) to perform an action and check for an error before performing additional actions, as in this pattern:

```powerapps-dot
IfError(
    Patch( DS1, ... ), Notify( "problem in the first action" ),
    Patch( DS2, ... ), Notify( "problem in the second action" )
)
```

If the first patch encounters a problem, the first **Notify** runs, no further processing occurs, and the second patch doesn't run. If the first patch succeeds, the second patch runs and, if it encounters a problem, the second **Notify** runs.

If the formula doesn't find any errors and you've specified the optional *DefaultResult* argument, the formula returns the value that you specified for that argument. If the formula doesn't find any errors and you haven't specified that argument, the formula returns the last *Value* argument evaluated.

## Syntax

**IfError**( *Value1*, *Fallback1* [, *Value2*, *Fallback2*, ... [, *DefaultResult* ] ] )

* *Value(s)* - Required. Formula(s) to test for an error value.
* *Fallback(s)* - Required. The formulas to evaluate and values to return if matching *Value* arguments returned an error.
* *DefaultResult* - Optional.  The formulas to evaluate if the formula doesn't find any errors.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **IfError( 1, 2 )** |The first argument isn't an error. The function has no other errors to check and no default return value. The function returns the last *value* argument evaluated.   | 1 |
| **IfError( 1/0, 2 )** | The first argument returns an error value (due to division by zero). The function evaluates the second argument and returns it as the result. | 2 |
| **IfError( 1/0, Notify( "There was an internal problem", NotificationType.Error ) )** | The first argument returns an error value (due to division by zero). The function evaluates the second argument and displays a message to the user. The return value of **IfError** is the return value of **Notify**, coerced to the same type as the first argument to **IfError** (a number). | 1 |
| **IfError( 1, 2, 3, 4, 5 )** | The first argument isn't an error, so the function doesn't evaluate that argument's corresponding fallback. The third argument isn't an error either, so the function doesn't evaluate that argument's corresponding fallback. The fifth argument has no corresponding fallback and is the default result. The function returns that result because the formula contains no errors. | 5 |

### Step by step

1. Add a **[Text input](../controls/control-text-input.md)** control, and name it **TextInput1** if it doesn't have that name by default.

2. Add a **[Label](../controls/control-text-box.md)** control, and name it **Label1** if it doesn't have that name by default.

3. Set the formula for **Label1**'s **Text** property to:

	**IfError( Value( TextInput1.Text ), -1 )**

4. In **TextInput1**, type **1234**.  

	Label1 will show the value **1234** as this is a valid input to the Value function.

5. In **TextInput1**, type **ToInfinity**.

	Label1 will show the value **-1** as this is not a valid input to the Value function.  Without wrapping the Value function with IfError, the label would show no value as the error value is treated as a *blank*. 

