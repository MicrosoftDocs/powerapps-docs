<properties
	pageTitle="Trim and TrimEnds functions | Microsoft PowerApps"
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

# Trim and TrimEnds functions in PowerApps #

Removes extra spaces from a string of text.

## Description ##

The **Trim** function removes all spaces from a text string except for single spaces between words.  

The **TrimEnds** function removes all spaces from the ends of a string, but leaves spaces between words intact.

If you specify a single string, the return value is the string with extra spaces removed. If you specify a single-column [table](../working-with-tables.md) that contains strings, the return value is a single-column table of trimmed strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

By trimming spaces between words, **Trim** is consistent with the function of the same name in Microsoft Excel. However, other programming tools trim spaces only from the ends of strings, for which **TrimEnds** is a better choice.

**TrimEnds** can be delegated in **[Filter](function-filter.md)** and **[Sort](function-sort.md)** formulas.  **Trim** cannot be delegated.

## Syntax ##

**Trim**( *String* )<br>**TrimEnds**( *String* )

- *String* - Required. The string to remove spaces from.

**Trim**( *SingleColumnTable* )<br>**TrimEnds**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to remove spaces from.

## Example ##

| Formula | Description | Result |
|---------|-------------|--------|
| **Trim(&nbsp;"&nbsp;&nbsp;&nbsp;Hello&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;World&nbsp;&nbsp;&nbsp;"&nbsp;)** | Removes extra spaces from the start, middle, and end of the string. | "Hello World" |
| **TrimEnds(&nbsp;"&nbsp;&nbsp;&nbsp;Hello&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;World&nbsp;&nbsp;&nbsp;"&nbsp;)** | Removes extra spaces from the start and end of the string only. | "Hello&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;World" |

The following examples use a collection named **Strings**:

![](media/function-trim/input-strings.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Trim(&nbsp;Strings&nbsp;)** | Trims extra spaces from the start, middle, and end of each record of the collection **Strings**. | <style> img { max-width: none } </style> ![](media/function-trim/output-trim.png) |
| **TrimEnds(&nbsp;Strings&nbsp;)** | Trims extra spaces from the start and and of the string only in each record of the collection **Strings**. | <style> img { max-width: none } </style> ![](media/function-trim/output-trimends.png) |

You can create the **Strings** collection by evaluating the following formula (select and copy the below text, paste into the OnSelect property of a Button control, preview the app, and select the button):

**ClearCollect( Strings, [ "&nbsp;&nbsp;&nbsp;Jane&nbsp;&nbsp;&nbsp;Doe&nbsp;&nbsp;&nbsp;", "&nbsp;&nbsp;&nbsp;&nbsp;Jack&nbsp;&nbsp;&nbsp;and&nbsp;&nbsp;&nbsp;Jill", "Already&nbsp;trimmed", "&nbsp;&nbsp;&nbsp;Venus,&nbsp;&nbsp;&nbsp;Earth,&nbsp;&nbsp;&nbsp;Mars&nbsp;&nbsp;", "Oil&nbsp;and&nbsp;Water&nbsp;&nbsp;&nbsp;" ] )**

Note that when viewing collections in the **File** menu of the authoring experience, extra spaces are automatically trimmed.  Use the **[Len](function-len.md)** function to verify the length of strings.







