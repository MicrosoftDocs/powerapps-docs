<properties
	pageTitle="PowerApps: And, Or, and Not functions"
	description="Reference information for the And, Or, and Not functions in PowerApps, including syntax and examples"
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

# And, Or, and Not functions in PowerApps #

Boolean logic functions, commonly used to manipulate the results of comparisons and tests.

## Description ##

The **And** functions returns **true** if all of its arguments are **true**.  The **&&** operator is equivalent to using **And**.

The **Or** function returns true if any of its arguments are **true**.  The **||** operator is equivalent to **Or**.

The **Not** function returns **true** if its argument is **false**; it returns **false** if its argument is **true**.  The **!** operator is equivalent to **Not**.

These functions work with logical values.  They cannot be passed a number or string directly, instead a comparison or test must be made.  For example, comparisons such as **x > 1** is a logical value that evaluates to the Boolean value **true** if x is greater than 1, and **false** otherwise.  

## Syntax ##

**And**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Or**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Not**( *LogicalFormula* )

- *LogicalFormula(s)* - Required.  Logical formulas to evaluate and operate on.

## Examples ##

<!-- TODO: Examples. -->

### Step by step ###

You can use this function to determine whether a slider's value falls outside the 50 to 100 range:

**Or(Slider1!Value < 50, Slider1!Value> 100)**

If a table contained a Dept column and a Salary column, you could use this function in a Result column to show true in all rows in which the value in the Dept column was HR or the value in the Salary column was larger than 200000:

**Or(Dept = HR, Salary >= 200000)**

As an alternative, you can use the || operator to get the same results as what the previous functions return:

**Slider1!Value < 50 || Slider1!Value> 100**

**Dept = "HR" || Salary > 200000**
