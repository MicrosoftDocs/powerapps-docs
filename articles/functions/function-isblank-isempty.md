<properties
	pageTitle="PowerApps: IsBlank and IsEmpty functions"
	description="Reference information for the IsBlank and IsEmpty functions in PowerApps, including syntax and examples"
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
   ms.date="11/01/2015"
   ms.author="gregli"/>

# IsBlank and IsEmpty functions in PowerApps #

Tests if a value is blank or a [table](working-with-tables.md) contains no [records](working-with-tables.md#records).

## Overview ##

*Blank* is not the same thing as *empty*.  

Blank indicates "no value" or "unknown value."  For example, a Boolean can normally have one of two values: **true** or **false**.  But in addition, it can also be *blank*, and be neither **true** nor **false**.  This is similar to Excel, where a workbook cell starts out as blank but can hold **TRUE** or **FALSE**.

Empty indicates a table that has no records.  The table structure may be there, complete with [column](working-with-tables.md#columns) names.  But there is no data in the table.

## Description ##

**IsBlank** tests for a *blank* value.  Blank values are found in these situations:

- A control property has no value or formula set for it.
- The user of an app has not entered a value into an Input Text control or made a selection in a Listbox control.  You can use **IsBlank** to provide required field feedback. 
- An empty string with **Len** of 0.
- An error occurred in a function.  Often the arguments to the function were invalid.
- Connected [data sources](working-with-data-sources.md) such as SQL Server may use "null" values.  These values appear as *blank* in PowerApps.
- The *else* portion of an **If** function was not specified, and the condition was **false**.
- A column was not included when using the **[Update](function-update-updateif.md)** function, and no value was placed in that column as a result.

Most functions in PowerApps propagate *blank* values for the handling of errors.  Unless checked, error values flow through a formula, resulting in a *blank* value displayed to the user of the app.  

<!-- TODO: example of a function that propagates blank -->

**IsEmpty** tests if a table has any records in it.

The return value for both functions is a Boolean **true** or **false**.

## Syntax ##

**IsBlank**( *Value* )

- *Value* – Required. Value to test.

**IsEmpty**( *Table* )

- *Table* - Required. Table to test for records.

<!-- TODO: Examples -->

