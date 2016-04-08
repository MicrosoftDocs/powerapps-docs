<properties
	pageTitle="Trim function | Microsoft PowerApps"
	description="Reference information, including syntax and an example, for the Trim function in PowerApps"
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

Removes extra spaces from a string of text.

## Description ##

The **Trim** function removes all spaces from a text string except for single spaces between words.  

If you specify a single string, the return value is the string with extra spaces removed. If you specify a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of trimmed strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

By trimming spaces between words, **Trim** is consistent with the function of the same name in Microsoft Excel. However, other programming tools trim spaces only from the ends of strings.

## Syntax ##

**Trim**( *String* )

- *String* - Required. The string to remove spaces from.

**Trim**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to remove spaces from.

## Example ##

| Formula | Description | Result |
|---------|-------------|--------|
| **Trim( "&nbsp;&nbsp;Hello&nbsp;&nbsp;&nbsp;&nbsp;World&nbsp;&nbsp;&nbsp;" )** | Removes extra spaces from the start, middle, and end of the string | "Hello World" |
