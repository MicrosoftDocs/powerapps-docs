---
title: Distinct function | Microsoft Docs
description: Reference information, including syntax and examples, for the Distinct function in PowerApps
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
# Distinct function in PowerApps
Summarizes [records](../working-with-tables.md#records) of a [table](../working-with-tables.md), removing duplicates.

## Description
The **Distinct** function evaluates a formula across each record of a table. **Distinct** returns a one-column table that contains the results, with duplicate values removed.  

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

## Syntax
**Distinct**( *Table*, *Formula* )

* *Table* - Required.  Table to evaluate across.
* *Formula* - Required.  Formula to evaluate for each record.

## Example
If you had an **Employees** table that contained a **Department** column, this function would list each unique department name in that column, no matter how many times each name appeared in that column:

**Distinct(Employees, Department)**

