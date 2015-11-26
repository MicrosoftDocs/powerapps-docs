<properties
	pageTitle="PowerApps: Table function"
	description="Reference information for the Table function in PowerApps, including syntax and examples"
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

# Table function in PowerApps #

Creates a temporary [table](working-with-tables.md).

## Description ##

The **Table** function creates a table from an argument list of [records](working-with-tables.md#records).

The table's [columns](working-with-tables.md#columns) will be the union of all the properties from all the argument records.  Each record need not include a value for every column, in which case a *blank* value will be used.

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **Table** does not create a permanent table, instead it returns a temporary table made of its arguments.  This temporary table can be be passed to other functions, visualized in Gallery controls, or embedded in other tables.  See [working with tables](working-with-tables.md) for more details. 

You can also create a single-column table with the **[ value1, value2, ... ]** syntax.

## Syntax ##

**Table**( *Record1* [, *Record2*, ... ] )

- *Record(s)* - Required. The records to add to the table.

## Examples ##

1. Add a list box control, and then set its **Items** property to this function:

	**Table({Color:"red"}, {Color:"green"}, {Color:"blue"})**

1. Add a text gallery, and set its **Items** property to this function:

	**Table({Item:"Violin123", Location:"France", Owner:"Fabrikam"}, {Item:"Violin456", Location:"Chile"})**

1. (optional) Set the **Text** property of the **Heading1** label to **ThisItem!Item**, set the **Text** property of the **Subtitle1** label to **ThisItem!Owner**, and set the **Text** property of the **Body1** label to **ThisItem!Location**.



