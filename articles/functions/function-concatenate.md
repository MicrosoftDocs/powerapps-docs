<properties
	pageTitle="PowerApps: Concat and Concatenate functions"
	description="Reference information for the Concat and Concatenate functions in PowerApps, including syntax and examples"
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

# Concat and Concatenate functions in PowerApps #

Concatenates individual strings and strings in tables.

## Description ##

The **Concat** function concatenates the result of a formula applied across all the records of a table, resulting in a single string.  You can use this function to summarize the strings of a table, just as **[Sum](function-aggregates.md)** does for numbers.

The **Concatenate** function concatenates a mix of individual strings and single-column table of strings.  Used with individual strings, this function is equivalent to using the **&** operator.  The single-column table may be created by a formula.

## Syntax ##

**Concat**( *Table*, *Formula* )

- *Table* - Required.  Table to operate on.
- *Formula* - Required.  Formula to apply across the records of the table.

**Concatenate**( *String1* [, *String2*, ...] )

- *String(s)* - Required.  Mix of individual strings or single-column table of strings.

## Examples ##

### Step by step ###

#### Concat ####

1. Add a button, and set its OnSelect property to this function:

	**Collect(Products, {String:"Violin", Wind:"Trombone", Percussion:"Bongos"}, {String:"Cello", Wind:"Trumpet", Percussion:"Tambourine"})**

2. Press F5, click the button, and then press Esc to return to the design workspace.

3. Add a label, and set its Text property to this function:

	**Concat(Products, String & " ")**

	The label shows Violin Cello.

#### Concatenate ####

If you created an input-text control named AuthorName, the following function would prepend "By" to text that the user typed in that control:

**Concatenate("By ", AuthorName!Text)**

If you had an Employees table that contained a FirstName column and a LastName column, the following function would concatenate the data in each row of those columns.

**Concatenate(Employees!FirstName, " ", Employees!LastName)**


