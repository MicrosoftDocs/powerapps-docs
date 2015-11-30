<properties
	pageTitle="PowerApps: Average, Max, Min, StdevP, Sum, and VarP functions"
	description="Reference information for the Average, Max, Min, StdevP, Sum, and VarP functions in PowerApps, including syntax and examples"
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

# Average, Max, Min, StdevP, Sum, and VarP functions in PowerApps #

Aggregate functions that summarize a set of numbers.

## Description ##

The **Average** function calculates the average, or arithmetic mean, of all values.

The **Max** function finds the maximum value.

The **Min** function finds the minimum value.

The **Sum** function adds all values together and returns the sum.

The **StdevP** function calculates the standard deviation of its arguments.

The **VarP** function calculates the variance of its arguments.

These functions can be used in two different ways:

- You can supply the values as separate arguments.  For example, **Sum( 1, 2, 3 )** returns 6.
- You can supply a [table](working-with-tables.md) and a formula to operate over that table.  The aggregate will be calculated on the values of the formula for each [record](working-with-tables.md#records).  The formula can reference [columns](working-with-tables.md#columns) in the table.  

These functions only operate on numeric values.  Other types of values, such as strings or records, are ignored.  Use the **[Value](function-value.md)** function to convert a string into a number.   

## Syntax ##

**Average**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Max**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Min**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Sum**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**StdevP**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**VarP**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )

- *NumericalFormula(s)* - Required.  Numeric values to operate on.

**Average**( *Table*, *NumericalFormula* )<br>**Max**( *Table*, *NumericalFormula* )<br>**Min**( *Table*, *NumericalFormula* )<br>**Sum**( *Table*, *NumericalFormula* )<br>**StdevP**( *Table*, *NumericalFormula* )<br>**VarP**( *Table*, *NumericalFormula* )

- *Table* - Required.  Table to operate on.
- *NumericalFormula* - Required. Formula to evaluate for each record. The result of this formula is used for the aggregation. Columns of the table may be used in the formula.  

## Examples ##

### Step by step ###

If you had a [data source](working-with-data-sources.md) named **Sales** that contained a **CostPerUnit** column and a **UnitsSold** column, this function would calculate total sales by adding together the result of multiplying these two values:

**Sum(Sales, CostPerUnit * UnitsSold)**

To calculate the sum of the values set for sliders 1, 2, and 3:

**Sum(Slider1!Value, Slider2!Value, Slider3!Value)**
