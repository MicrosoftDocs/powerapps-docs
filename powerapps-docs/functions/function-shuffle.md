---
title: Shuffle function | Microsoft Docs
description: Reference information, including syntax and an example, for the Shuffle function in PowerApps
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
# Shuffle function in PowerApps
Randomly reorders the [records](../maker/working-with-tables.md#records) of a [table](../maker/working-with-tables.md).

## Description
The **Shuffle** function reorders the records of a table.

**Shuffle** returns a table that has the same [columns](../maker/working-with-tables.md#columns) and number of rows as the argument.

## Syntax
**Shuffle**( *Table* )

* *Table* - Required.  Table to shuffle.

## Example
If you stored details about playing cards in a [collection](../maker/working-with-data-sources.md#collections) named **Deck**, this formula would return a copy of that collection that has been randomly shuffled.

**Shuffle(Deck)**

