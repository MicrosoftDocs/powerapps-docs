<properties
	pageTitle="PowerApps: First, FirstN, Last, and LastN functions"
	description="Reference information for the First, FirstN, Last, and LastN functions in PowerApps, including syntax and examples"
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

# First, FirstN, Last, and LastN functions in PowerApps #

Returns a table's first or last set of records. 

## Description ##

The **First** function returns the first record of a table.

The **FirstN** function returns the first set of records of a table, the second argument specifies the number of records to return.

The **Last** function returns the last record of a table.

The **LastN** function returns the last set of records of a table, the second argument specifies the number of records to return.

**First** and **Last** return a single record.  **FirstN** and **LastN** return a table, even if only a single record is specified.

## Syntax ##

**First**( *Table* )<br>
**Last**( *Table* )

- *Table* - Rquired. Table to operate on.

**FirstN**( *Table* [, *NumberOfRecords* ] )<br>
**LastN**( *Table* [, *NumberOfRecords* ] )

- *Table* - Rquired. Table to operate on.
- *NumberOfRecords* - Optional.  Number of records to return. If not specified, the result table will contain one record.

## Examples ##

<!-- TODO: Examples. -->

### Step by step ###

If you had an Employees table, this function would return the first record from that table:

**First(Employees)**

And this function would return the last 15 records from that table:

**LastN(Employees, 15)**

