<properties
	pageTitle="Distinct function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Distinct function in PowerApps"
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

# Distinct function in PowerApps #

Summarizes [records](working-with-tables.md#records) of a [table](working-with-tables.md), removing duplicates.

## Description ##

The **Distinct** function evaluates a formula across each record of a table. [Columns](working-with-tables.md#columns) of the table can be used in the formula.  **Distinct** returns a one-column table that contains the results, with duplicate values removed.  

## Syntax ##

**Distinct**( *Table*, *Formula* )

- *Table* - Required.  Table to evaluate across.
- *Formula* - Required.  Formula to evaluate for each record.

## Example ##

If you had an **Employees** table that contained a **Department** column, this function would list each unique department name in that column, no matter how many times each name appeared in that column:

**Distinct(Employees, Department)**
