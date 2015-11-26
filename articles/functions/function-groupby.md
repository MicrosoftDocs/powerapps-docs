<properties
	pageTitle="PowerApps: GroupBy and Ungroup functions"
	description="Reference information for the GroupBy and Ungroup functions in PowerApps, including syntax and examples"
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

# GroupBy and Ungroup functions in PowerApps #

Groups and ungroups [records](working-with-tables.md#records) of a [table](working-with-tables.md).

## Description ##

The **GroupBy** function groups records together, based on the values in one or more [columns](working-with-tables.md#columns).  Records that are grouped together are placed into a single record, with a column added to hold a nested table of data that is unique.  **GroupBy** returns a table.   

The **Ungroup** function reverses the **GroupBy** process.  Records that were grouped together are broken out into separate records.  **Ungroup** also returns a table.

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **GroupBy** and **Ungroup** does not modify a table, instead it takes a table as an argument and return a new table.  See [working with tables](working-with-tables.md) for more details.

## Syntax ##

**GroupBy**( *Table*, *ColumnName1* [, *ColumnName2*, ... ], *GroupColumnName* )

- *Table* - Required. Table to be grouped.
- *ColumnName(s)* - Required.  The column names in *table* to group on.  These columns become columns in the resulting table.
- *GroupColumnName* - Required.  The column name for the storage of record data not in the *ColumnName(s)*. 

**Ungroup**( *Table*, *GroupColumnName* )

- *Table* - Required. Table to be ungrouped.
- *GroupColumnName* - Required.  The column containing the record data setup with the **GroupBy** function. 





