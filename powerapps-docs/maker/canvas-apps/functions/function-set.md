---
title: Set function in Power Apps
description: Reference information including syntax and examples for the Set function in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/29/2017
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - tapanm-msft
---
# Set function in Power Apps
Sets the value of a global variable.

## Overview
Use the **Set** function to set the value of a global variable, which temporarily holds a piece of information, such as the number of times the user has selected a button or the result of a data operation.  

Global variables are available throughout your app on all screens. These are the simplest kind of variables and fill the needs of most situations. There are also context variables which are scoped to a single screen and collections that allow row level modifications to tables. For more information about these other options, review [Understand variables](../working-with-variables.md).

Power Apps are based on formulas that automatically recalculate as the user interacts with an app. Any formulas that depend on a variable will automatically update when it changes. However, the variable won't be automatically updated if the value of the formula used in the **Set** function changes. This requires the app maker to manually update the variable, which can be error prone and harder for others to understand. Before you use a variable, review [Understand variables](../working-with-variables.md).

## Description
Global variables are implicitly created by using the **Set** function. No explicit declaration is required. If you remove all the **Set** functions for a global variable, that global variable will cease to exist. To clear a variable, set its value to the result of the [**Blank** function](function-isblank-isempty.md).

You can see your variables' values, definitions, and uses with the Variables view under the **File** menu in Power Apps Studio.

As the examples later in this topic show, global variables can hold several kinds of information, including these:

* a single value
* a record
* a table
* an object reference
* any result from a formula

A global variable holds its value until the app is closed.  Once closed, the global variable's value will be lost and must be recreated when the app is loaded again.

Global variables cannot use the same name as an existing collection or control.  It can use the same name as a context variable.  To disambiguate between the two, use the [disambiguation operator](operators.md#disambiguation-operator).

**Set** has no return value, and you can use it only within a [behavior formula](../working-with-formulas-in-depth.md).

## Syntax
**Set**( *VariableName*, *Value* )

* *VariableName* - Required.  The name of a global variable to create or update.
* *Value* - Required.  The value to assign to the context variable.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Set(&nbsp;Counter,&nbsp;1&nbsp;)** |Creates or modifies the global variable **Counter**, setting its value to **1**. |**Counter** has the value **1**. You can reference that variable by using the name **Counter** in a formula on any screen. |
| **Set(&nbsp;Counter,&nbsp;2&nbsp;)** |Sets the value of the **Counter** global variable from the previous example to **2**. |**Counter** has the value **2**. |
| **Set(&nbsp;Counter,&nbsp;Counter + 1&nbsp;)** |Increments the value of the **Counter** global variable from the previous example to **3**. |**Counter** has the value **3**. |
| **Set(&nbsp;Name,&nbsp;"Lily" )** |Creates or modifies the global variable **Name** setting its value to **Lily**. |**Name** has the value **Lily**. |
| **Set(&nbsp;Person,&nbsp;{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;} )** |Creates or modifies the global variable **Person**, setting its value to a record. The record contains two columns, named **Name** and **Address**. The value of the **Name** column is **Milton**, and the value of the **Address** column is **1 Main St**. |**Person** has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;}**.<br><br>Reference this record as a whole with the name **Person**, or reference an individual column of this record with **Person.Name** or **Person.Address**. |
| **Set(&nbsp;Person, Patch(&nbsp;Person,&nbsp;{Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}&nbsp;)&nbsp;)** |Works with the **[Patch](function-patch.md)** function to update the **Person** global variable by setting the value of the **Address** column to **2 Main St**. |**Person** now has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}**. |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]