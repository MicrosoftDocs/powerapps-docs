<properties
	pageTitle="PowerApps: Filter and LookUp functions"
	description="Reference information for the Filter and LookUp function in PowerApps, including syntax and examples"
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
   ms.date="10/21/2015"
   ms.author="gregli"/>

# Filter and LookUp functions in PowerApps #

Finds one or more records in a table.

## Description ##

The **Filter** function finds records in a table based on a formula.

The **LookUp** function finds the first record in a table that satisfies a formula.

The formula is evaluated for each record of the table.  Records that result in *true* are included in the result.  Columns of the table can be used in the formula.  

**Filter** returns all records found, as a table.  **LookUp** returns only the first record found.  Optionally, **LookUp** can evaluate an additional formula to further reduce the record to a single value.  

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **Filter** and **LookUp** do not modify a table, instead they take a table as an argument and return a table, record, or single value from it.  See [working with tables](working-with-tables.md) for more details.

## Syntax ##

**Filter**( *Table*, *Formula1* [, *Formula2*, ... ] )

- *Table* - Required. Table to search.
- *Formula(s)* - Required. This formula is evaluated for each record of the table, and those that result in **true** are included in the result of **Filter**.  You can reference columns within the table.  If more than one formula is supplied, the results of all formulas are combined with the **And** function.

**LookUp**( *Table*, *Formula* [, *ReductionFormula* ] )

- *Table* - Required. Table to search.
- *Formula* - Required. This formula is evaluated for each record of the table, and the first record that results in **true** is returned by **LookUp**.  You can reference columns within the table.  
- *ReductionFormula* - Optional. This formula is evaluated with the record that was found, reducing the result from **LookUp** to a single value.  You can reference columns within the table.  

## Examples ##

<!-- TODO: Examples. -->

### Step by step ###

If you had an Employees table that contained a Salary column, this function would identify the employees whose salaries were greater than 100,000:

**Filter(Employees, Salary > 100000)**

If you had an Employees table that contained a FirstName column and a LastName column, this function would return the salary for the employee named "John Smith":

**LookUp(Employees, FirstName = "John" && LastName = "Smith", Salary)**



