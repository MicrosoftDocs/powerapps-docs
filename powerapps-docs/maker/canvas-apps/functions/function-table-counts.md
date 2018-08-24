---
title: Count, CountA, CountIf, and CountRows functions | Microsoft Docs
description: Reference information, including syntax and an example, for the Count, CountA, CounfIf, and CountRows functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Count, CountA, CountIf, and CountRows functions in PowerApps
Counts all [records](../working-with-tables.md#records) in a [table](../working-with-tables.md), or counts all records that satisfy a condition.

## Description
The **Count** function counts the number of records that contain a number in a single-column table.

The **CountA** function counts the number of records that aren't *blank* in a single-column table. This function includes [empty](function-isblank-isempty.md) text ("") in the count.

The **CountIf** function counts the number of records in a table that are **true** for a logical formula.  The formula can reference [columns](../working-with-tables.md#columns) of the table.

The **CountRows** function counts the number records in a table.

Each of these functions returns a number.

[!INCLUDE [delegation-no](../../../includes/delegation-no.md)]

## Syntax
**Count**( *SingleColumnTable* )<br>
**CountA**( *SingleColumnTable* )

* *SingleColumnTable* - Required.  Column of records to count.  

**CountIf**( *Table*, *LogicalFormula* )

* *Table* - Required.  Table of records to count.
* *LogicalFormula* - Required.  Formula to evaluate for each record of the table.  Records that return **true** for this formula are counted.  The formula can reference columns of the table.

**CountRows**( *Table* )

* *Table* - Required.  Table of records to count.

## Example
1. Import or create a [collection](../working-with-data-sources.md#collections) named **Inventory**, as the first subprocedure in [Show images and text in a gallery](../show-images-text-gallery-sort-filter.md) describes.
2. Add a label, and set its **[Text](../controls/properties-core.md)** property to this formula:
   
    **CountIf(Inventory, UnitsInStock < 30)**
   
    The label shows **2** because two products (Ganymede and Callisto) have fewer than 30 units in stock.
3. Add another label, and set its **[Text](../controls/properties-core.md)** property to this formula:
   
    **CountA(Inventory.UnitsInStock)**
   
    The label shows **5**, the number of non-empty cells in the **UnitsInStock** column.
4. Add another label, and set its **[Text](../controls/properties-core.md)** property to this formula:
   
    **CountRows(Inventory)**
   
    The label shows **5** because the collection contains five rows.

