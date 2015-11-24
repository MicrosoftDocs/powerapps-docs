<properties
	pageTitle="PowerApps: Sort function"
	description="Reference information for the Sort function in PowerApps, including syntax and examples"
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

# Sort function in PowerApps #

Sorts a table.

## Description ##

The **Sort** function sorts a table based on a formula.  

The formula is evaluated for each record of the table, and the results are used to sort the table.  Columns of the table can be used in the formula.  The formula must result in a number, string, or boolean value; it cannot result in a table or record.

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **Sort** does not modify a table, instead it takes a table as an argument and return a new table that has been sorted.  See [working with tables](working-with-tables.md) for more details.

## Syntax ##

**Sort**( *Table*, *Formula* [, *SortOrder* ] )

- *Table* - Required. Table to sort.
- *Formula* - Required. This formula is evaluated for each record of the table, and the results are used to sort the table.  You can reference columns within the table.
- *SortOrder* - Optional.  **SortOrder!Ascending** or **SortOrder!Descending**.  **SortOrder!Ascending** is the default.

## Examples ##

<!-- TODO: Examples. -->

### Step by step ###

If you had an Employees table that contained a Salary column, this function would list the employees with higher salaries above those with lower ones:

**Sort(Employees, Salary, SortOrder!Descending)**