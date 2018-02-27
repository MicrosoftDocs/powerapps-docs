---
title: Table function | Microsoft Docs
description: Reference information, including syntax and examples, for the Table function in PowerApps
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
# Table function in PowerApps
Creates a temporary [table](../maker/working-with-tables.md).

## Description
The **Table** function creates a table from an argument list of [records](../maker/working-with-tables.md#records).

The table's [columns](../maker/working-with-tables.md#columns) will be the union of all the properties from all the argument records. A *blank* value is added to any column for which a record doesn't include a value.

A table is a value in PowerApps, just like a string or a number. You can specify a table as an argument for a function, and functions can return a table as a result. **Table** doesn't create a permanent table. Instead it returns a temporary table made of its arguments.  You can specify this temporary table as an argument for another function, visualize it in a gallery, or embed it in another table.  See [working with tables](../maker/working-with-tables.md) for more details.

You can also create a single-column table with the **[ value1, value2, ... ]** syntax.

## Syntax
**Table**( *Record1* [, *Record2*, ... ] )

* *Record(s)* - Required. The records to add to the table.

## Examples
* Set the **[Items](../maker/controls/properties-core.md)** property of a listbox to this formula:
  <br>**Table({Color:"red"}, {Color:"green"}, {Color:"blue"})**
  
    The listbox shows each color as an option.
* Add a text gallery, and set its **[Items](../maker/controls/properties-core.md)** property to this function:<br>
  **Table({Item:"Violin123", Location:"France", Owner:"Fabrikam"}, {Item:"Violin456", Location:"Chile"})**
  
    The gallery shows two records, both of which contain the name and location of an item. Only one record contains the name of the owner.

