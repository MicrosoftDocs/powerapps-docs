---
title: And, Or, and Not functions | Microsoft Docs
description: Reference information, including syntax and examples, for the And, Or, and Not functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# And, Or, and Not functions in PowerApps
Boolean logic functions, commonly used to manipulate the results of comparisons and tests.

## Description
The **And** function returns **true** if all of its arguments are **true**.  The **&&** [operator](operators.md) is equivalent to **And**.

The **Or** function returns **true** if any of its arguments are **true**.  The **||** operator is equivalent to **Or**.

The **Not** function returns **true** if its argument is **false**; it returns **false** if its argument is **true**.  The **!** operator is equivalent to **Not**.

These functions work with logical values. They can't be passed a number or a string directly; instead a comparison or test must be made. For example, a comparison such as **x > 1** is a logical formula that evaluates to the Boolean value **true** if **x** is greater than **1**. If **x** is less than **1**, the formula evaluates to **false.**

## Syntax
**And**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Or**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Not**( *LogicalFormula* )

* *LogicalFormula(s)* - Required.  Logical formulas to evaluate and operate on.

## Examples
### Step by step
Use this function to determine whether a slider's value falls outside the 50 to 100 range:

**Or(Slider1.Value < 50, Slider1.Value> 100)**

If a [table](../working-with-tables.md) contained a **Dept** [column](../working-with-tables.md#columns) and a **Salary** column, you could use this function in a **Result** column to show **true** in all rows in which the value in the **Dept** column was **HR** or the value in the **Salary** column was larger than **200000**:

**Or(Dept = HR, Salary >= 200000)**

As an alternative, use the || operator to get the same results as what the previous formulas return:

**Slider1.Value < 50 || Slider1.Value> 100**

**Dept = "HR" || Salary > 200000**

