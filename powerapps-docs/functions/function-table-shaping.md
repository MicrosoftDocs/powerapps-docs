---
title: AddColumns, DropColumns, RenameColumns, and ShowColumns functions | Microsoft Docs
description: Reference information, including syntax and examples, for the AddColumns, DropColumns, RenameColumns, and ShowColumns functions in PowerApps
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 11/07/2015
ms.author: gregli

---
# AddColumns, DropColumns, RenameColumns, and ShowColumns functions in PowerApps
Shapes a [table](../working-with-tables.md) by adding, dropping, renaming, and selecting its [columns](../working-with-tables.md#columns).

## Overview
These functions shape a table by adjusting its columns:

* Reduce a table that contains multiple columns down to a single column for use with single-column functions, such as **[Lower](function-lower-upper-proper.md)** or **[Abs](function-numericals.md)**.  
* Add a calculated column to a table (for example, a **Total Price** column that shows the results of multiplying **Quantity** by **Unit Price**).
* Rename a column to something more meaningful, for display to users or for use in formulas.

A table is a value in PowerApps, just like a string or a number.  You can specify a table as an argument in a formula, and functions can return a table as a result. The functions that this topic describes don't modify a table. Instead they take a table as an argument and return a new table with a transform applied.  See [working with tables](../working-with-tables.md) for more details.  

You can't modify the columns of a [data source](../working-with-data-sources.md) by using these functions. You must modify the data at its source. You can add columns to a [collection](../working-with-data-sources.md#collections) with the **[Collect](function-clear-collect-clearcollect.md)** function.  See [working with data sources](../working-with-data-sources.md) for more details.  

## Description
The **AddColumns** function adds a column to a table, and a formula defines the values in that column. Existing columns remain unmodified.

The formula is evaluated for each record of the table.
[!INCLUDE [record-scope](../includes/record-scope.md)]

The **DropColumns** function excludes columns from a table.  All other columns remain unmodified. **DropColumns** excludes columns, and **ShowColumns** includes columns.

The **RenameColumns** function renames columns of a table. All other columns retain their original names.

The **ShowColumns** function includes columns of a table and drops all other columns. You can use **ShowColumns** to create a single-column table from a multi-column table.  **ShowColumns** includes columns, and **DropColumns** excludes columns.  

For all these functions, the result is a new table with the transform applied.  The original table isn't modified.

[!INCLUDE [delegation-no](../includes/delegation-no.md)]

## Syntax
**AddColumns**( *Table*, *ColumnName1*, *Formula1* [, *ColumnName2*, *Formula2*, ... ] )

* *Table* - Required.  Table to operate on.
* *ColumnName(s)* - Required. Name(s) of the column(s) to add.  You must specify a string (for example, **"Name"** with double quotes included) for this argument.
* *Formula(s)* - Required.  Formula(s) to evaluate for each record. The result is added as the value of the corresponding new column. You can reference other columns of the table in this formula.

**DropColumns**( *Table*, *ColumnName1* [, *ColumnName2*, ... ] )

* *Table* - Required.  Table to operate on.
* *ColumnName(s)* - Required. Name(s) of the column(s) to drop. You must specify a string (for example, **"Name"** with double quotes included) for this argument.

**RenameColumns**( *Table*, *OldColumneName*, *NewColumnName* )

* *Table* - Required.  Table to operate on.
* *OldColumnName* - Required. Name of the column to rename. This name must be a string (for example **"Name"** with double quotes included).
* *NewColumnName* - Required. Replacement name. You must specify a string (for example, **"Customer Name"** with double quotes included) for this argument.

**ShowColumns**( *Table*, *ColumnName1* [, *ColumnName2*, ... ] )

* *Table* - Required.  Table to operate on.
* *ColumnName(s)* - Required. Name(s) of the column(s) to include. You must specify a string (for example, **"Name"** with double quotes included) for this argument.

## Examples
The examples in this section use the **IceCreamSales** data source, which contains the data in this table:

![](media/function-table-shaping/icecream.png)

None of these examples modify the **IceCreamSales** data source. Each function transforms the value of the data source as a table and returns that value as the result.

| Formula | Description | Result |
| --- | --- | --- |
| **AddColumns( IceCreamSales, "Revenue", UnitPrice * QuantitySold )** |Adds a **Revenue** column to the result.  For each record, **UnitPrice * QuantitySold** is evaluated, and the result is placed in the new column. |<style> img { max-width: none; } </style> ![](media/function-table-shaping/icecream-add-revenue.png) |
| **DropColumns( IceCreamSales, "UnitPrice" )** |Excludes the **UnitPrice** column from the result. Use this function to exclude columns, and use **ShowColumns** to include them. |![](media/function-table-shaping/icecream-drop-price.png) |
| **ShowColumns( IceCreamSales, "Flavor" )** |Includes only the **Flavor** column in the result. Use this function include columns, and use **DropColumns** to exclude them. |![](media/function-table-shaping/icecream-select-flavor.png) |
| **RenameColumns( IceCreamSales, "UnitPrice", "Price")** |Renames the **UnitPrice** colum in the result. |![](media/function-table-shaping/icecream-rename-price.png) |
| **DropColumns(<br>RenameColumns(<br>AddColumns( IceCreamSales, "Revenue",<br>UnitPrice * QuantitySold ),<br>"UnitPrice", "Price" ),<br>"Quantity" )** |Performs the following table transforms in order, starting from the inside of the formula: <ol><li>Adds a **Revenue** column based on the per-record calculation of **UnitPrice * Quantity**.<li>Renames **UnitPrice** to **Price**.<li>Excludes the **Quantity** column.</ol>  Note that order is important. For example, we can't calculate with **UnitPrice** after it has been renamed. |![](media/function-table-shaping/icecream-all-transforms.png) |

### Step by step
1. Import or create a collection named **Inventory** as the first subprocedure in [Show text and images in a gallery](../maker/show-images-text-gallery-sort-filter.md) describes.
2. Add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:
   
    **ClearCollect(Inventory2, RenameColumns(Inventory, "ProductName", "JacketID"))**
3. Press F5, select the button that you just created, and then press Esc to return to the design workspace.
4. On the **File** menu, select **Collections**.
5. Confirm that you've created a collection, named **Inventory2**. The new collection contains the same information as **Inventory** except that the column named **ProductName** in **Inventory** is named **JacketID** in **Inventory2**.

