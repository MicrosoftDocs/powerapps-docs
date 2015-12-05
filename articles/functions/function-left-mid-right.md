<properties
	pageTitle="PowerApps: Left, Mid, and Right functions"
	description="Reference information for the Left, Mid, and Right functions in PowerApps, including syntax and examples"
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

# Left, Mid, and Right functions in PowerApps #

Extracts the left, middle, or right portion of a string.

## Description ##

The **Left**, **Mid**, and **Right** functions return a portion of a string.

- **Left** returns the beginning characters of a string.
- **Mid** returns the middle characters of a string.
- **Right** returns the ending characters of a string.

If you pass a single string, the return value is the requested portion as a string.  If you pass a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of the requested portions of those strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

If the starting position is negative or beyond the end of the string, **Mid** will return *blank*.  You can check the length of a string with the **[Len](function-len.md)** function.  If the number of characters requested is more than the length of the string, as many characters as possible are returned.

## Syntax ##

**Left**( *String*, *NumberOfCharacters* )<br>**Mid**( *String*, *StartingPosition*, *NumberOfCharacters* )<br>**Right**( *String*, *NumberOfCharacters* )

- *String* - Required. The string to extract from.
- *StartingPosition* - Required (**Mid** only).  The starting position.  The first character of the string is position 1.
- *NumberOfCharacters* - Required.  The number of characters to return.

**Left**( *SingleColumnTable*, *NumberOfCharacters* )<br>**Mid**( *SingleColumnTable*, *StartingPosition*, *NumberOfCharacters* )<br>**Right**( *SingleColumnTable*, *NumberOfCharacters* )

- *SingleColumnTable* - Required. A single-column table of strings to extract from.
- *StartingPosition* - Required (**Mid** only).  The starting position.  The first character of the string is position 1.
- *NumberOfCharacters* - Required.  The number of characters to return.

## Examples ##

### Single string ###
The examples in this section use an input-text control, named **Author**, as their [data source](working-with-data-sources.md). The control contains the string "E. E. Cummings".

| Formula | Description | Result |
|---------|-------------|--------|
| **Left( Author!Text, 5 )** | Extracts the beginning, or left, portion of the string up to 5 characters. | "E. E." |
| **Mid( Author!Text, 7, 4 )** | Extracts the middle portion of the string, starting a position 7, up to 4 characters. | "Cumm" |
| **Right( Author!Text, 5 )** | Extracts the ending, or right, portion of the string up to 5 characters. | "mings" |

### Single-column table
The examples in this section use this data source, named **People**:

![](media/function-left-mid-right/people-table.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Left( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;), 8 )** |  In the **Address** [column](working-with-tables.md#columns) of the **People** table:<br><ul><li>Extracts the first 8 characters of each string.</li><li>Returns a single-column table that contains the extracted strings.</li> | <style> img { max-width: none } </style> ![](media/function-left-mid-right/people-table-left.png) |
| **Mid( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;), 5, 7 )** | In the **Address** column of the **People** table:<br><ul><li>Extracts the middle 7 characters of each string, starting at position 5.</li><li>Returns a single-column table that contains the extracted strings.</li> | ![](media/function-left-mid-right/people-table-mid.png) |
| **Right( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;), 7 )** | In the **Address** column of the **People** table:<br><ul><li>Extracts the last 7 characters of each string.</li><li>Returns a single-column table that contains the extracted strings.</li> | ![](media/function-left-mid-right/people-table-right.png) |

### Step-by-step example ###

1. Import or create a [collection](working-with-data-sources.md#collections) named **Inventory**, and show it in a gallery.

2. Set the Text property of the lower label in the gallery to this function:

	**Right(ThisItem!ProductName, 3)**

	The label shows the last three characters in each product name.


