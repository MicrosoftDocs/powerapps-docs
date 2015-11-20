<properties
	pageTitle="PowerApps: Count, CountA, CountIf, and CountRows functions"
	description="Reference information for the Count, CountA, CounfIf, and CountRows functions in PowerApps, including syntax and examples"
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

# Count, CountA, CountIf, and CountRows functions in PowerApps #

Counts the number of records in a table that satisfy a condition, or all records. 

## Description ##

The **Count** function counts the number of records in a single-column table that contain a number.

The **CountaA** function counts the number of records in a single-column table that are not *blank*.  This function includes error values and empty text ("") in the count.  TODO: not consistent.

The **CountIf** functions counts the number of records in a table that are **true** for a logical formula.  The formula can reference columns of the table.

The **CountRows** function counts the number records in a table.

All of these functions return a number.

## Syntax ##

**Count**( *SingleColumnTable* )
**CountA**( *SingleColumnTable* )

- *SingleColumnTable* - Required.  Column of records to count.  

**CountIf**( *Table*, *LogicalFormula* )

- *Table* - Required.  Table of records to count.
- *LogiaclFormula* - Required.  Formula to evaluate for each record of the table.  Records that reutrn **true** for this formula are counted.  The formula can reference columns of the table.

**CountRows**( *Table* )

- *Table* - Required.  Table of records to count.

## Examples ##

TODO: Examples.

TODO: Single column notation.

### Step by step ###

1. Import or create a collection named Inventory, as Create your first app describes.

2. Add a label, and set its Text property to this function:

	**CountIf(Inventory, UnitsInStock < 30)**

	The label shows 2 because two products (Ganymede and Callisto) have fewer than 30 units in stock.

2. Add another label, and set its Text property to this function:

	**CountA(Inventory!UnitsInStock)**

	The label shows 5, the number of non-empty cells in the UnitsInStock column.

2. Add another label, and set its Text property to this function:

	**CountRows(Inventory)**

	The label shows 5 because the collection contains five rows.




