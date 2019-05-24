---
title: IfError function | Microsoft Docs
description: Reference information, including syntax and examples, for the IfError function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 03/21/2018
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# IfError function in PowerApps
Detects errors and provides an alternative value or takes action.

## Description
> [!NOTE]
> This function is part of an experimental feature and is subject to change.  The behavior described here is only available when the *Formula-level error management* feature is turned on.  This is an app level setting that defaults to off.  To turn this feature on, navigate to the *File* tab, *App settings* in the left hand menu, and then *Experimental features*.  Your feedback is very valuable to us - please let us know what you think in the [PowerApps community forums](https://powerusers.microsoft.com/t5/Expressions-and-Formulas/bd-p/How-To).

The **IfError** function tests one or more values until an error result is found. If an error is found, a corresponding value is returned. If no error is found, a default value is returned.  In either case, the returned value might be a string to show, a formula to evaluate, or another form of result.  The **IfError** function is very similar to the **If** function: **IfError** tests for errors, while **If** tests for **true**.

Use **IfError** to replace error values with a valid value.  For example, if it is possible that user input may result in a division by zero, replace it with a 0 or other valid value that is appropriate for your app so that downstream calculations can proceed.  For example, a simple pattern is:

```powerapps-dot
IfError( 1/x, 0 )
```

If the value of **x** is non-zero, the formula will return **1/x**.  However, if **x** is zero, **1/x** will result in an error, and **IfError** will return 0 instead. 

Use **IfError** in [behavior formulas](../working-with-formulas-in-depth.md) to perform an action and check for an error before continuing to perform additional actions.  For example in this pattern:

```powerapps-dot
IfError( 
    Patch( DS1, ... ), Notify( "problem in the first action" ), 
    Patch( DS2, ... ), Notify( "problem in the second action" )
)
```

If there is a problem with the **Patch( DS1, ... )** then the first **Notify** will execute and no further processing will occur and **Patch( DS2, ... )** will not happen.  But if **Patch( DS1, ... )** succeeds then the second patch will happen, and the second **Notify** executed if there is a problem with it.

If no errors are found, the value of the optional *DefaultResult* is returned.  If that argument is not provided, the value of the last *Value* argument evaluated is returned.

## Syntax
**IfError**( *Value1*, *Fallback1* [, *Value2*, *Fallback2*, ... [, *DefaultResult* ] ] )

* *Value(s)* - Required. Formula(s) to test for an error value. 
* *Fallback(s)* - Required. The formulas to evaluate and values to return if matching *Value* arguments returned an error.  
* *DefaultResult* - Optional.  The formulas to evaluate if no errors were found.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **IfError( 1, 2 )** |The first argument is not an error.  There are no other errors to check and no default return value was provided.  The formula returns the last *value* argument evaluated.   | 1 |
| **IfError( 1/0, 2 )** | The first argument is returning an error value (due to division by zero).  The second argument is evaluated and returned as the result. | 2 | 
| **IfError( 1/0, Notify( "There was an internal problem", NotificationType.Error ) )** | The first argument is returning an error value (due to division by zero).  The second argument is evaluated which displays a messages to the user.  The return value of **IfError** is the return value of **Notify**, coerced to the same type as the first argument to **IfError** (a number). | 1 |
| **IfError( 1, 2, 3, 4, 5 )** | The first argument is not returning an error, so its corresponding fallback is not evaluated.  The third argument is not return an error either, so its corresponding fallback is not evaluated.  The fifth argument has no corresponding fallback and is the default result which is returned since no errors were found. | 5 |

### Step by step

1. Add a **[Text input](../controls/control-text-input.md)** control, and name it **TextInput1** if it doesn't have that name by default.

2. Add a **[Label](../controls/control-text-box.md)** control, and name it **Label1** if it doesn't have that name by default.

3. Set the formula for **Label1**'s **Text** property to:

	**IfError( Value( TextInput1.Text ), -1 )**

4. In **TextInput1**, type **1234**.  

	Label1 will show the value **1234** as this is a valid input to the Value function.

5. In **TextInput1**, type **ToInfinity**.

	Label1 will show the value **-1** as this is not a valid input to the Value function.  Without wrapping the Value function with IfError, the label would show no value as the error value is treated as a *blank*. 

