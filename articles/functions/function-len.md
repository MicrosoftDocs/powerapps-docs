<properties
	pageTitle="PowerApps: Len function"
	description="Reference information for the Len function in PowerApps, including syntax and examples"
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

# Len function in PowerApps #

Returns the length of a string.

## Description ##

The **Len** functions returns the length of a string.  

If you pass a single string, the return value is the length as a number.  If you pass a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of lengths of each string. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

If a string is [empty](function-isblank-isempty.md), **Len** will return 0.

## Syntax ##

**Len**( *String* )

- *String* - Required. The string to measure.

**Len**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to measure.

## Examples ##

### Single string ###
The examples in this section use an input-text control, named **Author**, as their [data source](working-with-data-sources.md). The control contains the string "E. E. Cummings".

| Formula | Description | Result |
|---------|-------------|--------|
| **Len( Author!Text )** | Measures the length of the string in the **Author** control. | 14 |
| **Len( "" )** | Measures the length of an empty string. | 0 |

### Single-column table
The examples in this section use this data source, named **People**:

![](media/function-len/people-table.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Len( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** |  In the **Address** [column](working-with-tables.md#columns) of the **People** table:<br><ul><li>Measures the length of each string.</li><li>Returns a single-column table that contains the length of each string.</li> | <style> img { max-width:none; } </style> ![](media/function-len/people-table-len.png) |
| **Len( [ "Hello", "to the", "World", "" ] )** |  In the **[Value](function-value.md)** column of the inline table:<br><ul><li>Measures the length of each string.</li><li>Returns a single-column table that contains the length of each string.</li> | ![](media/function-len/people-table-len-inline.png) |


