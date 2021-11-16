---
title: First, FirstN, Last, and LastN functions in Power Apps
description: Reference information including syntax and examples for the First, FirstN, Last, and LastN functions in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/07/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# First, FirstN, Last, and LastN functions in Power Apps
Returns a table's first or last set of [records](../working-with-tables.md#records).

## Description
The **First** function returns the first record of a [table](../working-with-tables.md).

The **FirstN** function returns the first set of records of a table; the second argument specifies the number of records to return.

The **Last** function returns the last record of a table.

The **LastN** function returns the last set of records of a table; the second argument specifies the number of records to return.

**First** and **Last** return a single record.  **FirstN** and **LastN** return a table, even if you specify only a single record.

[!INCLUDE [delegation-no](../../../includes/delegation-no.md)]

## Syntax
**First**( *Table* )<br>**Last**( *Table* )

* *Table* - Required. Table to operate on.

**FirstN**( *Table* [, *NumberOfRecords* ] )<br>**LastN**( *Table* [, *NumberOfRecords* ] )

* *Table* - Required. Table to operate on.
* *NumberOfRecords* - Optional.  Number of records to return. If you don't specify this argument, the function returns one record.

## Examples
This formula returns the first record from a table named **Employees**:<br>
**First(Employees)**

This formula returns the last 15 records from a table named **Employees**:<br>
**LastN(Employees, 15)**



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]