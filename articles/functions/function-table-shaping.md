<properties
	pageTitle="PowerApps: AddColumns, DropColumns, RenameColumns, and ShowColumns functions"
	description="Reference information for the AddColumns, DropColumns, RenameColumns, and ShowColumns functions in PowerApps, including syntax and examples"
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

# AddColumns, DropColumns, RenameColumns, and ShowColumns functions in PowerApps #

Shapes a [table](working-with-tables.md) by adding, dropping, renaming, and selecting [columns](working-with-tables.md#columns) of a table.

## Overview ##

These functions shape a table by making adjustments to the columns.  You use this to reduce a table down to one column, for passing to single-column functions such as **[Lower](function-lower-upper-proper.md)** or **[Abs](function-numericals.md)**.  Or you might use this to add a calculated column to a table.

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  The functions described here do not modify a table, instead they take a table as an argument and return a new table with a transform applied.  See [working with tables](working-with-tables.md) for more details.  

The columns of a [data source](working-with-data-sources.md) cannot be modified with these functions.  The columns of a [collection](working-with-data-sources.md#collections) can be modified with the **[Collect](function-clear-collect-clearcollect.md)** function.  The columns of other data sources must be modified at their source. See [working with data sources](working-with-data-sources.md) for more details.  

## Description ##

The **AddColumns** functions adds a column to a table, with values given by a formula.  Existing columns remain unmodified.  The formula is evaluated for each [record](working-with-tables.md#records) of the table and can reference other columns in the table.

The **DropColumns** function removes columns from a table.  All other columns remain unmodified.

The **RenameColumns** function renames columns of a table.  All other columns retain their original names.

The **ShowColumns** function selects columns to include in a table.  All other columns are dropped.

The result is a new table with the transform applied.

## Syntax ##

**AddColumns**( *Table*, *ColumnName1*, *Formula1* [, *ColumnName2*, *Formula2*, ... ] )
- *Table* - Required.  Table to operate on.
- *ColumnName(s)* - Required. Names of the column to add.  This name must be a string, for example **"Name"** with double quotes included.
- *Formula(s)* - Required.  Formulas to evaluate for each record, the result is added as the value of the corresponding new column.  Other columns in the table can be referenced in this formula.

**DropColumns**( *Table*, *ColumnName1* [, *ColumnName2*, ... ] )
- *Table* - Required.  Table to operate on.
- *ColumnName(s)* - Required. Names of the columns to drop. This name must be a string, for example **"Name"** with double quotes included.

**RenameColumns**( *Table*, *OldColumneName*, *NewColumnName* )
- *Table* - Required.  Table to operate on.
- *OldColumnName* - Required. Names of the column to rename. This name must be a string, for example **"Name"** with double quotes included.
- *NewColumnName* - Required. Replacement name. This name must be a string, for example **"Customer Name"** with double quotes included.

**ShowColumns**( *Table*, *ColumnName1* [, *ColumnName2*, ... ] )
- *Table* - Required.  Table to operate on.
- *ColumnName(s)* - Required. Names of the columns to include. This name must be a string, for example **"Name"** with double quotes included.

## Examples ##

### Step by step ###

1. Import or create a collection named Inventory as Create your first app describes.

2. Add an image gallery with text, name it TableHolder, and set its Items property to this function:

	**RenameColumns(Inventory, "ProductName", "JacketID")**
	
3. Add a button, and set its OnSelect property to this function:

	**Collect(Inventory2, TableHolder!AllItems)**

4. Press F5, click the button you just created, and then press Esc to return to the design workspace.

5. Press Alt-D, and then click Collections in the left navigation bar.

6. Confirm that you've duplicated the Inventory collection, except that the new collection, named Inventory2, contains the same information in a column named JacketID as the original collection did in a column named ProductName.


