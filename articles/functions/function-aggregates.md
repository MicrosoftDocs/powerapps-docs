<properties
	pageTitle="PowerApps: Average, Max, Min, and Sum functions"
	description="Reference information for the Average, Max, Min, and Sum functions in PowerApps, including syntax and examples"
	services="powerapps"
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

# Average, Max, Min, and Sum functions in PowerApps #

Aggregate functions that summarize a set of numbers. 

## Description ##

The **Average** function calculates the average, or arithmetic mean, of all values.

The **Max** function finds the maximum value.

The **Min** function finds the minimum value.

The **Sum** function adds all values together and returns the sum.

These functions can be used in two different ways:

- You can supply the values as separate arguments.  For example, **Sum( 1, 2, 3 )** returns 6. 
- You can supply a table and a formula to operate over that table.  The aggregate will be calculated on the values of the formula for each record.  The formula can reference columns in the table.  

These functions only operate on numeric values.  Other types of values, such as strings or records, are ignored.  Use the **Value** function to convert a string into a number.   
 
## Syntax ##

**Average**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )
**Max**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )
**Min**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )
**Sum**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )

- *NumericalFormula(s)* - Required.  Numeric values to operate on.

**Average**( *Table*, *NumericalFormula* )
**Max**( *Table*, *NumericalFormula* )
**Min**( *Table*, *NumericalFormula* )
**Sum**( *Table*, *NumericalFormula* )

- *Table* - Required.  Table to operate on.
- *NumericalFormula* - Required. Formula to evaluate for each record. The result of this formula is used for the aggregation. Columns of the table may be used in the formula.  

## Examples ##

TODO: Examples.

### Step by step ###

If you had a data source named **Sales** that contained a **CostPerUnit** column and a **UnitsSold** column, this function would calculate total sales by adding together the result of multiplying these two values:

**Sum(Sales, CostPerUnit * UnitsSold)**

To calculate the sum of the values set for sliders 1, 2, and 3:

**Sum(Slider1!Value, Slider2!Value, Slider3!Value)**
