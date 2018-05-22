---
title: Shuffle function | Microsoft Docs
description: Reference information, including syntax and an example, for the Shuffle function in PowerApps
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 11/07/2015
ms.author: gregli

---
# Shuffle function in PowerApps
Randomly reorders the [records](../working-with-tables.md#records) of a [table](../working-with-tables.md).

## Description
The **Shuffle** function reorders the records of a table.

**Shuffle** returns a table that has the same [columns](../working-with-tables.md#columns) and number of rows as the argument.

## Syntax
**Shuffle**( *Table* )

* *Table* - Required.  Table to shuffle.

## Example
If you stored details about playing cards in a [collection](../working-with-data-sources.md#collections) named **Deck**, this formula would return a copy of that collection that has been randomly shuffled.

**Shuffle(Deck)**

