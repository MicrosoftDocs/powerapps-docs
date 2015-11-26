<properties
	pageTitle="PowerApps: Trim function"
	description="Reference information for the Trim function in PowerApps, including syntax and examples"
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

# Trim function in PowerApps #

Removes extra spaces from a string.

## Description ##

The **Trim** functions removes all spaces from a text string except for single spaces between words.  

If you pass a single string, the return value is the string with extra spaces removed.  If you pass a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of stripped strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

Trimming spaces between words is consistent with the Microsoft Excel's Trim function, but may be different from other programming tools you have used that only trim spaces from the ends.

## Syntax ##

**Trim**( *String* )

- *String* - Required. The string to remove spaces from.

**Trim**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to remove spaces from.

## Examples ##

### Single string ###

| Formula | Description | Result |
|---------|-------------|--------|
| **Trim( "&nbsp;&nbsp;Hello&nbsp;&nbsp;&nbsp;&nbsp;World&nbsp;&nbsp;&nbsp;" )** | Removes extra spaces from the beginning, middle, and end of the string | "Hello World" |

