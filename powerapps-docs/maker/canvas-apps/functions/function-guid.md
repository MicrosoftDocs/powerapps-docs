---
title: GUID function | Microsoft Docs
description: Reference information, including syntax, for the GUID function in PowerApps
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 06/09/2018
ms.author: gregli

---
# GUID function in PowerApps
Converts a GUID (Globally Unique Identifier) string to a GUID or creates a new GUID.

## Description
Use the **GUID** function to convert a string containing the hexadecimal representation of a GUID into a GUID value.  GUID values are used as keys in some database systems.  

The string passed must be 32 hexadecimal digits in the standard form "123e4567-e89b-12d3-a456-426655440000" or without dashes "123e4567e89b12d3a456426655440000".

The **GUID** function can also create a new GUID if no argument is supplied.

To convert a GUID value to a string use it in a string context and it will automatically be converted to a hexadecimal representation. 

## Volatile Functions
**GUID** is a volatile function when used without an argument.  Each time the function is evaluated it returns a different value.  

When used in a data flow formula, a volatile function will only return a different value if the formula in which it appears is reevaluated.  If nothing else changes in the formula then it will have the same value throughout the execution of your app.

For example, a label control with **Label1.Text = GUID()** will not change while your app is active.  Only closing and reopening the app will result in a new value.

The function will be reevaluated if it is part of a formula in which something else has changed.  For example, if we change our example to involve a text input control with **Label1.Text = TextInput1.Text & " " & GUID()** then a new GUID is generated each time the text input's value changes and the label's text property is reevaluated.  

When used in a [behavior formula](../working-with-formulas-in-depth.md), **GUID** will be evaluated each time the behavior formula is evaluated.  See below for an example.

## Syntax
**GUID**( [ *GUIDString* ] )

* *GUIDString* – Optional.  A text string containing the hexadecimal representation of a GUID. A new GUID is created if no string is supplied.

## Examples

#### 

#### Create a table of new GUIDs

1. Place a **[Button](../controls/control-button.md)** control on the canvas.  Set its **[OnSelect](../controls/properties-core.md)** property to **ClearCollect( NewGUIDs, ForAll( [ 1, 2, 3, 4, 5 ], GUID() )**.  The single column table [1, 2, 3, 4, 5] is only used to iterate 5 times, resulting in 5 random numbers.
2. Place a **[Data table](../controls/control-data-table.md)** control on the canvas.  Select the **NewGUIDs** collection as the data source for the data table and select the **Value** field to display.
3. Press the button.  You will see a list of random numbers in the data table:
    ![A screen showing a data table with five different decimal values 0.857, 0.105, 0.979, 0.167, 0.814](media/function-rand/rand-collection-1.png)
4. Press the button again.  You will see a different list of random numbers:
    ![The same screen showing a data table with a new set of five different decimal values 0.414, 0.128, 0.860, 0.303, 0.568](media/function-rand/rand-collection-2.png)
5. In this example, a table of random values was created.  To create a single random number, use **Set( RandomNumber, Rand() )**.


