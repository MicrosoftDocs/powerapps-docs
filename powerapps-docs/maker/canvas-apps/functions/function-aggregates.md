---
title: Average, Max, Min, StdevP, Sum, and VarP functions in Power Apps
description: Reference information including syntax and examples for the Average, Max, Min, StdevP, Sum, and VarP functions in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/15/2017
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# Average, Max, Min, StdevP, Sum, and VarP functions in Power Apps
Aggregate functions that summarize a set of numbers.

## Description
The **Average** function calculates the average, or arithmetic mean, of its arguments.

The **Max** function finds the maximum value.

The **Min** function finds the minimum value.

The **Sum** function calculates the sum of its arguments.

The **StdevP** function calculates the standard deviation of its arguments.

The **VarP** function calculates the variance of its arguments.

You can supply the values for these functions as:

* Separate arguments. For example, **Sum( 1, 2, 3 )** returns 6.
* A [table](../working-with-tables.md) and a formula to operate over that table.  The aggregate will be calculated on the values of the formula for each [record](../working-with-tables.md#records).  

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

These functions operate on numeric values only. Other types of values, such as strings or records, are ignored. Use the **[Value](function-value.md)** function to convert a string into a number.

The **Average**, **Max**, **Min**, and **Sum** functions can be delegated when used with a [data source that supports delegation for these functions](../delegation-overview.md).  However, **StdevP** and **VarP** can't be delegated for any data sources.  If delegation is not supported, only the first portion of the data will be retrieved and then the function applied locally.  The result may not represent the complete story.  A delegation warning will appear at authoring time to remind you of this limitation and to suggest switching to delegable alternatives where possible. For more information, see the [delegation overview](../delegation-overview.md).

## Syntax
**Average**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Max**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Min**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**Sum**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**StdevP**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )<br>**VarP**( *NumericalFormula1*, [ *NumericalFormula2*, ... ] )

* *NumericalFormula(s)* - Required.  Numeric values to operate on.

**Average**( *Table*, *NumericalFormula* )<br>**Max**( *Table*, *NumericalFormula* )<br>**Min**( *Table*, *NumericalFormula* )<br>**Sum**( *Table*, *NumericalFormula* )<br>**StdevP**( *Table*, *NumericalFormula* )<br>**VarP**( *Table*, *NumericalFormula* )

* *Table* - Required.  Table to operate on.
* *NumericalFormula* - Required. Formula to evaluate for each record. The result of this formula is used for the aggregation. You can use columns of the table in the formula.

## Examples
### Step by step
Let's say that you had a [data source](../working-with-data-sources.md) named **Sales** that contained a **CostPerUnit** column and a **UnitsSold** column, and you set the **[Text](../controls/properties-core.md)** property of a label to this function:<br>
**Sum(Sales, CostPerUnit * UnitsSold)**

The label would show total sales by multiplying the values in those columns for each record and then adding the results from all records together:<br>![Calculate total sales from units sold and cost per unit.](./media/function-aggregates/total-sales.png)

As a different example, let's say that you had sliders that were named **Slider1**, **Slider2**, and **Slider3** and a label with its **[Text](../controls/properties-core.md)** property set to this formula:<br>
**Sum(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the sum of all values to which the sliders were set.<br>
**Average(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the average of all values to which the sliders were set.<br>
**Max(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the maximum of all values to which the sliders were set.<br>
**Min(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the minimum of all values to which the sliders were set.<br>
**StdevP(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the standard deviation of all values to which the sliders were set.<br>
**VarP(Slider1.Value, Slider2.Value, Slider3.Value)**: The label would show the variance of all values to which the sliders were set.





[!INCLUDE[footer-include](../../../includes/footer-banner.md)]