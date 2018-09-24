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

The **IfError** function tests each of its arguments in order for an error value, stopping when the first non-error value is found.  The arguments after the non-error value is found are ignored and not evaluated.

Use **IfError** to replace error values with a valid value.  For example, if it is possible that user input may result in a division by zero, replace it with a 0 or other valid value that is appropriate for your app so that downstream calculations can proceed.

Use **IfError** in [behavior formulas](../working-with-formulas-in-depth.md) to perform actions, check the results for errors, and if needed take further actions or display an error message to the user with [**Notify**](function-showerror.md).

If all of the arguments to **IfError** result in an error, the value of the last argument is returned (which will be an error value). 

## Syntax
**IfError**( *Value*, *Fallback1* [, *Fallback2*, ... ] )

* *Value* - Required. Formula(s) to test for an error value. 
* *Fallback(s)* - Required. The formulas to evaluate and values to return if previous arguments returned an error.  *Fallback* arguments are evaluated in order up to the point a a non-error value is found.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **IfError( 1, 2 )** |The first argument is not an error.  It is returned and subsequent arguments are not evaluated.   | 1 |
| **IfError( 1/0, 2 )** | The first argument is returning an error value (due to division by zero).  The second argument is evaluated resulting in a non-error value which is returned. | 2 | 
| **IfError( 1/0, Notify( "There was an internal problem", NotificationType.Error ) )** | The first argument is returning an error value (due to division by zero).  The second argument is evaluated which displays a messages to the user.  The return value of **IfError** is the return value of **Notify**, coerced to the same type as the first argument to **IfError** (a number). | 1 |
| **IfError( 1/0, 1/0, 2, 1/0, 3 )** | The first argument is returning an error value (due to division by zero).  The second argument is evaluated, also resulting in an error value (another division by zero).  The third argument is evaluated, which does not return in an error value which is returned.  The fourth and fifth arguments are ignored.  | 2 |

### Step by step

1. Add a **[Text input](../controls/control-text-input.md)** control, and name it **TextInput1** if it doesn't have that name by default.

2. Add a **[Label](../controls/control-text-box.md)** control, and name it **Label1** if it doesn't have that name by default.

3. Set the formula for **Label1**'s **Text** property to:

	**IfError( Value( TextInput1.Text ), -1 )**

4. In **TextInput1**, type **1234**.  

	Label1 will show the value **1234** as this is a valid input to the Value function.

5. In **TextInput1**, type **ToInfinity**.

	Label1 will show the value **-1** as this is not a valid input to the Value function.  Without wrapping the Value function with IfError, the label would show no value as the error value is treated as a *blank*. 

