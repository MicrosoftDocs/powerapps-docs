---
title: Concat and Concatenate functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Concat and Concatenate functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/28/2017
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Concat and Concatenate functions in PowerApps
Concatenates individual strings of text and strings in [tables](../working-with-tables.md).

## Description
The **Concat** function concatenates the result of a formula applied across all the [records](../working-with-tables.md#records) of a table, resulting in a single string. Use this function to summarize the strings of a table, just as the **[Sum](function-aggregates.md)** function does for numbers.

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

Use the **[Split](function-split.md)** function to split a string into a table of substrings.

The **Concatenate** function concatenates a mix of individual strings and a single-column table of strings. Used with individual strings, this function is equivalent to using the **&** [operator](operators.md). You can use a formula that includes the **[ShowColumns](function-table-shaping.md)** function to create a single-column table from a table that has multiple columns.

## Syntax
**Concat**( *Table*, *Formula* )

* *Table* - Required.  Table to operate on.
* *Formula* - Required.  Formula to apply across the records of the table.

**Concatenate**( *String1* [, *String2*, ...] )

* *String(s)* - Required.  Mix of individual strings or a single-column table of strings.

## Examples
#### Concat
1. Add a **[Button](../controls/control-button.md)** control, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:
   
    **Collect(Products, {String:"Violin", Wind:"Trombone", Percussion:"Bongos"}, {String:"Cello", Wind:"Trumpet", Percussion:"Tambourine"})**
2. Press F5, click the button, and then press Esc to return to the design workspace.
3. Add a **[Label](../controls/control-text-box.md)** control, and set its **[Text](../controls/properties-core.md)** property to this formula:
   
    **Concat(Products, String & " ")**
   
    The label shows **Violin Cello**.

#### Concatenate
1. Add a **[Text input](../controls/control-text-input.md)** control, and name it **AuthorName**.
2. Add a **[Label](../controls/control-text-box.md)** control, and set its **[Text](../controls/properties-core.md)** property to this formula:<br>
   **Concatenate("By ", AuthorName.Text)**
3. Type your name in **AuthorName**.
   
    The label shows **By** followed by your name.

If you had an **Employees** table that contained a **FirstName** column and a **LastName** column, this formula would concatenate the data in each row of those columns.
<br>**Concatenate(Employees.FirstName, " ", Employees.LastName)**

